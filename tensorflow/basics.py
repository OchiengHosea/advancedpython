import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
import numpy as np

# Trainign the first model
# create features and labels

celcius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenhite_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

lort = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celcius_q, fahrenhite_a, epochs=500, verbose=False)
print("Finished training the model")

print(model.predict([100.00]))

print(lort.get_weights())

# Display the statistics
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel('Loss Magnitude')
plt.plot(history.history['loss'])