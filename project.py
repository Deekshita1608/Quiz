import pygame
from moviepy.editor import *
import mysql.connector
from gtts import gTTS
import playsound
import time
import os
import speech_recognition as sr
import random
import turtle
import level_123
import level_456
import level_789
import sys
from tkinter import *
import congratulations

demodb = mysql.connector.connect(host="localhost", user="root", passwd="udgam", database="kbc")
democursor=demodb.cursor( )


def questionaudio(q,op1,op2,op3,op4):
    language='en'
    question=gTTS(text=q, lang=language, slow=False)
    question.save('question.mp3')
    playsound.playsound('question.mp3')
    os.remove('question.mp3')
    
    question=gTTS(text=op1, lang=language, slow=False)
    question.save('option1.mp3')
    playsound.playsound('option1.mp3')
    os.remove('option1.mp3')
    
    question=gTTS(text=op2, lang=language, slow=False)
    question.save('option2.mp3')
    playsound.playsound('option2.mp3')
    os.remove('option2.mp3')
    
    question=gTTS(text=op3, lang=language, slow=False)
    question.save('option3.mp3')
    playsound.playsound('option3.mp3')
    os.remove('option3.mp3')
    
    question=gTTS(text=op4, lang=language, slow=False)
    question.save('option4.mp3')
    playsound.playsound('option4.mp3')
    os.remove('option4.mp3')

def other_speech(text):
    language='en'
    speech=gTTS(text=text, lang=language, slow=False)
    speech.save('speech.mp3')
    playsound.playsound('speech.mp3')
    os.remove('speech.mp3')

def correctans():
    compliments=['Well done', 'Yay! You got that', 'Awesome','You did it','You nailed it!']
    language='en'
    compliments=gTTS(text=random.choice(compliments), lang=language, slow=False)
    compliments.save('correct.mp3')
    playsound.playsound('correct.mp3')
    os.remove('correct.mp3')

def wrongans():
    words=['Sorry! That\'s incorrect...', 'Oh no! You were almost there','Too bad!Game is over']
    language='en'
    words=gTTS(text=random.choice(words), lang=language, slow=False)
    words.save('incorrect.mp3')
    playsound.playsound('incorrect.mp3')
    os.remove('incorrect.mp3')
    


def speechrecognition():
    r=sr.Recognizer()
    with sr.Microphone() as source:
                        playsound.playsound('beep.mp3')
                        print('I am listening...')
                        audio=r.record(source, duration=6)
    text=r.recognize_google(audio)
    return text

def error():
    words=['I couldn\'t understand what you said, please try again.']
    language='en'
    words=gTTS(text=random.choice(words), lang=language, slow=False)
    words.save('error.mp3')
    playsound.playsound('error.mp3')
    os.remove('error.mp3')
    

#END OF FUNCTION DEFINITIONS
#Main program

playsound.playsound('kbc intro tune.mp3',block=False)



root = Tk()
root.title('Main Menu')
root.geometry("175x100") 

def submit():
    global choice
    choice=v.get()
    root.destroy()

v = IntVar(root, 0)

Radiobutton(root, text = 'Administrator Login', variable = v,value = 1, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
Radiobutton(root, text = 'Player Login', variable = v,value = 2, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
Radiobutton(root, text = 'New Player Registration', variable = v,value = 3, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
Button1=Button(root, text = "Submit", command = submit)
Button1.pack(fill=X)
mainloop()



if choice==1:
    def submit1():
      global name
      global passw
      name=username.get()
      passw=password.get()       
      root.destroy()

    root = Tk()
    root.title('Administrator login')
    root.geometry('200x100')
    name_label=Label(root,text='Username')
    name_label.place(x=0,y=0)
    username= Entry(root)
    username.place(x=60,y=0)
    passw_label=Label(root,text='Password')
    passw_label.place(x=0,y=30)
    password= Entry(root,show='*')
    password.place(x=60,y=30)
    B=Button(root, text = "Submit", command = submit1)
    B.place(x=70,y=60)
    root.mainloop()

    if name=='admin' and passw=='admin@123':
        def submitx():
            global choice2
            choice2=v.get()
            root.destroy()
        root=Tk()
        v = IntVar(root, 0)

        Radiobutton(root, text = 'View all questions', variable = v,value = 1, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
        Radiobutton(root, text = 'Add new questions', variable = v,value = 2, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
        Radiobutton(root, text = 'Modify existing questions', variable = v,value = 3, indicator = 0,background = "light blue").pack(fill = X,ipadx=5,)
        Button1=Button(root, text = "Submit", command = submitx)
        Button1.pack(fill=X)
        mainloop()

    

        
        if choice2==1:
            def submit2():
                global level_required
                level_required=level_en.get()
                root.destroy()

            root = Tk()
            root.title('View all questions')
            root.geometry('400x100')
            level=Label(root,text='Enter level you wish to view:')
            level.place(x=0,y=0)
            level_en= Entry(root)
            level_en.place(x=190,y=0)
            Button2=Button(root, text = "Submit", command = submit2)
            Button2.place(x=200,y=50)
            root.mainloop()
          
            democursor.execute('select * from level'+str(level_required)+';')
            all_questions=democursor.fetchall()
            for i in all_questions:
                print(i[0],i[1])
                print('Option 1: ',i[2])
                print('Option 2: ',i[3])
                print('Option 3: ',i[4])
                print('Option 4: ',i[5])
                print('Answer: ',i[6])
            sys.exit()

            
        elif choice2==2:
                def submit3():
                     global serial
                     global quest
                     global opt1
                     global opt2
                     global opt3
                     global opt4
                     global an
                     global level_required
                     level_required=level_en.get()
                     serial=serialno.get()
                     quest=ques.get()
                     opt1=opt_1.get()
                     opt2=opt_2.get()
                     opt3=opt_3.get()
                     opt4=opt_4.get()
                     an=ans.get()
                     root.destroy()

                root = Tk()
                root.title('Add Questions')
                root.geometry('300x270')
                level_enl=Label(root,text='Enter level:')
                level_enl.place(x=0,y=0)
                level_en= Entry(root)
                level_en.place(x=120,y=0)
                serialno_l=Label(root,text='Enter serial number:')
                serialno_l.place(x=0,y=30)
                serialno= Entry(root)
                serialno.place(x=120,y=30)
                ques_l=Label(root,text='Enter question:')
                ques_l.place(x=0,y=60)
                ques= Entry(root)
                ques.place(x=120,y=60)
                opt_1l=Label(root,text='Enter option 1:')
                opt_1l.place(x=0,y=90)
                opt_1= Entry(root)
                opt_1.place(x=120,y=90)
                opt_2l=Label(root,text='Enter option 2:')
                opt_2l.place(x=0,y=120)
                opt_2= Entry(root)
                opt_2.place(x=120,y=120)
                opt_3l=Label(root,text='Enter option 3:')
                opt_3l.place(x=0,y=150)
                opt_3= Entry(root)
                opt_3.place(x=120,y=150)
                opt_4l=Label(root,text='Enter option 4:')
                opt_4l.place(x=0,y=180)
                opt_4= Entry(root)
                opt_4.place(x=120,y=180)
                ans_l=Label(root,text='Enter answer:')
                ans_l.place(x=0,y=210)
                ans= Entry(root)
                ans.place(x=120,y=210)
                Button4=Button(root, text = "Submit", command = submit3)
                Button4.place(x=150,y=240)
                root.mainloop()
                
                tup=(serial,quest,opt1,opt2,opt3,opt4,an)
                insert='INSERT IGNORE into level'+str(level_required)+' values(%s,"%s","%s","%s","%s","%s","%s");' %(tup)
                try:
                     democursor.execute(insert)
                     demodb.commit()
                     print('Question added successfully')
                except:
                     print('An error occurred. Please try again.')
                sys.exit()

        elif choice2==3:
            def submit4():
                global level_required
                global val
                global snum
                global col
                val=value.get()
                level_required=level_en.get()
                snum=snum_tk.get()
                col=column.get()
                root.destroy()

            root = Tk()
            root.title('Modify Questions')
            root.geometry('500x150')
            level_enl=Label(root,text='Enter level you wish to edit:')
            level_enl.place(x=0,y=0)
            level_en= Entry(root)
            level_en.place(x=250,y=0)
            snum_tkl=Label(root,text='Enter serial number of entry you wish to edit:')
            snum_tkl.place(x=0,y=30)
            snum_tk= Entry(root)
            snum_tk.place(x=250,y=30)
            column_l=Label(root,text='Enter column which you wish to edit:')
            column_l.place(x=0,y=60)
            column= Entry(root)
            column.place(x=250,y=60)
            value_l=Label(root,text='Enter new value:')
            value_l.place(x=0,y=90)
            value= Entry(root)
            value.place(x=250,y=90)
            Button2=Button(root, text = "Submit", command = submit4)
            Button2.place(x=250,y=120)
            root.mainloop()
          

            tup=(val,snum)
            edit='update level'+str(level_required)+' set '+col.lower()+'=%s'+' where sno=%s;'
            try:
               democursor.execute(edit,tup)
               demodb.commit()
               print('Update Successful!')
            except:
               print('An error occurred. Please try again.')
            sys.exit()

        else:
            print('Invalid User ID or password, please try again.')
            sys.exit()


elif choice==3:
    def submit6():
      global name
      global passw
      global passwf
      name=username.get()
      passw=password.get()
      passwf=passwordf.get()
      root.destroy()
      if name=='Username' or name=='username' or passw=='password' or passw=='Password':
          print('Invalid username or password. Please try again')
      elif passw==passwf:
          fin=open('C:\\Users\\91987\Desktop\\computer project\\Class 12\\Usernames and passwords.txt','r')
          data=fin.readlines()
          for x in data:
             if name in x:
                 print('User already exists')
                 sys.exit()
          fin.close()
        
          fout=open('C:\\Users\\91987\\Desktop\\computer project\\Class 12\\Usernames and passwords.txt','a')
          L=['Username:     ',name,' ','Password:     ',passw,'\n']
          fout.writelines(L)
          fout.close()
      else:
        print('Password and re-entered password do not match.Please try again.')
      sys.exit()

    root = Tk()
    root.title('New player registration')
    root.geometry('400x110')
    name_label=Label(root,text='Enter your Username')
    name_label.place(x=0,y=0)
    username= Entry(root)
    username.place(x=190,y=0)
    passw_label=Label(root,text='Enter your Password')
    passw_label.place(x=0,y=30)
    password= Entry(root)
    password.place(x=190,y=30)
    passwf_label=Label(root,text='Re-enter your Password:')
    passwf_label.place(x=0,y=60)
    passwordf= Entry(root)
    passwordf.place(x=190,y=60)
    B=Button(root, text = "Submit",command=submit6)
    B.place(x=200,y=90)
    root.mainloop()


                    
elif choice==2:
    def submit5():
      global name
      global passw
      name=username.get()
      passw=password.get()
      root.destroy()
      
      fin=open('C:\\Users\\91987\Desktop\\computer project\\Class 12\\Usernames and passwords.txt','r')
      data=fin.readlines()
      flag=0
      for x in data:
          if name in x and passw in x:
              flag=1
      
      if flag==1:
        print('Login successful')
        time.sleep(20)
        intro='Welcome to the KBC quiz game. This quiz consists of 9 levels of increasing difficulty. Please answer in terms of Alpha, Beta, Gamma or Delta. A correct answer will mean progressing to the next level, while a wrong answer will terminate the game. So lets get started.'
        other_speech(intro)

        for level in range(1,10):
            query1='select * from level'+str(level)+' order by RAND() LIMIT 1'
            democursor.execute(query1)
            result=democursor.fetchall()
            for x in result:
                  print('LEVEL',level)
                  print(x[1])
                  print('Alpha.', x[2])
                  print('Beta.', x[3])
                  print('Gamma.',x[4])
                  print('Delta.', x[5])
                  dic={'alpha':result[0][2].lower(),'beta':result[0][3].lower(),'gamma':result[0][4].lower(),'delta':result[0][5].lower()}
                  questionaudio(x[1],x[2],x[3],x[4],x[5])
                  playsound.playsound('clock.mp3')
                  while True:
                      
                     try:
                       answer=speechrecognition()
                       if answer.lower()=='gana'or answer.lower()=='gama':
                            answer='gamma'
                       if answer.lower()=='elsa':
                            answer='alpha'
                       if answer.lower() in dic.keys():
                           break
                       else:
                           error()
                           continue
                  
                     except:
                         error()
                         continue

                  print('Your answer is :', dic[answer.lower()].title())
                  if dic[answer.lower()].strip()==result[0][6].lower().strip():
                            correctans()
                            clip = VideoFileClip("smiley.mp4")
                            clip.preview()
                            pygame.quit()

                              
                            if level==9:
                                print('Congratulations!You won the game')
                                congratulations.congrats()
                                sys.exit
                            other_speech('Let\'s move on to the next question')
                            playsound.playsound('kbc next question.mp3')
                          
                  else:
                          ans=result[0][6].lower().strip()
                          wrongans()
                          other_speech('The correct answer is '+ ans)
                          clip = VideoFileClip("sad.mp4")
                          clip.preview()
                          pygame.quit()
                          sys.exit()
                      
               
        demodb.close()


      else:
          print('Username or password not valid')
          sys.exit()
      fin.close()
      

    root = Tk()
    root.title('Login')
    root.geometry('200x100')
    name_label=Label(root,text='Username')
    name_label.place(x=0,y=0)
    username= Entry(root)
    username.place(x=60,y=0)
    passw_label=Label(root,text='Password')
    passw_label.place(x=0,y=30)
    password= Entry(root,show='*')
    password.place(x=60,y=30)
    B=Button(root, text = "Submit", command = submit5)
    B.place(x=70,y=60)
    root.mainloop()


