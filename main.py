from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
driver = webdriver.Firefox(executable_path=r"C:\Users\user\Desktop\upwork\drivers\geckodriver.exe")
driver.get("https://www.mykybella.com/find-a-specialist")
all_data = []
with open('content.csv') as file:
    data = csv.reader(file)
    for row in data :
        if row[len(row)-1] != 'ZipCode':
            try:

                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(7)
                driver.find_element_by_xpath("//input[@id='fadSearchInput']").clear()
                print(" loading...please wait a moment")
                for i in range(0,50):
                    driver.find_element_by_xpath("//input[@name='searchRadius']").send_keys(Keys.LEFT)
                    if i%4==0 :
                        time.sleep(3)
                time.sleep(6)
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                driver.find_element_by_xpath("//input[@id='fadSearchInput']").clear()
                driver.find_element_by_xpath("//input[@id='fadSearchInput']").send_keys(row[len(row)-1])
                time.sleep(5)
                driver.find_element_by_xpath("//button[@id='searchButton']").click()
                time.sleep(5)
                for i in range(1,52):
                    
                    driver.find_element_by_xpath("//input[@name='searchRadius']").send_keys(Keys.RIGHT)
                    time.sleep(5)
                    div = driver.find_element_by_xpath("//div[@id='locator_root']")
                    container = div.find_element_by_xpath("//div[@id='container']")
                    elements = container.find_elements_by_xpath('//h4[@class="provider-card__content__display-name"]')
                    if len(elements) != 0 :
                        html_source = driver.page_source
                        soup = BeautifulSoup(html_source,'lxml')
                        container_el = soup.find("div", {"id": "container"})
                        account_1 = container_el.find_all(class_="provider-card")
                        account_2 = container_el.find_all(class_="provider-card flipInX")
                    try :
                        if len(account_1) != 0 :
                            for x in account_1 :
                                
                                name = x.find('h4').text
                                address = x.find(class_ = "address").text
                                address = address.replace('\n',"")
                                phone = x.find(class_ = 'phone').text
                                contact_links = x.find(class_ = 'contact_links').find_all('a', href=True)
                                direction = contact_links[0]['href']
                                website = contact_links[1]['href']
                                Email = contact_links[2]['href']
                                Email = Email.replace('mailto:',"")
                                
                                data = {
                                    'name': name,
                                    'address' : address,
                                    'phone': phone,
                                    'direction': direction,
                                    'website': website,
                                    'Email' : Email

                                }
                                print(data)
                                all_data.append(data)
                                df = pd.DataFrame(all_data)
                                df.to_csv("data.csv")  
                        if len(account_2) != 0 :
                            for x in account_2 :
                                
                                name = x.find('h4').text
                                address = x.find(class_ = "address").text
                                address = address.replace('\n',"")
                                phone = x.find(class_ = 'phone').text
                                contact_links = x.find(class_ = 'contact_links').find_all('a', href=True)
                                direction = contact_links[0]['href']
                                website = contact_links[1]['href']
                                Email = contact_links[2]['href']
                                Email = Email.replace('mailto:',"")

                                data = {
                                    'name': name,
                                    'address' : address,
                                    'phone': phone,
                                    'direction': direction,
                                    'website': website,
                                    'Email' : Email

                                }
                                print(data)    
                                all_data.append(data)
                                df = pd.DataFrame(all_data)
                                df.to_csv("data.csv")  
                        
                                
                        else :
                            print('no data')
                    except:
                        pass          
            except : 
                print('some probleme retry again ..')
        
        
