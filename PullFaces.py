'''
Extract Every  face form the photo(group)
and display it one by one

'''
from  PIL import Image
import face_recognition

import FindFaces


def pullfaces(imagelocation):

    FaceLocations = FindFaces.findfaces(imagelocation) # get the face locations
    image  = face_recognition.load_image_file(imagelocation)

    # looping through face locations
    for FaceLocation in FaceLocations:
        top, right, bottom, left = FaceLocation
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image) # Extracts the faces
        pil_image.show() # renders the faces in default image viewer





#pullfaces('./Unknown_faces/group/neymar-group.jpg')

