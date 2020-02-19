# Helps us in getting the data from the URL
import requests
from bs4 import BeautifulSoup

# URL of the product page which you want.
URL = "https://www.amazon.in/Bangalore-Refinery-999-9-Yellow-Gold/dp/B01HVB3PPC/ref=sxin_4?ascsubtag=amzn1.osa.841988af-23c9-4aa4-8bf3-522fe12d3817.A21TJRUUN4KGV.en_IN&creativeASIN=B01HVB3PPC&cv_ct_cx=gold&cv_ct_id=amzn1.osa.841988af-23c9-4aa4-8bf3-522fe12d3817.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_wn=osp-single-source&keywords=gold&linkCode=oas&pd_rd_i=B01HVB3PPC&pd_rd_r=b5b3bfc8-1bb1-4041-86f0-4683928aa0b2&pd_rd_w=Uwu8Q&pd_rd_wg=dE82S&pf_rd_p=c08fa7ba-5992-402a-8cce-56eabbfee1ac&pf_rd_r=YC4SKYC5NGAMAMVQX3V3&qid=1582088333&tag=htsyndicate-21#customerReviews"

header = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()
    float_price = float(price[2:4]+price[5:8])

    if ( float_price < 22000.0):
        send_mail()

