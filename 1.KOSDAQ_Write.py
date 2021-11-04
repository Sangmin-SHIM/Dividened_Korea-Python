import csv
import requests
from datetime import date
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/dividend_list.nhn?sosok=KOSDAQ&page="


def get_filename_datetime():
    return "KOSDAQ (" + str(date.today()) + ").csv"


filename = get_filename_datetime()
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "종목명	현재가	기준월	배당금	수익률(%)	배당성향(%)".split("\t")  # tab으로 구분된 자료들 list화
# ["종목명", "현재가", ...]
writer.writerow(title)

for page in range(1, 13):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    data_rows = soup.find("table", attrs={"class": "type_1 tb_ty"}).find("tbody").find_all("tr")
    tr_frst = soup.find("table", attrs={"class": "type_1 tb_ty"}).find("tbody").find("tr", attrs={
        "class": "tr_frst"}).find_all("td")
    tr_last = soup.find("table", attrs={"class": "type_1 tb_ty"}).find("tbody").find("tr", attrs={
        "class": "tr_last"}).find_all("td")

    for row in data_rows:
        columns = row.find_all("td", limit=6)

        data = [column.get_text().strip() for column in columns]  # strip을 통해서 데이터 내에 의미없는 \n 등을 제거
        if data == ['', '', '', '', '', '', ]:
            continue
        baedang_last = row.find("td", attrs={"class": "num pnt last"})

        print(data)
        writer.writerow(data)

        print("배당금")
        baedangs = row.find_all("td", attrs={"class": "num pnt"})

        idy = 0

        if len(columns) == 6:
            for baedang in baedangs:
                idk = 0

                print("{}년 전 : ".format(idk + 1), baedang.get_text())

                if idy != 0:
                    year = "2년 전 배당금".split("\t")
                    # writer.writerow(zip(year,baedang))  2년 전 배당금 텍스트 포함
                    writer.writerow(baedang)
                else:
                    year = "1년 전 배당금".split("\t")
                    # writer.writerow(zip(year,baedang))   1년 전 배당금 텍스트 포함
                    writer.writerow(baedang)

                idy += 1

            print("3년 전 : ", baedang_last)
            year = "3년 전 배당금".split("\t")

        # writer.writerow(zip(year,baedang_last)) 3년 전 배당금 텍스트 포함
        writer.writerow(baedang_last)

