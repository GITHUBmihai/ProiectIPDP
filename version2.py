import cv2
import tkinter as tk
from tkinter import filedialog

import numpy as np
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")
        self.root.state('zoomed')

        # Create buttons
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.grid(row=0, column=0, padx=10, pady=10)

        self.grayscale_button = tk.Button(root, text="Grayscale", command=self.apply_grayscale)
        self.grayscale_button.grid(row=1, column=0, padx=10, pady=10)

        self.low_blur_button = tk.Button(root, text="Low Blur", command=self.apply_low_blur)
        self.low_blur_button.grid(row=2, column=0, padx=10, pady=10)

        self.medium_blur_button = tk.Button(root, text="Medium Blur", command=self.apply_medium_blur)
        self.medium_blur_button.grid(row=3, column=0, padx=10, pady=10)

        self.high_blur_button = tk.Button(root, text="High Blur", command=self.apply_high_blur)
        self.high_blur_button.grid(row=4, column=0, padx=10, pady=10)

        self.sharpen_button = tk.Button(root, text="Sharpen", command=self.apply_sharpen)
        self.sharpen_button.grid(row=5, column=0, padx=10, pady=10)

        self.inverted_button = tk.Button(root, text="Inverted", command=self.apply_inverted)
        self.inverted_button.grid(row=6, column=0, padx=10, pady=10)

        self.green_tint_button = tk.Button(root, text="Green Tint", command=self.apply_green_tint)
        self.green_tint_button.grid(row=7, column=0, padx=10, pady=10)

        self.red_tint_button = tk.Button(root, text="Red Tint", command=self.apply_red_tint)
        self.red_tint_button.grid(row=8, column=0, padx=10, pady=10)

        self.blue_tint_button = tk.Button(root, text="Blue Tint", command=self.apply_blue_tint)
        self.blue_tint_button.grid(row=9, column=0, padx=10, pady=10)

        self.pixelated_button = tk.Button(root, text="Pixelated", command=self.apply_pixelate)
        self.pixelated_button.grid(row=10, column=0, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Return to Default", command=self.reset_image)
        self.reset_button.grid(row=11, column=0, padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=12, column=0, padx=10, pady=10)

        # Bind mouse hover events to change button color
        self.select_button.bind("<Enter>", lambda event: self.change_button_color(self.select_button))
        self.select_button.bind("<Leave>", lambda event: self.reset_button_color(self.select_button))
        self.grayscale_button.bind("<Enter>", lambda event: self.change_button_color(self.grayscale_button))
        self.grayscale_button.bind("<Leave>", lambda event: self.reset_button_color(self.grayscale_button))
        self.low_blur_button.bind("<Enter>", lambda event: self.change_button_color(self.low_blur_button))
        self.low_blur_button.bind("<Leave>", lambda event: self.reset_button_color(self.low_blur_button))
        self.medium_blur_button.bind("<Enter>", lambda event: self.change_button_color(self.medium_blur_button))
        self.medium_blur_button.bind("<Leave>", lambda event: self.reset_button_color(self.medium_blur_button))
        self.high_blur_button.bind("<Enter>", lambda event: self.change_button_color(self.high_blur_button))
        self.high_blur_button.bind("<Leave>", lambda event: self.reset_button_color(self.high_blur_button))
        self.sharpen_button.bind("<Enter>", lambda event: self.change_button_color(self.sharpen_button))
        self.sharpen_button.bind("<Leave>", lambda event: self.reset_button_color(self.sharpen_button))
        self.inverted_button.bind("<Enter>", lambda event: self.change_button_color(self.inverted_button))
        self.inverted_button.bind("<Leave>", lambda event: self.reset_button_color(self.inverted_button))
        self.green_tint_button.bind("<Enter>", lambda event: self.change_button_color(self.green_tint_button))
        self.green_tint_button.bind("<Leave>", lambda event: self.reset_button_color(self.green_tint_button))
        self.red_tint_button.bind("<Enter>", lambda event: self.change_button_color(self.red_tint_button))
        self.red_tint_button.bind("<Leave>", lambda event: self.reset_button_color(self.red_tint_button))
        self.blue_tint_button.bind("<Enter>", lambda event: self.change_button_color(self.blue_tint_button))
        self.blue_tint_button.bind("<Leave>", lambda event: self.reset_button_color(self.blue_tint_button))
        self.pixelated_button.bind("<Enter>", lambda event: self.change_button_color(self.pixelated_button))
        self.pixelated_button.bind("<Leave>", lambda event: self.reset_button_color(self.pixelated_button))
        self.reset_button.bind("<Enter>", lambda event: self.change_button_color(self.reset_button))
        self.reset_button.bind("<Leave>", lambda event: self.reset_button_color(self.reset_button))
        self.save_button.bind("<Enter>", lambda event: self.change_button_color(self.save_button))
        self.save_button.bind("<Leave>", lambda event: self.reset_button_color(self.save_button))

        # Variables
        self.image_path = None
        self.image = None
        self.original_image = None

    def select_image(self):
        #if self.image is not None:
           #image_1 = self.image
           #image_1.destroy()
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = cv2.imread(self.image_path)
            self.image = cv2.imread(self.image_path)
            self.resize_image_to_fit_screen()
        self.show_image()

    def resize_image_to_fit_screen(self):
        if self.image is not None:
            # Get the dimensions of the screen
            screen_width = self.root.winfo_screenwidth() - 100
            screen_height = self.root.winfo_screenheight() - 100

            # Get the dimensions of the image
            image_width, image_height = self.image.shape[1], self.image.shape[0]
            if image_width > screen_width or image_height > screen_height:
               # Calculate scaling factors
               width_scale = screen_width / image_width
               height_scale = screen_height / image_height
               scale = min(width_scale, height_scale) - 0.05
               # Resize the image using OpenCV
               self.image = cv2.resize(self.image, None, fx=scale, fy=scale)
               self.original_image = cv2.resize(self.original_image, None, fx=scale, fy=scale)

            # Update the image displayed in the GUI
            self.show_image()

    def apply_grayscale(self):
        if self.original_image is not None:
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            self.image = gray_image
            self.show_image()

    def apply_low_blur(self):
        if self.original_image is not None:
            blurred_image = cv2.GaussianBlur(self.original_image, (17, 17), 10)
            self.image = blurred_image
            self.show_image()

    def apply_medium_blur(self):
        if self.original_image is not None:
            blurred_image = cv2.GaussianBlur(self.original_image, (31, 31), 15)
            self.image = blurred_image
            self.show_image()

    def apply_high_blur(self):
        if self.original_image is not None:
            blurred_image = cv2.GaussianBlur(self.original_image, (61, 61), 19)
            self.image = blurred_image
            self.show_image()

    def apply_sharpen(self):
        if self.original_image is not None:
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
            sharpened_image = cv2.filter2D(self.original_image, -1, kernel)
            self.image = sharpened_image
            self.show_image()

    def apply_inverted(self):
        if self.original_image is not None:
            inverted_image = cv2.bitwise_not(self.original_image)
            self.image = inverted_image
            self.show_image()

    def apply_green_tint(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.image[:, :, 1] = cv2.add(self.image[:, :, 1], 100)  # Add green channel
            self.show_image()

    def apply_red_tint(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.image[:, :, 2] = cv2.add(self.image[:, :, 2], 100)  # Add red channel
            self.show_image()

    def apply_blue_tint(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.image[:, :, 0] = cv2.add(self.image[:, :, 0], 100)  # Add blue channel
            self.show_image()

    def apply_pixelate(self):
        if self.original_image is not None:
            height, width = self.original_image.shape[:2]
            pixel_size = 6  # Size of the pixel blocks

            # Resize the image to a smaller size
            temp_image = cv2.resize(self.original_image,
                                    (width // pixel_size, height // pixel_size),
                                    interpolation=cv2.INTER_LINEAR)

            # Resize back to the original size
            self.image = cv2.resize(temp_image, (width, height), interpolation=cv2.INTER_NEAREST)
            self.show_image()

    def reset_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.show_image()

    def save_image(self):
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.image)

    def show_image(self):
        if self.image is not None:
            img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)  # creates object from the image
            panel = tk.Label(root, image=img)  # display in the Tkinter window
            panel.image = img
            panel.grid(row=0, column=1, rowspan=300, padx=10, pady=10)

    def change_button_color(self, button):
        button.config(bg="#AAAAAA", activebackground="#AAAAAA")

    def reset_button_color(self, button):
        button.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()