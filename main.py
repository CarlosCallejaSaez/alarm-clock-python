import tkinter as tk
from tkinter import messagebox
import time
import pygame

pygame.mixer.init()  

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            pygame.mixer.music.load("sound.mp3")  
            pygame.mixer.music.play()  
            messagebox.showinfo("Developed with 💓","by Carlos Calleja Saez")
            break

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Introduce la hora de tu alarma (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Añadir Alarma", command=set_alarm)
set_button.pack()

root.mainloop()
