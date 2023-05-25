from playwright.sync_api import Playwright, sync_playwright, expect
import time
import test
import json
import os
import lib.network as net

# from tqdm import tqdm
PROJECT_PATH=os.getcwd()
# dipinthomas004@gmail.com
# Jinz@5792
# command
#  playwright codegen --load-storage=state.json https://www.linkedin.com/uas/login-cap
main_json={

}
data=[]


def run(playwright: Playwright) -> None:
    page_count=0

    with open(PROJECT_PATH+"/config/config.json","r")as f:
        page_js=json.loads(f.read())
        page_count=page_js["count"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    # user_data_path=os.getcwd()
    # browser = playwright.chromium.launch_persistent_context(user_data_path,headless=False)
    # page = browser.new_page()
    page.goto("https://www.linkedin.com/uas/login-cap")
    page.get_by_label("Email or Phone").click()
    page.get_by_label("Email or Phone").fill("dipinthomas004@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Jinz@5792")
    page.get_by_role("button", name="Sign in").click()

    # storage = context.storage_state(path="state1.json")
    # with open("contextbk.json","w") as f:
    #     f.write(str(storage))


    page.get_by_role("button", name="Select BOLGATTY TECHNOLOGIES PRIVATE LIMITED- Global Recruiter Corporate contract").click()
    
    page.get_by_placeholder("Start a new search…").click()
    page.get_by_placeholder("Start a new search…").fill("asml")
    page.get_by_placeholder("Start a new search…").press("Enter")
    page.get_by_role("button", name="Companies or boolean").click()
    page.get_by_placeholder("enter a company or boolean…").fill("asml")
    page.get_by_role("option", name="ASML", exact=True).get_by_text("ASML").click()
    gen_url=page.url

    gen_url.replace(gen_url.split("&")[::-1][1],"start=49000")

    input()
    page.goto(gen_url.replace(gen_url.split("&")[::-1][1],"start=49000"))
    # input("jdif")
    # page.locator(".mini-pagination__quick-link").click()
    # input("dcdsfsdfsdfsdfsd")
    
    for i in range(49000):
        while(not net.is_connected()):
            time.sleep(1)
            print("NO network :(")
            pass
        print(i)
        for i in range(10):
            time.sleep(2)
            page.mouse.wheel(0, 1000)
        ob_html=page.inner_html('*')
        with open("data/source/link_source/page"+str(page_count)+".html","w") as f:
            f.writelines(ob_html)
        page_count+=1
        # input()
    #     page.locator("//*[@class]/div[2]/a",has_text="Next").click()
        page.locator(".mini-pagination__quick-link").click()

        time.sleep(2)
        with open(PROJECT_PATH+"/config/config.json","w")as f:
            page_js["count"]=page_count
            f.write(json.dumps(page_js))
    #     # input()



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
    # try:
        
    # except:
        # print("playwright error")
# main_json["data"]=data
# with open("main_database.json","w") as f:
#         f.writelines(json.dumps(main_json))
# ['Manish Pardeshi', 'Nazim Zeki Ugur', 'Ved Prakash', 'Lucas Dias', 'Serkan D.',
#  'Ganesh S', 'Thiago Silva', 'Ahmed Adel', 'PS SANTHOSH', 'Brook Gebremedhin',
#  'Dillip Kumar Bhanja', 'Yu-Che Hsiao, PhD', 'Haridas Sagar', 'Nikolai Smirnov',
#  'Karst Brummelhuis', 'Miguel Rueda Cuerda', 'Christian Bakker', 'Bas Mevissen',
#  'Miquel Espada', 'Shiv kumar Yadav', 'Manoj Gayadin']