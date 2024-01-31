import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        youtubeObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = youtubeObject.streams.get_highest_resolution()
        
        title.configure(text=youtubeObject.title, text_color="white")
        video.download()
        finishLabel.configure(text="Download Finished", text_color="green")
    except(Exception) as e:
        #finishLabel.configure(text='Download Error', text_color="red")
        finishLabel.configure(text=e, text_color="red")
        print(e)
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_completion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()
    # update progressbar
    progressBar.set(float(percentage_completion) / 100)
    
# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Angel Youtube Downloaded")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#progress
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(pady=10, padx=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=10, padx=10)

# Run app
app.mainloop()
