import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------- LOAD IMAGE -------- #
# ✅ Use raw string (r) to avoid path errors
image_path = r"C:\Users\sushm\Downloads\logo 1.jpg"

img = cv2.imread(image_path)

# -------- CHECK IMAGE -------- #
if img is None:
    print("❌ Error: Image not found! Check the file path.")
    exit()
else:
    print("✅ Image loaded successfully!")

# -------- BASIC DETAILS -------- #
print("\n--- IMAGE DETAILS ---")

print("Shape (Height, Width, Channels):", img.shape)

height, width, channels = img.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

# -------- PIXEL VALUES -------- #
print("\n--- PIXEL VALUES ---")

# Pixel at (0,0)
print("Pixel value at (0,0):", img[0, 0])

# Small section
print("\nTop-left 5x5 pixels:\n", img[0:5, 0:5])

# -------- COLOR CHANNELS -------- #
print("\n--- COLOR CHANNELS ---")

b, g, r = cv2.split(img)

print("Blue channel shape:", b.shape)
print("Green channel shape:", g.shape)
print("Red channel shape:", r.shape)

# -------- DISPLAY IMAGES -------- #
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,5))

plt.subplot(1,4,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(b, cmap='Blues')
plt.title("Blue Channel")
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(g, cmap='Greens')
plt.title("Green Channel")
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(r, cmap='Reds')
plt.title("Red Channel")
plt.axis('off')

plt.show()

# -------- EXPLANATION -------- #
print("\n--- EXPLANATION ---")

print("""
1. Shape:
   Image is stored as a 3D array (Height x Width x Channels).

2. Pixel Values:
   Each pixel has 3 values (Blue, Green, Red) from 0 to 255.
   Example: [255, 0, 0] = strong blue color.

3. Channels:
   Blue, Green, Red channels represent color intensity.

4. Image as Numbers:
   Image is a matrix of numbers.
   Computers process images using these numerical values.
""")