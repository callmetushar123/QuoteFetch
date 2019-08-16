from bs4 import BeautifulSoup
import requests
import time
import tkinter as tk



while True:
    source = requests.get("https://www.quoteoftheday.nu/").text #text will convert the response object
    #to html codes
    #print(source)
    soup  = BeautifulSoup(source, "lxml")

    match = soup.find("div").find("p").text

    root = tk.Tk()
    T = tk.Text(root, height = 5, width =50)
    T.pack()
    T.insert(tk.END, match)
    tk.mainloop()
    time.sleep(86400)
    #print(match)
