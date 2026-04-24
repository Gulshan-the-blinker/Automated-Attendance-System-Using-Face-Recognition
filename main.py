import cv2
import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace


# -------------------------------
# Attendance Function
# -------------------------------
def mark_attendance(name):

    file = "Attendance.csv"

    # Create CSV if not present
    if not os.path.exists(file):
        df = pd.DataFrame(
            columns=["Name","Time","Date","Status"]
        )
        df.to_csv(file,index=False)

    try:
        df = pd.read_csv(file)

    except:
        df = pd.DataFrame(
            columns=["Name","Time","Date","Status"]
        )

    today = datetime.now().strftime("%d-%m-%Y")

    # Prevent duplicate attendance same day
    if not (
        (df["Name"] == name) &
        (df["Date"] == today)
    ).any():

        now = datetime.now()

        new_row = {
            "Name": name,
            "Time": now.strftime("%H:%M:%S"),
            "Date": today,
            "Status": "Present"
        }

        df.loc[len(df)] = new_row
        df.to_csv(file,index=False)

        print(f"{name} attendance marked.")

    else:
        print(f"{name} already marked today.")


# -------------------------------
# Face Database Folder
# -------------------------------
db_path = "faces"

if not os.path.exists(db_path):
    print("Create a 'faces' folder and add photos.")
    exit()


# -------------------------------
# Webcam Start
# -------------------------------
cap = cv2.VideoCapture(0)

print("\n========== Attendance System ==========")
print("Press C -> Capture Face")
print("Press Q -> Quit")
print("=======================================\n")


while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not detected.")
        break


    cv2.imshow("Face Recognition Attendance", frame)

    key = cv2.waitKey(1) & 0xFF


    # Capture Face
    if key == ord('c'):

        cv2.imwrite("capture.jpg", frame)

        try:
            print("Recognizing...")

            result = DeepFace.find(
                img_path="capture.jpg",
                db_path=db_path,
                detector_backend="opencv",
                enforce_detection=False
            )


            if len(result) > 0 and len(result[0]) > 0:

                identity = result[0]['identity'][0]

                name = os.path.basename(
                    identity
                ).split('.')[0].upper()

                print("Recognized:", name)

                mark_attendance(name)

            else:
                print("No Match Found")


        except Exception as e:
            print("Error:", e)



    # Quit
    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()