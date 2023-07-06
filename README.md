# ImageConverter
Convert JPG to PNG and PNG to JPG

GUI Implementation to convert file from jpg to png using Python
Approach:
In Function jpg_to_png we first Check whether The Selecting the image is in the same Format (.jpg) which to convert to .png if not then return Error.
Else Convert the image the to .png
To open the Image we use the Function in tkinter called the FileDialog which helps to open the image from the folder
from tkinter import filedialog as fd
Same Approach for the PNG to JPG
