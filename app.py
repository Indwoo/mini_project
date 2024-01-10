from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

#client = MongoClient('mongodb://test:test@54.180.112.156', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost',27017)
db = client.db_jungle_firstPro                        # 'jungle'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
    return render_template('category.html')

@app.route('/main')
def main():
    return render_template('main.html')

# API 가게 리스트 반환하기
@app.route('/list', methods=['GET'])
def show_store():
    # client 에서 요청한 정렬 방식이 있는지를 확인합니다.기본으로 별점 순으로 정렬합니다.
    sortMode = request.args.get('sortMode','likes')
    
    stores = list(db.chiness.find())
    
    # 성공하면 success 메시지와 함께 store_list 목록을 클라이언트에 전달.
    return jsonify({'result': 'success', 'store_list': stores})


@app.route('/reply', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    article = {'comment': comment_receive}
    
    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})


@app.route('/reply', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    
    
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)