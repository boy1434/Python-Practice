# 20개의 영화 데이터의 제목, 평점, 러닝시간, 미디엄-커버-이미지
# 반복문을 돌려서 Console에 이쁘게 출력하시오
# 구분(============================= "="*50)

# 제목 : 쇼생크탈출
# 평점 : 9.5
# 러닝시간 : 77분
# 사진 :

import requests

url = '''
 https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
'''

response = requests.get(url)
responseDict = response.json()

movies = responseDict["data"]["movies"]


for movie in movies:

    print("제목: " + movie["title"])
    print("평점: " + str(movie["rating"]) + "점")
    print("러닝시간: " + str(movie["runtime"]) + "분")
    print("사진: " + movie["medium_cover_image"])
    print("="*50)
