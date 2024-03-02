import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def pick_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if image_path:
        load_image()
        detect_button.config(state=tk.NORMAL)

def load_image():
    global image, photo
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def detect_number():
    # Placeholder function for detecting numbers in the image
    # In a real application, you would implement your number detection logic here
    detected_number_label.config(text="1234")

def clear_canvas():
    canvas.delete("all")
    detected_number_label.config(text="")
    detect_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Image Picker App")

frame1 = tk.Frame(root, width=200, height=400)
frame1.pack_propagate(False)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root, bg="white")
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

pick_button = tk.Button(frame1, text="Pick Image", command=pick_image)
pick_button.pack(pady=10)

detect_button = tk.Button(frame1, text="Detect", state=tk.DISABLED, command=detect_number)
detect_button.pack(pady=10)

canvas = tk.Canvas(frame2, width=400, height=400, bg="white")
canvas.pack(expand=True, fill=tk.BOTH)

some_text_label = tk.Label(frame2, text="Some Text")
some_text_label.pack()

plate_image = tk.Label(frame2, text="Plate Image")
plate_image.pack()

text_label = tk.Label(frame2, text="Detected Number:")
text_label.pack(pady=10)

detected_number_label = tk.Label(frame2, text="")
detected_number_label.pack()

clear_button = tk.Button(frame2, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

root.mainloop()
