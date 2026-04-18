import tkinter as tk
def show_info():
    info_label.config(
        text="Adrian Kushneryk\n4704 Martingale Alcove\nWoodbury, MN 55129"
    )

def main():

    global info_label

    window = tk.Tk()
    window.title("Personal Info")
    window.geometry("300x300")

    instruction_label = tk.Label(
        window,
        text="Click the button to show information.",
        font=("Arial", 13),
        pady=10
    )
    instruction_label.pack()

    show_button = tk.Button(
        window,
        text="Show Info",
        font=("Arial", 13),
        width=12,
        command=show_info
    )
    show_button.pack(pady=10)

    info_label = tk.Label(
        window,
        text="",
        font=("Arial", 13),
        pady=20
    )
    info_label.pack()

    quit_button = tk.Button(
        window,
        text="Quit",
        font=("Arial", 13),
        width=12,
        command=window.destroy
    )
    quit_button.pack(pady=10)

    window.mainloop()
if __name__ == "__main__":
    main()