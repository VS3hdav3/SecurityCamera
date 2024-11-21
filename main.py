import cv2
import time
import datetime


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")
scaleFactor = 1.3
frame_size = (int(cap.get(3)), int(cap.get(4))) # Gets width from cap(3) and height from cap(4)
four_cc = cv2.VideoWriter_fourcc(*"mp4v") # Format of video saved

def main():
    run = True
    recording = False
    detection_stopped_time = None
    timer_started = False
    seconds_record_after_detection = 5
    while run:
        _, frame  = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor, 5)
        bodies = body_cascade.detectMultiScale(gray, scaleFactor, 5)
        
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0))
        
        if len(faces) + len(bodies) > 0:
            if recording:
                timer_started = False
            else:
                recording = True
                curr_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"{curr_time}.mp4", four_cc, 20, frame_size)
                print("Started Recording!")
        elif recording:
            if timer_started:
                if time.time() - detection_stopped_time >= seconds_record_after_detection:
                    recording = False
                    timer_started = False
                    out.release()
                    print("Stopped Recording!")
            else:
                timer_started = True
                detection_stopped_time = time.time()
        if recording:
            out.write(frame)
        
        '''
        for (x, y, width, height) in bodies:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0))
        '''
        cv2.imshow("Camera", frame)
        
        if cv2.waitKey(1) == ord('q'):
            run = False
        
    
    out.release()
    cap.release()
    cv2.destroyAllWindows()

main()