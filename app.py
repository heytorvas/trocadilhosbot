from flask import Flask
from util import create_connection
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'hello world'

@app.route('/users', methods=['GET'])
def users():
    con = create_connection()
    cursor = con.cursor()
    sql = cursor.execute("SELECT * FROM user")
    users = [dict(id=row[0], is_bot=row[1], first_name=row[2], last_name=row[3], username=row[4], language_code=row[5]) for row in sql.fetchall()]
    cursor.close()
    return json.dumps(users, ensure_ascii=False)

if __name__ == '__main__':
    app.run(port=5000, debug=True)