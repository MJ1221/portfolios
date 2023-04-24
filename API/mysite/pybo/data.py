import requests
import xml.etree.ElementTree as ET
import pandas as pd
import re

url = 'http://api.data.go.kr/openapi/tn_pubr_public_frhl_exprn_vilage_api'
params ={'serviceKey' : 'vbAyHzayo2QCecq+00KCyFf9qnO9H/SSXObc1/y+mhH0NCpajZwrIDDD+EnsqcNbKsYSB0VmxHKtRuthO4UDLQ==', 
        'pageNo' : '1',
        'numOfRows' : '2000',
        'type' : 'xml',
        }

response = requests.get(url, params=params)

root = ET.fromstring(response.content)
data_list = []
for item in root.iter('item'):
        sigun_nm = None
        exprnvilagenm = None
        ctprvnnm = None
        exprnse = None
        exprncn = None
        holdfclty = None
        esprnar = None
        exprnricurl = None
        rdnmadr = None
        rprsntvnm = None
        phonenumber = None
        appndate = None
        homepageurl = None
        institutionnm = None
        latitude = None
        longitude = None

        for elem in item.iter():
            if elem.tag == 'signguNm':
                sigun_nm = elem.text if elem.text else ''
            elif elem.tag == 'exprnVilageNm':
                exprnvilagenm = elem.text if elem.text else ''
            elif elem.tag == 'ctprvnNm':
                ctprvnnm = elem.text if elem.text else ''
            elif elem.tag == 'exprnSe':
                exprnse = elem.text if elem.text else ''
            elif elem.tag == 'exprnCn':
                exprncn = elem.text if elem.text else ''
                exprncn = re.sub(r'[a-zA-Z&;]+', '+', exprncn)
                exprncn = ','.join([x for x in exprncn.split('+') if x])
            elif elem.tag == 'holdFclty':
                holdfclty = elem.text if elem.text else ''
            elif elem.tag == 'exprnAr':
                esprnar = elem.text if elem.text else ''
            elif elem.tag == 'exprnPicUrl':
                exprnricurl = elem.text if elem.text else ''
            elif elem.tag == 'rdnmadr':
                rdnmadr = elem.text if elem.text else ''
            elif elem.tag == 'rprsntvNm':
                rprsntvnm = elem.text if elem.text else ''
            elif elem.tag == 'phoneNumber':
                phonenumber = elem.text if elem.text else ''
            elif elem.tag == 'appnDate':
                appndate = elem.text if elem.text else ''
            elif elem.tag == 'homepageUrl':
                homepageurl = elem.text if elem.text else ''
            elif elem.tag == 'institutionNm':
                institutionnm = elem.text if elem.text else ''
            elif elem.tag == 'latitude':
                latitude = elem.text if elem.text else ''
            elif elem.tag == 'longitude':
                longitude = elem.text if elem.text else ''
        if sigun_nm is not None and exprnvilagenm is not None and ctprvnnm is not None and exprnse is not None and exprncn is not None and holdfclty is not None and esprnar is not None and exprnricurl is not None and rdnmadr is not None and rprsntvnm is not None and phonenumber is not None and appndate is not None and homepageurl is not None and institutionnm is not None and latitude is not None and longitude is not None:
            rprsntvnm = rprsntvnm if rprsntvnm else ''
            phonenumber = phonenumber if phonenumber else ''
            homepageurl = homepageurl if homepageurl else ''
            data_list.append([sigun_nm, exprnvilagenm, ctprvnnm,exprnse, exprncn,holdfclty, esprnar, exprnricurl,rdnmadr, rprsntvnm,phonenumber, appndate, homepageurl,institutionnm, latitude, longitude])

# 결과를 파일에 출력
df = pd.DataFrame(data_list, columns=['signguNm', 'exprnVilageNm', 'ctprvnNm','exprnSe', 'exprnCn', 'holdFclty','exprnAr', 'exprnPicUrl', 'rdnmadr','rprsntvNm', 'phoneNumber', 'appnDate','homepageUrl', 'institutionNm', 'latitude','longitude'])
# 엑셀 파일로 저장
df.to_excel('result4.xlsx', index=False)


   