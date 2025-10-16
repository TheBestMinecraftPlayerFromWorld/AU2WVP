import serial
import serial.tools
import serial.tools.list_ports
import time
import cv2

sPort = ""
with open("comPort.txt") as f:
    sPort = f.read()

ser = None
ser = serial.Serial(sPort,115200)
cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
running=True
while running:
    code = ""
    completed = True
    try:
        line = ser.readline().decode("ascii").strip()
    except: continue
    s = line.split(";")
    try:
        s.remove("")
    except:
        pass
    if len(s) != 6: continue
    if s[0] == "1": code = "A"
    elif s[1] == "1": code = "B"
    elif s[2] == "1": code = "C"
    else: 
        completed=False
    if s[3] == "1": code += "1"
    elif s[4] == "1": code += "2"
    elif s[5] == "1": code += "3"
    else: 
        completed=False
    if not completed: continue
    #if code=="A1":
    #    running=False
    #    break
    print(code)
    cap = cv2.VideoCapture(f'videos/{code}.mp4')

    if (cap.isOpened()== False):
        print("Error opening video file")

    # Read until video is completed
    while(cap.isOpened()):
        
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            if False and ser.inWaiting() > 0:
                print("H")
            
                char = ser.readline().decode("ascii").strip().split(";")
                print(char)
                countsOf1 = 0
                for a in char: 
                    if a == "1":
                        countsOf1+=1
                if countsOf1>1: break
                

    # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    ser.read_all()
