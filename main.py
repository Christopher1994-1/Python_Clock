import customtkinter
import tkinter
import time
import datetime


months = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December",
    }


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Python Clock")
        self.root.geometry("500x130")
        self.root.config(background="#282828")
        
        
        self.date_date = str(datetime.datetime.now()).split(" ")[0].split('-')
        self.year = self.date_date[0]
        self.month = months[str(self.date_date[1])]
        self.day = self.date_date[2]
        self.date = f" Today's Date: {self.month}-{self.day}-{self.year}  "
        

        # Main frame to hold label
        self.main_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.main_frame.pack()

        # Main label to display values
        self.time_var = tkinter.StringVar(value="02:09:59:AM")
        self.number_label = customtkinter.CTkLabel(self.main_frame, textvariable=self.time_var, text_font=("Consolas", 60), text_color=("cyan"))
        self.number_label.pack()
        
        
        # main frame to hold date
        self.date_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.date_frame.pack(side=tkinter.LEFT, padx=(10, 0))
        
        
        # Main label to display date
        self.date_variable = tkinter.StringVar(value=self.date)
        self.date_label = customtkinter.CTkLabel(self.date_frame, textvariable=self.date_variable, text_color=("cyan"))
        self.date_label.pack()
        
        
        self.time_function()
        self.root.mainloop()

    def time_function(self):
        """ Main method that updates time"""
        current_time = str(time.strftime("%H:%M:%S:%p"))
        self.time_var.set(value=current_time)
        self.root.after(1000, self.time_function)
        

if __name__ == "__main__":
    app = App()