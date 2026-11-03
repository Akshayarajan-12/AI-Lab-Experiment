import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
np.random.seed(42)
tf.random.set_seed(42)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)
y_train_encoded = tf.keras.utils.to_categorical(y_train, 10)
y_test_encoded = tf.keras.utils.to_categorical(y_test, 10)
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(128, activation="sigmoid"),
    tf.keras.layers.Dense(10, activation="sigmoid")
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="binary_crossentropy",
    metrics=[tf.keras.metrics.CategoricalAccuracy(name="accuracy")]
)
print("Handwritten Digit Recognition")
print("--------------------------------")
model.summary()
history = model.fit(
    x_train,
    y_train_encoded,
    epochs=5,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)
predicted_probabilities = model.predict(x_test, verbose=0)
y_pred = np.argmax(predicted_probabilities, axis=1)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("\nModel Evaluation")
print("--------------------------------")
print("Testing Accuracy: {:.2f}%".format(accuracy * 100))
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

