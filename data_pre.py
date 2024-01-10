import csv
import json
import numpy as np
import pandas as pd
from haversine import haversine
here = (37.29963, 127.0340)  #Latitude, Longitude

# csv 파일 경로
df = pd.read_csv('./csv_data/경기대양식.csv')

df_data= df[["이름", "도로명주소", "방문자 평점", "상세페이지URL", "위도", "경도", "썸네일이미지URL"]]
df_data = df_data.dropna()

print(df_data)

df_data.to_json('usa.json', force_ascii=False, orient= 'records', indent=4)
'''
df_data.to_csv("usa.csv", index=False, encoding="utf-8-sig")
'''
