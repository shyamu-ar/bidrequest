
# number = int(input("Enter number: "))
# raiseto = int(input("Enter raise to number : "))
# total = number
# for i in range(1,raiseto):
#     total *= number
# print(total)

# defined_list = list(range(1,101))
# user_list = input("Enter your list with comma seperated").split(",")
# print(type(user_list))
# not_available = []
# for element in user_list:
#     num = int(element)
#     if num in defined_list:
#         if not num in not_available:
#             not_available.append(num)
# print(not_available)

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# url = "http://filmgrapevine.com/beta.html"
# driver.get(url)
# iframe = driver.find_elements_by_tag_name('iframe')[0]
# driver.switch_to_frame(iframe)
# driver.implicitly_wait(5)
# elem = driver.find_element_by_xpath("//*[contains(@id,'vz-wrapper')]/img[1]").get_attribute('src')
# split = elem.split('&')
# with open('page_data.txt', 'a') as f:
#     f.write(split[1])
# f.close()
# driver.implicitly_wait(5)
# driver.close()

# import sys
# import os
# def run_command(command):
#     print("Running command: {}".format(command))
#     os.system(command)
#
# commands = "ssh -i Downloads/webairbetakey centos@103.14.99.180 -p 7559 -v"
# second_command = "sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config;"
# third_command = "sudo systemctl restart sshd"
# run_command(commands)
# run_command(second_command)
# run_command(third_command)
# run_command(commands)



# def animal_crackers(text):
#     worldlist = text.split()
#     return worldlist[0][0] == worldlist[1][0]
# animal_crackers("Shyamu Shyamu")


# /**
# *
# */
# package com.BannerCron.Util;
#
# /**
# * @author vertx-002
# *
# */
#
# import java.io.UnsupportedEncodingException;
# import java.net.URLDecoder;
# import java.net.URLEncoder;
# import java.util.Scanner;
#
# import javax.crypto.Cipher;
# import javax.crypto.spec.IvParameterSpec;
# import javax.crypto.spec.SecretKeySpec;
#
# import org.apache.commons.codec.binary.Base64;
#
# public class Encryptor {
#
# static final String key1 = "v$rt0zi789456123"; // 128 bit key
# static final String key2 = "v$rt0zSecretkey1";
#
# public static String encryptAndEncode(String value) {
# try {
# IvParameterSpec iv = new IvParameterSpec(key2.getBytes("UTF-8"));
#
# SecretKeySpec skeySpec = new SecretKeySpec(key1.getBytes("UTF-8"),
# "AES");
# Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
# cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);
# byte[] encrypted = cipher.doFinal(value.getBytes("UTF-8"));
# return URLEncoder.encode(Base64.encodeBase64URLSafeString(encrypted),"UTF-8");
# } catch (Exception ex) {
# ex.printStackTrace();
# }
# return null;
# }
#
# public static String decodeAndDecrypt(String encrypted) {
# try {
# encrypted = URLDecoder.decode(encrypted, "UTF-8");
# IvParameterSpec iv = new IvParameterSpec(key2.getBytes("UTF-8"));
#
# SecretKeySpec skeySpec = new SecretKeySpec(key1.getBytes("UTF-8"),
# "AES");
# Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
#
# cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);
# byte[] original = cipher.doFinal(Base64.decodeBase64(encrypted));
#
# return new String(original);
#
# } catch (Exception ex) {
# ex.printStackTrace();
# }
# return null;
# }
#
# public static void main(String[] args) throws UnsupportedEncodingException {
# System.out.println("Enter 1 for Encryption : ");
# System.out.println("Enter 2 for Decryption : ");
# Scanner sc = new Scanner(System.in);
#
#
# if (condition) {
#
# }
# System.out.println("dec :"+decodeAndDecrypt("5MLNEpGzO7gwalnznOcLBg"));
# }
#
# }
#
# from datetime import date
# date = date.today()
# print(date)
# file_path = "/home/tr-dt-096/Downloads/"
# file_name = "bidderserver"
# # file_path = input("Copy & paste your complete file path without file name ")
# # file_name = input("Enter your file name : ")
# file = f"mv bidderServer /home2/backup/{file_name}{date.today()}"
#
# print(file)

# auction_price = 0.4
# adm = ["find to went away&p &p"]
# actual_adm_url = adm.replace("&p", f"&p={auction_price}")
# print(actual_adm_url)

import requests
import datetime
import xlsxwriter
#import xlsxwriter
#workbook = xlsxwriter.Workbook('torcai.xlsx')
import json
import urllib.parse  # For decode url utf-8
from threading import Thread

action_on_text_file = int(input("Enter \n1 - To erase previous data on file.\n2 - To append data in the file\n"))
if action_on_text_file == 1:
    with open('impression.txt', 'w') as f:  # opening the excel file
        pass
print(" SSP IDS\n 1 - Vertoz \n 2 - Bidswitch \n 3 - Google")
ssp_id = int(input("Enter ssp id : "))
print(" MEDIA CHANNEL IDS\n 1 - Display\n 2 - Mobile\n 3 - Vast\n 4 - Native")
media_channel_id = int(input("Enter media channel : "))
impressions = int(input("Enter number of Impressions required : "))
count = 1
Start_time = datetime.datetime.now()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
with open('impression.txt', 'a') as f:  # opening the excel file
    f.write(f"\nDate : {Start_time}")  # appending campaign id in excel

def postman_request(ssp,media_channel):
    global count
    if ssp == 1:
        if media_channel == 1 or media_channel == 2:
            auction_price = input("Enter auction_price to be replaced with : ")  # Auction_price to be replaced with
            # endpoint_url = input("Please Paste endpoint url : ")  # Endpoint url along with ssp_id
            endpoint_url = "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")  # bid_request or json
            tmpjson = f'''{bidrequest}'''  # converting string to json format
            json = tmpjson.replace('\'', '\"')  # converting string to json format
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)  # post request
                response_status = response.status_code  # to get status after requesting
                # response_url = response.json()
                if response_status == 200:  # condition to check response
                    response_url = response.json()

                    ####################################### NURL ##################################################
                    actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]  # Getting nurl
                    # actual_nurl = actual_nurl.replace("&p=", f"&p={auction_price}&") # For vertoz_ssp no need to replace auction_price in nurl
                    # print(actual_nurl)
                    try:
                        print(f"\n{actual_nurl}")
                        actual_n_url_response = requests.get(actual_nurl, verify=True,
                                                             headers=headers)  # making get request for nurl
                        print(f"NURL response : {actual_n_url_response}\n")  # printing the response of nurl
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(
                                f"\n{actual_nurl}\nNurl : {actual_n_url_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for NURL   *****")
                        print("*****   Please check   *****\n")

                    ####################################### ADM ##################################################
                    trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                    first_part_split = trim_adm_url.split("adm='")[
                        1]  # spliting a string into list and assign 1 index to variable
                    second_part_split = first_part_split.split(" id=")[
                        0]  # Again spliting the last character to get actual adm url
                    actual_adm_url = second_part_split.replace("&p=${AUCTION_PRICE}&",
                                                               f"&p={auction_price}&")  # replacing auction price here
                    try:
                        print(actual_adm_url)  # printing adm url
                        adm_url_response = requests.get(actual_adm_url, verify=True,
                                                        headers=headers)  # Using get method request for adm url
                        print(f"ADM response : {adm_url_response}\n")  # printing the response of adm url
                        adm_response = adm_url_response.text  # storing adm response for further
                    except:
                        print("*****   Not getting 200 ok for ADM   *****")
                        print("*****   Please check   *****\n")

                    ###################################### Impression ############################################
                    imp_first_part_split = adm_response.split("<img src=", 2)[
                        1]  # using adm response spliting to get impression url
                    # partial_impression_url = str(imp_first_part_split[1])
                    # print(partial_impression_url)
                    impression_url = imp_first_part_split.rstrip(
                        " width=\"1\" height=\"1\" />")  # triming right side data to get impression url
                    final_impression_url = impression_url.lstrip("\"")  # triming left side data to get impression url
                    try:
                        print(final_impression_url)  # to print impression url
                        imp_response = requests.get(final_impression_url, verify=True,
                                                    headers=headers)  # requesting get method for impression url
                        print(f"Impression response : {imp_response}\n")  # printing impression url
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"Impression : {imp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for Impression_url   *****")
                        print("*****   Please check   *****\n")

                    ################################## CDN Impression ##########################################
                    cdnimp_first_part_split = adm_response.split("<img src=", 3)[2]
                    # print(cdnimp_first_part_split)
                    # partial_cdnimp_url = str(cdnimp_first_part_split[2])
                    # print(partial_cdnimp_url)
                    cdnimp_second_part_strip = cdnimp_first_part_split.rstrip(
                        " width=\"1\" height=\"1\" />")  # triming right side cdn impression url
                    cdn_impression_url = cdnimp_second_part_strip.lstrip("\"")  # triming left side cdn impression url
                    try:
                        print(cdn_impression_url)  # to print cdn impression url
                        cdnimp_response = requests.get(cdn_impression_url, verify=True,
                                                       headers=headers)  # requesting cdn impression url by get method
                        print(f"CDN response : {cdnimp_response}\n")  # printing the status of get request
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for CDN   *****")
                        print("*****   Please check   *****\n")

                    #############################  Click URL  #######################################

                    click_url_first_part = adm_response.split("href=")[1]
                    # print(click_url_first_part)
                    # partial_click_url = str(click_url_first_part[1])
                    click_url_second_part = click_url_first_part.split("img id=")[0]
                    # get_click_url = click_url_second_part[0]
                    rstrip_click_url = click_url_second_part.rstrip("\"> <")
                    actual_click_url = rstrip_click_url.lstrip("\"")
                    try:
                        print(actual_click_url)
                        actual_click_url_response = requests.get(actual_click_url, verify=True, headers=headers)
                        print(f"click_url response : {actual_click_url_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for ClickURL   *****")
                        print("*****   Please check   *****\n")
                    print(count)
                    count += 1
                else:
                    print(response)
                    print("\n\n ***** Not getting response, please input valid endpoint and request ***** \n\n")
                    break
            print(f"End_time : {datetime.datetime.now() - Start_time}")
        elif media_channel == 3:
            auction_price = input("Enter auction_price to be replaced with : ")
            endpoint_url = input("Please Paste endpoint url : ")
            # endpoint_url = "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                response_url = response.json()
                # print(response.text)

                ####################################### NURL ##################################################
                actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
                # actual_nurl = actual_nurl.replace("&p=", f"&p={auction_price}&") # For vertoz_ssp no need to replace auction_price in nurl
                print(actual_nurl)
                try:
                    actual_n_url_response = requests.get(actual_nurl, verify=True, headers=headers)
                    print(f"NURL response : {actual_n_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(
                            f"\n{actual_nurl}\nNurl : {actual_n_url_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for NURL   *****")
                    print("*****   Please check   *****\n")

                ####################################### ADM ##################################################
                trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                rtrim_adm_url = trim_adm_url.split("A[")[1]
                actual_adm_url = rtrim_adm_url.split("]]")[0]
                actual_adm_url = actual_adm_url.replace("&p=${AUCTION_PRICE}&", f"&p={auction_price}&")
                # print(actual_adm_url)
                try:
                    adm_url_response = requests.get(actual_adm_url, verify=True,
                                                    headers=headers)  # Using get method will get status of request
                    print(f"ADM response : {adm_url_response}\n")
                    adm_response = adm_url_response.text
                except:
                    print("*****   Not getting 200 ok for ADM   *****")
                    print("*****   Please check   *****\n")

                ###################################### Impression ############################################
                imp_first_part = adm_response.split("<![CDATA[")[2]
                final_impression_url = imp_first_part.split("]]")[0]
                print(final_impression_url)
                try:
                    imp_response = requests.get(final_impression_url, verify=True, headers=headers)
                    print(f"Impression response : {imp_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"Impression : {imp_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for Impression_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### CDN Impression ############################################
                cdnimp_first_part = adm_response.split("<![CDATA[")[3]
                final_cdnimpression_url = cdnimp_first_part.split("]]")[0]
                print(final_cdnimpression_url)
                try:
                    cdn_imp_response = requests.get(final_cdnimpression_url, verify=True, headers=headers)
                    print(f"CDN Impression response : {cdn_imp_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"Cdnimpression : {cdn_imp_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CDN Impression_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### Cookie_Sync ############################################
                cookie_first_part = adm_response.split("<![CDATA[")[4]
                cookie_sync_url = cookie_first_part.split("]]")[0]
                print(cookie_sync_url)
                try:
                    cookie_sync_response = requests.get(cookie_sync_url, verify=True, headers=headers)
                    print(f"Cookie_Sync response : {cookie_sync_response}\n")
                except:
                    print("*****   Not getting 200 ok for Cookie_sync_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### Click_URL ############################################
                click_first_part = adm_response.split("<![CDATA[")[6]
                click_url = click_first_part.split("]]")[0]
                print(click_url)
                try:
                    actual_click_url_response = requests.get(click_url, verify=True, headers=headers)
                    print(f"Click Url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CLICKURL   *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1

            print(f"End_time : {datetime.datetime.now() - Start_time}")


        else:
            print(f"Vertoz SSP does not support entered media channel, please try again !!!")

    elif ssp == 2:
        if media_channel == 1 or media_channel == 2:
            auction_price = input("Enter auction_price to be replaced with : ")
            # endpoint_url = input("Please Paste endpoint url : ")
            endpoint_url = "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=973fddb9324e46e598f0099b4a87b661"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                # response_url = response.json()
                if response_status == 200:
                    response_url = response.json()

                    ####################################### NURL ##################################################
                    actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
                    actual_nurl = actual_nurl.replace("&p=${AUCTION_PRICE}&",
                                                      f"&p={auction_price}&")  # For vertoz_ssp no need to replace auction_price in nurl
                    # print(actual_nurl)
                    try:
                        print(actual_nurl)
                        actual_n_url_response = requests.get(actual_nurl, verify=True, headers=headers)
                        print(f"NURL response : {actual_n_url_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(
                                f"\n{actual_nurl}\nNurl : {actual_n_url_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for NURL   *****")
                        print("*****   Please check   *****\n")

                    ####################################### ADM ##################################################
                    trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                    first_part_split = trim_adm_url.split("adm='")[1]  # spliting a string into list
                    # first_part_final = str(first_part_split[1])  # Taking 1 index string and assign it variable
                    actual_adm_url = first_part_split.split(" id=")[0]  # Again spliting the last character to get adm
                    # actual_adm_url = second_part_split[0]  # by this i got adm url
                    # actual_adm_url = actual_adm_url.replace("&p=", f"&p={auction_price}&") # for bidswitch will not replace in adm
                    try:
                        print(actual_adm_url)
                        adm_url_response = requests.get(actual_adm_url, verify=True,
                                                        headers=headers)  # Using get method will get status of request
                        print(f"ADM response : {adm_url_response}\n")
                        adm_response = adm_url_response.text
                    except:
                        print("*****   Not getting 200 ok for ADM   *****")
                        print("*****   Please check   *****\n")

                    ###################################### Impression ############################################
                    imp_first_part_split = adm_response.split("<img src=", 2)[1]
                    # partial_impression_url = str(imp_first_part_split[1])
                    # print(partial_impression_url)
                    impression_url = imp_first_part_split.rstrip(" width=\"1\" height=\"1\" />")
                    final_impression_url = impression_url.lstrip("\"")
                    try:
                        print(final_impression_url)
                        imp_response = requests.get(final_impression_url, verify=True, headers=headers)
                        print(f"Impression response : {imp_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"Impression : {imp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for Impression_url   *****")
                        print("*****   Please check   *****\n")

                    ################################## CDN Impression ##########################################
                    cdnimp_first_part_split = adm_response.split("<img src=", 3)[2]
                    # print(cdnimp_first_part_split)
                    # partial_cdnimp_url = str(cdnimp_first_part_split[2])
                    # print(partial_cdnimp_url)
                    cdnimp_second_part_strip = cdnimp_first_part_split.rstrip(" width=\"1\" height=\"1\" />")
                    cdn_impression_url = cdnimp_second_part_strip.lstrip("\"")
                    try:
                        print(cdn_impression_url)
                        cdnimp_response = requests.get(cdn_impression_url, verify=True, headers=headers)
                        print(f"CDN response : {cdnimp_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for CDN   *****")
                        print("*****   Please check   *****\n")

                    #############################  Click URL  #######################################

                    click_url_first_part = adm_response.split("href=")[1]
                    # partial_click_url = str(click_url_first_part[1])
                    click_url_second_part = click_url_first_part.split("img id=")[0]
                    # get_click_url = click_url_second_part[0]
                    rstrip_click_url = click_url_second_part.rstrip("\"> <")
                    actual_click_url = rstrip_click_url.lstrip("\"")
                    try:
                        print(actual_click_url)
                        actual_click_url_response = requests.get(actual_click_url, verify=True, headers=headers)
                        print(f"click_url response : {actual_click_url_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for ClickURL   *****")
                        print("*****   Please check   *****\n")
                    print(count)
                    count += 1
                else:
                    print(response)
                    print("\n\n ***** Not getting response, please input valid endpoint and request ***** \n\n")
                    break
            print(f"End_time : {datetime.datetime.now() - Start_time}")

        elif media_channel == 3:
            auction_price = input("Enter auction_price to be replaced with : ")
            # endpoint_url = input("Please Paste endpoint url : ")
            endpoint_url = "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=973fddb9324e46e598f0099b4a87b661"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                response_url = response.json()
                # print(response.text)

                ####################################### NURL ##################################################
                actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
                actual_nurl = actual_nurl.replace("&p=${AUCTION_PRICE}&",
                                                  f"&p={auction_price}&")  # For vertoz_ssp no need to replace auction_price in nurl
                print(actual_nurl)
                try:
                    actual_n_url_response = requests.get(actual_nurl, verify=True, headers=headers)
                    print(f"NURL response : {actual_n_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(
                            f"\n{actual_nurl}\nNurl : {actual_n_url_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for NURL   *****")
                    print("*****   Please check   *****\n")

                    ####################################### ADM ##################################################
                actual_adm_url = response_url["seatbid"][0]["bid"][0]["ext"]["vast_url"]
                # actual_adm_url = actual_adm_url.replace("&p=", f"&p={auction_price}&")
                print(actual_adm_url)
                try:
                    adm_url_response = requests.get(actual_adm_url, verify=True,
                                                    headers=headers)  # Using get method will get status of request
                    print(f"ADM response : {adm_url_response}\n")
                    adm_response = adm_url_response.text
                except:
                    print("*****   Not getting 200 ok for ADM   *****")
                    print("*****   Please check   *****\n")

                ###################################### Impression ############################################
                imp_first_part = adm_response.split("<![CDATA[")[2]
                final_impression_url = imp_first_part.split("]]")[0]
                print(final_impression_url)
                try:
                    imp_response = requests.get(final_impression_url, verify=True, headers=headers)
                    print(f"Impression response : {imp_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"Impression : {imp_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for Impression_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### CDN Impression ############################################
                cdnimp_first_part = adm_response.split("<![CDATA[")[3]
                final_cdnimpression_url = cdnimp_first_part.split("]]")[0]
                print(final_cdnimpression_url)
                try:
                    cdnimp_response = requests.get(final_cdnimpression_url, verify=True, headers=headers)
                    print(f"CDN Impression response : {cdnimp_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CDN Impression_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### Cookie_Sync ############################################
                cookie_first_part = adm_response.split("<![CDATA[")[4]
                cookie_sync_url = cookie_first_part.split("]]")[0]
                print(cookie_sync_url)
                try:
                    cookie_sync_response = requests.get(cookie_sync_url, verify=True, headers=headers)
                    print(f"Cookie_Sync response : {cookie_sync_response}\n")
                except:
                    print("*****   Not getting 200 ok for Cookie_sync_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### Click_URL ############################################
                click_first_part = adm_response.split("<![CDATA[")[6]
                click_url = click_first_part.split("]]")[0]
                print(click_url)
                try:
                    actual_click_url_response = requests.get(click_url, verify=True, headers=headers)
                    print(f"Click Url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CLICKURL   *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1
            print(f"End_time : {datetime.datetime.now() - Start_time}")

        elif media_channel == 4:
            auction_price = input("Enter auction_price to be replaced with : ")
            # endpoint_url = input("Please Paste endpoint url : ")
            endpoint_url = "http://webair-bidder-staging.vrtzads.com/vzbidder/bid?exchangeId=973fddb9324e46e598f0099b4a87b661"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                response_url = response.json()
                # print(response.text)
                ####################################### NURL ##################################################
                actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
                actual_nurl = actual_nurl.replace("&p=${AUCTION_PRICE}&",
                                                  f"&p={auction_price}&")  # For vertoz_ssp no need to replace auction_price in nurl
                print(actual_nurl)
                try:
                    actual_n_url_response = requests.get(actual_nurl, verify=True, headers=headers)
                    print(f"NURL response : {actual_n_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(
                            f"\n{actual_nurl}\nNurl : {actual_n_url_response},\t\t")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for NURL   *****")
                    print("*****   Please check   *****\n")

                ####################################### IMPRESSION TRACKER ####################################
                impression_tracker = response_url["seatbid"][0]["bid"][0]["ext"]["native"]["imptrackers"]
                # print(impression_tracker)
                for i in impression_tracker:
                    if "bidwin.vrtzads.com" in i:
                        try:
                            imp_response = requests.get(i, verify=True, headers=headers)
                            print(i)
                            print(f"Impression response : {imp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(f"Impression : {imp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for Impression_url   *****")
                            print("*****   Please check   *****\n")
                    elif "dspimp.vrtzads.com" in i:
                        try:
                            cdnimp_response = requests.get(i, verify=True, headers=headers)
                            print(i)
                            print(f"CDN Impression response : {cdnimp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for CDN Impression_url   *****")
                            print("*****   Please check   *****\n")
                    elif "cookie.vrtzads.com" in i:
                        try:
                            cookie_sync_response = requests.get(i, verify=True, headers=headers)
                            print(i)
                            print(f"Cookie_Sync response : {cookie_sync_response}\n")
                        except:
                            print("*****   Not getting 200 ok for Cookie_sync_url   *****")
                            print("*****   Please check   *****\n")
                    else:
                        print("New url is appended in impression tracker")

                ########################################### CLICKURL ################################
                click_url = response_url["seatbid"][0]["bid"][0]["ext"]["native"]["link"]["url"]
                click_url = click_url.replace("&sclk=${CLICK_URL:URLENCODE}",
                                              "&sclk=")  # For vertoz_ssp no need to replace auction_price in nurl
                print(click_url)
                try:
                    actual_click_url_response = requests.get(click_url, verify=True, headers=headers)
                    print(f"Click Url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CLICKURL   *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1
            print(f"End_time : {datetime.datetime.now() - Start_time}")
        else:
            print(f"Entered media_channel_id is incorrect, please check again !!!!")

    elif ssp == 3:
        if media_channel == 1 or media_channel == 2:
            auction_price = input("Enter auction_price to be replaced with : ")
            endpoint_url = input("Please Paste endpoint url : ")
            # endpoint_url = "http://webair-bidder-staging.vrtzads.com/vzbidder/bid?exchangeId=06d64ea0974c420ba497ab26b8e7faa2"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                # print(response.text)
                # response_url = response.json()
                if response_status == 200:
                    response_url = response.json()
                ####################################### IMPRESSION TRACKER ####################################
                impression_tracker = response_url["seatbid"][0]["bid"][0]["ext"]["impression_tracking_url"]
                # print(impression_tracker)
                for i in impression_tracker:
                    if "bidwin.vrtzads.com" in i or "beta-bidwin.vrtzads.com" in i:
                        try:
                            impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                            imp_response = requests.get(impression_url, verify=True, headers=headers)
                            print(impression_url)
                            print(f"Impression response : {imp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(
                                    f"\n{impression_url}\nImpression : {imp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for Impression_url   *****")
                            print("*****   Please check   *****\n")
                    elif "dspimp.vrtzads.com" in i or "dspimp-beta.vrtzads.com" in i:
                        try:
                            cdn_impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                            cdnimp_response = requests.get(cdn_impression_url, verify=True, headers=headers)
                            print(cdn_impression_url)
                            print(f"CDN Impression response : {cdnimp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for CDN Impression_url   *****")
                            print("*****   Please check   *****\n")
                    else:
                        print("New url appended in impression trackers")

                ########################### ADM URL ##################################
                trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                rtrim_adm_url = trim_adm_url.split("adm='")[1]
                actual_adm_url = rtrim_adm_url.split("' id=")[0]
                print(actual_adm_url)
                try:
                    adm_url_response = requests.get(actual_adm_url, verify=True,
                                                    headers=headers)  # Using get method will get status of request
                    print(f"ADM response : {adm_url_response}\n")
                    adm_response = adm_url_response.text
                except:
                    print("*****   Not getting 200 ok for ADM   *****")
                    print("*****   Please check   *****\n")

                ############################# CLICK URL #################################
                click_url_first_part = adm_response.split("href=")[1]
                # partial_click_url = str(click_url_first_part[1])
                click_url_second_part = click_url_first_part.split("img id=")[0]
                # get_click_url = click_url_second_part[0]
                rstrip_click_url = click_url_second_part.rstrip("\"> <")
                trim_click_url = rstrip_click_url.lstrip("\"")
                replace_click_url = trim_click_url.replace("%%CLICK_URL_ESC%%", "")
                actual_click_url = urllib.parse.unquote(replace_click_url)
                print(actual_click_url)
                try:
                    # print(actual_click_url)
                    actual_click_url_response = requests.get(actual_click_url, verify=True, headers=headers)
                    print(f"click_url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for ClickURL   *****")
                    print("*****   Please check   *****\n")

                ############################ Cookie_sync_url #################################
                vertozcookie_first_part = adm_response.split("<img src=")[
                    1]  # Directly using adm_url_response and split to get vertoz cookie sync url and using list index picking up cookie sync url
                partial_vertozcookie_url = vertozcookie_first_part.lstrip("\"")  # removing left side  text inside ()
                actual_vertozcookie_url = partial_vertozcookie_url.split("\"")[
                    0]  # split again to get cookie sync and using list index
                print(actual_vertozcookie_url)
                try:
                    actual_vertozcookie_url_response = requests.get(
                        actual_vertozcookie_url)  # Storing the response of click url from get method
                    print(f"Cookie_sync_url : {actual_vertozcookie_url_response}\n")
                except:
                    print("*****   Not getting 200 ok for cookie_sync url *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1
            print(f"End_time : {datetime.datetime.now() - Start_time}")

        elif media_channel == 3:
            auction_price = input("Enter auction_price to be replaced with : ")
            endpoint_url = input("Please Paste endpoint url : ")
            # endpoint_url = "http://webair-bidder-staging.vrtzads.com/vzbidder/bid?exchangeId=06d64ea0974c420ba497ab26b8e7faa2"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                # print(response.text)
                # response_url = response.json()
                if response_status == 200:
                    response_url = response.json()
                ####################################### IMPRESSION TRACKER ####################################
                impression_tracker = response_url["seatbid"][0]["bid"][0]["ext"]["impression_tracking_url"]
                # print(impression_tracker)
                for i in impression_tracker:
                    if "bidwin.vrtzads.com" in i or "beta-bidwin.vrtzads.com" in i:
                        try:
                            impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                            imp_response = requests.get(impression_url, verify=True, headers=headers)
                            print(impression_url)
                            print(f"Impression response : {imp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(
                                    f"\n{impression_url}\nImpression : {imp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for Impression_url   *****")
                            print("*****   Please check   *****\n")
                    elif "dspimp.vrtzads.com" in i or "dspimp-beta.vrtzads.com" in i:
                        try:
                            cdn_impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                            cdnimp_response = requests.get(cdn_impression_url, verify=True, headers=headers)
                            print(cdn_impression_url)
                            print(f"CDN Impression response : {cdnimp_response}\n")
                            with open('impression.txt', 'a') as f:  # opening the excel file
                                f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                        except:
                            print("*****   Not getting 200 ok for CDN Impression_url   *****")
                            print("*****   Please check   *****\n")
                    else:
                        print("Something went wrong")

                ########################### ADM URL ##################################
                actual_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                # rtrim_adm_url = trim_adm_url.split("adm='")[1]
                # actual_adm_url = rtrim_adm_url.split("' id=")[0]
                print(actual_adm_url)
                try:
                    adm_url_response = requests.get(actual_adm_url, verify=True,
                                                    headers=headers)  # Using get method will get status of request
                    print(f"ADM response : {adm_url_response}\n")
                    adm_response = adm_url_response.text
                except:
                    print("*****   Not getting 200 ok for ADM   *****")
                    print("*****   Please check   *****\n")

                ###################################### Cookie_Sync ############################################
                cookie_first_part = adm_response.split("<![CDATA[")[2]
                cookie_sync_url = cookie_first_part.split("]]")[0]
                print(cookie_sync_url)
                try:
                    cookie_sync_response = requests.get(cookie_sync_url, verify=True, headers=headers)
                    print(f"Cookie_Sync response : {cookie_sync_response}\n")
                except:
                    print("*****   Not getting 200 ok for Cookie_sync_url   *****")
                    print("*****   Please check   *****\n")

                ###################################### Click_URL ############################################
                click_first_part = adm_response.split("<![CDATA[")[6]
                trim_click_url = click_first_part.split("]]")[0]
                replace_click_url = trim_click_url.replace("%%CLICK_URL_ESC%%", "")
                click_url = urllib.parse.unquote(replace_click_url)
                print(click_url)
                try:
                    actual_click_url_response = requests.get(click_url, verify=True, headers=headers)
                    print(f"Click Url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CLICKURL   *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1
            print(f"End_time : {datetime.datetime.now() - Start_time}")

        elif media_channel == 4:
            auction_price = input("Enter auction_price to be replaced with : ")
            endpoint_url = input("Please Paste endpoint url : ")
            # endpoint_url = "http://webair-bidder-staging.vrtzads.com/vzbidder/bid?exchangeId=06d64ea0974c420ba497ab26b8e7faa2"
            print(
                "*****   Note: Please paste Minified bidrequest/json   *****\n Step 1: to minify bidrequest/json go to url https://jsonformatter.org/ \n Step 2: Paste bidrequest/json and click minify/compact option")
            bidrequest = input("Please Paste valid bidrequest or json : ")
            tmpjson = f'''{bidrequest}'''
            json = tmpjson.replace('\'', '\"')
            for i in range(impressions):
                response = requests.post(endpoint_url, data=json, verify=False, headers=headers)
                response_status = response.status_code
                # print(response.text)
                # response_url = response.json()
                if response_status == 200:
                    response_url = response.json()
            ####################################### IMPRESSION TRACKER ####################################
            impression_tracker = response_url["seatbid"][0]["bid"][0]["ext"]["impression_tracking_url"]
            # print(impression_tracker)
            for i in impression_tracker:
                if "bidwin.vrtzads.com" in i or "beta-bidwin.vrtzads.com":
                    try:
                        impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                        imp_response = requests.get(impression_url, verify=True, headers=headers)
                        print(impression_url)
                        print(f"Impression response : {imp_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(
                                f"\n{impression_url}\nImpression : {imp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for Impression_url   *****")
                        print("*****   Please check   *****\n")
                elif "dspimp.vrtzads.com" in i or "dspimp-beta.vrtzads.com" in i:
                    try:
                        cdn_impression_url = i.replace("&p=%%WINNING_PRICE%%&", f"&p={auction_price}&")
                        cdn_imp_response = requests.get(cdn_impression_url, verify=True, headers=headers)
                        print(cdn_impression_url)
                        print(f"CDN Impression response : {cdn_imp_response}\n")
                        with open('impression.txt', 'a') as f:  # opening the excel file
                            f.write(f"Cdnimpression : {cdnimp_response},\t\t")  # appending campaign id in excel
                    except:
                        print("*****   Not getting 200 ok for CDN Impression_url   *****")
                        print("*****   Please check   *****\n")
                else:
                    print("Something went wrong or extra url get appended!! ")

                ############################# ADM_URL #################################
                actual_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
                # print(actual_adm_url)

                ############################# Click_URL ###############################
                split_adm_url = actual_adm_url.split("url")[3]
                rtrim_adm_url = split_adm_url.split("\":\"")[1]
                click_url = rtrim_adm_url.split("\"}}")[0]
                print(click_url)
                try:
                    actual_click_url_response = requests.get(click_url, verify=True, headers=headers)
                    print(f"Click Url response : {actual_click_url_response}\n")
                    with open('impression.txt', 'a') as f:  # opening the excel file
                        f.write(f"ClickURL : {actual_click_url_response}\n")  # appending campaign id in excel
                except:
                    print("*****   Not getting 200 ok for CLICKURL   *****")
                    print("*****   Please check   *****\n")

                ############################ Cookie_Sync_URL #############################
                split_adm_url = actual_adm_url.split("\",\"")[4]
                cookie_sync_url = split_adm_url.split("\"],")[0]
                print(cookie_sync_url)
                try:
                    cookie_sync_response = requests.get(cookie_sync_url, verify=True, headers=headers)
                    print(f"Cookie_Sync response : {cookie_sync_response}\n")
                except:
                    print("*****   Not getting 200 ok for Cookie_sync_url   *****")
                    print("*****   Please check   *****\n")
                print(count)
                count += 1
            print(f"End_time : {datetime.datetime.now() - Start_time}")
        else:
            print("Invalid Media Channel ID")
    else:
        print("Not yet configured")

# postman_request(ssp_id,media_channel_id)
# t1 = Thread(target=postman_request, args=(ssp_id,media_channel_id,))
# t1.start()
# t2 = Thread(target=postman_request, args=(ssp_id,media_channel_id,))
# t2.start()
