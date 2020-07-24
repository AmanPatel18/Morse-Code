from os import system
from tkinter import *
from os import sys

class morseCode:
    
    def __init__(self):
          self.win=Tk()                   
          self.win.title("Morse Code")   #setting title
          self.win.geometry("1362x768")  #setting window size
          self.win.configure(bg='black') #setting background color
          self.message=""
          self.text=""
          self.output=""
          self.result=""
          self.output2=""
          self.result2=""
    
    # morse code dictionary      

    def MORSE_CODE_DICT(self):

        #morse code dictionary for every letter digits and some special characters

        MORSE_CODE_DICT={'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ',':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-'}

        return MORSE_CODE_DICT
    
    # function to convert message to morse code
    
    def to_morse_code(self):

        #incrementing the runtime to ensure that button associated with this functio clicked one time
        
        self.runtime+=1
        if self.runtime>1:  # if runtime is more than one destroying instances
            self.destroyf2()

        MORSE_CODE_DICT = self.MORSE_CODE_DICT()
        self.msg_label=Label(self.win,text="Enter the message:",font="Ariel 15 normal",bg='black',fg="green")
        self.msg_label.place(x=200,y=300)
        
        self.msg_field=Entry(self.win,width=30,font="Ariel 15 bold",bg='black',fg='white')
        self.msg_field.place(x=380,y=300)
        
        # function to perform conversion operation
        
        def conv():
            self.text=self.msg_field.get()
            
            if len(self.text)>=1:       # check whether user has enter something in entry field or not
               
                self.op_active=1   # setting the output status one to ensure that output has been given
                morse_code=""
                
                for letter in self.text:
                    if letter==' ':
                        morse_code+=' '
                        continue
                    morse_code+=MORSE_CODE_DICT[letter.upper()]+' '
    
                self.output=Label(self.win,text="Output:-",font="times 25 bold",bg='black',fg="white")
                self.output.place(x=100,y=400)
                
                self.result=Text(self.win,height=4,width=45,font="Ariel 35 normal",bg='darkgreen',fg="black")
                self.result.insert("0.0",morse_code)
                self.result.place(x=100,y=450)
        
        self.convert=Button(self.win,text="Convert",font="Ariel 15 bold",bg='green',fg='black',command=conv,cursor="hand2",borderwidth=5)
        self.convert.place(x=750,y=290)

        #function to reset the field

        def reset_field():
            if len(self.text)>0:             #checking whether the input in entry field is greater than 0 or not
                self.msg_field.delete(0,END)
                
            if self.op_active==1:             # checking whether output has been showed or not
                self.output.destroy()
                self.result.destroy()

        self.reset=Button(self.win,text="Reset",font="Ariel 15 bold",bg='green',fg='black',command=reset_field,cursor="hand2",borderwidth=5)
        self.reset.place(x=880,y=290)

    # function to morse code to message 
    
    def to_text(self):
        
        #incrementing the runtime to ensure that button associated with this functio clicked one time
        
        self.runtime+=1     # if runtime is more than one destroying instances
        if self.runtime>1:
            self.destroyf1()

        MORSE_CODE_DICT = self.MORSE_CODE_DICT()

        self.msg_label2=Label(self.win,text="Enter the morse code:",font="Ariel 15 normal",bg='black',fg="green")
        self.msg_label2.place(x=200,y=300)
        
        self.msg_field2=Entry(self.win,width=30,font="Ariel 15 bold",bg='black',fg='white')
        self.msg_field2.place(x=420,y=300)
        
        # function to perform conversion operation
        
        def conv():
            self.message=self.msg_field2.get()
            
            if len(self.message)>=1:       # check whether user has enter something in entry field or not
                
                self.op_active=1     # setting the output status one to ensure that output has been given
                self.message += ' '
                decipher = '' 
                citext = '' 
                for letter in self.message: 
                # checks for space 
                    if (letter != ' '): 
                    # counter to keep track of space 
                        i = 0
                    # storing morse code of a single character 
                        citext += letter 
                # in case of space 
                    else: 
                    # if i = 1 that indicates a new character 
                        i += 1
                    # if i = 2 that indicates a new word 
                        if i == 2 : 
                         # adding space to separate words 
                            decipher += ' '
                        else: 
                        # accessing the keys using their values (reverse of encryption) 
                            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                            citext = ''
    
                self.output2=Label(self.win,text="Output:-",font="times 25 bold",bg='black',fg="white")
                self.output2.place(x=100,y=400)
                
                self.result2=Text(self.win,height=7,width=80,font="Ariel 20 normal",bg='dark green',fg="black")
                self.result2.insert("0.0",decipher)
                self.result2.place(x=100,y=450) 

        self.convert2=Button(self.win,text="Convert",font="Ariel 15 bold",bg='green',fg='black',command=conv,cursor="hand2",borderwidth=5)
        self.convert2.place(x=780,y=290)
        
        #function to reset the field

        def reset_field():
            if len(self.message)>0:          #checking whether the input in entry field is greater than 0 or not
                self.msg_field2.delete(0,END)
                
            if self.op_active==1:            # checking whether output has been showed or not
                self.output2.destroy()
                self.result2.destroy()

        self.reset2=Button(self.win,text="Reset",font="Ariel 15 bold",bg='green',fg='black',command=reset_field,cursor="hand2",borderwidth=5)
        self.reset2.place(x=920,y=290)
    
    # function to destroy gui instances
    
    def destroyf1(self):
        self.msg_field.delete(0,END)
        self.reset.destroy()
        self.msg_label.destroy()
        self.msg_field.destroy()
        self.convert.destroy()
        
        
        #if output has been shown it will be one and then only we destroy its instances
        if self.op_active==1:
            self.output.destroy()
            self.result.destroy()
    
    def destroyf2(self):
        self.msg_field2.delete(0,END)
        self.reset2.destroy()
        self.msg_label2.destroy()
        self.msg_field2.destroy()
        self.convert2.destroy()
        
        #if output has been shown it will be one and then only we destroy its instances
        if self.op_active==1:
            self.output2.destroy()
            self.result2.destroy()
    
    # main function for home 

    def main(self):
        self.runtime=0  # to check how many time buttons have been clicked
        self.op_active=0  # to check whether the output has been shown or not

        # main heaading at home page

        self.heading=Label(self.win,text="Morse Code Conversion",bg='black',fg='green',font="helvetica 35 bold")
        self.heading.place(x=200,y=20)         
        
        # Button for conversion from code to text
        
        self.opt1=Button(self.win,text="From Text to Morse Code",font="Ariel 15 bold",bg='green',fg='black',command=self.to_morse_code,cursor="hand2")
        self.opt1.place(x=200,y=100)
        
        # button for conversion from text to code

        self.opt2=Button(self.win,text="From Morse Code to Text",font="Ariel 15 bold",bg='green',fg='black',command=self.to_text,cursor="hand2")
        self.opt2.place(x=200,y=150)
        
        # button to exit the app

        self.opt3=Button(self.win,text="Exit",width=21,font="Ariel 15 bold",bg='green',fg="black",command=sys.exit,cursor="hand2")
        self.opt3.place(x=200,y=200)
        
        input()

obj=morseCode()     # creating object namely 'obj'
obj.main()          # calling main function for the home page
tkinter.mainloop()  # for keeping the window open