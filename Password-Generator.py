from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("500x300")
root.resizable(False,False)

# Generate Random Strong Password
def new_rand():
    # Clear Our Entry Box
    pw_entry.delete(0, END)

    # Get PW Length and convert to integer
    pw_length = int(my_entry.get())

    # Create a variable to hold our password
    my_password = ''

    # Loop through Password Length
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    
    # Output Password to the screen
    pw_entry.insert(0, my_password)

# Copy to Clipbord
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to Clipboard
    root.clipboard_append(pw_entry.get())


# Label Frame
lf = LabelFrame(root, text="How Many Characters ?")
lf.pack(pady=20)

# Create Entry Box To Designate Number of Chararacter
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box For Our Returned Password
pw_entry = Entry(root,text='',font=("Helvetica", 24), bd=0 , bg="systembuttonface")
pw_entry.pack(pady=20)

# Create a Frame for our Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Our Buttons
my_button = Button(my_frame,text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipbord", command=clipper)
clip_button.grid(row=0,column=1,padx=10)


root.mainloop()
