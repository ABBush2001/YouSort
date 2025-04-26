import tkinter as tk
from Item import Item

# Create the main application window
root = tk.Tk()
root.title("Main Menu")
root.geometry("300x200")

# Container to hold all frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Dictionary to hold different screens
frames = {}

# === Main Menu Frame ===
main_menu = tk.Frame(container)
frames["MainMenu"] = main_menu
main_menu.grid(row=0, column=0, sticky="nsew")

title_label = tk.Label(main_menu, text="Main Menu", font=("Helvetica", 16))
title_label.pack(pady=20)

def show_game_screen():
    frames["GameScreen"].tkraise()

start_button = tk.Button(main_menu, text="Start", font=("Helvetica", 12), command=show_game_screen)
start_button.pack(pady=10)

quit_button = tk.Button(main_menu, text="Quit", font=("Helvetica", 12), command=root.destroy)
quit_button.pack(pady=10)

# === Game Screen Frame ===
game_screen = tk.Frame(container)
frames["GameScreen"] = game_screen
game_screen.grid(row=0, column=0, sticky="nsew")

game_label = tk.Label(game_screen, text="Game Screen", font=("Helvetica", 16))
game_label.pack(pady=20)

back_button = tk.Button(game_screen, text="Back to Menu", command=lambda: frames["MainMenu"].tkraise())
back_button.pack(pady=10)

# Start with the main menu
frames["MainMenu"].tkraise()

# Run the application
root.mainloop()
