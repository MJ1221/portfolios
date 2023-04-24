import pandas as pd
import tkinter as tk
from PIL import Image, ImageTk
import tkinter
from tkinter.font import Font
import time
import datetime

# 엑셀 파일 불러오기
excel_file = pd.read_excel('C:\python\노선도.xlsx', sheet_name='Sheet1')

# tkinter 윈도우 생성
window = tk.Tk()
window.title("노선도")
window.geometry("1920x1200")
window.state('zoomed')
window.configure(background='white')

Tf = ['신도림', '신길', '서울','시청', '종로3가', '동대문', '신설동', '창동', '시청', '을지로3가', '을지로4가',
            '동대문역사문화공원', '왕십리', '교대', '사당', '영등포구청', '충정로', '충무로', '오금', '금정', '까치산',
            '금천구청', '구로', '병점', '성수', '강동', '합정', '연신내', '불광', '공덕', '삼각지', '약수', '청구',
            '신당', '동묘앞', '석계']

li = {
    '1호선_서동탄행' : ['병점', '서동탄'],
    '1호선_광명행' : ['금천구청', '광명'],
    '1호선_인천행' : ['구로', '구일', '개봉', '오류동', '온수', '소사', '부천', '중동', '송내', '부개', '부평', '백운', '동암', '간석',
        '주안', '도화', '제물포', '도원', '동인천', '인천'],
    '1호선': ['소요산', '동두천', '보산', '동두천중앙', '지행', '덕정', ' 덕계', '양주', '녹양', ' 가능', '의정부', '회룡', '망월사',
        '도봉산', '도봉', '방학', '창동', '녹천', '월계', '광운대', '석계', '산이문', '외대앞', '회기', '청량리',
        '제기동', '신설동', '동묘앞', '동대문', '종로5가', '종로3가', '종각', '시청', '서울', '남영', '용산', '노량진',
        '대방', '신길', '영등포', '신도림', '구로', '가산디지털단지', '금천구청', '석수', '관악', '안양', '명학',
        '금정', '군포', '당정', '의왕', '성균관대', '화서', '수원', '세류', '병점', '세마', ' 오산대', '오산', '진위', ' 송탄', '서정리', '평택지제', '평택', '성환', '직산', '두정', '천안',
        '봉명', '쌍용', '아산', '탐정', '배방', '온양온천', '신창'],
    '2호선': ['시청', '을지로입구', '을지로3가', '을지로4가', '동대문역사문화공원', '신당', '상왕십리', '왕십리',
        '한양대', '뚝섬', '성수', '건대입구', '구의', '강변', '잠실나루', '잠실', '신천', '종합운동장',
        '삼성', '선릉', '역삼', '강남', '교대', '서초', '방배', '사당', '낙성대', '서울대입구', '봉천',
        '신림', '신대방', '구로디지털단지', '대림', '신도림', '문래', '영등포구청', '당산', '합정', '홍대입구',
        '신촌', '이대', '아현', '충정로'],
    '2호선_신설동행' : ['성수', '용답', '신답', '용두', '신설동'],
    '2호선_까치산행' : ['신도림', '도림천', '양천구청', '신정네거리', '까치산'],
    '3호선': ['대화', '주엽', '정발산', '마두', '백석', '대곡', '화정', '원당', '원흥',
        '삼송', '지축', '구파발', '연신내', '불광', '녹번', '홍제', '무악재', '독립문',
        '경복궁', '안국', '종로3가', '을지로3가', '충무로', '동대입구', '약수', '금호',
        '옥수', '압구정', '신사', '잠원', '고속터미널', '교대', '남부터미널', '양재',
        '매봉', '도곡', '대치', '학여울', '대청', '일원', '수서', '가락시장', '경찰병원', '오금'],
    '4호선': ['진접', '오남', '별내가람','당고개', '상계', '노원', '창동', '쌍문', '수유', '미아', '미아사거리', '길음', '성신여대입구',
        '한성대입구', '혜화', '동대문', '동대문역사문화공원', '충무로', '명동', '회현', '서울', '숙대입구',
        '삼각지', '신용산', '이촌', '동작', '총신대입구', '사당', '남태령', '선바위', '경마공원',
        '대공원', '과천', '정부과천청사', '인덕원', '평촌', '범계', '금정', '산본', '수리산', '대야미',
        '반월', '상록수', '한대앞', '중앙', '고잔', '초지', '안산', '신길온천', '정왕', '오이도'],
    '5호선': ['방화', '개화산', '김포공항', '송정', '마곡', '발산', '우장산', '화곡', '까치산', '신정', '목동',
        '오목교', '양평', '영등포구청', '영등포시장', '신길', '여의도', '여의나루', '마포', '공덕', '애오개',
        '충정로', '서대문', '광화문', '종로3가', '을지로4가', '동대문역사문화공원', '청구', '신금호', '행당',
        '왕십리', '마장', '답십리', '장한평', '군자', '아차산', '광나루', '천호',
        '강동', '길동', '굽은다리', '명일', '고덕', '상일동', '강일', '미사', '하남풍산', '하남시청', '하남검단산'],
    '5호선_마천행' : ['강동', '둔촌동', '올림픽공원', ' 방이', '오금', '개롱', '거여', '마천'],
    '6호선':['봉화산','화랑대','태릉입구','석계','돌곶이','상월곡','월곡','고려대','안암','보문','창신','동묘앞','신당','청구','약수','버티고개','한강진','이태원','녹사평',
        '삼각지','효창공원앞','공덕','대흥','광흥창','상수','합정','망원','마포구청','월드컵경기장','디지털미디어시티','증산','새절','응암','역촌','불광','독바위','연신내','구산']
}

def oneforall(start,final,Transfer,line):
    def create_station(line):
        st = {}
        for key, value in line.items():
            for i in range(len(value)):
                if value[i] not in st: 
                    st[value[i]] = {}
                    if i == 0:
                        st[value[i]][value[i+1]] = 1
                    elif i == len(value)-1:
                        st[value[i]][value[i-1]] = 1
                    else:
                        st[value[i]][value[i-1]] = 1
                        st[value[i]][value[i+1]] = 1
                else:
                    if i == 0:
                        st[value[i]][value[i+1]] = 1
                    elif i == len(value)-1:
                        st[value[i]][value[i-1]] = 1
                    else:
                        st[value[i]][value[i-1]] = 1
                        st[value[i]][value[i+1]] = 1
                    for k, v in st.items():
                        if value[i] in k and k != value[i]:
                            if i == 0:
                                st[k][value[i]] = 1
                            elif i == len(value)-1:
                                st[k][value[i]] = 1
                            else:
                                st[k][value[i]] = 1
                                st[value[i]][k] = 1
        return st

    station = create_station(line)
    TrFa = False
    cut = []
    cut_1 = []
    final_station = ''
    Transfer_1 = [0]
    Transfer_2 = []
    routing = {}

    for place in station.keys():
        routing[place]={'shortestDist':0, 'route':[], 'visited':0}

    def visitPlace(visit):
        routing[visit]['visited'] = 1
        for toGo, betweenDist in station[visit].items():
            toDist = routing[visit]['shortestDist'] + betweenDist
            if (routing[toGo]['shortestDist'] >= toDist) or  not routing[toGo]['route']:
                routing[toGo]['shortestDist'] = toDist
                routing[toGo]['route'] = routing[visit]['route'].copy()
                routing[toGo]['route'].append(visit)

    for line_name, stations in line.items():
        if start in stations:
            Transfer_1[0] = line_name
            continue
        if final in stations:
            cut.append(line_name)


    if start == final:
        print('출발역과 도착역이 같습니다.')
    elif not Transfer_1[-1] in cut:
        visitPlace(start)
        while 1 :
            minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
            toVisit = ''
            for name, search in routing.items():
                if 0 < search['shortestDist'] <= minDist and not search['visited']:
                    minDist = search['shortestDist']
                    toVisit = name
            if toVisit == '':
                break
            visitPlace(toVisit)
        routing[final]['route'] += [final]
        for rast in routing[final]['route']: # 환승
            for tf in Transfer:
                if TrFa:
                    for line_name, stations in line.items():
                        if rast in stations:
                            cut = line_name
                            break
                    if not Transfer_1[-1] in cut:
                        Transfer_1.append(cut)
                        Transfer_2.append(cut_1)
                    TrFa = False
                if rast == tf:
                    cut = []
                    cut_1 = ''
                    TrFa = True
                    cut_1 = rast
                    break
    else: # 같은 호선일때
        st_1 = line[cut[0]].index(start)
        fi_1 = line[cut[0]].index(final)
        if '2호선' in cut:
            if st_1 > fi_1:
                if round(len(line['2호선'])/2,0) > len(line[cut][st_1:fi_1]):
                    routing[final]['route'] = line['2호선'][fi_1:st_1+1][::-1]
                else:
                    for x in line['2호선'][st_1:]:
                        routing[final]['route'] += [x]
                    for x in line['2호선'][:fi_1+1]:
                        routing[final]['route'] += [x]
            else:
                if round(len(line['2호선'])/2,0) > len(line['2호선'][st_1:fi_1]):
                    routing[final]['route'] = line['2호선'][st_1:fi_1+1]
                else:
                    for x in line['2호선'][fi_1:]:
                        routing[final]['route'] += [x]
                    for x in line['2호선'][:st_1+1]:
                        routing[final]['route'] += [x]
                    routing[final]['route'] = routing[final]['route'][::-1]
            Transfer_1 = ['2호선']
        elif st_1 > fi_1:
            routing[final]['route'] = line[cut[0]][fi_1:st_1+1][::-1]
            Transfer_1 = cut[0]
        else:
            routing[final]['route'] = line[cut[0]][st_1:fi_1+1]
            Transfer_1 = cut[0]
        routing[final]['shortestDist'] = len(routing[final]['route'])-1
        Transfer_2 = []
    
    if len(Transfer_1) > 1:
        if Transfer_2[0] == start:
            Transfer_1 = Transfer_1[1:]
            Transfer_2 = Transfer_2[1:]
    else:
        if Transfer_2 == start:
            Transfer_1 = Transfer_1[1:]
            Transfer_2 = Transfer_2[1:]
            
    print ("\n", "[", start, "->", final,"]")
    print ("경로 :", routing[final]['route'])
    print ("거리/걸린시간 :", routing[final]['shortestDist'])
    print("지나가는 노선 :",Transfer_1)
    print("환승역 :",Transfer_2)
    c = {
        '시작역':[start],
        '마지막역':[final],
        '경로':routing[final]['route'],
        '거리':routing[final]['shortestDist'],
        '지나가는 노선':Transfer_1,
        '환승역':Transfer_2
    }
    return c


# 검색 결과를 출력할 텍스트 박스 생성
result_text1 = tk.Text(window, height=20, width=73,bd=0)
result_text1.place(x=100, y=200)

result_text2 = tk.Text(window, height=20, width=73,bd=0)
result_text2.place(x=100, y=500)

result_text3 = tk.Text(window, height=20, width=73,bd=0)
result_text3 = tk.Text(window, height=20, width=73,bd=0)
result_text3.place(x=100, y=800)

def mouse_click(event):                             # 클릭 시 좌표 출력
    x, y = event.x, event.y
    print("x:", x, "y:", y)

def clear_entries():                                # 초기화 버튼
    start_station.delete(0, tk.END)
    end_station.delete(0, tk.END)
    result_text1.delete('1.0', tk.END)
    result_text2.delete('1.0', tk.END)
    result_text3.delete('1.0', tk.END)
    start_button.destroy()
    end_button.destroy()
    trans.destroy()
    trans2.destroy()
    trans3.destroy()
    trans4.destroy()

def set_marker_on_button(button, image_file):       # 핀 이미지 함수
    img = ImageTk.PhotoImage(file=image_file)
    button.config(image=img)
    button.image = img
    
def set_marker_on_map(map, image_file):             # 지하철 노선도 함수
    map2 = ImageTk.PhotoImage(file=image_file)
    map.config(image=map2)
    map.image = map2
    
def set_marker_on_trans(trans, image_file):         # 출발역 환승 이미지 함수
    transs1 = ImageTk.PhotoImage(file=image_file)
    trans.config(image=transs1)
    trans.image = transs1
    
def set_marker_on_trans2(trans2, image_file):       # 도착역 환승 이미지 함수
    transs2 = ImageTk.PhotoImage(file=image_file)
    trans2.config(image=transs2)
    trans2.image = transs2

def set_marker_on_trans3(trans3, image_file):       # 도착역 환승 이미지 함수
    transs3 = ImageTk.PhotoImage(file=image_file)
    trans3.config(image=transs3)
    trans3.image = transs3
    
def set_marker_on_trans4(trans4, image_file):       # 도착역 환승 이미지 함수
    transs4 = ImageTk.PhotoImage(file=image_file)
    trans4.config(image=transs4)
    trans4.image = transs4
    
        
def search(*args):
    global start_button
    global end_button
    global trans
    global trans2
    global trans3
    global trans4
   
    start = start_station.get()
    end = end_station.get()
    
    result = excel_file[excel_file.iloc[:, 0].str.contains(start, na=False)]
    result2 = excel_file[excel_file.iloc[:, 0].str.contains(end, na=False)]

    # 검색된 결과가 있을 경우 해당 역의 행 정보 출력
    if len(result) > 0 and len(result2) > 0:
        new_font = Font(size=24, weight="bold")
        result_text1.delete("1.0", tk.END)  # 이전 검색 결과 삭제
        result_text1.insert(tk.END, "                   출발역 정보\n\n")
        result_text1.insert(tk.END, result.iloc[0]["역"]+"\n\n")
        result_text1.insert(tk.END, result.iloc[0]["주소"]+"\n")
        result_text1.insert(tk.END, result.iloc[0]["전화번호"])
        result_text1.configure(font=new_font)
        
        result_text2.delete("1.0", tk.END)  # 이전 검색 결과 삭제
        result_text2.insert(tk.END, "                   도착역 정보\n\n")
        result_text2.insert(tk.END, result2.iloc[0]["역"]+"\n\n")
        result_text2.insert(tk.END, result2.iloc[0]["주소"]+"\n")
        result_text2.insert(tk.END, result2.iloc[0]["전화번호"]+"\n")
        result_text2.configure(font=new_font)
        
        canvas = tk.Label(window, width=image.width, height=image.height)
        canvas.place(x=700, y=7)
        set_marker_on_map(canvas, "C:\python\지하철 노선도.png")
        
        start_button = tk.Label(window, width=50, height=50, bg="white")
        start_x, start_y = result.iloc[0]["x좌표"], result.iloc[0]["y좌표"]
        start_button.place(x=start_x+700, y=start_y+8)
        set_marker_on_button(start_button, "C:\python\빨간_도착지_핀_이미지-누끼제거.png")
        
        # 도착역 이미지에 마커 표시
        end_button = tk.Label(window, width=50, height=50, bg="white")
        end_x, end_y = result2.iloc[0]["x좌표"], result2.iloc[0]["y좌표"]
        end_button.place(x=end_x+700, y=end_y+8)
        set_marker_on_button(end_button, "C:\python\빨간_도착지_핀_이미지-누끼제거.png")
        
        if result.iloc[0]["환승"] == 1:
            trans = tk.Label(window, width=50, height=50, bg='white')
            trans.place(x=340, y=270)
            set_marker_on_trans(trans, "C:\python\환승역 이미지_누끼제거.png")
            
        else:
            trans = tk.Label(window, width=50, height=50, bg='white')
            trans.place(x=340, y=270)
            set_marker_on_trans(trans, "C:\Python\흰색 바탕 이미지 50x50.png")
            
        if result2.iloc[0]["환승"] == 1:
            trans2 = tk.Label(window, width=50, height=50, bg='white')
            trans2.place(x=340, y=570)
            set_marker_on_trans2(trans2, "C:\python\환승역 이미지_누끼제거.png")      
        else: 
            trans2 = tk.Label(window, width=50, height=50, bg='white')
            trans2.place(x=340, y=570)
            set_marker_on_trans2(trans2,"C:\Python\흰색 바탕 이미지 50x50.png")
            
        if result.iloc[0]["화장실"] == 1:
            trans3 = tk.Label(window, width=50, height=50, bg='white')
            trans3.place(x=440, y=270)
            set_marker_on_trans3(trans3, "C:\python\화장실 이미지_누끼제거.png")
        else:
            trans3 = tk.Label(window, width=50, height=50, bg='white')
            trans3.place(x=440, y=270)
            set_marker_on_trans3(trans3, "C:\python\화장실 이미지_누끼제거.png")
            
        if result2.iloc[0]["화장실"] == 1:
            trans4 = tk.Label(window, width=50, height=50, bg='white')
            trans4.place(x=440, y=570)
            set_marker_on_trans4(trans4, "C:\python\화장실 이미지_누끼제거.png")      
        else: 
            trans4 = tk.Label(window, width=50, height=50, bg='white')
            trans4.place(x=440, y=570)
            set_marker_on_trans4(trans4,"C:\python\화장실 이미지_누끼제거.png")
        
    if len(result) > 0 and len(result2) > 0:
        code1 = result.iloc[0]["역코드"]
        code2 = result2.iloc[0]["역코드"]
        diff = abs(code1 - code2)*3
        current_time = time.strftime("출발시간 :  %H 시 %M 분 \n")
        result_text3.delete("1.0", tk.END)
        result_text3.insert(tk.END, current_time)
        result_text3.insert(tk.END,"소요시간 :  ")
        
        result_text3.insert(tk.END,round(diff))
        result_text3.insert(tk.END," 분\n")
        result_text3.insert(tk.END,"도착시간 : ")
        result_text3.configure(font=new_font)
        
        current_time = datetime.datetime.strptime(time.strftime("%H:%M"), "%H:%M")
        new_time = current_time + datetime.timedelta(minutes=int(diff))
        new_time_int = new_time.strftime(" %H 시 %M 분")
        print(new_time_int)
        result_text3.insert(tk.END,new_time_int)
        
        print(result.iloc[0]["환승"])
    else:
        print("검색 결과가 없습니다.")
        

# 이미지 출력을 위한 canvas 생성
image = Image.open("C:\python\지하철 노선도.png")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.pack(side="right")
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

new_image = Image.open("C:\python\수도권_전철노선도_제목-removebg-preview.png")
new_photo = ImageTk.PhotoImage(new_image)
new_canvas = tk.Canvas(window, width=new_image.width, height=new_image.height, bg='white')
new_canvas.pack(pady=7)
new_canvas.create_image(0, 0, image=new_photo, anchor=tk.NW)

# 출발역, 도착역 입력 받기
frame1 = tk.Frame(window, width=100, height=80, relief='solid', bd=2)
frame2 = tk.Frame(window, width=200, height=80, relief='solid', bd=2)
frame1.place(x=60, y=120)
frame2.place(x=300, y=120)

start_station1 = tk.Label(frame1, text="출발역")
start_station = tk.Entry(frame1, width=30)
start_station1.pack()
start_station.pack()

end_station1 = tk.Label(frame2, text="도착역")
end_station = tk.Entry(frame2, width=30)
end_station1.pack()
end_station.pack()

# 초기화 버튼 생성
clear_button = tk.Button(window, text="초기화", command=clear_entries, width=5, height=2)
clear_button.place(x=600, y=120)

# 검색 버튼 생성
search_button = tk.Button(window, text="검색", command=search, width=5, height=2)
search_button.place(x=540, y=120)



# Enter 키 바인딩
start_station.bind('<Return>', search)
end_station.bind('<Return>', search)
canvas.bind("<Button-1>", mouse_click)

window.mainloop()