import tkinter as tk
from tkinter import ttk

def tab1():
    # Function to display content for Tab 1
    clear_frame(tab1_frame)
    label = tk.Label(tab1_frame, text="Content for Tab 1", padx=10, pady=10)
    label.pack()

def tab2():
    # Function to display content for Tab 2
    clear_frame(tab2_frame)
    label = tk.Label(tab2_frame, text="Content for Tab 2", padx=10, pady=10)
    label.pack()

def tab3():
    # Function to display content for Tab 3
    clear_frame(tab3_frame)
    label = tk.Label(tab3_frame, text="Content for Tab 3", padx=10, pady=10)
    label.pack()

def clear_frame(frame):
    # Function to clear the content of a frame
    for widget in frame.winfo_children():
        widget.destroy()

# Create the main application window
root = tk.Tk()
root.title("Tabbed Application")

# Create a tab control
tab_control = ttk.Notebook(root)

# Create the frames for each tab
tab1_frame = ttk.Frame(tab_control)
tab2_frame = ttk.Frame(tab_control)
tab3_frame = ttk.Frame(tab_control)

# Add the tabs to the tab control
tab_control.add(tab1_frame, text="Tab 1")
tab_control.add(tab2_frame, text="Tab 2")
tab_control.add(tab3_frame, text="Tab 3")

# Add event bindings to call functions when tabs are selected
tab_control.bind("<<NotebookTabChanged>>", lambda event: tab1() if tab_control.index("current") == 0 else tab2() if tab_control.index("current") == 1 else tab3())

# Pack the tab control into the main window
tab_control.pack(expand=1, fill="both")

# Call the functions for the default tab
tab1()

# Start the Tkinter event loop
root.mainloop()
