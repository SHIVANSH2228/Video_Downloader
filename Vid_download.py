from tkinter import*
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import*
import shutil


root = Tk()
root.title("Sintrosoft's Video Downloader ")
canvas =Canvas(root,width=600, height=600)
canvas.pack()

#creating the functions

def download():
    video_path= url_entry.get()
    file_path = path_label.cget("text")
    mp4= YouTube(video_path).streams.get_highest_resolution().download()
    video_clip= VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4,file_path)
def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

#app_label
app_label =Label(root,text="Video Downloader", fg="blue", font=("Arial",25))
canvas.create_window(300,100,window=app_label)

#creating entry widget
url_label= Label(root,text = "Enter the url of the video:",font=("Arial",15),fg="green")
canvas.create_window(300,200,window=url_label)
url_entry= Entry(root,width=35)
canvas.create_window(300,220,window=url_entry)

#path to download files
path_label = Label(root,text= "Select the path to download",font=("Arial",15),fg="red")
canvas.create_window(300,280,window=path_label)
path_button= Button(root,text= "Select",font=("Arial",15),command= get_path)
canvas.create_window(300,320, window=path_button)

#adding download button
down_label= Label(root,text= "Click the button to download:",font=("Arial",15),fg="green")
canvas.create_window(300,400,window=down_label)
download= Button(root,text= "Download",font=("Arial",15),fg="green",command = download)
canvas.create_window(300,450,window=download)
root.mainloop()