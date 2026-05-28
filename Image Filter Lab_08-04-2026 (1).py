import cv2
import matplotlib.pyplot as plt

# -------- LOAD IMAGE -------- #
image_path = r"C:\Users\sushm\Downloads\logo 1.jpg"  # change if needed

img = cv2.imread(image_path)

# -------- CHECK IMAGE -------- #
if img is None:
    print("❌ Error: Image not found!")
    exit()
else:
    print("✅ Image loaded successfully!")

# Convert BGR to RGB (for correct display)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# -------- GRAYSCALE -------- #
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------- BLUR -------- #
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# -------- EDGE DETECTION -------- #
edges = cv2.Canny(blur, 100, 200)

# -------- DISPLAY RESULTS -------- #
plt.figure(figsize=(12,6))

# Original
plt.subplot(1,4,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

# Grayscale
plt.subplot(1,4,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

# Blur
plt.subplot(1,4,3)
plt.imshow(blur, cmap='gray')
plt.title("Blur")
plt.axis('off')

# Edges
plt.subplot(1,4,4)
plt.imshow(edges, cmap='gray')
plt.title("Edges")
plt.axis('off')

plt.show()

# -------- EXPLANATION -------- #
print("\n--- EXPLANATION ---")

print("""
1. Grayscale:
   Converts image to black and white (removes color).

2. Blur:
   Smoothens the image and removes noise using Gaussian Blur.

3. Edge Detection:
   Detects boundaries of objects using Canny Edge Detection.

4. Before/After:
   Original image is compared with processed images.
""")