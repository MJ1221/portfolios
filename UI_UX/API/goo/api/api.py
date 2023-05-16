import requests
import xml.etree.ElementTree as ET

url = 'http://api.data.go.kr/openapi/tn_pubr_public_frhl_exprn_vilage_api'
params ={'serviceKey' : 'vbAyHzayo2QCecq+00KCyFf9qnO9H/SSXObc1/y+mhH0NCpajZwrIDDD+EnsqcNbKsYSB0VmxHKtRuthO4UDLQ==', 
        'pageNo' : '0',
        'numOfRows' : '100',
        'type' : 'xml',
        }

response = requests.get(url, params=params)
print(response.content)

root = ET.fromstring(response.content)

data_list = []  # 결과를 저장할 리스트

# 데이터에서 시군명과 주소 추출하여 리스트에 저장
for item in root.iter('item'):
    sigun_nm = None
    address = None
    farm_nm = None
    for elem in item.iter():
        if elem.tag == 'signguNm':
            sigun_nm = elem.text
        elif elem.tag == 'rdnmadr':
            address = elem.text
        elif elem.tag == 'exprnVilageNm':
            farm_nm = elem.text
    if sigun_nm is not None and address is not None and farm_nm is not None:
        data_list.append([sigun_nm, address,farm_nm])

# 결과를 파일에 출력
with open('new_result.txt', 'w', encoding='utf-8') as f:
    for data in data_list:
        if isinstance(data, str):  # 만약 데이터가 문자열이면
            f.write(f'{data}\n')  # 문자열 그대로 파일에 쓰기
        else:
            f.write(f'{data[0]}, {data[1]}, {data[2]}\n')  # 시군명, 주소, 농장명 파일에 쓰기
    f.close()

# 결과 출력
for data in data_list:
    print(data)