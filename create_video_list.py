import tkinter as tk
from tkinter import scrolledtext as tkst
import video_library as lib
from tkinter import messagebox as msb

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateVideoList:
    def __init__(self, window):
        self.window = window
        self.window.geometry('800x350')
        self.window.title('Create Video List')

        enter_video_lbl = tk.Label(self.window, text='Enter Video Number:')
        enter_video_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        self.enter_video_entry = tk.Entry(self.window, width=3)
        self.enter_video_entry.grid(row=0, column=1, padx=10, pady=10)

        add_to_playlist_btn = tk.Button(self.window, text='Add Item To Playlist', command=self.add_to_playlist_clicked)
        add_to_playlist_btn.grid(row=0, column=2, padx=10, pady=10)

        play_play_list_btn = tk.Button(self.window, text='Play Playlist', command=self.play_playlist_clicked)
        play_play_list_btn.grid(row=0, column=3, padx=10, pady=10)

        rest_playlist_btn = tk.Button(self.window, text='Reset Playlist', command=self.reset_playlist_clicked)
        rest_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        self.content_txt = tkst.ScrolledText(self.window, width=48, height=14)
        self.content_txt.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        announce_txt = tk.Label(self.window)
        announce_txt.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.show_txt = tk.Text(self.window, width=40, height=10)
        self.show_txt.grid(row=1, column=1, sticky='w', columnspan=4, padx=10, pady=10)

        self.status_lbl = tk.Label(self.window, text = '')
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky='w', padx=10, pady=10)

        self.playlist = []  
        self.key = []

    def add_to_playlist_clicked(self):
        key = self.enter_video_entry.get()
        name = lib.get_name(key)

        if key == "":
            msb.showerror('Error', 'You must enter vieo number!')
        if name is not None:
            self.key.append(key)
            self.playlist.append(name)
            set_text(self.content_txt, "\n".join(self.playlist))
            set_text(self.show_txt, f"Video {key} added to playlist!")
            self.status_lbl.configure(text="Add Item to Playlist was clicked!")
        else:
            set_text(self.show_txt, f"Video {key} is not found!")
            self.status_lbl.configure(text=f"Add Item to Playlist was clicked!")

    def play_playlist_clicked(self):
        try:
            if self.key[0] is not None:
                for i in self.key:
                    lib.increment_play_count(i)
                self.status_lbl.configure(text="Playlist played button was clicked!")
        except IndexError:
            msb.showerror('Error', 'You must add video to playlist first!')
            self.status_lbl.configure(text="There are no video in Playlist")

    def reset_playlist_clicked(self):
        self.playlist.clear()  
        set_text(self.show_txt, "") 
        self.key = []
        self.status_lbl.configure(text="Playlist cleared!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    gui =  CreateVideoList(window)
    gui.run()
    


        


