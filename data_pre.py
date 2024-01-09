import csv
import json
import numpy as np
import pandas as pd
from haversine import haversine
here = (37.29963, 127.0340)  #Latitude, Longitude

# csv 파일 경로
df = pd.read_csv('경기대양식.csv')

df_data= df[["이름", "도로명주소", "방문자 평점", "상세페이지URL"]]
df_data = df_data.dropna()

df_data.to_json('usa.json', force_ascii=False, orient= 'records', indent=4)
df_data.to_csv("usa.csv", index=False, encoding="utf-8-sig")
