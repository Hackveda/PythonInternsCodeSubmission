from selenium import webdriver
import time

# Access geeko driver
geeko_path = r"D:\selenium\geckodriver-v0.32.2-win64\geckodriver.exe"
browser = webdriver.Firefox(executable_path = geeko_path)
browser.maximize_window()
browser.get("https://www.knowafest.com/explore/upcomingfests")

# Find the table in website
table = browser.find_element_by_id("tablaDatos")

# Search the element with in the table
th = table.find_elements_by_tag_name("th")
th

table = browser.find_element_by_tag_name("table")
th_list = table.find_elements_by_tag_name("th")
for th in th_list:
    heading = th.text
    print(heading)
    
    
tbody = table.find_elements_by_tag_name("tbody")
tbody    


# Searching for tr tag in tbody with class
tr_list = []
for tbody_elem in tbody:
    tr_list += tbody_elem.find_elements_by_css_selector('tr.g-bg-gray-light-v8--opacity-0_4--checked.odd')
tr_list    



# Iterate over each table row and extract data
import pandas as pd

start_date_list = []
event_name_list = []
organiser_list = []
event_type_list = []
end_date_list = []

for tr in tr_list:
    td_list = tr.find_elements_by_tag_name("td")
    start_date = td_list[0].text
    event_name = td_list[1].text
    
    # Extract read more button on event name
    read_more_btn = td_list[1].find_element_by_class_name("btn")
    
    
    event_type = td_list[2].text
    organiser = td_list[3].text
    end_date = td_list[4].text
    if  start_date == "" or event_name == "":
        pass
    else:
        # print("Event Name: ",event_name, "Event Start Date: ", start_date,
        # "Organiser Name: ", organiser, "Event Type: ", event_type,
        # "Event End Date: ", end_date)
    #print("\n\n")
          start_date_list.append(start_date)
          event_name_list.append(event_name)
          organiser_list.append(organiser)
          event_type_list.append(event_type)
          end_date_list.append(end_date)

table_dict = {"Start Date": start_date_list,"Event Name":event_name_list,
         "Organiser Name": organiser_list, "Event Type": event_type_list,
         "Event End Date":end_date_list} 

event_data = pd.DataFrame(data=table_dict)

#Print the list of all events
event_data.to_csv("Know a fest events list.csv")
    
