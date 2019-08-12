from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=earphone&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3&as-pos=1&as-type=RECENT&as-backfill=on'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"_3liAhj _1R0K0g"})

container = containers[0]

filename = "Earphones.txt"
f = open(filename, "w+")

for container in containers:

	model = container.findAll("a",{"class":"_2cLu-l"})[0]["title"]

	color_list = list(container.findAll("div",{"class":"_1rcHFq"})[0].text.split()[0])
	if "," in color_list:
		color_list.remove(",")
	a=" "
	for i in color_list:
		a += i

	rating = container.findAll("div",{"class":"hGSR34"})[0].text

	original_price = container.findAll("div",{"class":"_3auQ3N"})[0].text
	discounted_price = container.findAll("div",{"class":"_1vC4OE"})[0].text

	if "₹" in list(original_price) or "₹" in list(discounted_price):
		b=list(original_price).remove("₹")
		b2=str(b)
		c=list(discounted_price).remove("₹")
		c2=str(c)

	discount = container.findAll("div",{"class":"VGWI6T"})[0].text

	if "%" in list(discount):
		d = list(discount).remove("%")
		d2 = str(d)

	f.write("Model: " + model + "\n")
	f.write("Colour: " + a + "\n")
	f.write("Rating: " + rating + "\n")
	f.write("Original Price: " + b2 + "\n")
	f.write("Discounted Price: " + c2 + "\n")
	f.write("Discount: " + d2 + "\n")
	f.write("\n")

f.close()


