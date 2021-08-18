import re 
from faker import Faker # glop also could be use 
import shutil # use to provided which support file copying and removal 

with open ('potential-contacts.txt') as file:
    poential_cont = file.read()
    
# useing regex to find the phone num

telephone_num = []
telephone_num.extend(re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',poential_cont))

# for duplicates 

duplicate_phone = list(set(telephone_num))
duplicate_phone.sort()

telephone = " "

for i in duplicate_phone:
    telephone += i + ', '
    # print (telephone)
    
    # for email 
    
    email_address = []
    email_address.extend(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", poential_cont))
    
    #remove duplicates 
    
    email_remove_duplicates = list(set(email_address)) #set use to remove the duplicates 
    
    email = " "
    for i in email_remove_duplicates:
        email += i + ','

# create new doc

with open ('new_telephone_number.txt' , 'w') as file :
    telephone_number = file.write(telephone)
    
with open ('new_email_address.txt' , 'w')as file :
    email_address_copy = file.write(email)
        
        