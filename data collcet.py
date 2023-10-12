import cv2
import os

# Initialize the webcam (0 denotes the default camera)
video = cv2.VideoCapture(0)

# Load the Haar Cascade Classifier for face detection
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Counter for the number of photos collected
photo_counter = 0

# Specify the folder where you want to save the images
output_folder = 'image_data/bappy/'

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the video frame
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    for x, y, w, h in faces:
        # Draw a rectangle around each detected face
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

        # Save the face as an image
        face_image = gray[y:y + h, x:x + w]
        image_path = os.path.join(output_folder, f'face_{photo_counter}.jpg')
        cv2.imwrite(image_path, face_image)
        # cv2.imwrite(f'face_{photo_counter}.jpg', face_image)
        photo_counter += 1

        if photo_counter >= 20:
            break

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q') or photo_counter >= 20:
        break

video.release()
cv2.destroyAllWindows()