'''
Holds all the Face Data
append the data
fetch the data

'''
import os
import face_recognition
import glob

Known_Encodings = list()
Known_Names = list()
data_sent = dict()

def dataHolder():
    global Known_Encodings
    global Known_Names
    # Contains Basic data
    files = glob.glob('./Known_faces/*.jpg') #  fetch all files inside  Known_faces dir with .jpg format only
    for file in files:

        if os.path.isdir(file): # check if it is directory
            continue

        else:
            known_img = face_recognition.load_image_file(file)
            NameFormated = (file.split('/')[2]).split('.')[0] # Get the Name from file Name
            known_img_encodings = face_recognition.face_encodings(known_img)[0]
            append_data(known_img_encodings, NameFormated)


def append_data(KE, KN):
    global Known_Encodings
    global Known_Names
    Known_Encodings.append(KE)
    Known_Names.append(KN)




def fetch_Data():
    global Known_Encodings, Known_Names, data_sent

    data_sent = {
        'KnownNames' : Known_Names,
        'KnownEncodings' : Known_Encodings
    }

    return (data_sent)


dataHolder()
