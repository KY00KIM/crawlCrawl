import argparse

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import json
import os

'''
기능: 
Input: 
Output: 
네이버 쇼핑에서의 골프 카테고리의 상품이름, 상품가격, 상품링크 를 지정한 경로로 data.json으로 반환
page_size = 20, 40, 60, 80
'''
def SearchGolfCategory(page_num, page_size=20, location='./',chromeDir='./' ):

    for loop in range(1, page_num+1):
        html = "https://search.shopping.naver.com/search/category/100004232?catId=50000029&origQuery&pagingIndex="+str(loop)+"&pagingSize="+str(page_size)+"&productSet=total&query&sort=rel&timestamp=&viewType=list"
        driver = webdriver.Chrome(os.path.join(chromeDir, "chromedriver"))
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(html)
        driver.implicitly_wait(3)

        #스크롤
        prev_height = driver.execute_script('return document.body.scrollHeight')

        for i in range(10):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
            
            current_height = driver.execute_script('return document.body.scrollHeight')
            
            if prev_height == current_height:
                break

        time.sleep(3)

        bsObject = BeautifulSoup(driver.page_source, "html.parser")


        date = datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")
        data = dict()
        data["date"] = date
        data["count"] = 0
        data["item"] =[]
        count = 0
        for item_info in bsObject.select('div.basicList_info_area__17Xyo'):
            title = item_info.select('div.basicList_title__3P9Q7>a')[0]
            link = title.get('href')
            name = title.get('title')
            price = item_info.select_one('div.basicList_price_area__1UXXR>strong.basicList_price__2r23_>span>span.price_num__2WUXn').text.strip()
                
            data["item"].append({"name": str(name), "price":str(price), "link":str(link) }) 
            count += 1
        data["count"]=count

        if loop == 1:
            with open(location+"data.json","w",encoding='utf-8') as file:
                json.dump(data, file, indent='\t', ensure_ascii=False)
        else:
            with open(location+"data.json","r",encoding='utf-8') as file:
                j = json.load(file)
                j["count"] += data["count"]
                j["item"] += data["item"]
            with open(location+"data.json","w",encoding='utf-8') as file:
                json.dump(j, file, indent='\t', ensure_ascii=False)


def getArgs():
    parser = argparse.ArgumentParser(description='Crawling Dir')
    parser.add_argument("--location", default='./', type=str, required=True)
    parser.add_argument("--PageCount", default=5, type=int, required=False)
    parser.add_argument("--PageSize", default=20, type=int, required=False)
    parser.add_argument("--ChromeDir", default='./', type=str, required=True)

    args = parser.parse_args()

    return args

def main():
    args = getArgs()
    searchGolfCategory(args.PageCount, args.PageSize, args.location, args.ChromeDir)

if __name__ == '__main__':
    main()




# # 메타 정보로부터 필요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.  
# for index, book_page_url in enumerate(item_page_urls):
#     html = urlopen(book_page_url)
#     bsObject = BeautifulSoup(html, "html.parser")
#     title = bsObject.find('meta', {'property':'og:title'}).get('content')
#     author = bsObject.select('span.name a')[0].text
#     image = bsObject.find('meta', {'property':'og:image'}).get('content')
#     url = bsObject.find('meta', {'property':'og:url'}).get('content')
#     Price = bsObject.find('meta', {'property': 'og:price'}).get('content')

#     print(index+1, title, author, image, url, Price)
    
    
    
    
# print(bsObject)

# print(bsObject.head.title)

# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))
    
# print(bsObject.head.find("meta", {"name":"description"}).get("content"))

# for link in bsObject.find_all('a'):
#     print(link.text.strip(), link.get('href'))

