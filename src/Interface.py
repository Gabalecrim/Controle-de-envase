import customtkinter
import serial
import time
#import serial.tools.list_ports

Data = serial.Serial('COM3', baudrate = 9600, timeout = 1)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('500x400')

def switch_event():
    status = switch_var.get()
    
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
    Data.write(freq)
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

root.mainloop()