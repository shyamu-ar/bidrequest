import requests
import datetime
import json
Start_time = datetime.datetime.now()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # User Agent of Chrome, you can set any browser user agent
useragents = ["Mozilla/5.0 (Linux; Android 4.0; ARM; iPhone; iPhone OS 5_0_0;) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile Safari/537",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; SM-G9500 Build/PPR1.180610.011) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 8 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; COL-AL10 Build/HUAWEICOL-AL10) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; LYA-AL10 Build/HUAWEILYA-AL10) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; BKL-AL20 Build/HUAWEIBKL-AL20) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 9; zh-cn; ONEPLUS A6000 Build/PKQ1.180716.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"SAMSUNG-GT-I9128I_TD/1.0 Android/4.2.2 Release/04.03.2013 Browser/AppleWebKit535.19",
"SAMSUNG-SM-G3508_TD/1.0 Android/4.1.2 Release/07.23.2013 Browser/AppleWebKit534.30",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; OE106 Build/OPM1.171019.026) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Plus Build/NMA26.42-152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-64-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U23 Build/HUAWEILUA-U23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.64 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.1; ALE-L23 Build/HuaweiALE-L23) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Plus Build/NPNS25.137-92-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 ",
"Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX3 Build/HUAWEIFIG-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; ATU-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; ASUS_X008DB Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Pixel 2 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) Build/OPS27.82-19-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
"Mozilla/5.0 (Android 6.0.1; Mobile; rv:53.0) Gecko/53.0 Firefox/53.0",
"Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) plus Build/OPW27.113-89) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; MYA-L03 Build/HUAWEIMYA-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]",
"Mozilla/5.0 (Linux; Android 4.4.2; ZTE Blade C370 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; DIG-L03) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; ZE553KL Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.3; D5322 Build/19.1.1.C.0.56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A3500-FL Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Android 6.0.1; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
"Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX3 Build/HUAWEIWAS-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; ASUS_X008DC Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; Moto Z2 Play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; TRT-L53 Build/HUAWEITRT-L53; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]",
"Mozilla/5.0 (Linux; Android 4.4.2; TR10CS1 Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Blade A310 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-L23 Build/HUAWEICUN-L23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Z2 Pro Build/OPM1.171019.021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9360; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.353 Mobile Safari/534.11+",
"Mozilla/5.0 (Linux; Android 7.0; G3313 Build/43.0.A.7.70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
"Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
"Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
"Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
"Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)",
"Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996",
"Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10",
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10",
"Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4",
"Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36"]
new_wurfl_data =[]
old_wurfl_data =[]
with open('wurfl.data', 'w') as f:
    pass
with open('difference.data', 'w') as f:
    pass
for ua in useragents:
    # endpoint_url= "https://betabidder.vertoz.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569" # Bidder Endpoint
    beta_endpoint_url= "http://beta-golang.vrtzads.com/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569" # Bidder Endpoint
    # Below is the json request
    beta_request = {
        "id": "vzc2138750-d5d7-4935-88e5-8164a0015a84",
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
            "page": "http://filmgrapevine.com/beta1.html",
            "ref": "  ",
            "publisher": {
                "id": "31241"
            }
        },
        "device": {
            "ua": f"{ua}",
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
            "id": "48eef382-ae37-4190-9e30-51298eea5a7e"
        },
        "at": 2
    }
    tmprequest = f'''{beta_request}'''
    request_json = tmprequest.replace('\'','\"')
    # print(request_json)
    response = requests.post(beta_endpoint_url, data=request_json, verify=False, headers=headers)
    response_url = response.json()
    beta_actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
    beta_actual_nurl = beta_actual_nurl.replace('&','","')
    beta_actual_nurl = f"\"{beta_actual_nurl}\""
    beta_actual_nurl = beta_actual_nurl.replace('\"', "")
    list_nurl = beta_actual_nurl.split(",")
    # print(list_nurl)
    # print(len(list_nurl))
    new_wurfl_data.append(list_nurl[10])
    new_wurfl_data.append(list_nurl[13])
    new_wurfl_data.append(list_nurl[22])
    new_wurfl_data.append(list_nurl[23])
    new_wurfl_data.append(list_nurl[24])
    new_wurfl_data.append(list_nurl[27])
    new_wurfl_data.append(list_nurl[31])
    with open('wurfl.data', 'a') as f:  # opening the excel file
        f.write("New Wurft Data \n")
        f.write(f"{ua} \n")
        f.write(f"{beta_actual_nurl}\n")
        for i in new_wurfl_data:
            f.write(f"{i} \n")
        f.write("\n")
    print(new_wurfl_data)
    # print(beta_actual_nurl)


    live_endpoint_url= "http://318.207.208.187/vzbidder/bid?exchangeId=705712f550cc479497fbdbf2edce5569" # Bidder Endpoint
    # Below is the json request
    live_request = {
        "id": "vz454f956f-12cd-443d-acfe-dc1cacf3f974",
        "imp": [{
            "id": "1",
            "banner": {
                "w": 300,
                "h": 50,
                "pos": 1
            },
            "tagid": "",
            "bidfloorcur": "USD",
            "secure": 1,
            "ext": {}
        }],
        "site": {
            "id": "13529",
            "domain": "filmgrapevine.com",
            "cat": ["IAB1", "IAB2", "IAB3"],
            "page": "http://filmgrapevine.com/mobile.html",
            "ref": "  ",
            "publisher": {
                "id": "31241"
            }
        },
        "device": {
            "ua": f"{ua}",
            "geo": {
                "lat": 18.9721,
                "lon": 72.8246,
                "type": 2,
                "country": "IND",
                "region": "MH",
                "city": "Mumbai",
                "zip": "400002"
            },
            "ip": "49.248.222.99",
            "devicetype": 4,
            "make": "samsung",
            "model": "sm-g900p",
            "os": "android",
            "osv": "5.0",
            "carrier": "Tata Teleservices (Maharashtra)",
            "connectiontype": 1
        },
        "user": {
            "id": "48eef382-ae37-4190-9e30-51298eea5a7e"
        },
        "at": 2
    }
    tmprequest = f'''{live_request}'''
    request_json = tmprequest.replace('\'','\"')
    # print(request_json)
    response = requests.post(live_endpoint_url, data=request_json, verify=False, headers=headers)
    response_url = response.json()
    live_actual_nurl = response_url["seatbid"][0]["bid"][0]["nurl"]
    live_actual_nurl = live_actual_nurl.replace('&','","')
    live_actual_nurl = f"\"{live_actual_nurl}\""
    live_actual_nurl = live_actual_nurl.replace('\"',"")
    live_list_nurl = live_actual_nurl.split(",")
    # print(live_list_nurl)
    # print(len(live_list_nurl))
    old_wurfl_data.append(live_list_nurl[10])
    old_wurfl_data.append(live_list_nurl[13])
    old_wurfl_data.append(live_list_nurl[22])
    old_wurfl_data.append(live_list_nurl[23])
    old_wurfl_data.append(live_list_nurl[24])
    old_wurfl_data.append(live_list_nurl[27])
    old_wurfl_data.append(live_list_nurl[30])
    with open('wurfl.data', 'a') as f:  # opening the excel file
        f.write("Old Wurft Data \n")
        f.write(f"{live_actual_nurl}\n")
        for j in old_wurfl_data:
            f.write(f"{j} \n")
        f.write("\n")
    print(f"old_wurfl_data{old_wurfl_data}")
    # print(live_actual_nurl)
    if old_wurfl_data == new_wurfl_data:
        pass
    else:
        with open('difference.data','a') as f:
            f.write(f"{ua} \n")
            for i in new_wurfl_data:
                f.write(f"{i} \n")
            f.write("\n")
            for j in old_wurfl_data:
                f.write(f"{j} \n")
            f.write("\n\n")
    old_wurfl_data = []
    new_wurfl_data = []








