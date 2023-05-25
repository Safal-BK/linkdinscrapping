from bs4 import BeautifulSoup
import json

import os
from os import path
from glob import glob  



single_json={

}

def extract_data(file_path):
    contents=""
    with open(file_path, 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html5lib')
    try:
        name=soup.find("div",class_="artdeco-entity-lockup__title ember-view")
        name=name.text.strip()
        single_json["name"]=name
    except:
        pass
    try:
        designation=soup.find("div",class_="artdeco-entity-lockup__subtitle ember-view")
        designation=designation.text.strip()
        single_json["designation"]=designation
    except:
        pass
    try:
        current_employer=soup.find("div",class_="artdeco-entity-lockup__caption ember-view")
        current_employer=current_employer.span.text.strip()
        single_json["current_employer"]=current_employer
    except:
        pass
    try:
        latest_education=soup.find("div",class_="artdeco-entity-lockup__caption ember-view")
        latest_education=latest_education.find_all("span")[1].text.strip()
        single_json["latest_education"]=latest_education
    except:
        pass
    try:
        location=soup.find("div",class_="artdeco-entity-lockup__metadata ember-view")
        location=location.find_all("div")[0].text.strip()
        single_json["location"]=location
    except:
        pass
    try:
        curent_sector=soup.find("div",class_="artdeco-entity-lockup__metadata ember-view")
        curent_sector=curent_sector.find_all("span")[0].text.strip()
        single_json["curent_sector"]=curent_sector
    except:
        pass
    try:
        summary=soup.find("span",class_="lt-line-clamp__raw-line")
        summary=summary.text
        single_json["summary"]=summary
    except:
        pass
    experience=[]
    ul=soup.find_all("ul",    class_="expandable-list-profile-core__list artdeco-list")
    lis=ul[0].find_all("li")
    # print(lis[0])
    for li in lis:
        try:
            exp_post=li.find("a",class_="ember-view position-item__position-title-link").text
            exp_company=(li.find("a",class_="position-item__company-link").text).strip()
            exp_full_time=(li.find("dd",class_="background-entity__summary-definition--subtitle"))
            exp_full_time=exp_full_time.find_all("span")[1].text.strip()
            exp_period=(li.find("dd",class_="background-entity__summary-definition--date-duration"))
            exp_period=exp_period.text.strip().split("\n")
            total_period=exp_period[2].strip()
            exp_period=exp_period[0].strip()

            exp_company_location=(li.find("dd",class_="background-entity__summary-definition--location")).text.strip()
            
            exp_blob=(li.find("dd",class_="background-entity__summary-definition--description")).text.strip()
            exp_skills=(li.find("div",class_="background-entity__skills-container")).text.strip()
            experience.append({
                "post":exp_post,
                "company":exp_company,
                "type":exp_full_time,
                "period":exp_period,
                "total_period":total_period,
                "company_location":exp_company_location,
                "blob":exp_blob,
                "skills":exp_skills
            
            })
        except:
            pass

    single_json["experience"]=experience

    edu=[]
    ul=soup.find_all("ul",    class_="background-section__list")
    lis=ul[0].find_all("li")
    # print(lis[0])
    for li in lis:
        try:
            edu_school_name=li.find("a",class_="background-entity__school-link").text

            edu_degree=(li.find("dd",class_="background-entity__summary-definition")).text.strip()
            edu_degree=edu_degree.split('\n')
            education=""
            for i in edu_degree:
                i=i.strip()
                if(i!=""):
                    education=education+i.strip()+"\n"
        # print(education)
        except:
            pass
        

        # try:
        #     pass
        # except:
        #     pass
        try:
            edu_timespan=(li.find("dd",class_="background-entity__summary-definition--date-duration")).text.strip()
            edu_blob=(li.find("dd",class_="background-entity__summary-definition--description")).text.strip()
            edu.append({
                "school_name":edu_school_name,
                "degree":education,
                "timespan":edu_timespan,
                "blob":edu_blob
            })
        except:
            pass
        

    single_json["education"]=edu
    try:
        lis=soup.find_all("li" ,class_='skill-entity__wrapper')
        skills=""
        for li in lis:
            i=li.dl.dt.text.strip()
            if(i!=""):
                skills=skills+i+"\n"
    except:
        pass
    
    single_json["skills"]=skills

    try:
        lis=soup.find("div" ,class_='personal-info__content')
        personal_link=lis.a.span.text.strip()
        single_json["personal_link"]=personal_link
    except:
        pass


    # print(skills)
    with open("databse.json","w") as f:
        f.writelines(json.dumps(single_json))
    
    return single_json


project_path=os.getcwd()
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))


texts=find_ext(os.path.join(project_path,"source"),"html")
for text in texts:
    path=text
    name=text.split("/")[::-1][0]
    print(name)
    print(json.dumps(extract_data(path)))
    break
    








