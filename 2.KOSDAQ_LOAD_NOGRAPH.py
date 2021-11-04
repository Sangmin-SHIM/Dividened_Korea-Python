import csv
from tkinter import *
from datetime import date
import tkinter.messagebox as msgbox

def get_filename_datetime():
    return "KOSDAQ (" + str(date.today()) + ").csv"


filename = get_filename_datetime()
f = open(filename, encoding="utf-8-sig", newline="")
Reader = csv.reader(f)
Data = list(Reader)

# Grab all columns information

list_of_brands = []

for x in list(range(1, len(Data), 4)):  # 끝 수에 len(Data)를 넣으면 전체 가능, 2587번째 : 일동제약

    list_of_brands.append(Data[x][0])

# 제목 및 아이콘
root = Tk()
root.geometry('730x400')
root.title("Dividend Tracker Korea - KOSDAQ")
icon = PhotoImage(file='icon.ico')  # png든 ico든 다 됨
root.iconphoto(False, icon)

# ScrollBox
yScroll = Scrollbar(orient=VERTICAL)
yScroll.grid(row=0, column=1, sticky=W + N + S, )

# ListBox
listbox1 = Listbox(root, yscrollcommand=yScroll.set)
listbox1.grid(row=0, column=0)

yScroll['command'] = listbox1.yview

for x, y in enumerate(list_of_brands):
    listbox1.insert(x, y)


# ListBox에서 찾아서 List 버튼으로 찾기
def update():
    index = listbox1.curselection()[0]
    brandlabel2.config(text=Data[index * 4 + 1][0])
    stockpricelabel2.config(text=Data[index * 4 + 1][1])
    datelabel2.config(text=Data[index * 4 + 1][2])
    dividendlabel2.config(text=Data[index * 4 + 1][3])
    ratelabel2.config(text=Data[index * 4 + 1][4] + " %")
    preferencelabel2.config(text=Data[index * 4 + 1][5] + " %")

    # 배당금

    baedang1.config(text=Data[index * 4 + 2][0])
    baedang2.config(text=Data[index * 4 + 3][0])
    baedang3.config(text=Data[index * 4 + 4][0])

    return None


# 기업(종목)명을 찾으세요.
label1font = ('times', 8)
label1 = Label(root, text="기업(종목)명을 찾으세요.")
label1.config(font=label1font)
label1.grid(row=1, column=0)

# 기업(종목)명을 입력하세요.
label1font = ('times', 8)
label1 = Label(root, text="기업(종목)명을 입력하세요.")
label1.config(font=label1font)
label1.grid(row=3, column=0)

# Entry
ent = Entry()
ent.grid(row=4, column=0)


# Search Button 기능
def ent_p():
    search = ent.get()
    # print(search)
    # list_of_brands 기업명 [0] : 1번째 기업
    if search in list_of_brands:
        index = list_of_brands.index(search)
        brandlabel2.config(text=Data[index * 4 + 1][0])
        stockpricelabel2.config(text=Data[index * 4 + 1][1])
        datelabel2.config(text=Data[index * 4 + 1][2])
        dividendlabel2.config(text=Data[index * 4 + 1][3])
        ratelabel2.config(text=Data[index * 4 + 1][4] + " %")
        preferencelabel2.config(text=Data[index * 4 + 1][5] + " %")

        # 배당금

        baedang1.config(text=Data[index * 4 + 2][0])
        baedang2.config(text=Data[index * 4 + 3][0])
        baedang3.config(text=Data[index * 4 + 4][0])

    else:
        msgbox.showwarning("해당 사항 없음", "해당하는 기업(종목)명이 없습니다. 정확하게 다시 써주십시오. \n (알파벳 대/소문자 구분 필수)")


# Button for ListBox
btn = Button(root, text="List", command=update, width=12, height=2)
btn.grid(row=2, column=0, pady=10)

# Button for Search
btn2 = Button(root, text="Search", command=ent_p, width=10, height=2)
btn2.grid(row=5, column=0, pady=20)

# 안내문
label2font = ('times', 8)
label2 = Label(root, text="※ 두 기능 중 하나 선택")
label2.config(font=label2font)
label2.grid(row=6, column=0)

# ---------------------------------- 실제로 표시되는 값들 ---------------------------------
brandlabel = Label(root, text="종목명").grid(row=0, column=3, sticky=N, padx=10, pady=10)
stockpricelabel = Label(root, text="현재가").grid(row=0, column=4, sticky=N, padx=10, pady=10)
datelabel = Label(root, text="기준월").grid(row=0, column=5, sticky=N, padx=10, pady=10)
dividendlabel = Label(root, text="배당금").grid(row=0, column=6, sticky=N, padx=10, pady=10)
ratelabel = Label(root, text="수익률(%)").grid(row=0, column=7, sticky=N, padx=10, pady=10)
preferencelabel = Label(root, text="배당성향(%)").grid(row=0, column=8, sticky=N, padx=10, pady=10)

line1label = Label(root, text="---------------").grid(row=0, column=3, sticky=N, pady=30)
line2label = Label(root, text="---------------").grid(row=0, column=4, sticky=N, pady=30)
line3label = Label(root, text="---------------").grid(row=0, column=5, sticky=N, pady=30)
line4label = Label(root, text="---------------").grid(row=0, column=6, sticky=N, pady=30)
line5label = Label(root, text="---------------").grid(row=0, column=7, sticky=N, pady=30)
line6label = Label(root, text="---------------").grid(row=0, column=8, sticky=N, pady=30)

brandlabel2 = Label(root, text="")
brandlabel2.grid(row=0, column=3, padx=10, pady=10)
stockpricelabel2 = Label(root, text="")
stockpricelabel2.grid(row=0, column=4, padx=10, pady=10)
datelabel2 = Label(root, text="")
datelabel2.grid(row=0, column=5, padx=10, pady=10)
dividendlabel2 = Label(root, text="")
dividendlabel2.grid(row=0, column=6, padx=10, pady=10)
ratelabel2 = Label(root, text="")
ratelabel2.grid(row=0, column=7, padx=10, pady=10)
preferencelabel2 = Label(root, text="")
preferencelabel2.grid(row=0, column=8, padx=10, pady=10)

line2_1label = Label(root, text="---------------").grid(row=0, column=3, sticky=S)
line2_2label = Label(root, text="---------------").grid(row=0, column=4, sticky=S)
line2_3label = Label(root, text="---------------").grid(row=0, column=5, sticky=S)
line2_4label = Label(root, text="---------------").grid(row=0, column=6, sticky=S)
line2_5label = Label(root, text="---------------").grid(row=0, column=7, sticky=S)
line2_6label = Label(root, text="---------------").grid(row=0, column=8, sticky=S)

year1label3 = Label(root, text="1년전").grid(row=2, column=4, sticky=N, padx=10, pady=10)
year2label3 = Label(root, text="2년전").grid(row=2, column=5, sticky=N, padx=10, pady=10)
year3label3 = Label(root, text="3년전").grid(row=2, column=6, sticky=N, padx=10, pady=10)

line3_1label = Label(root, text="----------").grid(row=2, column=4, sticky=S, pady=5)
line3_2label = Label(root, text="----------").grid(row=2, column=5, sticky=S, pady=5)
line3_3label = Label(root, text="----------").grid(row=2, column=6, sticky=S, pady=5)

baedang1 = Label(root, text="")
baedang1.grid(row=3, column=4, padx=10, pady=10)
baedang2 = Label(root, text="")
baedang2.grid(row=3, column=5, padx=10, pady=10)
baedang3 = Label(root, text="")
baedang3.grid(row=3, column=6, padx=10, pady=10)

line4_1label = Label(root, text="----------").grid(row=4, column=4, sticky=S, pady=5)
line4_2label = Label(root, text="----------").grid(row=4, column=5, sticky=S, pady=5)
line4_3label = Label(root, text="----------").grid(row=4, column=6, sticky=S, pady=5)

root.mainloop()
