# This requires:
# pip install requests Pillow


import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main window
root = tk.Tk()
root.title("Cat Image Loader")
root.geometry("420x350")

# Initially, photo_label is None, it will be set after the image is loaded for the first time
photo_label = None

def load_image():
    global photo_label
    """Load an image from the internet and display it in the Tkinter window."""
    url = 'https://cataas.com/cat'  # URL of a cat image
    response = requests.get(url)  # Make a GET request to the URL
    img_data = response.content  # Get the image data from the response

    # Open the image from the bytes data and convert it for Tkinter
    img = Image.open(BytesIO(img_data))
    tk_img = ImageTk.PhotoImage(img)

    # Check if 'photo_label' already exists
    if photo_label is None:
        # Create a new label because one does not exist
        photo_label = tk.Label(root, image=tk_img)
        photo_label.image = tk_img  # Keep a reference!
        photo_label.pack()
    else:
        # Update the existing label
        photo_label.config(image=tk_img)
        photo_label.image = tk_img  # Keep a reference!

# Create a button to load the image
load_button = tk.Button(root, text="Load Cat Image", command=load_image)
load_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
