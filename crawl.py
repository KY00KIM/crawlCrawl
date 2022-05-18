import argparse
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import json
import os

'''
기능: 네이버쇼핑의 골프 카테고리 상품들을 가져와 ./data/data.json 으로 저장
Input: PageNum : 검색할 페이지 개수 / DataDir : 결과 저장할 경로 / ChromeDir : chromedriver 경로
Output: DataDir/data.json 에 상품 {이름, 가격, 링크} 저장
주의 : chromedriver 있어야 한다.
      페이지 당 86개의 상품 정보를 가져온다.
      data.json을 덮어쓴다.
예시 : python crawl.py --DataDir ./data --ChromeDir ./
'''
def SearchGolfCategory(PageNum, DataDir='./data/',ChromeDir='./' ):

    for loop in range(1, PageNum+1):
        
        #open webpage by chromedriver
        html = "https://search.shopping.naver.com/search/category/100004232?catId=50000029&origQuery&pagingIndex="+str(loop)+"&pagingSize=80&productSet=total&query&sort=rel&timestamp=&viewType=list"
        driver = webdriver.Chrome(os.path.join(ChromeDir, "chromedriver"))
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(html)
        driver.implicitly_wait(3)
        

        #scroll down webpage
        prev_height = driver.execute_script('return document.body.scrollHeight')
        
        for i in range(10):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
            
            current_height = driver.execute_script('return document.body.scrollHeight')
            
            if prev_height == current_height:
                break
        time.sleep(3)
        

        #parse html
        bsObject = BeautifulSoup(driver.page_source, "html.parser")

        #data to be stored
        date = datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")
        data = dict()
        data["date"] = date
        data["count"] = 0
        data["item"] =[]
        count = 0
        
        #get item data from html
        for item_info in bsObject.select('div.basicList_info_area__17Xyo'):
            title = item_info.select('div.basicList_title__3P9Q7>a')[0]
            link = title.get('href')
            name = title.get('title')
            price = item_info.select_one('div.basicList_price_area__1UXXR>strong.basicList_price__2r23_>span>span.price_num__2WUXn').text.strip()
                
            data["item"].append({"name": str(name), "price":str(price), "link":str(link) }) 
            count += 1
        data["count"]=count

        #push item into ./data/data.json
        if loop == 1:
            with open(os.path.join(DataDir, "data.json"),"w",encoding='utf-8') as file:
                json.dump(data, file, indent='\t', ensure_ascii=False)
        else:
            with open(os.path.join(DataDir, "data.json"),"r",encoding='utf-8') as file:
                JsonFile = json.load(file)
                JsonFile["count"] += data["count"]
                JsonFile["item"] += data["item"]
            with open(os.path.join(DataDir, "data.json"),"w",encoding='utf-8') as file:
                json.dump(JsonFile, file, indent='\t', ensure_ascii=False)


def getArgs():
    parser = argparse.ArgumentParser(description='Crawling Dir')
    parser.add_argument("--DataDir", default='./', type=str, required=True)
    parser.add_argument("--PageCount", default=5, type=int, required=False)
    parser.add_argument("--ChromeDir", default='./', type=str, required=True)

    args = parser.parse_args()

    return args

def main():
    args = getArgs()
    SearchGolfCategory(args.PageCount, args.DataDir, args.ChromeDir)

if __name__ == '__main__':
    main()
