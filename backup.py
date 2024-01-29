from pytube import YouTube
from tkinter import ttk
import tkinter as tk

def download():
    link_value = link_entry.get()
    resolution_value = resolution_menu.get()

    youtube_object = YouTube(link_value)
    youtube_object = youtube_object.streams.get_by_resolution(resolution=resolution_value)

    try: 
        youtube_object.download()
        print("Download complete")
    except Exception as e:
        print(f"An error has occured: {e}")


root = tk.Tk()
root.title("Youtube downloader")
root.geometry("400x200")

link_label = ttk.Label(root, text="Enter the Youtube URL")
link_label.pack(pady=10)

link_entry = tk.Entry(root, width=40)
link_entry.pack(pady=10)

resolution_label = ttk.Label(root, text="Select Resolution:")
resolution_label.pack(pady=10)

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]

resolution_menu = ttk.Combobox(root, state="readonly", values=resolutions)
resolution_menu.pack(pady=10)

download_button = ttk.Button(root, text="Download", command=download)
download_button.pack(pady=10)

root.mainloop()