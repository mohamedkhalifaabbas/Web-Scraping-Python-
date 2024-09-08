import requests 
from bs4 import BeautifulSoup
import csv 


def web_scripting(model ,length)  :

    url = f"https://gcshopeg.com/collections/{model}" 

    for i in range(2 , length) :

        page = requests.get(url)
        page = BeautifulSoup(page.content, 'html.parser')

        brand  = page.findAll("p" ,  class_="h4")
        model  = page.findAll("h3" ,  class_="mb0")
        price_after_dis  = page.findAll("span" ,  class_="price-item price-item--sale")
        price_before_dis = page.findAll("s" ,  class_="price-item price-item--regular")

        images = page.find_all('img')
        

        for j in range(len(brand)):
                
                img_url = images[j].get("src")
                if not img_url.startswith("http"):
                    img_url = "https:" + img_url
                response_img = requests.get(img_url)
                img_name = f"F:/AI (instant)/images/{model[j]}{j}-{i}.jpg"
                
                with open(img_name, 'wb') as img_file:
                    img_file.write(response_img.content)


                csv_.writerow([brand[j].text.strip() 
                               , model[j].text.strip() 
                               , price_after_dis[j].text.strip() 
                               , price_before_dis[j].text.strip()])


        url = f"https://gcshopeg.com/collections/{model}?page={i}"



file = open(r"F:\AI (instant)\watches.csv", mode="w", newline="", encoding="utf-8")
csv_ = csv.writer(file)
csv_.writerow(["Brand", "Model", "Price After Discount", "Price Before Discount"])  # write the header


models = {"fossil" : 5  , "guess-watches" : 5, "g-shock" : 8 , "citizen" : 11 ,"casio" : 12 , "swatch" : 3} 

for model , length in models.items() : 
    web_scripting(model , int(length))



file.close()
