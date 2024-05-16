import customtkinter
import serial
import time
import serial.threaded
from threading import Thread
#import serial.tools.list_ports

Data = serial.Serial('COM3', baudrate = 115200, timeout = 1)


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('500x400')

def switch_event():
    status = switch_var.get()
    if (not Data.is_open):
        Data.open()
    if status == 'on':
        
        Data.write(b'1')
        print('led on')
    if status == 'off':

        Data.write(b'0')
        print('led off')

def button_event():
    Data.write(b'3')
    time.sleep(0.1)
    freq = entry.get()
    #Data.write(freq)
    print('Frequencia set')


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60)



entry = customtkinter.CTkEntry(frame, placeholder_text="Frequência")
entry.pack(pady=20, padx=120)
button = customtkinter.CTkButton(frame, text="Set", command=button_event)
button.pack(pady=20, padx=60)
switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(frame, text="", command=switch_event, variable=switch_var, onvalue="on", offvalue="off", switch_width=140, switch_height=60)
switch.pack(pady=60, padx=120)

def Loop1S():  
    if(Data.in_waiting != 0):
        if (not Data.is_open):
            Data.open()
        vari = Data.read_all()
        vari = vari.decode()
        print(vari)

    root.after(ms=1000,func=Loop1S)

root.after(ms=1000,func=Loop1S)

car = "tensao:24/corrente:323/vel:23"
car2 = (car.split("/"))
print(car2)
print(car2[0].split(":"))

root.mainloop()






