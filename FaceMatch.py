'''

Compare Images for faces and find the match


'''


import face_recognition
import os
import glob # import to read the files from directory

from EncodingsNames import append_data

def facematch(unknown_img_location):
    unknown_img = face_recognition.load_image_file(unknown_img_location)
    unknown_img_encodings = face_recognition.face_encodings(unknown_img)[0]
    files = glob.glob('./Known_faces/*.jpg') #  fetch all files inside  Known_faces dir with .jpg format only
    for file in files:

        if os.path.isdir(file): # check if it is directory
            continue

        else:
            known_img = face_recognition.load_image_file(file)
            NameFormated = (file.split('/')[2]).split('.')[0] # Get the Name from file Name
            known_img_encodings = face_recognition.face_encodings(known_img)[0]
            append_data(known_img_encodings, NameFormated)
            match = face_recognition.compare_faces([known_img_encodings], unknown_img_encodings)

        if match == [True]:
            print(f'Your uploaded Image is matched with {file}')
        else:
            continue

    # if no match found
    if not match[0]:
        print('No Match Found')




facematch('./Unknown_faces/img4.jpg')