import requests
import json



# url = 'https://openapi.naver.com/v1/search/shop.json?'
# header = {'X-Naver-Client-Id': '6pbEF8SaasJLGAz5PcQw',
#           'X-Naver-Client-Secret':'bV2z0EmLjt'}
# query= 'query=골프'

# res = requests.get(url+query,header)

# print(res.status_code)
# print(res.headers['content-type'])
# print(res.encoding)
# print(res.text)
# print(res.json())

# print(len(res.json()['list']))

 
client_id = '6pbEF8SaasJLGAz5PcQw'
client_secret = 'bV2z0EmLjt'
keyword = '골프' 
url = 'https://openapi.naver.com/v1/search/shop.json' 
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 

reqSize = 10;
for loop in range(5):
    params = {'query':keyword, 'display':reqSize, 'start':1+loop*reqSize, 'sort':'sim'} 
    r = requests.get(url, params = params, headers = headers) 
    j = r.json() 
    print(j)
    
    if loop == 0:
        with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/record.json", 'w', encoding='utf-8') as file:
            json.dump(j, file, indent='\t', ensure_ascii=False)
    else : 
        with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/record.json", 'r', encoding='utf-8')as file:
            data = json.load(file)
            data["items"]+=(j["items"])
            data["display"]+=j["display"]
            data["lastBuildDate"]=j["lastBuildDate"]
        with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/record.json", 'w', encoding='utf-8')as file:
            json.dump(data, file, indent='\t', ensure_ascii=False)
    
