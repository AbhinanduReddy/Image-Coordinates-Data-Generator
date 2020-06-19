from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename,askdirectory
from PIL import Image
from PIL import ImageTk
import os
import csv
from csv import writer
output_path = r'F:\How_to_simulate_a_self_driving_car-master\labels.csv'
mylist=[]
global counter
counter=0
input_path="image_dataset/"

def display_coordinates(event):
    my_label['text']=f'x={event.x} y={event.y}'
    mylist.append((event.x,event.y))
    print(mylist)


def delete():
    mylist.clear()
    my_label['text']=""

    
def next_img():
    global counter
    counter=counter+1
    print(counter)
    delete()
    img_label.img = tk.PhotoImage(file=next(imgs))
    img_label.config(image=img_label.img)
    

    

def save():
    with open(output_path, "a", newline='') as f:
        writer = csv.writer(f)
        
        position=mylist
        xr, yr = position[0][0], position[0][1]
        xl, yl = position[1][0], position[1][1]
        list_of_elem=[counter,xr,yr,xl,yl]
        writer.writerow(list_of_elem)
        print("saved ",counter)
        
    #file.write({'frame_no':counter ,'x_position_right_hand': xr, 'y_position_right_hand': yr,'x_position_left_hand': xl, 'y_position_left_hand': yl})
        
        
output_path = r'F:\How_to_simulate_a_self_driving_car-master\labels.csv'
fieldNames = ['frame_no',
              'x_position_right_hand',
              'y_position_right_hand',
              'x_position_left_hand',
              'y_position_left_hand']

if os.path.exists(output_path):
    print("file present")
else:
    with open(output_path,'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldNames)



    
       
root=Tk()
root.title("Coordinate tool")
root.iconbitmap('n.ico')

img_dir = askdirectory(parent=root, initialdir="F:/How_to_simulate_a_self_driving_car-master/", title='Choose folder')
os.chdir(img_dir)
imgs = iter(os.listdir(img_dir))

img_label = tk.Label(root)
img_label.grid(row=0,column=0,columnspan=3)

my_label=Label(bd=4,relief='solid',font="Times 22 bold",bg='white',fg='black')
img_label.bind('<Button-1>',display_coordinates)


my_label.grid(row=1,column=1)
save_button=Button(root,text='save_corrdinates',command=save)
save_button.grid(row=2,column=1)
delete_button=Button(root,text='delete_corrdinates',command=delete)
delete_button.grid(row=2,column=0)
next_button=Button(root,text='next>>',command=next_img)
next_button.grid(row=2,column=2)
next_img()
root.mainloop()
