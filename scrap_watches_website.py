import requests 
from bs4 import BeautifulSoup
import csv 


def web_scripting(watch_model ,length)  :

    # This function scrapes the watch data from the gcshopeg.com website.


    url = f"https://gcshopeg.com/collections/{watch_model}" 

    for i in range(2 , length+1) :
        try :
            # Fetch the webpage
            page = requests.get(url)
            page = BeautifulSoup(page.content, 'html.parser')

            # Extract data
            brand  = page.findAll("p" ,  class_="h4")
            watch_model  = page.findAll("h3" ,  class_="mb0")
            price_after_dis  = page.findAll("span" ,  class_="price-item price-item--sale")
            price_before_dis = page.findAll("s" ,  class_="price-item price-item--regular")

            images = page.find_all('img')
            
            # Iterate through the scraped data
            for j in range(len(brand)):
                    # Get the image URL and check if it's relative or absolute
                    img_url = images[j].get("src")
                    if not img_url.startswith("http"):
                        img_url = "https:" + img_url

                    # Download the image
                    response_img = requests.get(img_url)
                    img_name = f"F:/AI (instant)/images/{watch_model[j]}{j}-{i}.jpg"

                    # Save the image
                    with open(img_name, 'wb') as img_file:
                        img_file.write(response_img.content)

                    # Write data to CSV
                    csv_.writerow([brand[j].text.strip() 
                                , watch_model[j].text.strip() 
                                , price_after_dis[j].text.strip() 
                                , price_before_dis[j].text.strip()])

        except Exception as e :
             print(e)             


        url = f"https://gcshopeg.com/collections/{watch_model}?page={i}"


# Open CSV file for writing
file = open(r"F:\AI (instant)\watches.csv", mode="w", newline="", encoding="utf-8")
csv_ = csv.writer(file)

# write the header
csv_.writerow(["Brand", "watch_Model", "Price After Discount", "Price Before Discount"])  

# Dictionary of watch brands and the number of pages to scrape
watch_models ={
     "fossil" : 4  , 
     "guess-watches" : 4 , 
     "g-shock" : 7 , 
     "citizen" : 10 ,
     "casio" : 11 , 
     "swatch" : 2
     } 


# Loop through each brand and scrape the data
for watch_model , length in watch_models.items() : 
    web_scripting(watch_model , int(length))


# Close the CSV file
file.close()
