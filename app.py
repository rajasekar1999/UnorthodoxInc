from keras.models import model_from_json

# Model reconstruction from JSON file
with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())

# Load weights into the new model
model.load_weights('model.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('testimages\\boy.jpeg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)

#training_set.class_indices
if result[0][0] == 1:
	prediction = 'stressed'
	print('The given image denotes a stressed Person')
else:
	prediction = 'notstressed'
	print('The given image denotes a notstressed Person')