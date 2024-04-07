import numpy as np
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Function to extract hair length feature from image
def extract_hair_length_feature(image_array):
    # Here you can implement your logic to extract features related to hair length
    # For demonstration purposes, let's assume that the average pixel intensity in the upper part of the image represents hair length
    upper_part = image_array[:112, :]  # Considering the upper half of the image
    hair_length_feature = np.mean(upper_part)  # Taking the average pixel intensity as the feature
    return hair_length_feature

# Load images from the specified directory
data_dir = r"C:\Users\Supri\OneDrive\Desktop\haa"
images = []
labels = []

image_paths = []  # Store image paths

for filename in os.listdir(data_dir):
    if filename.endswith(".png"):  # Assuming images are in PNG format
        img_path = os.path.join(data_dir, filename)  # Get image path
        img = Image.open(img_path).convert('L')  # Convert to grayscale
        img = img.resize((224, 224))  # Resize images to a consistent size
        img_array = np.array(img) / 255.0  # Normalize pixel values
        
        # Extract features related to hair length (e.g., pixel intensity in specific regions)
        hair_length_feature = extract_hair_length_feature(img_array)
        
        images.append(img_array)
        labels.append(hair_length_feature)
        image_paths.append(img_path)

# Convert lists to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Split data into train and test sets
train_images, test_images, train_labels, test_labels, train_paths, test_paths = train_test_split(images, labels, image_paths, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    Flatten(input_shape=(224, 224)),  # Flatten the 2D image arrays
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(1)  # Output layer for hair length regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Make predictions on test images
predicted_hair_lengths = model.predict(test_images)

# Map predicted hair lengths to gender labels
predicted_genders = ['Female' if length > 0.5 else 'Male' for length in predicted_hair_lengths]

# Display the predicted gender for each image along with the image
for i in range(len(test_images)):
    img = Image.open(test_paths[i])
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Predicted Gender: {predicted_genders[i]}")
    plt.show()

# Function to extract hair length feature from image
def extract_hair_length_feature(image_array):
    # Here you can implement your logic to extract features related to hair length
    # For demonstration purposes, let's assume that the average pixel intensity in the upper part of the image represents hair length
    upper_part = image_array[:112, :]  # Considering the upper half of the image
    hair_length_feature = np.mean(upper_part)  # Taking the average pixel intensity as the feature
    return hair_length_feature

# Load images from the specified directory
data_dir = r"C:\Users\Supri\OneDrive\Desktop\haa"
images = []
labels = []

image_paths = []  # Store image paths

for filename in os.listdir(data_dir):
    if filename.endswith(".png"):  # Assuming images are in PNG format
        img_path = os.path.join(data_dir, filename)  # Get image path
        img = Image.open(img_path).convert('L')  # Convert to grayscale
        img = img.resize((224, 224))  # Resize images to a consistent size
        img_array = np.array(img) / 255.0  # Normalize pixel values
        
        # Extract features related to hair length (e.g., pixel intensity in specific regions)
        hair_length_feature = extract_hair_length_feature(img_array)
        
        images.append(img_array)
        labels.append(hair_length_feature)
        image_paths.append(img_path)

# Convert lists to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Split data into train and test sets
train_images, test_images, train_labels, test_labels, train_paths, test_paths = train_test_split(images, labels, image_paths, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    Flatten(input_shape=(224, 224)),  # Flatten the 2D image arrays
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(1)  # Output layer for hair length regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Make predictions on test images
predicted_hair_lengths = model.predict(test_images)

# Map predicted hair lengths to gender labels
predicted_genders = ['Female' if length > 0.5 else 'Male' for length in predicted_hair_lengths]

# Display the predicted gender for each image along with the image
for i in range(len(test_images)):
    img = Image.open(test_paths[i])
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Predicted Gender: {predicted_genders[i]}")
    plt.show()
