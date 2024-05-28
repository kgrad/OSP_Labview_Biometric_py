import cv2
import face_recognition
import os
import sys

def find_face_encodings():
    
    registered_users_folder = r"C:\Users\obiwa\Desktop\Studia\Sem6\OSP\GIT\OSP_Labview_Biometric_py\New-Approach\Face ID JKI SM plus Python\Data\Registered_Users"
    image_2_temp = cv2.imread(r"C:\Users\obiwa\Desktop\Studia\Sem6\OSP\GIT\OSP_Labview_Biometric_py\New-Approach\Face ID JKI SM plus Python\Data\Log_temp_storage\log.jpg")

    face_enc2 = face_recognition.face_encodings(image_2_temp)

    if not face_enc2:
        print("Nie udało się wykryć twarzy w obrazie logowania.")
        return False

    img_2_detected = face_enc2[0]

    for filename in os.listdir(registered_users_folder):
        if filename.endswith(('.bmp', '.jpg', '.jpeg', '.png')):
            file_path = os.path.join(registered_users_folder, filename)
            image_1_temp = cv2.imread(file_path)

            face_enc1 = face_recognition.face_encodings(image_1_temp)
            if not face_enc1:
                print(f"Nie udało się wykryć twarzy w obrazie: {filename}")
                continue

            img_1_detected = face_enc1[0]

            # Porównanie kodowania twarzy
            is_same = face_recognition.compare_faces([img_1_detected], img_2_detected)[0]
            print(f"Porównanie z {filename}: Is Same: {is_same}")

            if is_same:
                # Obliczenie odległości i dokładności
                distance = face_recognition.face_distance([img_1_detected], img_2_detected)
                distance = round(distance[0] * 100)
                accuracy = 100 - round(distance)
                print(f"The images are same: {filename}")
                print(f"Accuracy Level: {accuracy}%")
                return True

    print("The images are not same")
    return False

find_face_encodings()