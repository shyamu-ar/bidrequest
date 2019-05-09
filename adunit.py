
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



import pdb

url = "http://consolebeta.vertoz.com/index.html" #beta
# url = "https://console.vertoz.com" #live
# driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
def login(name,password):
    driver.find_element_by_id("Emailid").send_keys(name)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("Login").click()
    driver.implicitly_wait(10)
    try:
        my_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"vertozmenu4")))
        #find_element=driver.find_element_by_id("vertozmenu4")
        print("successfully Login")
        driver.implicitly_wait(10)
    except:
        print("Internal Server Error")

def create_Adunit():
    adunit=driver.find_element_by_id("vertozmenu4").click()
    new_adunit = driver.find_element_by_link_text("Ad Unit Management").click()
    driver.implicitly_wait(10)
    add_new_ad_unit = driver.find_element_by_xpath("//*[@id='page-content']/div[2]/div[4]/a").click()
    driver.implicitly_wait(10)
    client_name = driver.find_element_by_id("newclientdropdown").send_keys("sabyasachii chatterjee")
    client = driver.find_element_by_xpath("//*[@id='ClientListes']/div/div/ul/li/a").click()
    site = driver.find_element_by_id("website").send_keys("filmgrapevine.com")
    actual_site = driver.find_element_by_link_text("filmgrapevine.com - (12939)").click() #beta
    # actual_site = driver.find_element_by_link_text("filmgrapevine.com - (14221)").click()  #live
    driver.implicitly_wait(10)
    # elem = driver.find_element_by_id("square-300x250")
    # elem = driver.find_elements_by_css_selector("#square-300x250")
    # elem = driver.find_element_by_css_selector("input[name='square-300x250'][value='3']").click()
    # elem = driver.find_element_by_xpath("//input[@name='square-300x250' and @value='3']").click()
    elem = driver.find_element_by_xpath("//input[@id='square-300x250']").click()
    # elem = driver.find_elements_by_xpath("//*[@id='square-300x250']").click()
    submit = driver.find_element_by_id("PageAds").click()
    try:
        my_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "+ Add New Ad Unit")))
        print("Adunit created Successfully !!!!")
        client_tag = driver.find_element_by_xpath("//*[@id='maintbl']/div/table/tbody/tr[1]/td[6]/a/b").text
        if client_tag == "Sabyasachii Chatterjee (22094)":
            Adunit_tag = driver.find_element_by_xpath("//*[@id='maintbl']/div/table/tbody/tr[1]/td[5]").text
            print(Adunit_tag)
        else:
            print("Adunit created in first row of different client")
            second_client_tag = driver.find_element_by_xpath("//*[@id='maintbl']/div/table/tbody/tr[2]/td[6]/a/b").text
            if second_client_tag == "Sabyasachii Chatterjee (22094)":
                Adunit_tag = driver.find_element_by_xpath("//*[@id='maintbl']/div/table/tbody/tr[2]/td[5]").text
                print(Adunit_tag)
    except:
        print("Error while creating adunit")
        # driver.find_element_by_xpath("//*[@id='page-content']/div[2]/div[4]/a")

# login("alliance@vertoz.com","vertoz$123") # beta
# login("qa-team@vertoz.com","GVzAWLib") #live
login("qa-team@vertoz.com","qa-team8") #beta
create_Adunit()
#
# # Ignore
# #adsize = driver.find_element_by_xpath("//input[@name='square-300x250' and @checklist-value='3'")
#     #adsize.click()
# # Sabyasachii Chatterjee (22094)
# # python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
# # print(client)
#     # select = Select(driver.find_element_by_id("ClientListes"))
#     # select.select_by_visible_text('sabyasachii chatterjee')
#     # client=driver.find_elements_by_xpath("//*[@id='ClientListes']/div/div/ul/li/a")
#     # client.click()
print("Its done")
