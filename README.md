
# **Watch Collection Web Scraper**

This Python script is designed to scrape data from the [gcshopeg.com](https://gcshopeg.com/) website, specifically from the watches section. It extracts the brand, model, price (both discounted and regular), and images of various watch brands, saving the scraped data into a CSV file and the images locally.

## **Features**

- Scrapes brand name, model name, and price details (regular and discounted prices) from the watch collections.
- Downloads images of each watch and stores them in a specified directory.
- Saves all the extracted information into a CSV file.

## **Requirements**

To run this script, you need the following Python packages:
1. `requests`: For sending HTTP requests to fetch web pages.
2. `beautifulsoup4`: For parsing the HTML content of web pages.
3. `csv`: For saving the scraped data to a CSV file.

You can install the required packages using the following command:

```bash
pip install requests beautifulsoup4
```

## **How the Script Works**

1. **Website URL Structure**: The script scrapes watches from the [gcshopeg.com](https://gcshopeg.com/) website. Each brand's collection is organized under URLs like:
   ```
   https://gcshopeg.com/collections/<brand>
   ```
   For example, the URL for Fossil watches is:
   ```
   https://gcshopeg.com/collections/fossil
   ```

2. **Input Brands and Pages**: A dictionary of brands and their respective page lengths is used to specify how many pages of watches should be scraped for each brand. For example:
   ```python
   models = 
   {
    "fossil": 5,
    "guess-watches": 5,
    "g-shock": 8,
    "citizen": 11,
    "casio": 12, 
    "swatch": 3
    }
   ```

3. **Web Scraping Process**: 
   - For each brand, the script loops through the specified number of pages and scrapes the watch data:
     - **Brand Name**: Extracted from the page using the class `h4`.
     - **Model Name**: Extracted from the page using the class `mb0`.
     - **Price**: Both the discounted and regular prices are extracted using the classes `price-item price-item--sale` and `price-item price-item--regular`, respectively.
     - **Images**: Images are downloaded by accessing the `src` attribute of the `img` tags.

4. **Data Storage**:
   - **CSV File**: All the scraped data (brand, model, price after discount, and price before discount) is saved into a CSV file called `watches.csv`.
   - **Image Files**: Each image is downloaded and stored in a local directory with a unique file name that combines the model name, index, and page number.

## **Usage Instructions**

1. **Clone the Repository**: Start by cloning this repository to your local machine.
   
2. **Run the Script**:
   Ensure your Python environment is set up, and then run the script:
   ```bash
   python web_scraping.py
   ```

3. **Output**:
   - A CSV file named `watches.csv` will be created in the `Web Scraping` directory with the following columns:
     - **Brand**: The name of the watch brand.
     - **Model**: The model name of the watch.
     - **Price After Discount**: The discounted price of the watch (if available).
     - **Price Before Discount**: The original price of the watch.
   - Watch images will be saved in the `images` folder.

## **Code Overview**

```python
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

```

## **Directory Structure**

```
Web Scraping/
│
├── watches.csv                  # CSV file with scraped data
└── images/                      # Folder where watch images are saved
    ├── model1-1.jpg
    ├── model2-1.jpg
    └── ...
```

## **Notes**

- Ensure the local directories for storing CSV files and images exist before running the script.
- The script handles multiple pages of data for each brand as specified in the `models` dictionary.
- Make sure to update the paths in the script according to your environment.
