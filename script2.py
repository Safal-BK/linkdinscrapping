
import os
from os import path
from glob import glob  
from bs4 import BeautifulSoup
import json
PROJECT_PATH=os.getcwd()
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))
id=[]
count=0
texts=find_ext(os.path.join(PROJECT_PATH,"link_source"),"html")
for text in texts:
    path=text
    name=text.split("/")[::-1][0]
    with open(path, 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html5lib')
            allspan=soup.find_all("div",class_="artdeco-entity-lockup__title ember-view")
            for i in allspan:
                id.append({"name":i.a.text.strip() ,"link":i.a["href"]})
    count+=1
    print(count)


j={

}
j["profile_link"]=id
with open("extract/profile_link/candidates_link.json","w") as f:
        f.writelines(json.dumps(j))