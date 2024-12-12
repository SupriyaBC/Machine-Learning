#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Simulate EEG Features (alpha, beta, theta, gamma waves)
def generate_eeg_data(samples):
    return np.random.rand(samples, 4)  # 4 EEG features

# Simulate Facial Emotion Features (pre-defined scores for emotions)
def generate_facial_features(samples):
    return np.random.rand(samples, 5)  # 5 Facial emotion features

# Labels for Emotions
emotions = ['Happy', 'Sad', 'Angry', 'Neutral', 'Surprised']

# Dataset Generation
def create_emotion_dataset(samples=100):
    eeg_data = generate_eeg_data(samples)
    facial_data = generate_facial_features(samples)
    labels = np.random.choice(emotions, samples)
    
    # Combine data
    dataset = pd.DataFrame(
        np.hstack((eeg_data, facial_data)),
        columns=['EEG_Alpha', 'EEG_Beta', 'EEG_Theta', 'EEG_Gamma',
                 'Facial_Happy', 'Facial_Sad', 'Facial_Angry', 'Facial_Neutral', 'Facial_Surprised']
    )
    dataset['Emotion'] = labels
    return dataset

# Generate Dataset
dataset = create_emotion_dataset(1000)

# Save to CSV
dataset.to_csv('emotion_detection_dataset.csv', index=False)
print("Dataset saved as 'emotion_detection_dataset.csv'")


# In[10]:


import pandas as pd

# Load your custom dataset
data = pd.read_csv('emotion_detection_dataset.csv')

# Display the first few rows of the dataset
print(data.head())

# Check the columns in your dataset to confirm they match the required features
print(data.columns)


# In[11]:


# Drop rows with missing values, if necessary
data = data.dropna()

# Select only the relevant features
features = ['EEG_Alpha', 'EEG_Beta', 'EEG_Theta', 'EEG_Gamma',
            'Facial_Happy', 'Facial_Sad', 'Facial_Angry', 
            'Facial_Neutral', 'Facial_Surprised']
X = data[features]

# Assuming you have a target column 'Emotion' that indicates the emotion label
y = data['Emotion']


# In[12]:


from sklearn.model_selection import train_test_split

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[13]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))


# In[14]:


import joblib

# Save the model to a file
joblib.dump(model, 'emotion_detection_model.pkl')


# In[15]:


# Load the saved model
model = joblib.load('emotion_detection_model.pkl')

# Use the model to make predictions on new data
new_data = [[0.5, 0.3, 0.1, 0.2, 0, 1, 0, 0, 0]]  # Example input with features
prediction = model.predict(new_data)
print('Predicted Emotion:', prediction)


# In[ ]:





# In[26]:


import cv2
from fer import FER

# Load the image
image_path = r'C:\Users\Supri\OneDrive\Pictures\suppii.jpg'  # Replace with the actual path
image = cv2.imread(image_path)

# Check if the image is loaded correctly
if image is None:
    raise ValueError("Image not found or failed to load.")

# Ensure the image has 3 channels (check if it is not grayscale)
if len(image.shape) != 3 or image.shape[2] != 3:
    raise ValueError("Input image must be a 3-channel color image.")

# Create an emotion detector instance
detector = FER()

# Detect emotions in the image (using the 3-channel image)
emotions = detector.top_emotion(image)

if emotions:
    print(f"Detected emotion: {emotions}")
else:
    print("No emotions detected.")


# In[ ]:




