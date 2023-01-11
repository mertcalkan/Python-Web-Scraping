import requests
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
PATH = "C:\Program Files\WebDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
import webbrowser
from tkinter import *
import urllib
import math
from PIL import ImageTk, Image
from tkinter import messagebox

# Array for storing Amazon product after retrieving it from Amazon website
amazonProductArr = []

# Array for storing N11 product after retrieving it from N11 website
n11ProductArr = []

# Array for storing Trendyol product after retrieving it from Trendyol website
trendyolProductArr = []

root = Tk()
root.title("Product Price Comparison")
root.geometry("1500x1070")
root.configure(bg='#333533')


search = StringVar()
state = StringVar()


# Function to get products from Amazon
def getDetailsAmazon():
	# title = document.querySelectorAll(".s-title-instructions-style h2 a span")
	# price = .a-price .a-offscreen
	# link = .aok-relative span a
	# photo = .aok-relative span a div img
	amazonURL = f"https://www.amazon.com.tr/s?k={search.get()}"
	# Entering options to not open the browser just get the data without opening the browser
	options = Options()
	options.headless = False
	print("Search Started")
	state.set(f"Searching {search.get()} on Amazon")

	driver = webdriver.Chrome(options=options, executable_path=r'geckodriver.exe')
	driver.get(amazonURL)
	print("Search End")
	state.set(f"Searched Finished")

	print("Finding Elements")
	state.set(f"Finding Products....")

	# Finding Product title, price and photo
	title = driver.find_element(By.CSS_SELECTOR, ".s-title-instructions-style h2 a span")
	price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")

	print(price)

	link = driver.find_element(By.CSS_SELECTOR, f".aok-relative span a").get_attribute("href")
	photo = driver.find_element(By.CSS_SELECTOR, f".aok-relative span a div img")

	print("Elements Found")	
	state.set(f"Products Found")

	print("Showing Elements on UI")	
	state.set(f"Showing Products")

	# Clearing all previous items from array
	amazonProductArr.clear()

	# Adding product to array
	amazonProductArr.append(link)
	amazonProductArr.append(title.text)
	amazonProductArr.append(price.get_attribute("textContent"))
	amazonProductArr.append(photo.get_attribute("src"))

	print("Amazon Products Done")	
	state.set(f"Amazon Products Done")

	print(amazonProductArr)
	
	# Checking if no product found
	assert "No results found." not in driver.page_source
	driver.close()

	showAmazonProducts()

# Function to get products from N11
def getDetailsN11():
    
	#GETTING URL OF N11 WEBPAGE.
	N11URL = f"https://www.n11.com/arama?q={search.get()}"

	# Entering options to not open the browser just get the data without opening the browser
	options = Options()
	options.headless = False
	print("Search Started")
	state.set(f"Searching {search.get()} on N11")

	driver = webdriver.Chrome(options=options, executable_path=r'geckodriver.exe')
	driver.get(N11URL)
	print("Search End")
	state.set(f"Searching End")
	state.set(f"Finding Products on N11")

	print("Finding Elements")

	#birinci elem : moria-ProductCard-dglYMa 
	# ikinci elem foto : moria-ProductCard-dglYMa 
	# test href parent div  : moria-ProductCard-joawUM reYsY sz0ny92mhlu
	# ikinci test href parent div : 
	# Finding Product title, price and photo
	# div = driver.find_element(By.CSS_SELECTOR, f".moria-ProductCard-gLyfvY span")
	# element = driver.find_element(By.CSS_SELECTOR , "div.moria-ProductCard-joawUM")
	photo = driver.find_element(By.CSS_SELECTOR, ".imgHolder img")
	price = driver.find_element(By.CSS_SELECTOR, f".priceContainer div span.newPrice ins");

	link = driver.find_element(By.CSS_SELECTOR, f".plink").get_attribute("href")
	title = driver.find_element(By.CSS_SELECTOR, f".productName")
	print("Elements Found")	
	print(price)
	state.set(f"Products found on N11")

	print("Showing N11 Products")	

	# Clearing all previous items from array
	n11ProductArr.clear()

	# Adding prouduct to array
	n11ProductArr.append(link)
	n11ProductArr.append(title.text)
	n11ProductArr.append(price.text)
	n11ProductArr.append(photo.get_attribute("src"))

	print("Elements Appear on UI")	
	state.set(f"N11 Products Showed")


	# Checking if no product found
	assert "No results found." not in driver.page_source
	driver.close()

	showN11Products()

# Function to get products from Trendyol
def getDetailsTrendyol():
    # title = document.querySelectorAll(".s-title-instructions-style h2 a span")
	# price = .a-price .a-offscreen
	# link = .aok-relative span a
	# photo = .aok-relative span a div img
	trendyolURL = f"https://www.trendyol.com/sr?q={search.get()}"
	# Entering options to not open the browser just get the data without opening the browser
	options = Options()
	options.headless = False
	print("Search Started")
	state.set(f"Searching {search.get()} on Trendyol")

	driver = webdriver.Chrome(options=options, executable_path=r'geckodriver.exe')
	driver.get(trendyolURL)
	print("Search End")
	state.set(f"Searched Finished")

	print("Finding Elements")
	state.set(f"Finding Products....")

	# Finding Product title, price and photo
	title = driver.find_element(By.CSS_SELECTOR, ".prdct-desc-cntnr-ttl")
	price = driver.find_element(By.CSS_SELECTOR, ".prc-box-dscntd")
	print(price)
	link = driver.find_element(By.CSS_SELECTOR, f".p-card-chldrn-cntnr.card-border a").get_attribute("href")
	
	photo = driver.find_element(By.CSS_SELECTOR, f".p-card-img")
	print("Elements Found")	
	state.set(f"Products Found")

	print("Showing Elements on UI")	
	state.set(f"Showing Products")

	# Clearing all previous items from array
	trendyolProductArr.clear()

	# Adding prouduct to array
	trendyolProductArr.append(link)
	trendyolProductArr.append(title.text)
	trendyolProductArr.append(price.get_attribute("textContent"))
	trendyolProductArr.append(photo.get_attribute("src"))

	print("Trendyol Products Done")	
	state.set(f"Trendyol Products Done")

	print(trendyolProductArr)
	# Checking if no product found
	assert "No results found." not in driver.page_source
	driver.close()

	showTrendyolProducts()

# Function to add spacing to text
def addSpacing(text):
	newText = ""
	i = 0
	text = text.split(" ")
	for val in text:
		if i == 10:
			newText += "\n "
			i = 0
		newText += f"{val} "
		i += 1
		
	return newText

# Delete Frame
def deleteFrame(frame):
	for item in frame.winfo_children():
		item.destroy()

	print("Items Deleted")


def showAmazonProducts():
    
	deleteFrame(amazonProductFrame)
	global amazonProductArr
	global img2
	
    # Ad
	AmazonTitle = Label(amazonProductFrame, bg ="#333533", fg = "#D6D6D6", text="AMAZON", font=("Calibri", 30, "bold"))
	AmazonTitle.pack()

	# Icerik
	AmazonProductName = Label(amazonProductFrame, bg ="#333533",fg = "#D6D6D6", text=addSpacing(amazonProductArr[1]), font=("Calibri", 13, "italic"),wraplengt=200)  
	AmazonProductName.pack(padx = 20, pady = 20)

	# Fiyat
	AmazonPriceLabel = Label(amazonProductFrame, bg ="#333533", fg = "#FFEE32", text=amazonProductArr[2], font=("Calibri", 13, "bold"))
	AmazonPriceLabel.pack(padx = 20, pady = 20)

	# Link Buton
	img2 = PhotoImage(file = f"./images/img2.png")
	AmazonLinkBtn = Button(amazonProductFrame, image = img2 ,borderwidth = 0, highlightthickness = 0, relief = "flat", cursor="hand2", text="Open in AMAZON", command=lambda: webbrowser.open(amazonProductArr[0]))
	AmazonLinkBtn.pack(padx = 20, pady = 20)

	# Image
	raw_data = urllib.request.urlopen(amazonProductArr[3])
	u = raw_data.read()
	raw_data.close()
	photo = ImageTk.PhotoImage(data=u)
	label1 = Label(amazonProductFrame, image=photo, width=300, height=300)
	label1.image = photo
	label1.pack(side=RIGHT, pady=100, padx=50)

	print("Amazon DONE")

def showN11Products():
    
	deleteFrame(n11ProductFrame)
	global n11ProductArr
	global imgN11

	# Ad
	N11Title = Label(n11ProductFrame, bg ="#333533",fg = "#D6D6D6", text="N11", font = ("Calibri", 30, "bold"))
	N11Title.pack()

	# Icerik
	N11ProductName = Label(n11ProductFrame, bg ="#333533",fg = "#D6D6D6", text = addSpacing(n11ProductArr[1]), font=("Calibri", 13, "italic"),wraplengt=200)  
	N11ProductName.pack(padx = 20, pady = 20)

	# Fiyat
	N11PriceLabel = Label(n11ProductFrame, bg ="#333533",fg = "#FFEE32", text = n11ProductArr[2], font=("Calibri", 13, "bold"))
	N11PriceLabel.pack(padx = 20, pady = 20)

	# Link Buton
	imgN11 = PhotoImage(file = f"./images/imgN11.png")
	N11LinkBtn = Button(n11ProductFrame, image = imgN11 ,borderwidth = 0, highlightthickness = 0, relief = "flat", cursor="hand2", command=lambda: webbrowser.open(n11ProductArr[0]))
	N11LinkBtn.pack(padx = 20, pady = 20)

	# Image
	raw_data = urllib.request.urlopen(n11ProductArr[3])
	u = raw_data.read()
	raw_data.close()
	photo = ImageTk.PhotoImage(data=u)
	label1 = Label(n11ProductFrame, image=photo, width=300, height=300)
	label1.image = photo
	label1.pack(side=RIGHT, pady=100)

	print("N11 DONE")

def showTrendyolProducts():
    
    deleteFrame(trendyolProductFrame)
    global trendyolProductArr
    global img0
	
    # Ad
    TrendyolTitle  = Label(trendyolProductFrame, bg ="#333533",fg = "#D6D6D6", text="TRENDYOL", font=("Calibri", 30, "bold"))
    TrendyolTitle.pack()
    
    #Icerik
    TrendyolProductName = Label(trendyolProductFrame, bg ="#333533",fg = "#D6D6D6", text=addSpacing(trendyolProductArr[1]), font=("Calibri", 13, "italic"),wraplengt=200)  
    TrendyolProductName.pack(pady = 20)
    
	# Fiyat
    TrendyolPriceLabel = Label(trendyolProductFrame, bg ="#333533",fg = "#FFEE32", text=trendyolProductArr[2], font=("Calibri", 13, "bold"))
    TrendyolPriceLabel.pack(pady = 20)
    
    # Link Buton
    img0 = PhotoImage(file = f"./images/img0.png")
    TrendyolLinkBtn = Button(trendyolProductFrame, image = img0 ,borderwidth = 0, highlightthickness = 0, relief = "flat", text="Open in Trendyol", cursor="hand2", command=lambda: webbrowser.open(trendyolProductArr[0]))
    TrendyolLinkBtn.pack(padx = 20, pady = 20)
    
	# Image
    raw_data = urllib.request.urlopen(trendyolProductArr[3])
    u = raw_data.read()
    raw_data.close()
    photo = ImageTk.PhotoImage(data=u)
    label1 = Label(trendyolProductFrame, image=photo, width=300, height=300)
    label1.image = photo
    label1.pack(side=RIGHT, pady=100)
    
    print("Trendyol DONE")

# Main function that will run when user enter product name and click on SEARCH PRODUCT
def getResult():
    if (search.get() == ""):
        messagebox.showwarning("Warning!!!","Please enter a product name!!!")
    else:
        getDetailsTrendyol()
        getDetailsAmazon()
        getDetailsN11()
        state.set(f"Ready")
        messagebox.showinfo("Information","Search Completed!!!")

# Enter The Product Name
label = Label(root, text="Enter The Product Name", font=("Calibri", 20, "bold"), bg = "#333533", fg = "#D6D6D6")
label.pack(pady = 10)

# Please enter a specific product name. Do not enter general product name!!!
label = Label(root, text="(Please enter a specific product name. Do not enter general product name!!!)", font=("Calibri", 13, "italic"), bg = "#333533", fg = "#D6D6D6")
label.pack()

# Entry 
entry = Entry(root, width=40, bg = "#202020", fg = "#D6D6D6", font=("Calibri", 13, "italic"), textvariable=search)
entry.pack(pady = 15)

# Search Button
img3 = PhotoImage(file = f"./images/img3.png")
button = Button(root, image = img3,borderwidth = 0, highlightthickness = 0, relief = "flat", cursor="hand2", command=getResult)
button.place(
    x = 632, y = 126,
    width = 175,
    height = 50)
button.pack()


# Product Frame for showing daraz and other websites product
productFrame = Frame(root, relief=RAISED)

# Amazon Frame where Amazon product will be shown
amazonProductFrame = Frame(root, bg ="#333533")
amazonProductFrame.pack(side=LEFT)

# Trendyol Frame where Trendyol product will be shown
trendyolProductFrame = Frame(root, bg ="#333533")
trendyolProductFrame.pack(side=LEFT, padx = 200)

# N11 Frame where N11 product will be shown
n11ProductFrame = Frame(root, bg ="#333533")
n11ProductFrame.pack(side=LEFT)

productFrame.pack(side=TOP, anchor=CENTER)

# Enter tusuna basildigi zaman da calisacak
root.bind("<Return>", (lambda event: getResult()))

root.mainloop()