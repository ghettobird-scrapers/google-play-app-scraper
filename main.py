#Based on:
#https://github.com/danieliu/play-scraper/blob/89be7091fe02b4402c0ae8a72a94e360364080ac/play_scraper/utils.py#L236

from ghettobird import fly

bird = {
 "url": "https://play.google.com/store/apps/details?id=com.chess",
    "flightpath": {
     "genre": "//a[@itemprop='genre']",
     "content_rating": "//div[@class='hAyfc'][./div[contains(text(),'Content Rating')]]//span//div//span//div",
     "updated": "//div[@class='hAyfc'][./div[contains(text(),'Updated')]]//span//div//span",
     "version": "//div[@class='hAyfc'][./div[contains(text(),'Current Version')]]//span//div//span",
     "required_android_version": "//div[@class='hAyfc'][./div[contains(text(),'Requires Android')]]//span//div//span",
     "installs": "//div[@class='hAyfc'][./div[contains(text(),'Installs')]]//span//div//span",
     "in_app_products": "//div[@class='hAyfc'][./div[contains(text(),'In-app Products')]]//span//div//span",
     "offered_by": "//div[@class='hAyfc'][./div[contains(text(),'Offered By')]]//span//div//span",
     "size": "//div[@class='hAyfc'][./div[contains(text(),'Size')]]//span//div//span",
     "interactive_elements": "//div[@class='hAyfc'][./div[contains(text(),'Interactive Elements')]]//span//div//span",
     "developer_email":  "//div[@class='hAyfc'][./div[contains(text(),'Developer')]]//span//div[2]//a",
     "developer_address":  "//div[@class='hAyfc'][./div[contains(text(),'Developer')]]//span//div[4]",
     "rating": "//div[@class='K9wGie']//div[@class='BHMmbe']"
    }
}


scraped = fly(bird)
print(scraped['results'])

