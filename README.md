# UnorthodoxInc
Team Unorthodox Inc - EngiNx 2019 - Mental Health Detection by means of Thermal Imaging.


# Dependencies

1. Python 3.x
2. Tensorflow
3. Keras

# How To Run

1. Upload the images to test to the folder testimages
2. Update image.load_img('testimages/{'filename'}', target_size = (64, 64)) in app.py with the image file name
3. Update open('model/model_architecture.json', 'r') to open('model/model_architecture.json', 'r') in app.py
4. Update model.load_weights('model.h5') to model.load_weights('model/model.h5') in app.py
5. Open Command Prompt and run `python app.py` to see the results
