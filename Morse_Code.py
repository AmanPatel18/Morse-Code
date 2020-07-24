from os import system
from tkinter import Label,Tk,Button,Text,Entry
class morseCode:
    def __init__(self):
          self.win=Tk()
          self.win.title("Morse Code")
          self.win.geometry("1362x768")
          self.win.configure(bg='purple')

    def to_morse_code(self):
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
        
        msg_label=Label(self.win,text="Enter the message:",font="Ariel 15 normal",bg='purple',fg="violet")
        msg_label.place(x=200,y=300)
        
        msg_field=Entry(self.win,width=30,font="Ariel 15 bold",bg='indigo',fg='white')
        msg_field.place(x=380,y=300)
        
        def conv():
            text=msg_field.get()
            morse_code=""
            
            for letter in text:
                if letter==' ':
                    morse_code+=' '
                    continue
                morse_code+=MORSE_CODE_DICT[letter.upper()]+' '

            output=Label(self.win,text="Output:-",font="times 25 bold",bg='purple',fg="white")
            output.place(x=100,y=400)
            
            result=Text(self.win,height=4,width=45,font="Ariel 35 normal",bg='indigo',fg="violet")
            result.insert("1.0",morse_code)
            result.place(x=100,y=450)
    
        convert=Button(self.win,text="Convert",font="Ariel 15 bold",bg='violet',fg='purple',command=conv,cursor="hand2",borderwidth=5)
        convert.place(x=750,y=290)
    
    def to_text(self):
        MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 
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
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
        msg_label=Label(self.win,text="Enter the morse code:",font="Ariel 15 normal",bg='purple',fg="violet")
        msg_label.place(x=200,y=300)
        
        msg_field=Entry(self.win,width=30,font="Ariel 15 bold",bg='indigo',fg='white')
        msg_field.place(x=420,y=300)
        
        def conv():
            message=msg_field.get()
            message += ' '
            decipher = '' 
            citext = '' 
            for letter in message: 
    
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
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).    index(citext)]
                        citext = ''

            output=Label(self.win,text="Output:-",font="times 25 bold",bg='purple',fg="white")
            output.place(x=100,y=400)
            
            result=Text(self.win,height=7,width=80,font="Ariel 20 normal",bg='indigo',fg="violet")
            result.insert("1.0",decipher)
            result.place(x=100,y=450) 
  
        convert=Button(self.win,text="Convert",font="Ariel 15 bold",bg='violet',fg='purple',command=conv,cursor="hand2",borderwidth=5)
        convert.place(x=780,y=290)

    def main(self):
        heading=Label(self.win,text="Morse Code Conversion",bg='purple',fg='violet',font="helvetica 35 bold")
        heading.place(x=200,y=20)
        
        opt1=Button(self.win,text="From Text to Morse Code",font="Ariel 15 bold",bg='violet',fg='purple',command=self.to_morse_code,cursor="hand2")
        opt1.place(x=200,y=100)
        
        opt2=Button(self.win,text="From Morse Code to Text",font="Ariel 15 bold",bg='violet',fg='purple',command=self.to_text,cursor="hand2")
        opt2.place(x=200,y=150)

        opt3=Button(self.win,text="Exit",width=21,font="Ariel 15 bold",bg='violet',fg="purple",command=quit,cursor="hand2")
        opt3.place(x=200,y=200)
        
        input()

obj=morseCode()
obj.main()
tkinter.mainloop()
