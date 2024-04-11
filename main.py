import cv2
import tkinter as tk
from tkinter import filedialog

import numpy as np
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        # Create buttons
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.grid(row=0, column=0, padx=10, pady=10)

        self.grayscale_button = tk.Button(root, text="Grayscale", command=self.apply_grayscale)
        self.grayscale_button.grid(row=1, column=0, padx=10, pady=10)

        self.blur_button = tk.Button(root, text="Blur", command=self.apply_blur)
        self.blur_button.grid(row=2, column=0, padx=10, pady=10)

        self.sharpen_button = tk.Button(root, text="Sharpen", command=self.apply_sharpen)
        self.sharpen_button.grid(row=3, column=0, padx=10, pady=10)

        self.inverted_button = tk.Button(root, text="Inverted", command=self.apply_inverted)
        self.inverted_button.grid(row=4, column=0, padx=10, pady=10)

        # Bind mouse hover events to change button color
        self.select_button.bind("<Enter>", lambda event: self.change_button_color(self.select_button))
        self.select_button.bind("<Leave>", lambda event: self.change_button_color(self.select_button))
        self.grayscale_button.bind("<Enter>", lambda event: self.change_button_color(self.grayscale_button))
        self.grayscale_button.bind("<Leave>", lambda event: self.change_button_color(self.grayscale_button))
        self.blur_button.bind("<Enter>", lambda event: self.change_button_color(self.blur_button))
        self.blur_button.bind("<Leave>", lambda event: self.change_button_color(self.blur_button))
        self.sharpen_button.bind("<Enter>", lambda event: self.change_button_color(self.sharpen_button))
        self.sharpen_button.bind("<Leave>", lambda event: self.change_button_color(self.sharpen_button))
        self.inverted_button.bind("<Enter>", lambda event: self.change_button_color(self.inverted_button))
        self.inverted_button.bind("<Leave>", lambda event: self.change_button_color(self.inverted_button))

        # Variables
        self.image_path = None
        self.image = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image = cv2.imread(self.image_path)
            self.show_image()

    def apply_grayscale(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = gray_image
            self.show_image()

    def apply_blur(self):
        if self.image is not None:
            blurred_image = cv2.GaussianBlur(self.image, (5, 5), 0)
            self.image = blurred_image
            self.show_image()

    def apply_sharpen(self):
        if self.image is not None:
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
            sharpened_image = cv2.filter2D(self.image, -1, kernel)
            self.image = sharpened_image
            self.show_image()

    def apply_inverted(self):
        if self.image is not None:
            inverted_image = cv2.bitwise_not(self.image)
            self.image = inverted_image
            self.show_image()

    def show_image(self):
        if self.image is not None:
            img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(root, image=img)
            panel.image = img
            panel.grid(row=0, column=1, rowspan=5, padx=10, pady=10)

    def change_button_color(self, button):
        button.config(bg="purple", activebackground="purple")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
