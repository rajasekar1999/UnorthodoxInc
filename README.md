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

## Project Description
 
* Detection of Mental Health diseases with accuracy by means of generating a body heat map of the patient with the help of a thermal camera and applying techniques of image processing and Deep Learning image classification models to measure the magnitude of the detected disease.

## Dataset !!

* [Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/download.html)
* [Sample Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/face01.zip) 


### After installing all requirements, to run in cmd:
   ```sh
   $ cd tutorial-2-image-classifier

   $ python predict.py <imageInputFileName.extension>
   ```

### To run the WebApp:
   ```sh
   $ cd project\thermalai

   $ python manage.py runserver
   ```   

### Author

<p align="center"> Made with ❤</p>

[Rajasekar M](https://www.linkedin.com/in/rajasekar1999/),
[Sudharshan S](https://www.linkedin.com/in/sudharshan-shanmugasundaram-2b8b80176/),
[Udhay Aakash R](https://www.linkedin.com/in/udhay-aakash-21b74a116/),
[Manojkumar VK](https://www.linkedin.com/in/vkmanojk/).

### Research papers, news, articles & sources

[Paper 1](https://www.semanticscholar.org/paper/Facial-Thermal-Image-Analysis-for-Stress-Detection-Hong-Liu/2e8ccf7156629bcf14d43b946397eb04a14b9d78),
[Paper 2](http://www.pnas.org/content/pnas/suppl/2013/12/26/1321664111.DCSupplemental/pnas.201321664SI.pdf),
[Source 1](https://www.businesstoday.in/lifestyle/off-track/indians-suffer-from-stress-depression/story/280119.html),
[Source 2](https://economictimes.indiatimes.com/magazines/panache/89-per-cent-of-indias-population-suffering-from-stress-most-dont-feel-comfortable-talking-to-medical-professionals/articleshow/64926633.cms),
[Source 3](https://www.mentalhealth.org.uk/statistics/mental-health-statistics-stress),
[Paper 4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3968009/),
[Paper 5](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090782),
[Paper 6](https://www.researchgate.net/publication/261206963_Modeling_Stress_Using_Thermal_Facial_Patterns_A_Spatio-Temporal_Approach).
