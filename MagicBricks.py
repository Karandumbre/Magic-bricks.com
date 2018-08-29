#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:30:59 2018

@author: karan.ganesh.dumbre
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:12:25 2018

@author: karan.ganesh.dumbre
"""
import pandas as pd
from pandas import ExcelWriter
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='/Users/karan.ganesh.dumbre/chromedriver');
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai")
urls = []

for i in range(1,18): 
    html = driver.page_source
    soup = BeautifulSoup(html)

    for tag in soup.find_all(class_='flex relative clearfix m-srp-card__container'):
        if tag.a:
            urls.append(tag.a['href'])
            
    next_page = driver.find_element_by_link_text('Next Page')
    next_page.click()
    time.sleep(5)

#### Deleting unnecessary variables
del(i,html)       
#### Define all the variables
data = []
values = []
address = [];
age_of_construction = [];
amenities = [];
authority_approval = [];
bathrooms = [];
bedrooms = [];
car_parking = [];
carpetarea = [];
description = [];
electricity = [];
facing = [];
floor = [];
flooring= [];
furnishing = []
landmarks = [];
lift = [];
overlooking = [];
pujarooms = [];
society = [];
superArea = [];
status = [];
storerooms = [];
studyrooms = [];
transaction_type = [];
type_of_ownership = [];
water_availability = [];
product_price = [];
product_title = [];

##Function to extract data

def extract(a):
    common = soup1.find("div", {"class": a})
    if(common == None):
        return;
    else:
        value = common.find_all("div", {"class": "p_value"})
        title = common.find_all("div", {"class": "p_title"})
        data[:] = []
        values[:]=[]
    
        for d in title:
            freetext = d.text.encode('ascii','ignore')
            freetext = freetext.decode('utf8')
            data.append(freetext.replace('\n',''))
        
        for v in value:
            freetext = v.text.encode('ascii','ignore')
            freetext = freetext.decode('utf8')
            values.append(freetext.replace('\n',''))

## to check null Variables
def checkNull(variable):
    if(variable == None):
        print(variable)
        return None;
    else:
        value = variable.text.encode('ascii','ignore')
        value = value.decode('utf8')
        return value.replace('\n','')


## function to check null value
def nullFunction(array,variable):
    if variable is None:
        array.append(variable)
    else:
        array.append(variable)
        
 ### Apending data to variables
def callFunction():
    nullFunction(address,Address);
    nullFunction(age_of_construction,Age_of_Construction);
    nullFunction(amenities,Amenities);
    nullFunction(authority_approval,Authority_Approval);
    nullFunction(bathrooms,Bathrooms);
    nullFunction(bedrooms,Bedrooms);
    nullFunction(car_parking,Car_parking);
    nullFunction(carpetarea,Carpet_Area);
    nullFunction(electricity,Electricity);
    nullFunction(facing,Facing);
    nullFunction(floor,Floor);
    nullFunction(flooring,Flooring);
    nullFunction(furnishing,Furnishing)
    nullFunction(landmarks,Landmarks);
    nullFunction(lift,Lift);
    nullFunction(overlooking,Overlooking);
    nullFunction(pujarooms,PujaRoom);
    nullFunction(storerooms,Store_room)
    nullFunction(society,Society);
    nullFunction(superArea,Super_Area);
    nullFunction(status,Status);
    nullFunction(studyrooms,StudyRoom);
    nullFunction(transaction_type,Transaction_type);
    nullFunction(type_of_ownership,Type_of_Ownership);
    nullFunction(water_availability,Water_Availability);
    nullFunction(product_price,price);
    nullFunction(product_title,title);

j = 0
### Execution begins
for i in urls:  
    print(j)
    if j > 500: #### Condition to check 500 entries
        break;
    j = j + 1
    #### Initialise all variables to None
    Store_room = None;
    Bedrooms = None;
    Bathrooms = None;
    PujaRoom = None;
    StudyRoom = None;
    Balconies = None;
    Age_of_Construction = None;
    Address = None;
    Landmarks = None;
    Facing = None;
    Overlooking = None;
    Flooring = None;
    Authority_Approval = None;
    Water_Availability = None;
    Electricity = None;
    Lift = None;
    Furnishing = None;
    Type_of_Ownership = None;
    Amenities = None;
    Car_parking= None;
    title= None;
    price= None;
    Transaction_type= None;
    Status= None;
    Super_Area= None;
    Society= None;
    Floor= None;
    Description= None;
    Carpet_Area= None;
    
    
    #Extract Price and title of property
    contents = requests.get(i)
    soup1 = BeautifulSoup(contents.content)
    price = soup1.find("div", {"id": "priceSv"})
    price = checkNull(price);
    
    title = soup1.find("span", {"class": "p_bhk"})
    title = checkNull(title);


    #####Extract basic details 
    extract("propInfoBlockInn")    
    count = 0;
    for d in data:
        if(d == 'Store Room'):
            Store_room = values[count]
        if(d in ('Bedrooms','Bedroom')):
            Bedrooms = values[count]
            Bedrooms = Bedrooms[:1]
        if(d == 'Bathrooms'):
            Bathrooms = values[count]        
        if(d in ('PujaRoom','Puja Room')):
            PujaRoom = values[count]
        if(d == 'StudyRoom'):
            StudyRoom = values[count]
        if(d == 'Transaction type'):
            Transaction_type = values[count]
        if(d == 'Balconies'):
            Balconies = values[count]
        if(d == 'Society'):
            Society = values[count]
        if(d == 'Status'):
            Status = values[count]
        if(d == 'Transaction type'):
            Transaction_type = values[count]
        if(d =='Floor'):
            Floor = values[count]
        if(d == 'Furnished status'):
            Furnishing = values[count]
        if(d == 'Car parking'):
            Car_parking = values[count]
        if(d == 'Lifts'):
            Lift = values[count]
        count = count + 1;

    ###Extract the carpet and super Area
    common = soup1.find("div", {"id": "secondFoldDisplay"})
    if(common == None):
        Super_Area = None;
        Carpet_Area = None;
    else:
        Super_Area = common.find("span", {"id": "coveredAreaDisplay"})
        Super_Area = checkNull(Super_Area)
            
        Carpet_Area = common.find("div", {"id": "carpetArea"})
        Carpet_Area = checkNull(Carpet_Area)


    ############descriptionCont
    extract("descriptionCont")
    
    count = 0;
    for d in data:
        if(d == 'Address'):
            Address = values[count]
        if(d == 'Landmarks'):
            Landmarks = values[count]
        if(d =='Facing'):
            Facing = values[count]
        if(d == 'Overlooking'):
            Overlooking = values[count]
        if(d == 'Flooring'):
            Flooring = values[count]
        if(d == 'Water Availability'):
            Water_Availability = values[count]
        if(d =='Status of Electricity'):
            Electricity = values[count]
        if(d == 'Lift'):
            Lift = values[count]
        if(d == 'Age of Construction'):
            Age_of_Construction = values[count]
        if(d =='Furnishing'):
            Furnishing = values[count]
        if(d == 'Authority Approval'):
            Authority_Approval = values[count]
        if(d == 'Type of Ownership'):
            Type_of_Ownership = values[count]
        if(d =='Amenities'):
            Amenities = values[count]
        count = count + 1

    callFunction()



### All unnecessary variables
del(Transaction_type,d,count,i,Store_room,Bedrooms,Bathrooms,PujaRoom,StudyRoom,Balconies,Age_of_Construction,Address,Landmarks,Facing,Overlooking,Flooring,Authority_Approval,Water_Availability,Electricity,Lift,Furnishing,Type_of_Ownership,Amenities,Car_parking,title,price,Status,Super_Area,Society,Floor,Description,Carpet_Area)


df = pd.DataFrame({
        "title":product_title,
        "price":product_price,
        "Address":address,
        "Age_of_Construction":age_of_construction,
        "Amenities":amenities,
        "Authority_Approval":authority_approval,
        "Bathrooms":bathrooms,
        "Bedrooms":bedrooms,
        "Car_parking":car_parking,
        "Carpet_Area":carpetarea,
        "Electricity":electricity,
        "Facing":facing,
        "Floor":floor,
        "Flooring":flooring,
        "Furnishing":furnishing,
        "Landmarks":landmarks,
        "Lift":lift,
        "Overlooking":overlooking,
        "PujaRoom":pujarooms,
        "Store_room":storerooms,
        "Society":society,
        "Super_Area":superArea,
        "Status":status,
        "StudyRoom":studyrooms,
        "Transaction_type":transaction_type,
        "Type_of_Ownership":type_of_ownership,
        "Water_Availability":water_availability,
        })




#Export To excel
writer = ExcelWriter('MagicBriks.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()



