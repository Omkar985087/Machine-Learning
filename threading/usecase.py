'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/v0.2/docs/introduction/',

    'https://python.langchain.com/v0.2/docs/concepts/',

    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def feth_content(url):
    reponse=requests.get(url)
    soup=BeautifulSoup(reponse.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=feth_content,args=(url,))
    threads.append(thread)
    thread.start()

for thrad in threads:
    thread.join()

print("ALL web pages")