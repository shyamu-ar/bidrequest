from selenium import webdriver
from datetime import datetime
import threading
impressions = int(input("Enter no of impressions: "))  # Inputting no of impressions required
no_of_tabs = int(input("Enter of tabs required: "))     # No of tabs to be opened
tag_id = input("Enter your tag_id: ")       # If Tag_id inserted on page or not
start_time = datetime.now()
print(start_time)
url = "http://filmgrapevine.com/beta1.html"
driver = webdriver.Chrome()
driver.minimize_window()
driver.get(url)
count = 1
for i in range(1,no_of_tabs):  # this method only for opening the tabs
    driver.execute_script("window.open('');") #opens new windows
    driver.switch_to_window(driver.window_handles[i])  # switch to opened new window
    driver.get(url) # calling the url
    count += 1
print(count)
j = 0
for window in range(impressions):   # looping refresh until reaching impression limit
    if count< impressions: # checks impression count
        driver.switch_to_window(driver.window_handles[j]) # Switching the tab
        driver.refresh() # refresh the page
        assert (tag_id in driver.page_source)  # Find the tag_id in page
        print("Element found , page loaded")
        iframe1 = driver.find_elements_by_tag_name('iframe')[0]  # Index of 1st iframe
        driver.switch_to_frame(iframe1)  # switching to iframe
        # name = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src')  # getting impression url
        name = driver.find_element_by_xpath("//*[contains(@id,'')]/img[5]").get_attribute('src')  # getting impression url
        print(name)
        # split1 = name.split('&')  # converting string in to list
        with open('page_data.txt', 'a') as f:  # opening the excel file
            f.write(f"{name} \n")  # appending campaign id in excel
        f.close()  # closing the excel file
        count +=1
        print(count)
        j += 1
        if j == no_of_tabs:
            j = 0
    else:
        break
end_time = datetime.now()
total_time = end_time - start_time # to get total time taken to run cron
print(total_time)
driver.quit()

#
# iframe = driver.find_elements_by_tag_name('iframe')[0]
#         driver.switch_to_frame(iframe)
#         driver.implicitly_wait(5)
#         elem = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src')
#         split = elem.split('&')
# with open('page_data.txt', 'a') as f:
#     f.write(f"{split1[1]} \n")
# f.close()