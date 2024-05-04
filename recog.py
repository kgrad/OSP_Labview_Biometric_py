import cv2
import face_recognition

def find_face_encodings(image_path):
    image = cv2.imread(image_path)
    face_enc = face_recognition.face_encodings(image)
    return face_enc[0]

image_1 = find_face_encodings("C:\\Users\\jakub\\Desktop\\Face ID JKI SM plus Python\\Data\\Jakub\\jakub1.jpg")
image_2 = find_face_encodings("C:\\Users\\jakub\\Desktop\\Face ID JKI SM plus Python\\Data\\Jakub\\jakub1.jpg")

is_same = face_recognition.compare_faces([image_1], image_2)[0]
print(f"Is Same: {is_same}")

if is_same:
    distance = face_recognition.face_distance([image_1], image_2)
    distance = round(distance[0] * 100)
    accuracy = 100 - round(distance)
    print("The images are same")
    print(f"Accuracy Level: {accuracy}%")
else:
    print("The images are not same")
