import kagglehub
import tensorflow as tf

# # Download latest version
# path = kagglehub.dataset_download("amankumar234/body-movement-classification")
path = kagglehub.dataset_download("tapakah68/segmentation-full-body-tiktok-dancing-dataset")
print("Path to dataset files:", path)
path = kagglehub.dataset_download("yasaminjafarian/tiktokdataset")
print("Path to dataset files:", path)

# # path to dataset = "C:\Users\epics\.cache\kagglehub\datasets\amankumar234\body-movement-classification\versions\1"

# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(height, width, channels)),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.LSTM(50, return_sequences=True),
#     tf.keras.layers.Dense(1, activation='softmax')  
# ])