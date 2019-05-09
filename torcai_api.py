import json
import requests
import datetime
#import xlsxwriter
#workbook = xlsxwriter.Workbook('torcai.xlsx')
auction_price = float(input("Enter auction_price to be replaced with: "))
impressions = int(input("Enter number of Impressions required"))
count1 = 0
Start_time = datetime.datetime.now()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
endpoint_url= "http://webair-bidder-staging.vrtzads.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569"
request_json = '''
{
	"id": "vzddb4caf8-853d-48ec-84dc-230e0d607f80",
	"imp": [{
		"id": "1",
		"banner": {
			"w": 300,
			"h": 250,
			"pos": 1
		},
		"tagid": "VZI403706V2F1606",
		"bidfloorcur": "USD",
		"secure": 1,
		"ext": {}
	}],
	"site": {
		"id": "13529",
		"domain": "filmgrapevine.com",
		"cat": ["IAB1", "IAB2", "IAB3"],
		"page": "http://filmgrapevine.com/beta.html",
		"ref": "  ",
		"publisher": {
			"id": "31241"
		}
	},
	"device": {
		"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
		"geo": {
			"lat": 18.975,
			"lon": 72.8258,
			"type": 2,
			"country": "ind",
			"region": "mh",
			"city": "mumbai"
		},
		"ip": "49.248.222.99",
		"devicetype": 2,
		"os": "linux",
		"carrier": "tata teleservices (maharashtra)"
	},
	"user": {
		"id": "5fd57b54-fd5e-435b-b09e-6d183903cd8e"
	},
	"at": 2
}'''

for i in range(impressions):
    response = requests.post(endpoint_url, data = request_json, verify = False, headers = headers)
    #response = requests.api.request('post', endpoint_url, data= request_json, verify=False).json()
    #response_url = json.loads(response.text)
    response_url = response.json()
    print(response_url)
    #print(type(response_url))



####################################### NURL ##################################################
    actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
    # actual_nurl = actual_nurl.replace("&p=", f"&p={auction_price}&")
    # print(actual_nurl)
    with open('impression.txt', 'a') as f:  # opening the excel file
        f.write(f"{actual_nurl} \n\n")  # appending campaign id in excel
    f.close()  # closing the excel file
    actual_n_url_response = requests.get(actual_nurl , verify = False, headers = headers)
    print(actual_n_url_response)

####################################### ADM ##################################################
    trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
    first_part_split= trim_adm_url.split("adm='") # spliting a string into list
    first_part_final= str(first_part_split[1]) #Taking 1 index string and assign it variable
    second_part_split = first_part_final.split(" id=") #Again spliting the last character to get adm
    actual_adm_url = second_part_split[0] #by this i got adm url
    actual_adm_url = actual_adm_url.replace("&p=", f"&p={auction_price}&")
    adm_url_response = requests.get(actual_adm_url,verify = False, headers = headers) #Using get method will get status of request
    print(actual_adm_url)
    print(adm_url_response)


###################################### Impression ############################################
    impression_url = requests.get(actual_adm_url, verify = False, headers = headers)
    adm_response = impression_url.text
    #print(f"Adm response: {adm_response}")
    imp_first_part_split = adm_response.split("<img src=")
    partial_impression_url = str(imp_first_part_split[1])
    #print(partial_impression_url)
    impression_url = partial_impression_url.rstrip(" width=\"1\" height=\"1\" />")
    final_impression_url = impression_url.lstrip("\"")
    print(final_impression_url)
    imp_response = requests.get(final_impression_url, verify = False, headers = headers)
    print(imp_response)



################################## CDN Impression ##########################################
    adm_url = requests.get(actual_adm_url, verify = False,headers = headers)
    adm_response = adm_url.text
    #print(f"Adm response: {adm_response}")
    cdnimp_first_part_split = adm_response.split("<img src=",3)
    #print(cdnimp_first_part_split)
    partial_cdnimp_url = str(cdnimp_first_part_split[2])
    #print(partial_cdnimp_url)
    cdnimp_second_part_strip = partial_cdnimp_url.rstrip(" width=\"1\" height=\"1\" />")
    cdn_impression_url = cdnimp_second_part_strip.lstrip("\"")
    print(cdn_impression_url)
    cdnimp_response = requests.get(cdn_impression_url, verify = False,headers = headers)
    print(cdnimp_response)


#############################  Click URL  #######################################



    adm_url = requests.get(actual_adm_url, verify = False, headers = headers)
    adm_response = adm_url.text
    #print(adm_response)
    click_url_first_part = adm_response.split("href=")
    #print(click_url_first_part)
    partial_click_url = str(click_url_first_part[1])
    #print(partial_click_url)
    click_url_second_part = partial_click_url.split("img id=")
    get_click_url = click_url_second_part[0]
    #print(actual_click_url)
    rstrip_click_url = get_click_url.rstrip("\"> <")
    #print(rstrip_click_url)
    actual_click_url = rstrip_click_url.lstrip("\"")
    print(actual_click_url)
    actual_click_url_response = requests.get(actual_click_url, verify = False, headers = headers)
    print(actual_click_url_response)
    print(count1)
    count1 += 1
print(f"End_time : {datetime.datetime.now()- Start_time}")

