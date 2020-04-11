'''
locate the faces in the image
count the number of faces in the image

'''

import face_recognition

image = face_recognition.load_image_file('./Unknown_faces/group/Messi-Ronaldo.jpg')

faceLocation = face_recognition.face_locations(image)

print(f'There are {len(faceLocation)} peoples in the Image') # get the number of people in the image

for face in faceLocation:
    un_encode = face_recognition.face_encodings(face)
    kn_img = face_recognition.load_image_file('./Known_faces/Messi.jpg')
    kn_encode = face_recognition.face_encodings(kn_img)
    match = face_recognition.compare_faces([kn_encode], un_encode)
    print(match)
    if match == '[True]':
        print('match Found')
    else:
        print('match not found')

