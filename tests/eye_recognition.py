import cv2

# Load the Haar cascade file for detecting eyes
eye_cascade = cv2.CascadeClassifier(r"C:\Users\filip\Documents\python\AI\tests\haarcascade_eye.xml")

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    _, img = cap.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the image
    eyes = eye_cascade.detectMultiScale(gray)

    # Draw a rectangle around the eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the video frame
    cv2.imshow('Video', img)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object
cap.release()
