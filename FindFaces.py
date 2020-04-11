'''
locate the faces in the image
count the number of faces in the image
Get the exact facelocations

'''

import face_recognition

def findfaces(imagelocation):
    image = face_recognition.load_image_file(imagelocation)
    FaceLocations = face_recognition.face_locations(image)
    print(f'There are {len(FaceLocations)} peoples in the Image') # get the number of people in the image
    return FaceLocations

