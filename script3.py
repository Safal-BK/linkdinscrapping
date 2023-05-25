from playwright.sync_api import Playwright, sync_playwright, expect
import time
import json
import re
import os
from os import path
from glob import glob  
from bs4 import BeautifulSoup
import json
import random
import lib.network as net

# from tqdm import tqdm
os.getcwd()
# dipinthomas004@gmail.com
# Jinz@5792
# command
#  playwright codegen --load-storage=state.json https://www.linkedin.com/uas/login-cap

profiles=[]

errorfiles=[]
with open("data/extract/profile_link/candidates_link.json", 'r') as f:
        profiles = json.loads(f.read())
        profiles=profiles["profile_link"]


count=0
fin_urls=[]
with open('log/finishedurl.txt', 'r') as f:
    fin_urls = f.readlines()
f_url=[]
for u in fin_urls:
        u=u.split("#")[1].replace("\n","")
        f_url.append(u)
temp_profiles=[]
for profile in profiles:#scrape each profiles
        if (profile["link"] in f_url):
            count+=1
            # print(profile)
        else:
            print(profile)
            temp_profiles.append(profile)
profiles=temp_profiles
print(len(profiles),count)
exit()
def get_id(source):

    soup = BeautifulSoup(source, 'html5lib')
    id=[]
    allspan=soup.find_all("button",    class_="artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--2 artdeco-button--tertiary ember-view expandable-list__button expandable-list__button--standard")
    for i in allspan:
        button_text=str(i.find("span",  class_="artdeco-button__text").text).strip()
        if(button_text=="Show more"):
        # if(i['aria-expanded']=="false"):
            id.append(i['id'])
        # print(i['aria-expanded'])
    return id
def get_skill():
    contents=""
    with open('data/temp/eachprofile.html', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html5lib')
    id=[]
    allspan=soup.find_all("button",    class_="expandable-list__button")
    for i in allspan:
        try:
            if("skills" in i.text):     
                id.append(i['id'])
                # print(i.text)
                # print(i['id'])
        except:
            pass

    return id

# with open("data/temp/eachprofile.html","r") as f:
#     source=get_id(f.read())

# print(source)
# exit()
def is_show():
    with open("data/temp/eachprofile.html","r") as f:
        source=f.readlines()
    count=0
    for idx,i in enumerate(source):
        if(i.strip()=="Show more"):
            print(i.strip())
            count+=1
                
    return count
def check_summary():
    with open("data/temp/eachprofile.html","r") as f:
        source=f.read()
    txt="See more of summary"
    count=0
    while(source.find(txt)>=0):
        start=source.find(txt)
        count+=1
        source=source[:start]+source[start+len(txt):]
    return count
def check_skill():
    count=0
    with open("data/temp/eachprofile.html","r") as f:
        source=f.read()
    pattern=re.compile(r'Show all .* skills')
    matches=pattern.finditer(source)
    for i in matches:
        # print(i.group())
        count+=1
    return count



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()

    page.goto("https://www.linkedin.com/uas/login-cap")
    page.get_by_label("Email or Phone").click()

    for i in "dipinthomas004@gmail.com":
        a=random.randint(30,50)
        time.sleep(a/100)
        page.get_by_label("Email or Phone").type(i)

    page.get_by_label("Password").click()
    for i in "Jinz@5792":
        a=random.randint(30,50)
        time.sleep(a/100)
        page.get_by_label("Password").type(i)
    
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Select BOLGATTY TECHNOLOGIES PRIVATE LIMITED- Global Recruiter Corporate contract").click()
    time.sleep(2)
    
    for profile in profiles:#scrape each profiles
        # while(not net.is_connected()):
        #      time.sleep(1)
        #     print("NO network :(")
        #     pass
        # if (profile["link"] in f_url):
        #     count+=1
        #     continue
        page.goto(profile["link"])
        time.sleep(4)

        #  scroll screenn
        for i in range(5):
            time.sleep(1)
            page.mouse.wheel(0, 1000)
        
        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
            f.writelines(source)
        
        # input("enter for summary")
        try:
            if (check_summary()>0):
                page.get_by_role("button" ,name="See more of summary").click()
        except:
            errorfiles.append(profile["link"])


        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
            f.writelines(source)

        ids=get_id(source)
        for id in ids:
            page.locator("#"+id).click()
            time.sleep(0.5)

        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
            f.writelines(source)

        
        ids=get_id(source)
        for id in ids:
            page.locator("#"+id).click()
            time.sleep(0.5)
            ids=get_id(source)

        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
            f.writelines(source)

        
        ids=get_id(source)
        for id in ids:
            page.locator("#"+id).click()
            time.sleep(0.5)
            ids=get_id(source)
        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
                    f.writelines(source)

        # for i in range(is_show()):
        #     ids=get_id(source)
        #     for id in ids:
        #         page.locator("#"+id).click()
        #         time.sleep(0.5)
        #     # source=page.inner_html('*')
        #     # with open("data/temp/eachprofile.html","w") as f:
        #     #             f.writelines(source)
        #     print("in loop")
        

        if(check_skill()>0):
            skill_ids=get_skill()
            for id in skill_ids:
                print("skill is",id)
                page.locator("#"+id).click()
                time.sleep(2)
        source=page.inner_html('*')
        with open("data/temp/eachprofile.html","w") as f:
                    f.writelines(source)
        # while (source.find("See more of summary")!=-1):
        #     page.locator("#"+"line-clamp-show-more-button").click()
        #     time.sleep(0.5)
        #     print("summoery")
        #     source=page.inner_html('*')

        with open("data/source/candidate_source/candidate"+str(count)+".html","w") as f:
            f.writelines(source)
        with open("log/finishedurl.txt","a") as f:
            f.write(str(count)+"#"+profile["link"]+"\n")
        count+=1
        print(count)
        # print("enter a button")
        # input()
        # for i in page.locator("button",has_text="Show more"):
        #     i.click()
        #     input()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# main_json["data"]=data
with open("log/eroorfiles.txt","w") as f:
        f.writelines(errorfiles)
