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
  google_url = "https://www.googleapis.com/customsearch/v1/?key=AIzaSyD7I4LXGIKuClG82edIkNREBcwQPN1X3Dc&cx=2228319334d154985"
  google_url = google_url + "&q=" + keyword
  print("Google URL: " + google_url)

  #Send a network request to google
  response = requests.get(google_url)
  #print("Response: " + str(response.text))

  #convert Response string into Json
  json_response = json.loads(response.text)
  search_time = json_response["searchInformation"] ["searchTime"]
  print("Search time taken is:", search_time)


  #convert Result string into Json
  total_results = json_response["searchInformation"] ["totalResults"]
  print("Total result are:", total_results)
  #Reset the keyword
  keyword = keyword1
