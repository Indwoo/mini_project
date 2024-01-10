from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.json.provider import JSONProvider
from pymongo import MongoClient
from bson import ObjectId
import json
import sys


app = Flask(__name__)

# 이하 MongoDB 설정은 이전과 동일하게 유지
# MongoDB 연결 설정
client = MongoClient('mongodb://test:test@54.180.112.156',27017)
db = client.db_jungle_firstPro

#####################################################################################
# 이 부분은 코드를 건드리지 말고 그냥 두세요. 코드를 이해하지 못해도 상관없는 부분입니다.
#
# ObjectId 타입으로 되어있는 _id 필드는 Flask 의 jsonify 호출시 문제가 된다.
# 이를 처리하기 위해서 기본 JsonEncoder 가 아닌 custom encoder 를 사용한다.
# Custom encoder 는 다른 부분은 모두 기본 encoder 에 동작을 위임하고 ObjectId 타입만 직접 처리한다.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class CustomJSONProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=CustomJSONEncoder)

    def loads(self, s, **kwargs):
        return json.loads(s, **kwargs)


# 위에 정의되 custom encoder 를 사용하게끔 설정한다.
app.json = CustomJSONProvider(app)

# 여기까지 이해 못해도 그냥 넘어갈 코드입니다.
# #####################################################################################




@app.route('/')
def index():
    return render_template('login.html')

@app.route('/category')
def select_category():
    return render_template('category.html')

@app.route('/signin', methods=['POST'])
def signin():
    user_id = request.form.get('user_id') 
    password = request.form.get('password')
    print(user_id)
    print(password)

    loginUser = db.users.count_documents({"user_id":user_id, "password" : password })
    print(loginUser)

    if loginUser == 0:
        return jsonify({'result': 'failure'})
    else:
        return jsonify({'result': 'success'})

@app.route('/signup')
def signup():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_signup():
    
    # HTML에서 전송된 데이터 받기
    name = request.form.get('name')
    user_id = request.form.get('user_id') 
    password = request.form.get('password')
    kakao_id = request.form.get('kakao_id')


    # MongoDB에 데이터 삽입
    user_data = {
        'name': name,
        'user_id': user_id,
        'password': password,
        'kakao_id': kakao_id
    }
    db.users.insert_one(user_data)

    if True :
        return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
