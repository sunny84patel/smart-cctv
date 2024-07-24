# import cv2
# from spot_diff import spot_diff
# import time
# import numpy as np

# def find_motion():
#     motion_detected = False
#     is_start_done = False
#     cap = cv2.VideoCapture(0)
#     check = []
#     print("waiting for 2 seconds")
#     time.sleep(2)
#     _, frame1 = cap.read()
#     _, frm1 = cap.read()
#     frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)
    
#     while True:
#         _, frm2 = cap.read()
#         frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)
        
#         diff = cv2.absdiff(frm1, frm2)
#         _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
#         contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
#         is_start_done = False
#         motion_detected = False
        
#         # Filter contours
#         contors = [c for c in contors if cv2.contourArea(c) > 25]
        
#         if len(contors) > 5:
#             cv2.putText(thresh, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
#             motion_detected = True
#             is_start_done = False
#         elif motion_detected and len(contors) < 3:
#             if (is_start_done) == False:
#                 start = time.time()
#                 is_start_done = True
            
#             end = time.time()
#             print(end - start)
            
#             if (end - start) > 4:
#                 frame2 = cap.read()
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 x = spot_diff(frame1, frame2)
#                 if x == 0:
#                     print("running again")
#                     return
#                 else:
#                     print("found motion")
#                     return
#         else:
#             cv2.putText(thresh, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        
#         cv2.imshow("winname", thresh)
#         _, frm1 = cap.read()
#         frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)
        
#         if cv2.waitKey(1) == 27:
#             break
#     return


import cv2

def noise():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        
        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.blur(diff, (5,5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            max_cnt = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)
        
        cv2.imshow("Press Esc to exit", frame1)
        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break