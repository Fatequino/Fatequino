
import cv2
import dlib

video_capture = cv2.VideoCapture('http://192.168.0.106:4747/video')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Change Resolution
detector = dlib.get_frontal_face_detector() #Face detector
#Landmark identifier. Set the filename to whatever you named the downloaded file
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 


while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,180) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)

    detections = detector(clahe_image, 1) #Detect the faces in the image

    for k,d in enumerate(detections): #For each detected face  
        shape = predictor(clahe_image, d) #Get coordinates
        for i in range(1,68): #There are 68 landmark points on each face
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,255,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame
            #cv2.putText(frame, str(i), (shape.part(i).x,shape.part(i).y),
            #        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            #        fontScale=0.3,
            #        color=(0, 0, 255))
    cv2.imshow("image", frame) #Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'): #Exit program when the user presses 'q'
        break
    
cv2.destroyAllWindows()