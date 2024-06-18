import cv2
def canny_edge_tection(frame): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BIG2GRAY)
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5)
    edges = cv2.Canny(blurred, 70, 135)
    return blurred, edges
def main():
    #open default webcam
    cap = cv2.VideoCapture(0)

while True:
    #read a fram efrom the webcam
    ret, frame = cap.read