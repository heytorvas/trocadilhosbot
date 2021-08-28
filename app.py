from flask import Flask, request, jsonify
from util import create_connection, get_data_yaml
import json, requests, datetime, logging

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

logging.basicConfig(filename="api.log", level=logging.INFO)

app = Flask(__name__)
TOKEN = get_data_yaml('TOKEN')
api = get_data_yaml('api')

app.config["JWT_SECRET_KEY"] = api['secret_key']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(seconds=350)
jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def hello():
    return 'hello world'

@app.route("/token/", methods=["POST"])
def token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != api['username'] or password != api['password']:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/users/', methods=['GET'])
@jwt_required()
def users():
    con = create_connection()
    cursor = con.cursor()
    sql = cursor.execute("SELECT * FROM user")
    users = [dict(id=row[0], first_name=row[1], last_name=row[2], username=row[3]) for row in sql.fetchall()]
    cursor.close()
    return json.dumps(users, ensure_ascii=False)

@app.route('/messages/', methods=['GET'])
@jwt_required()
def messages():
    con = create_connection()
    cursor = con.cursor()
    sql = cursor.execute("SELECT * FROM message")
    users = [dict(id=row[0], message=row[1]) for row in sql.fetchall()]
    cursor.close()
    return json.dumps(users, ensure_ascii=False)

@app.route('/send_message/', methods=['POST'])
@jwt_required()
def send_message():
    data = request.get_json()
    body_post = [None, None]

    if 'text' in data:
        body_post[0] = data['text']

    if 'id' in data:
        body_post[1] = data['id']

    if None in body_post:
        return {"msg": "Bad request"}, 400

    try:
        response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={int(body_post[1])}&text={str(body_post[0])}')

        con = create_connection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO message(id,message) VALUES (?,?);", 
                (int(body_post[1]), str(body_post[0])))
        con.commit()
        return {"status_code": response.status_code}, response.status_code
    except:
        return {"status_code": 400}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)