import tkinter as tk
from tkinter import messagebox
import requests

def shorten_url():
    original_url = entry.get()
    response = requests.post('http://127.0.0.1:5000/shorten', data={'url': original_url})
    if response.status_code == 200:
        short_url = response.text
        result_label.config(text=f'Short URL: {short_url}')
    else:
        messagebox.showerror('Error', 'Failed to shorten URL')

root = tk.Tk()
root.title('URL Shortener')

tk.Label(root, text='Enter URL:').grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text='Shorten', command=shorten_url).grid(row=1, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text='')
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
