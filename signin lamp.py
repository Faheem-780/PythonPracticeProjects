import customtkinter as ctk

class LampApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.is_on = False
        self.geometry("400x300")
        self.title("Python Lamp Toggle")
        
        # Initial Background (Darker)
        self.configure(fg_color="#121417")

        # The Toggle Button
        self.button = ctk.CTkButton(self, text="Toggle Lamp", command=self.toggle_lamp)
        self.button.pack(pady=100)

    def toggle_lamp(self):
        # 1. Flip the state
        self.is_on = not self.is_on
        
        # 2. Update UI based on state
        if self.is_on:
            # Change background to lighter grey
            self.configure(fg_color="#e6e9ef")
            print("Lamp is ON - Sound Played!")
        else:
            # Change background back to darker
            self.configure(fg_color="#121417")
            print("Lamp is OFF - Sound Played!")

if __name__ == "__main__":
    app = LampApp()
    app.mainloop()