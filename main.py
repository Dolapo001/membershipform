from tkinter import *
root = Tk()
root.geometry("500x300")

# Heading
Label(root, text="Membership Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field Name
fullname = Label(root, text="Fullname")
username = Label(root, text="Username")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
email = Label(root, text="Email")
paymentmode= Label(root, text="Payment Mode")

# Packing Fields
fullname.grid(row=1, column=2)
username.grid(row=2, column=2)
phone.grid(row=3, column=2)
gender.grid(row=4, column=2)
email.grid(row=5, column=2)
paymentmode.grid(row=6, column=2)

# Variable for storing data
fullnamevalue = StringVar
usernamevalue =  StringVar
phonevalue =  StringVar
gendervalue =  StringVar
emailvalue =  StringVar
paymentmodevalue =  StringVar
checkval = IntVar

# Creating entry field
fullnameentry = Entry(root, textvariable =fullnamevalue)
usernameentry = Entry(root, textvariable =usernamevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emailentry = Entry(root, textvariable =emailvalue)
paymentmodeentry = Entry(root, textvariable =paymentmodevalue)

# Packing entry fields
fullnameentry.grid(row=1, column=3)
usernameentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)
paymentmodeentry.grid(row=6, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text ="remember me?", variable = checkval)
checkbtn.grid(row=7, column= 3)

# Submit button
Button(text="Submit",command='getvals').grid(row=8,column=3)


root.mainloop()