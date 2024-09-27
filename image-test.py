
import cv2
import numpy as np
import pickle
import face_recognition
import csv

global known_face_encodings, known_face_metadata

def register_new_face(face_encoding, face_image, identifiers):
    """
    Add a new person to our list of known faces
    """
    # Add the face encoding to the list of known faces
    known_face_encodings.append(face_encoding)
    # Add a matching dictionary entry to our metadata list.
    # We can use this to keep track of how many times a person has visited, when we last saw them, etc.
    known_face_metadata.append({
        "face_id": identifiers[0],
        "Last": identifiers[1],
        "First": identifiers[2],
        "face_image": face_image
    })
    

known_face_encodings = []
known_face_metadata = []

classRegFile = "./data/class_reg_info.csv"
with open(classRegFile, "r") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	output = list(map(tuple,reader))

for metadata in output:
	identifiers = metadata[:-1]
	imFile = "./data/images/"+metadata[3]

	image = face_recognition.load_image_file(imFile)
	if image is None:
		break

	face_locations = face_recognition.face_locations(image)
	face_encodings = face_recognition.face_encodings(image, face_locations)

	small_frame = cv2.resize(image, (0,0), fx=0.5, fy=0.5)

	face_encoding = face_encodings[0]
	face_location = face_locations[0]

	top, right, bottom, left = face_location
	face_image = small_frame[top:bottom, left:right]
	face_image = cv2.resize(face_image, (150,150))

	register_new_face(face_encoding, face_image, identifiers)
	print(identifiers)
 
    
    