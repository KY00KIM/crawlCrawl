import requests
import json

def shopSearchCrawl (html, keyword, sort, size, startIdx=1):
    #startIdx 1~1000
    #size 10~100
    #sort sim, date, asc, dsc
    
    data = []
    loop = size//100
    for i in range(loop):
        curSize = 0
        if size>=100: curSize =100 
        else: curSize = size
        
        data += getItems(html, keyword, sort, curSize, startIdx+(i*100))
        
        if size>=100: size-=100
        else: size = 0
    
    
    return data

def getItems(html, keyword, sort, size, startIdx):
    with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/auth/auth.json","r") as file:
        auth = json.load(file)
        client_id=auth["client_id"]
        client_secret=auth["client_secret"]
    url = 'https://openapi.naver.com/v1/search/shop.json' 
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 
    params = {'query':keyword, 'display':reqSize, 'start':1+loop*reqSize, 'sort':'sim'} 
    r = requests.get(url, params = params, headers = headers) 
    j = r.json()
    
    #response log 
    print(json.dumps(j, indent="\t"))
    
    return j["items"]



# with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/auth/auth.json","r") as file:
#     auth = json.load(file)
#     client_id=auth["client_id"]
#     client_secret=auth["client_secret"]
    
# keyword = '골프' 
# url = 'https://openapi.naver.com/v1/search/shop.json' 
# headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 

# reqSize = 10;
# for loop in range(5):
#     params = {'query':keyword, 'display':reqSize, 'start':1+loop*reqSize, 'sort':'sim'} 
#     r = requests.get(url, params = params, headers = headers) 
#     j = r.json() 
#     print(j)
    
#     if loop == 0:
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'w', encoding='utf-8') as file:
#             json.dump(j, file, indent='\t', ensure_ascii=False)
#     else : 
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'r', encoding='utf-8')as file:
#             data = json.load(file)
#             data["items"]+=(j["items"])
#             data["display"]+=j["display"]
#             data["lastBuildDate"]=j["lastBuildDate"]
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'w', encoding='utf-8')as file:
#             json.dump(data, file, indent='\t', ensure_ascii=False)
#  if loop == 0:
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'w', encoding='utf-8') as file:
#             json.dump(j, file, indent='\t', ensure_ascii=False)
#     else : 
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'r', encoding='utf-8')as file:
#             data = json.load(file)
#             data["items"]+=(j["items"])
#             data["display"]+=j["display"]
#             data["lastBuildDate"]=j["lastBuildDate"]
#         with open("/Users/kimkyumin/Desktop/SWM 13기/test네이버API/testNaverCrawl/data/record.json", 'w', encoding='utf-8')as file:
#             json.dump(data, file, indent='\t', ensure_ascii=False)
    
