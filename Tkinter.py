
#A simple project with the task of storing information in a .txt file. The program is a login page


from tkinter import *

r = Tk()

r.config(background='#36454F') 


#الدوال

def save_bata() :
	
	#جلب قيم الندخلات
	name = E1.get()
	age = E2.get()
	phone = E3.get()
	
	#اضافة القيم الى ملف
	f = open("xx.txt",'a')

	f.write(f'''
--------------------------------------------------
name : {name}
age : {age}
number phone : {phone}
--------------------------------------------------
''')

	f.close()
	
	#فتح نافذة جديدة
	KT = Tk()
	
	#تعريض النافذة
	Km = Label(KT,text='_______________________________________________',fg='white',bg='white',height='39')
	Km.pack()
	
	##زر لانتهاء البرنامج
	BO = Button(KT,text='Finch',bg='white',command=(KT.quit))
	BO.place(x=800,y=1200)
	
	#نص ترحيب
	La1 = Label(KT,text='Welcom',fg='green',bg='white',font=('a',30))
	La1.place(x=200,y=50)
	

	



#المدخلات
E1 = Entry(r , width =20,justify='center' )
E1.place(x= 320 , y = 300)

E2 = Entry(r , width =20,justify='center' )
E2.place(x= 320 , y = 500)

E3 = Entry(r , width =20,justify='center' )
E3.place(x= 320 , y = 700)




#النصوص
L1 = Label(r , text = 'Enter your name',bg = '#36454F',font=('',10))
L1.place(x= 320 , y = 200)

L2 = Label(r , text = 'Enter your age',bg = '#36454F',font=('',10))
L2.place(x= 320 , y = 400)

L3 = Label(r , text = 'Enter your phone n..',bg = '#36454F',font=('',10))
L3.place(x= 320 , y = 600)




#الازرار
B = Button(r, text='gain it' , width=8,command=(save_bata))
B.place(x= 700 , y = 1000)

B1 = Button(r, text='Fainsh' , width=8,command=(r.quit))
B1.place(x= 70 , y = 1000)


  
r.mainloop() 
