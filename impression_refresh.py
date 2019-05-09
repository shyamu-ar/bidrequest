from selenium import webdriver
from datetime import datetime

url = input("Enter complete url including https : ")
impressions = int(input("Enter no of times to refresh : "))
no_of_tabs = int(input("Enter of tabs required want to open : "))
tag_id = input("Enter unique tag_id/word to identify from page source : ")
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
assert (tag_id in driver.page_source)
print("Element found , page loaded")
driver.implicitly_wait(3)
start_time = datetime.now()
print(start_time)
count = 1

def iframe():
    iframe1 = driver.find_elements_by_tag_name('iframe')[0]  # Index of 1st iframe
    driver.switch_to_frame(iframe1) # switching to iframe
    name = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src') # getting impression url
    split1 = name.split('&') # converting string in to list
    with open('page_data.txt', 'a') as f: # opening the excel file
        f.write(f"{split1[1]} \n")  #appending campaign id in excel
    f.close() # closing the excel file

for i in range(1,no_of_tabs):
    driver.execute_script("window.open('');") #opens new windows
    driver.switch_to_window(driver.window_handles[i])  # switch to opened new window
    driver.get(url) # calling the url
    driver.implicitly_wait(2)
    iframe() # pre-defined function
    count += 1
print(count)
j = 0
for window in range(impressions):   # looping refresh until reaching impression limit
    if count< impressions: # checks impression count
        driver.switch_to_window(driver.window_handles[j]) # switch to new window
        driver.refresh()  # refresh the page
        iframe() # pre-defined function to get campaign id
        count +=1  # increasing the count of impression by 1
        print(count) # printing count
        j += 1 # increasing the value of tab_window
        if j == no_of_tabs: # if the value reach more than tab_window then reset it to 0
            j = 0
    else: #if impression limit is reached then will exit the for loop
        break
end_time = datetime.now()
total_time = end_time - start_time # To get total time to run this cron
print(total_time)
driver.quit() # To close browser including all tabs
