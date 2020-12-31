import json
import time
import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import sys
import os



temp={} #'d' is the dictionary in which we store data

while(True):
    try:
    #input to perform operation in master,existing or new file
        x=int(input('ON WHICH FILE(DATABASE) DO YOU WANT TO PERFORM OPERATIONS ? \n1.MASTER DATABASE(file) 2.OPEN EXISTING DATABASE(file) 3.NEW DATABASE(file): '))
    except:
        print("Enter integer input")
        continue



    if (x==1): #for master file
        print('Loading master database in temp...')
        with open('master.json','r') as masteropen:
            try:
                user_input="default";
                data_load=json.load(masteropen)
                temp=data_load
                print('loaded master database->', end=' ')  #load master database
                print(temp)
                break
            except:
                print("No data exist")
                break

    elif(x==2): #for existing file              
        user_input = input("Enter the path of your file(with file name) or only file name (ex:filename.json) : ")

        if(os.path.exists(user_input)):
            print("Hooray we found your file! ->",end=' ')
            with open(user_input,'r+') as masteropen:
                try:
                    data_load=json.load(masteropen)
                    temp=data_load
                    print('loaded master database->', end=' ') #load master database
                    print(temp)
                    break
                except:
                    print("No data exist")
                    break
        else:
            print("File not exist")

            
    elif(x==3): #for new file

            a=input("Do you want to create new file -> [yes/no] :");
            if(a.lower()=='yes'):
                user_input = input("Enter the path (with file name) or only file name(ex:filename.json): ")
                print("Hooray we created your file! ->",end=' ')
                with open(user_input,'w+') as masteropen:
                    try:
                        data_load=json.load(masteropen)
                        temp=data_load
                        print('loaded master database->', end=' ')   #load master database
                        print(temp)
                        break
                    except:
                        print("But No data exist ")
                        break
            if (a!='yes' and a!='no'):
                print("pls enter yes/no")
                
                
    elif(x!=1 and x!=2 and x!=3):
        print("Wrong input!")
    
        


d=temp

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
def read(k):
    if k not in d:
        print("error: the key is not present ")
    else:
        b=d[k]
        if b[1]!=0:
            if time.time()<b[i]:
                stri=str[k]+":"+ str(b[0])
                return stri
            else:
                print("error:time-to-live of",k,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if str(time.time())<str(b[1]): #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")
            
            
while(True):            
    x=input('ENTER -> 1.FOR CREATE 2.FOR READ 3.FOR DELETE 4 TO EXIT ,5.TO SHOW DATA :')  #input for operations
    try:
        x=int(x)
    except:
        print("Enter integer input only")
        continue

    if(x==4):
        break
    if(x==1):
        key=input("enter ->key for input:")
        value=int(input("enter its corresponding -> value :")) #Timeout=int(input('enter time ,default is 0')) 
        create(key,value)
    if (x==2):
        key=input("enter key to read:")
        print(read(str(key)))
    if (x==3):
        key=input("enter key:")
        delete(key)
    if (x==5):
        print('Data is ->',d)
    if (x!=1 and x!=2 and x!=3 and x!=4 and x!=5):
        print("Wrong input")
        continue

    




temp=d
with open('temp.json','w') as fp:
          json.dump(temp,fp)



print("your database after operations are: ",end='' )
print(temp)





while (True) :
    

        
    y=input("Do you want to save this in the master dataset [yes/no]:")
    y=y.lower()
    if (y=='yes'):
        data={}
        
        
        if(user_input=='default'):
            with open('master.json','r') as fp:
                try:
                    data=json.load(fp)
                except:
                    print()
                master=dict(data)
                master.update(temp)    
            with open('master.json','w') as fp:
                json.dump(temp,fp)
            print("all task done,thanks")
            break
        else:
            with open(user_input,'r') as fp:
                try:
                    data=json.load(fp)
                except:
                    print()
                master=dict(data)
                master.update(temp)    
            with open(user_input,'w') as fp:
                json.dump(temp,fp)
                print("all task done,thanks")
                break
    if (y=='no'):
        break

    elif (y!='yes' and  y!='no'):
        print("wrong input")
        continue
        
                
                       
 
