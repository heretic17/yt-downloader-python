from pytube import YouTube
from tkinter import ttk
import tkinter as tk

def download():
    resolution_value = resolution_menu.get()
    link_value = link_entry.get()
    audio_only_value = audio_variable.get()
    
    try:
        youtube_object = YouTube(link_value)

        if audio_only_value:
            audio = youtube_object.streams.filter(only_audio=True).first()
            output_path = f"downloads/{youtube_object.title}/{resolution_value}_audio"
            audio.download(output_path=output_path)
            completion_label.config(text="Audio download complete")
        else:
            youtube_object = youtube_object.streams.get_by_resolution(resolution=resolution_value)
            output_path = f"downloads/{youtube_object.title}/{resolution_value}_video"
            youtube_object.download(output_path=output_path)
            completion_label.config(text="Video download complete")
    except:   
        completion_label.config(text=f"No stream available for resolution: {resolution_value}")

root = tk.Tk()
root.title("Youtube downloader")
root.geometry("400x300")
root.resizable(height = False, width = False)

link_label = ttk.Label(root, text="Enter the Youtube URL")
link_label.pack(pady=10)

link_entry = tk.Entry(width=40)
link_entry.pack(pady=10)

audio_variable = tk.BooleanVar()
audio_only = ttk.Checkbutton(root, text="Audio Only", variable=audio_variable)
audio_only.pack(pady=10)

resolution_label = ttk.Label(root, text="Select Resolution:")
resolution_label.pack(pady=10)

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution_menu = ttk.Combobox(root, state="readonly", values=resolutions)
resolution_menu.pack(pady=10)

download_button = ttk.Button(root, command=download, text="Download")
download_button.pack(pady=10)

completion_label = ttk.Label(root, text="")
completion_label.pack(pady=10)

root.mainloop()