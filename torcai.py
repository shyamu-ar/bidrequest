import requests
import datetime
# import simplejson as json
impressions = int(input("Enter number of Impressions required : "))
Start_time = datetime.datetime.now()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # User Agent of Chrome, you can set any browser user agent
# endpoint_url= "https://betabidder.vertoz.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569" # Bidder Endpoint
endpoint_url= "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=973fddb9324e46e598f0099b4a87b661" # Bidder Endpoint
# Below is the json request
request_json = '''{
	"id": "13b274d5_067-2-1-1518600261806158",
	"site": {
		"id": "aol_364003",
		"mobile": 0,
		"publisher": {
			"id": "aol_10224",
			"name": ""
		},
		"domain": "filmgrapevine.com",
		"ext": {
			"mobile_site": 0
		},
		"page": "http://www.andhrajyothy.com/artical?SID=552625"
	},
	"imp": [{
		"bidfloor": 0.0009,
		"id": "1",
		"banner": {
			"h": 250,
			"battr": [1, 8, 9],
			"w": 300,
			"btype": [1, 2]
		},
		"exp": 300,
		"bidfloorcur": "USD",
		"ext": {},
		"secure": 0,
		"instl": 0
	}],
	"user": {
		"id": "27e66d3c-fc15-4b0b-8238-7b3f3128e631",
		"ext": {
			"cookie_age": 161,
			"ug": 0
		}
	},
	"device": {
		"language": "en",
		"geo": {
			"country": "IN",
			"city": "Mumbai",
			"zip": "400067",
			"region": "16",
			"type": 2
		},
		"make": "Google",
		"os": "Windows 10",
		"devicetype": 2,
		"js": 1,
		"ip": "49.248.222.99",
		"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
	},
	"tmax": 140,
	"cur": ["USD"],
	"source": {
		"pchain": "-35d5010d7789b49d:aol"
	},
	"bcat": ["BSW3", "BSW2", "IAB14-1", "IAB26", "IAB25", "IAB6", "IAB7", "BSW1", "IAB25-3", "BSW10", "BSW4"],
	"ext": {
		"wt": 1,
		"clktrkrq": 0,
		"ssp": "aol",
		"is_secure": 0,
		"media_src": "aol"
	},
	"at": 2
}'''

count = 1
for i in range(impressions):
    try:
        response = requests.post(endpoint_url, data = request_json, verify = False, headers = headers)
        response_url = response.json()
        print(response_url)

        ####################################### NURL ##################################################
        actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
        actual_nurl_response = requests.get(actual_nurl, verify=False, headers=headers)
        print(actual_nurl)
        print(actual_nurl_response)

        ####################################### ADM ##################################################
        trim_adm_url = response_url["seatbid"][0]["bid"][0]["adm"]
        split_adm = trim_adm_url.split("adm='")[1]  # spliting a string into list and using index picking up adm_url
        split_first_part = split_adm.split(" id=")[
            0]  # Again spliting the last character to get adm and using list index picking up adm_url
        actual_adm_url = split_first_part.replace("${AUCTION_PRICE}", "0.1")
        adm_url = requests.get(actual_adm_url, verify=False,
                               headers=headers)  # Using get method will get status of adm_url
        print(actual_adm_url)
        print(adm_url)

        adm_url_response = adm_url.text  # Storing adm_response in a variable to use futher
        print(adm_url_response)

        ###################################### Impression ############################################
        imp_first_part_split = adm_url_response.split("<img src=")[
            1]  # Directly using adm_response and split to get impression url and using list index picking up impression url
        partial_impression_url = imp_first_part_split.rstrip(
            " width=\"1\" height=\"1\" />")  # trim the right part i.e width and height
        actual_impression_url = partial_impression_url.lstrip("\"")  # Removing " from the start of impression url
        print(actual_impression_url)
        actual_impression_response = requests.get(actual_impression_url, verify=False,
                                                  headers=headers)  # Storing the response of impression url from get method
        print(actual_impression_response)

        ################################## CDN Impression ##########################################
        cdnimp_first_part_split = adm_url_response.split("<img src=", 3)[
            2]  # Directly using adm_url_response and split to get cdn impression url and using list index picking up cdn impression url
        cdnimp_second_part_strip = cdnimp_first_part_split.rstrip(
            " width=\"1\" height=\"1\" />")  # trim the right part i.e width and height
        actual_cdn_impression_url = cdnimp_second_part_strip.lstrip(
            "\"")  # Removing " from the start of cdn impression url
        print(actual_cdn_impression_url)
        actual_cdn_impression_response = requests.get(actual_cdn_impression_url, verify=False,
                                                      headers=headers)  # Storing the response of cdn impression url from get method
        print(actual_cdn_impression_response)

        #############################  Click URL  #######################################

        click_url_first_part = adm_url_response.split("href=")[
            1]  # Directly using adm_url_response and split to get click url and using list index picking up click url
        click_url_second_part = click_url_first_part.split("img id=")[
            0]  # Split again to get click_url and using list index
        rstrip_click_url = click_url_second_part.rstrip("\"> <")  # removing right side text inside ()
        actual_click_url = rstrip_click_url.lstrip("\"")  # removing left side text inside ()
        print(actual_click_url)
        actual_click_url_response = requests.get(actual_click_url, verify=False,
                                                 headers=headers)  # Storing the response of click url from get method
        print(actual_click_url_response)

        ###############################  Vertoz Cookie Sync #######################################
        vertozcookie_first_part = adm_url_response.split("<img src=", 5)[3]  # Directly using adm_url_response and split to get vertoz cookie sync url and using list index picking up cookie sync url
        partial_vertozcookie_url = vertozcookie_first_part.lstrip("\"")  # removing left side  text inside ()
        actual_vertozcookie_url = partial_vertozcookie_url.split("\"")[0]  # split again to get cookie sync and using list index
        print(actual_vertozcookie_url)
        actual_vertozcookie_url_response = requests.get(
            actual_vertozcookie_url)  # Storing the response of click url from get method
        print(actual_vertozcookie_url_response)
        count += 1
    except:
        print(response)
        print("Campaign not getting qualified for above request ")

print(f"End_time : {datetime.datetime.now() - Start_time}")

