import os
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def file_to_image():
    # Open file dialog to select a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file")
    
    if not file_path:
        print("No file selected.")
        return
    
    # Read the file as bytes
    with open(file_path, "rb") as f:
        data = f.read()
    
    file_size = len(data)
    print(f"File size: {file_size} bytes")
    
    # Each pixel is 4 bytes (BGRX format)
    pixel_count = (file_size + 3) // 4  # Ensure all bytes are counted
    
    # Calculate image dimensions (better aspect ratio)
    width = int(np.sqrt(pixel_count))
    height = (pixel_count + width - 1) // width  # More accurate height calculation
    print(f"Image dimensions: {width}x{height}")
    
    # Pad the data to fit into full pixels
    padded_size = width * height * 4
    padded_data = data.ljust(padded_size, b'\x00')  # Padding with zero bytes
    
    # Convert to NumPy array
    img_data = np.frombuffer(padded_data, dtype=np.uint8)
    img_data = img_data.reshape((height, width, 4))
    
    # Create and save image using PIL
    image = Image.fromarray(img_data[:, :, :3], 'RGB')  # Convert to RGB (ignore X channel)
    output_path = os.path.splitext(file_path)[0] + "_output.png"
    image.save(output_path)
    print(f"Image saved at: {output_path}")

if __name__ == "__main__":
    file_to_image()
