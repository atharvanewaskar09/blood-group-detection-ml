import os
import cv2
import numpy as np
import pickle
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# CONFIG
DATASET_DIR = "dataset"
IMAGE_SIZE = 64
MAX_IMAGES_PER_CLASS = 200

X = []
y = []

# LOAD DATA
for label in sorted(os.listdir(DATASET_DIR)):
    label_path = os.path.join(DATASET_DIR, label)

    if not os.path.isdir(label_path):
        continue

    images = os.listdir(label_path)[:MAX_IMAGES_PER_CLASS]

    for img_name in images:
        img_path = os.path.join(label_path, img_name)

        try:
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
            X.append(img.flatten())
            y.append(label)
        except:
            pass

# CHECK CLASSES
print("Samples per class:", Counter(y))

# CONVERT
X = np.array(X)
y = np.array(y)

# ENCODE LABELS
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# TRAIN MODEL
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)

# ACCURACY
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# SAVE MODEL
with open("model.pkl", "wb") as f:
    pickle.dump((model, encoder), f)

print("model.pkl saved")