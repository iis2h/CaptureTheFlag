# !/usr/bin/python3
import requests

URL = "https://crumbs.web.actf.co/"

responses = ['61f57d99-6d8e-4e5e-bfc1-995dc358fce7'] # First Random String
try:
	for h in responses:
		a = requests.get(URL + h).text # Sending GET Request
		print(str(responses.index(h)) + " => " + h)
		if "actf" not in a: # if the flag is not in the response continue
			b = a.strip("Go to")
			responses.append(b)
		else:
			print("Flag => " + a) # Print the flag
except KeyboardInterrupt:
	print("\nKeyboardInterrupt")
