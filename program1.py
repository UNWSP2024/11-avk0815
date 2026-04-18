#Program #1:
#Create a GUI window that displays your favorite saying.

import tkinter as tk

def main():
    window= tk.Tk()
    window.title("Favorite Saying")
    window.geometry("400x400")
    
    saying_label=tk.Label(
        window,
        text="The love of money is the root of all evil",
        font=("Arial", 10),
        padx=20,
        pady=40
    )
    saying_label.pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()
