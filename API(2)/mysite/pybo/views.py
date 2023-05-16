
from django.utils import timezone
import pandas as pd
from django.shortcuts import render, redirect
import requests
import xml.etree.ElementTree as ET
import re
import openpyxl

def start(request):
    return render(request,'pybo/start.html')

def main(request):
    return render(request,'pybo/main.html')

ar = [None, None, None]

def farm_nm1(request):
    global ar
    ar[0] = request.GET.get('q')
    if ar[0] == "광주광역시" or ar[0] == "세종특별자치시" or ar[0] == "제주특별자치도" or ar[0] == "울산광역시":
        df = pd.read_excel('C:\API(2)\mysite\static\data/result4.xlsx', sheet_name='Sheet1')
        # ar[1] 변수에 저장된 값과 '시군구' 컬럼 값이 같은 경우에만 데이터를 필터링합니다.
        if ar[0]:
            df = df[df['ctprvnNm'] == ar[0]]
   
        # 데이터프레임에서 필요한 컬럼만 선택합니다.
        columns = ['exprnVilageNm','rdnmadr','exprnCn','rprsntvNm','phoneNumber','homepageUrl', 'latitude', 'longitude']
        df = df[columns]
        df = df.fillna('없음')
   
        
        # 데이터프레임의 각 row에 대해 리스트를 만들어줍니다.
        data_list = []
        for row in df.itertuples(index=False):
            data_list.append(list(row))
 
        # 위도와 경도를 추출하여 배열에 저장
        locations = [(row[-2], row[-1]) for row in df.itertuples(index=False)]
    
        context = {'data_list': data_list, 'locations': locations}
        return render(request, 'pybo/조회.html', context)

    url = ''.join(['pybo/',ar[0],'.html'])

    return render(request, url)

data_list=[]
def farm_nm2(request):
    global ar
    ar[1] = request.GET.get('w')
    df = pd.read_excel('C:\API(2)\mysite\static\data/result4.xlsx', sheet_name='Sheet1')

    # ar[1] 변수에 저장된 값과 '시군구' 컬럼 값이 같은 경우에만 데이터를 필터링합니다.
    if ar[0]:
        df = df[df['ctprvnNm'] == ar[0]]
    if ar[1]:
        df = df[df['signguNm'] == ar[1]]

    # 데이터프레임에서 필요한 컬럼만 선택합니다.
    columns = ['exprnVilageNm','rdnmadr','exprnCn','rprsntvNm','phoneNumber','homepageUrl', 'latitude', 'longitude']
    df = df[columns]
    df = df.fillna('없음')

    
    # 데이터프레임의 각 row에 대해 리스트를 만들어줍니다.
    data_list = []
    for row in df.itertuples(index=False):
        data_list.append(list(row))
  
    # 위도와 경도를 추출하여 배열에 저장
    locations = [(row[-2], row[-1]) for row in df.itertuples(index=False)]
   

    context = {'data_list': data_list, 'locations': locations}
    return render(request, 'pybo/조회.html', context)

def back(request):
    global ar
    ar[0]=None
    if ar[0] != None:
        url = ''.join(['pybo/',ar[0],'.html'])
       
        return render(request, url)
    else :
        url1 = 'pybo/main.html'
        return render(request,url1)