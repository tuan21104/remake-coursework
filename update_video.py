import tkinter as tk
from tkinter import messagebox as msb
from video_library import get_director, get_play_count, get_name, get_rating, set_rating
import library_item as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideo:

    def __init__(self, window):
        self.window = window
        window.geometry("500x300")
        window.title('Update Video')

        enter_video_lbl = tk.Label(self.window, text='Enter video number:')
        enter_video_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        self.video_number_input_txt = tk.Entry(self.window, width=30)
        self.video_number_input_txt.grid(row=0, column=1,sticky='w', padx=10, pady=10)

        update_rating_lbl = tk.Label(self.window, text='Enter new rating:')
        update_rating_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        self.update_rating_input_txt = tk.Entry(self.window, width=30)
        self.update_rating_input_txt.grid(row=1, column=1, sticky='w', padx=10, pady=10)


        confirm_btn = tk.Button(self.window, text='Confirm', command=self.update_rating)
        confirm_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_txt = tk.Text(self.window, width=40, height=10)
        self.show_txt.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.status_txt_lbl = tk.Label(self.window, text='')
        self.status_txt_lbl.grid(row=3, column=0, columnspan=3, sticky='w', padx=10, pady=10)

    

    def update_rating(self):
        video_number = self.video_number_input_txt.get()
        new_rating = self.update_rating_input_txt.get()

        if video_number == '':
            msb.showerror('Error', 'You have to enter the video number!')
            return
        try:
            video_name = get_name(video_number)
            if video_name:
                new_rating = int(new_rating)
                if not 1 <= new_rating <= 5:
                    msb.showerror('Error', 'New rating must be between 1 and 5!')
                    return
                set_rating(video_number, new_rating)
                play_count = get_play_count(video_number)
                set_text(self.show_txt, f"Video: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}")
                self.status_txt_lbl.config(text='Video was updated!')
            else:
                raise ValueError(f"Video {video_number} not found")
        except ValueError as e:
            msb.showerror("Error", 'Invalid value! Please try again!')
            set_text(self.show_txt, '')
            self.status_txt_lbl.configure(text='')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    gui = UpdateVideo(window)
    gui.run()