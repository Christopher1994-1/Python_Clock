import customtkinter
import tkinter



class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Python Clock")
        self.root.geometry("500x130")

        # Main frame to hold label
        self.main_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.main_frame.pack(pady=(20, 0))

        # Main label to display values
        self.time_var = tkinter.StringVar(value="02:09:59:AM")
        self.number_label = customtkinter.CTkLabel(self.main_frame, textvariable=self.time_var, font=("Consolas", 75), text_color=("cyan"))
        self.number_label.pack()


        self.root.mainloop()

    def time_function(self):
        pass



if __name__ == "__main__":
    app = App()