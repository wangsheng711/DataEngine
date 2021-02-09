import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd

page_total=int(input('输入需要翻页的次数:'))

url1 = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for page in range(0,page_total):
    url=url1+str(page+1)+'.shtml'
    html=requests.get(url,headers=headers,timeout=10)
    content = html.text
    soup = bs(content, 'html.parser', from_encoding='utf-8')
    temp = soup.find('div',class_="tslb_b")
    
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        print(tr.type)
        if (len(tr.find_all('td'))):
            id=tr.find_all('td')[0].get_text()
            brand=tr.find_all('td')[1].get_text()
            car_model=tr.find_all('td')[2].get_text()
            type=tr.find_all('td')[3].get_text()
            desc=tr.find_all('td')[4].get_text()
            problem=tr.find_all('td')[5].get_text()
            datetime=tr.find_all('td')[6].get_text()
            status=tr.find_all('td')[7].get_text()
            df=df.append(pd.Series(dict(zip(df.columns, [id,brand,car_model,type,desc,problem,datetime,status]))), ignore_index=True)
            
print(df)
df.to_excel('CompainCollection.xls')
