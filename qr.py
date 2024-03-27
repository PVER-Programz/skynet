from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox as msg
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from io import BytesIO

# Defaults
img_url = "None"
ext = "Image files"
ftypes = [(ext, '*.png'),(ext, '*.jpg'),(ext, '*.tif'),(ext, '*.tiff'),(ext, '*.pdf'),(ext, '*.webp'),(ext, '*.jpeg')]

# Funcs
def saveQR(): 
	savefile = asksaveasfile(default = "png", filetypes = ftypes)
	print(savefile.name)
	imgcheck.save(savefile.name)

def convert(img_size, code_text, img_type):
	global img_url

	selection = var.get()

	try:
		if selection == 1:
			img_url = f"https://chart.apis.google.com/chart?cht=qr&chs={img_size}x{img_size}&choe=UTF-8&chld=H%7C0&chl={code_text}"
		elif selection == 2:
			img_url = f"https://www.scandit.com/wp-content/themes/scandit/barcode-generator.php?symbology=code128&size={img_size}&ec=L&value={code_text}"
		response = requests.get(img_url)
		img_data = response.content

		imgcheck = Image.open(BytesIO(img_data))
		size = imgcheck.width
		while size > 201:
			size = size-1
		divisor = imgcheck.width//size
		img = imgcheck.resize((imgcheck.width//divisor, imgcheck.height//divisor))
		img = ImageTk.PhotoImage(img)

		panel.config(image=img)

	except Exception as e:
		print("Invalid URL")
		print(e)
		msg.showerror("Invalid URL", "Please Enter a valid URL")


root = Tk()
root.title("QR & Barcode Generator for PC")

app = Frame(root)
app.pack(expand=1)

ttl = Label(app, text="PVER Code Generator", font=("Jokerman", 30))
ttl.grid(row=1, column=1, columnspan=3)

panel = Label(app, image=None)
panel.grid(row=2, column=1, padx=20, pady=10, rowspan=3)

url_frm = LabelFrame(app, text="Enter Text Here")
url_frm.grid(row=2, column=2, padx=10)
url_ent = ttk.Entry(url_frm, width=30, font=("Helvetica", 13))
url_ent.insert(0, "PVER")
url_ent.pack()

radios = Frame(app)
radios.grid(row=3, column=2)
var = IntVar()
R1 = Radiobutton(radios, text="QR Code", variable=var, value=1, font=("Helvetica", 13))
R1.select()
R1.pack()
R2 = Radiobutton(radios, text="Barcode", variable=var, value=2, font=("Helvetica", 13))
R2.pack()

btns = Frame(app)
btns.grid(row=4, column=2)
gen = ttk.Button(btns, text="Generate", width=13)
gen.pack(side=LEFT, padx=5)
save = ttk.Button(btns, text="Save", width=13)
save.pack(side=RIGHT, padx=5)

img_url = f"https://chart.apis.google.com/chart?cht=qr&chs=500x500&choe=UTF-8&chld=H%7C0&chl=PVER"
response = requests.get(img_url)
img_data = response.content

imgcheck = Image.open(BytesIO(img_data))
size = imgcheck.width
while size > 201:
	size = size-1
divisor = imgcheck.width//size
img = imgcheck.resize((imgcheck.width//divisor, imgcheck.height//divisor))
img = ImageTk.PhotoImage(img)

panel.config(image=img)

root.mainloop()

# print(type(img), img.height(), img.width())
# print(type(imgcheck), imgcheck.height, imgcheck.width)


'''
png-
jpg-
pdf-
tif-
tiff-
webp
jpeg

'''