import subprocess
import time
import tkinter as tk
from tkinter import ttk

label_var = 0
dropdown = 0
def on_dropdown_change(event):
    global label_var,dropdown
    selected_value = dropdown.get()
    label_var.set(f"Selected: {selected_value}")

def create_dropdown():
    global label_var,dropdown
    label_var = tk.StringVar()
    label = tk.Label(root, textvariable=label_var)
    label.pack(pady=10)

    # Create a dropdown list
    options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
    dropdown = ttk.Combobox(root, values=options)
    dropdown.set(options[0])  # Set the default value
    dropdown.pack(pady=10)

# Bind the event handler to the dropdown change event

def on_checkbox_clicked(checkbox_value):
    if checkbox_value == "single file":
        create_dropdown()
    else:
        pass

# Create the main window
root = tk.Tk()
root.title("Checkbox GUI")

# Function to create checkboxes
def create_checkbox(checkbox_value):
    checkbox = tk.Checkbutton(root, text=f"{checkbox_value}", variable=checkbox_value, command=lambda: on_checkbox_clicked(checkbox_value))
    checkbox.pack()

# Create checkboxes with values 1 to 5

checkbox_value = tk.BooleanVar()
create_checkbox("Single file")
checkbox_value = tk.BooleanVar()
create_checkbox("Multiple files")

# Start the GUI event loop
root.mainloop()

'''with open("loc.txt", "w") as file1:
    # Writing data to a file
        file1.write(str(1))  '''
'''def get_gfortran_version():
    try:
        # Run the command to get the GNU Fortran compiler version
        result = subprocess.run(['gfortran', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Extract and print the version information
            version_info = result.stdout.strip()
            print(f"GNU Fortran Compiler Version: {version_info}")
        else:
            # Print error message if the command failed
            print(f"Error retrieving GNU Fortran Compiler version. Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get the compiler version
get_gfortran_version()'''


