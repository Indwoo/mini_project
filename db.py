from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test:test@54.180.112.156', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.db_jungle_firstPro                        # 'jungle'라는 이름의 db를 만듭니다.


title = list(db.china.distinct(("이름")))
like = list(db.china.distinct(("방문자 평점")))
address = list(db.china.distinct(("도로명주소")))
url = list(db.china.distinct(("상세페이지URL")))

doc = {
    'title':title,
    'like':like,
    'address':address,
    'url':url
}

#db.chiness.insert_one(doc)

chiness = list(db.chiness.find())

print(chiness)

