

from tkinter import *
from datetime import date
import requests
import datetime
from bs4 import BeautifulSoup
from xml.dom import minidom
import json
import xml.etree.ElementTree as ET
import tkinter.scrolledtext as st
import tkinter as tk
from tkinter.ttk import Combobox  
import pdb



res1=0
res2=0
res=0

def  clicked1():
    global res2
    global res
    global res1
    global combo1
    res = combo.get()
    print('res=',res)
    slov={"Вельяминово":"9602029", "Жилево":"9600694", "Михнево":"9600749", "Павелецкий вокзал":"2000005",  "Ступино":"9601202",  "Акри":"9601726", "Белопесоцкий":"9600772", "Грачевская":"9603877", "Моссельмаш":"9603478", "Химки":"9603401",
          "Малино":"9600212", "Ленинградский вокзал":"2006004", "Конаково":"9603735"}
    res1=slov.get(res)
    print('res1=',res1)
   
    if res1=='9603877':
       lbl1 = Label(window, text="Ленинградское")  
       lbl1.grid(column=0, row=6)
       combo1 = Combobox(window)
       combo1['values'] = ("Ленинградский вокзал","Химки","Моссельмаш")  
       combo1.current(1)  # установите вариант по умолчанию  
       combo1.grid(column=0, row=8) 
       #res3=combo1.get()
       #print('comma=',res3)
 
    
    elif res1=='2000005':
       lbl1 = Label(window, text="Павелецкое")  
       lbl1.grid(column=0, row=6)
       combo1 = Combobox(window)  
       combo1['values'] = ("Михнево", "Акри", "Ступино", "Белопесоцкий")  
       combo1.current(1)  # установите вариант по умолчанию
       combo1.grid(column=0, row=8)
    

      #pdb.set_trace()  
    return(res1)
    
def clicked2():
      global res3
      global res5
      global res6
      global txt3
      global txt4
      print('rres1=',res1)
      res3=combo1.get()
      print('станция прибытия=',res3)
      lbl3 = Label(window, text="час")  
      lbl3.grid(column=0, row=14)  
      txt3 = Entry(window,width=10)  
      txt3.grid(column=0, row=16)

      lbl4 = Label(window, text="мин")  
      lbl4.grid(column=0, row=18)  
      txt4 = Entry(window,width=10)  
      txt4.grid(column=0, row=20)
      #res5=txt3.get()
      #res6= txt4.get()
    
      return(res3)
def clicked():
    
       global res5
       global res6
       
       c=0
       m=0
       cm=0
       res2=combo.get()
       print('command=',res2)
       slov1=[]
       res5=txt3.get()
       res6= txt4.get()
       print('res5=',res5)  
       k=0
       nak=0
       nk=0
       slov={"Вельяминово":"9602029", "Жилево":"9600694", "Михнево":"9600749", "Павелецкий вокзал":"2000005",  "Ступино":"9601202",  "Акри":"9601726", "Белопесоцкий":"9600772", "Грачевская":"9603877", "Моссельмаш":"9603478", "Химки":"9603401",
          "Малино":"9600212", "Ленинградский вокзал":"2006004", "Конаково":"9603735"}
       res1=slov.get(res2)
   
       print('res11=',res1)
    
       res4=slov.get(res3)
       print('res12=',res4)
      
       current_date = date.today()
       url11=chr(34)

       url="https://api.rasp.yandex.net/v3.0/search/?apikey=622f978d-a274-41bd-b297-e7de99a7ab1f&format=json&from=s"
       url1=res4
       url2="&to=s"
       url3=res1
       url4="&lang=ru_RU&page=1&date="
       url5=str(current_date)
       url6=url1+url1+url2+url3+url4+url5
       print(url6)    
       response = requests.get(url6.strip())
       data = response.json()
       i=0
       
#работаем со временем
    
       print('res5=',res5)
       try:
         chas2=int(res5)
         print('chas2=',chas2)
       except ValueError:
        print('Это что ещё такое?')
        ls='Это что ещё такое?'
        k=1 
       try:  
         min2=int(res6)
       except ValueError:
         print('Это что ещё такое?')
         ls='Это что ещё такое?'
         k==1
       except UnboundLocalError:
         print('Это что ещё такое?')
         ls='Это что ещё такое?'
         k=1
       print('k=',k)  
       if k==1: text6.insert(tk.INSERT," Введите время")
       else:      
          now = datetime.datetime.now()  
          print('nak=',nak)
          realchas=int(now.hour)
          realmin=int( now.minute)
          min=realmin+min2+20
          
          if (min>=60):
            min=min-60
            if (nak==1):chas=realchas+chas2+2      
            else:chas=realchas+chas2+1
           
          else:     
            if nak==1: chas=realchas+chas2+1
            else:chas=realchas+chas2      
       
          for item in data:
           print(item)     
          for item in data['segments']:
            it=item
            it1=item['departure']
       
            dt=it1[11:16]
            ch=dt[0:2]
            mn=dt[3:5]
            print('ch=',ch)
            print('mn=',mn)
      
            ch1=int(ch)
            mn1=int(mn)
       
            if (ch1>chas) :
              print(it1[11:16])
              slov1.append(it1[11:16])
            elif (ch1==chas) and (mn1>=min):
              print (it1[11:16])   
              slov1.append(it1[11:16])
            i=i+1
         
          print(slov1)
          i=0
    
      
          print(len(slov1))
          text6.delete(1.0, END) 
          if len(slov1)!=0:
            while i<=(len(slov1)-1):
             print(slov1[i])       
             text6.insert(tk.INSERT,slov1[i])
             text6.insert(tk.INSERT,"                                                  ")
             i=i+1
          else: text6.insert(tk.INSERT," Вы не успеваете ни на один")     
#def clicked2():
      #res3=combo1.get()
      #print('comma=',res3) 
 
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")  
 

window.geometry('400x250')  
lbl = Label(window, text="станция отправления")  
lbl.grid(column=0, row=0)


window.geometry('400x250')  
combo = Combobox(window)  
combo['values'] = ("Павелецкий вокзал", "Грачевская")  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=0, row=2)
btn = Button(window, text="станция прибытия", command=clicked1)  
btn.grid(column=0, row=4)





#pdb.set_trace()

#lbl2 = Label(window, text="Ваше время до выхода,час,мин")
#lbl2.grid(column=0, row=12)

btn = Button(window, text="время до выхода", command=clicked2)  
btn.grid(column=0, row=12)

btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=0, row=24) 
 

#
text6 = st.ScrolledText(window,width = 30, height = 8,font = ("Times New Roman",15))
  
text6.grid(column = 0, pady = 10, padx = 10)
 




window.mainloop()
