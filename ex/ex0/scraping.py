import sys
import csv
import requests
from bs4 import BeautifulSoup



if len(sys.argv) < 3:
    print("table名、ページ番号を指定してください")
else:
    table = sys.argv[1]
    page = sys.argv[2]


    load_url = "http://localhost:8080/ex2/%s?page=%s" % (table, str(page))
    response = requests.get(load_url)
    if response.status_code == 200:
        html = requests.get(load_url)
        soup = BeautifulSoup(html.text, "html.parser")

        f = open('./example.csv','w',newline='')
        csv_writer = csv.writer(f)
        for element in soup.find_all("tr"):
            csv_writer.writerow(element.text)
        f.close()
        print("CSV出力が完了しました！")
    else:
        print("Web site does not exist")
