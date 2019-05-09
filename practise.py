# from selenium import webdriver
# from datetime import datetime
# import threading
# from threading import *
# impressions = int(input("Enter no of impressions: "))  # Inputting no of impressions required
# no_of_tabs = int(input("Enter of tabs required: "))     # No of tabs to be opened
# tag_id = input("Enter your tag_id: ")       # If Tag_id inserted on page or not
# start_time = datetime.now()
# print(start_time)
# url = "http://filmgrapevine.com/beta1.html"
# driver = webdriver.Chrome()
# driver.minimize_window()
# driver.get(url)
# count = 1
# for i in range(1,3):  # this method only for opening the tabs
#     driver.execute_script("window.open('');") #opens new windows
#     driver.switch_to_window(driver.window_handles[i])  # switch to opened new window
#     driver.get(url) # calling the url
#     count += 1
# print(count)
# j = 0
# for window in range(impressions):   # looping refresh until reaching impression limit
#     if count< impressions: # checks impression count
#         driver.switch_to_window(driver.window_handles[j])
#         driver.refresh()
#         assert (tag_id in driver.page_source)
#         print("Element found , page loaded")
#         iframe1 = driver.find_elements_by_tag_name('iframe')[0]  # Index of 1st iframe
#         driver.switch_to_frame(iframe1)  # switching to iframe
#         name = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src')  # getting impression url
#         split1 = name.split('&')  # converting string in to list
#         with open('page_data.txt', 'a') as f:  # opening the excel file
#             f.write(f"{split1[1]} \n")  # appending campaign id in excel
#         f.close()  # closing the excel file
#         count +=1
#         print(count)
#         j += 1
#         if j == no_of_tabs:
#             j = 0
#     else:
#         break
# end_time = datetime.now()
# total_time = end_time - start_time
# print(total_time)
# driver.quit()
#
# #
# # iframe = driver.find_elements_by_tag_name('iframe')[0]
# #         driver.switch_to_frame(iframe)
# #         driver.implicitly_wait(5)
# #         elem = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src')
# #         split = elem.split('&')
# # with open('page_data.txt', 'a') as f:
# #     f.write(f"{split1[1]} \n")
# # f.close()
#
# import urllib.parse
# text = "%%CLICK_URL_ESC%%https%3A%2F%2Fclk.vrtzads.com%2Fbidderclick%2Fclick%2Fay7IxQeVk_guQXAoDO-zCQ%2FimuvNubf9jc8Qi63QyfUoQ%2Fd1918786-6173-44ba-8189-92192f45b04b_1%2F1149%2FnKUwfj1q7Xfs3N1PG-GRpw%2F0%3Fck%3D45.120.89.0Mozilla%252F5.0%2B%2528Windows%2BNT%2B6.3%253B%2BWin64%253B%2Bx64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F64.0.3282.186%2BSafari%252F537.36%26ac%3D%26ip%3D45.120.89.0%26h%3Dfilmgrapevine.com%26sclk%3D%26stat%3DMaharashtra%26dt%3Ddesktop%26pc%3D413703%26o%3Dwindows%26ov%3D8.1%26dm%3D%26cat%3D%26ap%3D1%26br%3Dchrome%26hr%3D4%26sn%3D%26cu%3Dindia%26ci%3Dahmednagar%26dmf%3D%26ssn%3DGoogle%2BAdx_SSP%26con%3DCable%252FDSL%26ti%3D4189539504%26isp%3DKumar%2BConstructions%26s%3D300x250%26m%3D1%26r%3DAXLLdS5mMs59lZkscfCsXrhVX8___BxImfSDKlGGUpfbgQIVEZdqcoYn3NTOih0xQJDVvYkyMvaLiPX184Z76jJXHDeGg-smI56jlotKjR77jt2GkvODByq5cwYnE2vj3S2EqMQf7cl-gkVK21wbPPdjh9A3iUUV80YM6K8f9cBgeVP8NYhqeJk2v3LlzYhE2CGsXlBo9iq1o2j7EbmZ6fmaSKCMEB4d5za0MkQzRfR40vfSdysq9v29soyacD_5tUfvpkFSKYPKpc7V_HghmHFx1Lm0Ye4wrpnJDkZffxtNl5Zovd47J15lFRee_l5zRx1IcaW_B-fOzcVRNs0TczlNykMutcuA0Mz4VQMDX2UTaU_nUrTnIsn22EI7QcxAy1TYbx5Uxj3wMQjoUXcMYUBMJFNx0kTZEEO9WuZBex4eJoEnd-drPGiOnDU6CYToq4DG1-CF_ll7DmUAFVlqe0vfN4lGwka3l_8fGm7Y-p-GQ4w5SRR77ruU22hC7PdIZLLHSXtzwO5k9bczFnSYRaDVbjjH7-HTb0odJbinCS6oISXD1TRwrcxFBiyjfa5xHIuM5duGkqRzZjOrWnDfUw"
# print(urllib.parse.unquote(text))

# import Workbook
from openpyxl import Workbook
wb = Workbook()
filepath = "/home/tr-dt-096/Shyamu/Python_programs/demo.xlsx"
wb.save
# try:
#     workbook = xlsxwriter.Workbook('home/tr-dt-096/Shyamu/Python_programs/demo.xlsx')
#     print("File created!!")
# except:
#     print("Unable to create!!! ")
# worksheet = workbook.add_worksheet()

print("hello")