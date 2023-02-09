#Digital Marketing Tool using API
import requests      #requests is used to send HTTP request
import pandas as pd  #it is used to representdata in tabular form
import json          #for data representation during transmission


from datetime import date,timedelta

#Take keyword from the user
keyword = input("Enter a keyword: ")
keyword1 = keyword
#Search keyword on quora
#keyword = keyword + "site:quora.com" this is used for single website

#Search in multiple website
site_list = ["quora.com","reditt.com","microsoft.com"]
for site in site_list:
  keyword = keyword + "site: " + site
  print(keyword)
  # Search on google using google APi
  #file - AIzaSyD7I4LXGIKuClG82edIkNREBcwQPN1X3Dc
  google_url = "https://www.googleapis.com/customsearch/v1/?key=AIzaSyD7I4LXGIKuClG82edIkNREBcwQPN1X3Dc"
  google_url = google_url + "&q=" + keyword
  print("Google URL: " + google_url)

  #Send a network request to google
  response = requests.get(google_url)
  print("Response: " + str(response))
  #REset the keyword
  keyword = keyword1
