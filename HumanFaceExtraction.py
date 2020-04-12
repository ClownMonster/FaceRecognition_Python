'''
 Extract Only Human faces from the image and Display Them in PIL format
 using Convolution Neural Network model

'''
from face_recognition_models import cnn_face_detector_model_location
import face_recognition
from PIL import Image
import  time

time_count =  time.time()

img = face_recognition.load_image_file('./Images/img1.jpg')

FaceLocations = face_recognition.face_locations(img, model = cnn_face_detector_model_location)
print(f'There are(is) : {len(FaceLocations)} Human Face(s) in the image ')

# looping through the faces in the image
for FaceLocation in FaceLocations:
    top, right, bottom, left = FaceLocation
    face_img  = img[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.show()

time_count_end = time.time()

print(f'Final time is {time_count_end - time_count}')





