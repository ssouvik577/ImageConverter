# import all prerequisite
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

root = Tk()

# naming the GUI interface to image_conversion_APP
root.title("Image_Conversion_App")


# creating the Function which converts the jpg_to_png
def jpg_to_png():
    global im1

    # import the image from the folder
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".jpg"):

        im1 = Image.open(import_filename)

        # after converting the image save to desired
        # location with the Extersion .png
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im1.save(export_filename)

        # displaying the Messaging box with the Success
        messagebox.showinfo("success ", "your Image converted to Png")
    else:

        # if Image select is not with the Format of .jpg
        # then display the Error
        Label_2 = Label(root, text="Error!", width=20,
                        fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)
        messagebox.showerror("Fail!!", "Something Went Wrong...")


def png_to_jpg():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith(".png"):
        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")
        im1.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to jpg ")
    else:
        Label_2 = Label(root, text="Error!", width=20,
                        fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)

        messagebox.showerror("Fail!!", "Something Went Wrong...")


button1 = Button(root, text="JPG_to_PNG", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png)

button1.place(x=120, y=120)

button2 = Button(root, text="PNG_to_JPEG", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=png_to_jpg)

button2.place(x=120, y=220)
root.geometry("500x500+400+200")
root.mainloop()