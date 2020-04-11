'''
    Identify the Faces in the image and draw box around their face with their names
    and unknown face is done with unknown name


'''

import face_recognition
from PIL import Image, ImageDraw


from EncodingsNames import  fetch_Data
from FindFaces import findfaces

data_Fetched = fetch_Data()

image_location = './Unknown_faces/group/Messi-Neymar2.jpg'

test_img = face_recognition.load_image_file(image_location)

# find faces in test image
test_img_locations = findfaces(image_location)
test_img_encodings =  face_recognition.face_encodings(test_img, test_img_locations)

# convert to PIL format
pil_img = Image.fromarray(test_img)

# Creating Image Drawer Instance
draw = ImageDraw.Draw(pil_img)


for (top, right, bottom, left), test_img_encoding in zip(test_img_locations, test_img_encodings):
    matches = face_recognition.compare_faces(data_Fetched['KnownEncodings'], test_img_encoding)
    name = "Unknown Person"
    if True in matches:
        first_match_index = matches.index(True)
        name = data_Fetched['KnownNames'][first_match_index]

    # Draw box arround the face
    draw.rectangle(( (left, top ), (right, bottom) ), outline = (0,0,0))

    # Draw Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(( (left, bottom - text_height-4 ), (right, bottom)  ),
                    fill= (0,0,0,), outline= (0,0,0))

    draw.text((left +6 , bottom - text_height - 5), name, fill= (255,255,255,255))

del draw # deleting the Draw Instance

pil_img.show()

