from re import search
#Digital Marketing Tool using API

import requests      #requests is used to send HTTP request
import pandas as pd  #it is used to representdata data in tabular form
import json          #for data representation during transmission

from datetime import date,timedelta   #this is used to manage data and time 


#Global variable
questions_list = []


#Take keyword from the user
keyword = input("Enter a keyword: ")
keyword1 = keyword

#Search keyword on quora
#keyword = keyword + "site:quora.com" this is used for single website

#Search on multiple website
site_list = ["quora.com", "reditt.com"]
for site in site_list:
  keyword = keyword + "site:" + site


  # Search on google using google API
  #file - AIzaSyD7I4LXGIKuClG82edIkNREBcwQPN1X3Dc
  google_url = "https://www.googleapis.com/customsearch/v1/?key=AIzaSyD7I4LXGIKuClG82edIkNREBcwQPN1X3Dc&cx=2228319334d154985"
  google_url = google_url + "&q=" + keyword
  #print("Google URL: " + google_url)

  #Send a network request to google
  response = requests.get(google_url)
  #print("Response: " + str(response.text))

  #convert Response string into Json
  json_response = json.loads(response.text)
  #search_time = json_response["searchInformation"] ["searchTime"]
  #print("Search time taken is:", search_time)


  #convert Result string into Json
  total_results = int(json_response["searchInformation"] ["totalResults"])
  #print("Total result are:", total_results)

  #get the start index of next page
  #next_index = json_response["queries"]["nextPage"][0]["startIndex"]

  #Loop through all responses from google
  total_pages = round(total_results / 10)

  try:
    #loop through the responses
      for item in json_response["items"]:
       title = item["title"]
       title = title.replace("-Quora","")
       questions_list.append(title)


  except Exception as e:
    pass


  #Reset the keyword
  keyword = keyword1


#questions_list  
questions_dict = {"Questions" : questions_list}
df = pd.DataFrame(data=questions_dict)
df

