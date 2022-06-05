import random

list1 = ("rice","tuna","salmon","groud_meat", "potato","bread_sandwich_meat", "chicken","steak","lentals","hummis", "sweet_potato", "ravioli_pastasauce") #legendary to buy

list2 = ("oatmels","beans","pita_bread", "sardines","eggs","ginger_ale","frozen_section","spinach","milk", "mac_n_cheese","mushrooms") #rare to buy

list3 = ("snacks","cereal","banana","broccli","cashews","green_pea","bogo","pita_bread", "pickles") #common to buy
    
print ('''
Mondays Here! 

Time to head to the store!

Make sure to follow the 
list an stay in the boundaries!!

|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
V   V   V   V   V   V   V   V
''')


list1 = random.sample (list1 , k=5) 
print  (list1)

list2 = random.sample (list2 , k=6) 
print (list2)

list3 = random.sample (list3 , k=5) 
print  (list3)