# import cv2
# import os
# import numpy as np
# import tkinter as tk
# import tkinter.font as font

# def collect_data():
#     name = input("Enter name of person : ")
#     count = 1
#     ids = input("Enter ID: ")
#     cap = cv2.VideoCapture(0)
#     filename = "haarcascade_frontalface_default.xml"
#     cascade = cv2.CascadeClassifier(filename)
#     while True:
#         _, frm = cap.read()
#         gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
#         faces = cascade.detectMultiScale(gray, 1.4, 1)
#         for x,y,w,h in faces:
#             cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
#             roi = gray[y:y+h, x:x+w]
#             cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
#             count = count + 1
#             cv2.putText(frm, f"{count}", (20,20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)
#             cv2.imshow("new", roi)
#             cv2.imshow("identify", frm)
#             if cv2.waitKey(1) == 27 or count > 300:
#                 cv2.destroyAllWindows()
#                 cap.release()
#                 train()
#                 break

# def train():
#     print("training part initiated !")
#     recog = cv2.face.LBPHFaceRecognizer_create()
#     dataset = 'persons'
#     paths = [os.path.join(dataset, im) for im in os.listdir(dataset)]
#     faces = []
#     ids = []
#     labels = []
#     for path in paths:
#         labels.append(path.split('/')[-1].split('-')[0])
#         ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))
#         faces.append(cv2.imread(path, 0))
#     recog.train(faces, np.array(ids))
#     recog.save('model.yml')
#     return

# def identify():
#     cap = cv2.VideoCapture(0)
#     filename = "haarcascade_frontalface_default.xml"
#     paths = [os.path.join("persons", im) for im in os.listdir("persons")]
#     labelslist = {}
#     for path in paths:
#         labelslist[path.split('/')[-1].split('-')[2].split('.')[0]] = path.split('/')[-1].split('-')[0]
#     print(labelslist)
#     recog = cv2.face.LBPHFaceRecognizer_create()
#     recog.read('model.yml')
#     cascade = cv2.CascadeClassifier(filename)
#     while True:
#         _, frm = cap.read()
#         gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
#         faces = cascade.detectMultiScale(gray, 1.3, 2)
#         for x,y,w,h in faces:
#             cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
#             roi = gray[y:y+h, x:x+w]
#             label = recog.predict(roi)
#             if label[1] < 100:
#                 cv2.putText(frm, f"{labelslist[str(label[0])]} + {int(label[1])}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
#             else:
#                 cv2.putText(frm, "unkown", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
#         cv2.imshow("identify", frm)
#         if cv2.waitKey(1) == 27:
#             cv2.destroyAllWindows()
#             cap.release()
#             break

# def maincall():
#     root = tk.Tk()
#     label = tk.Label(root, text="Select below buttons ")
#     label.grid(row=0, columnspan=2)
#     label_font = font.Font(size=35, weight='bold', family='Helvetica') 
#     label['font'] = label_font
#     root.title("identify")
#     root.geometry("480x100")
#     btn_font = font.Font(size=25)
#     button1 = tk.Button(root, text="Add Member ", command=collect_data, height=2, width=20)
#     button1.grid(row=1, column=0, pady=(10,10), padx=(5,5))
#     button1['font'] = btn_font
#     button2 = tk.Button(root, text="Start with known ", command=identify, height=2, width=20)
#     button2.grid(row=1, column=1,pady=(10,10), padx=(5,5))
#     button2['font'] = btn_font
#     root.mainloop()
#     return

# if __name__ == "__main__":
#     maincall()



# import cv2
# import os
# import numpy as np
# import tkinter as tk
# import tkinter.font as font
# # import face_recognition

# def collect_data():
#     name = input_name.get()
#     count = 1
#     ids = input_id.get()
#     cap = cv2.VideoCapture(0)
#     filename = "haarcascade_frontalface_default.xml"
#     cascade = cv2.CascadeClassifier(filename)
#     while True:
#         _, frm = cap.read()
#         gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
#         faces = cascade.detectMultiScale(gray, 1.4, 1)
#         for x,y,w,h in faces:
#             cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
#             roi = gray[y:y+h, x:x+w]
#             cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
#             count = count + 1
#             cv2.putText(frm, f"{count}", (20,20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)
#             cv2.imshow("new", roi)
#             cv2.imshow("identify", frm)
#             if cv2.waitKey(1) == 27 or count > 300:
#                 cv2.destroyAllWindows()
#                 cap.release()
#                 train()
#                 break

# def train():
#     print("training part initiated !")
#     recog = cv2.face.LBPHFaceRecognizer_create()
#     dataset = 'persons'
#     paths = [os.path.join(dataset, im) for im in os.listdir(dataset)]
#     faces = []
#     ids = []
#     labels = []
#     for path in paths:
#         labels.append(path.split('/')[-1].split('-')[0])
#         ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))
#         faces.append(cv2.imread(path, 0))
#     recog.train(faces, np.array(ids))
#     recog.save('model.yml')
#     return

# def identify():
#     cap = cv2.VideoCapture(0)
#     filename = "haarcascade_frontalface_default.xml"
#     paths = [os.path.join("persons", im) for im in os.listdir("persons")]
#     labelslist = {}
#     for path in paths:
#         labelslist[path.split('/')[-1].split('-')[2].split('.')[0]] = path.split('/')[-1].split('-')[0]
#     print(labelslist)
#     recog = cv2.face.LBPHFaceRecognizer_create()
#     recog.read('model.yml')
#     cascade = cv2.CascadeClassifier(filename)
#     while True:
#         _, frm = cap.read()
#         gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
#         faces = cascade.detectMultiScale(gray, 1.3, 2)
#         for x,y,w,h in faces:
#             cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
#             roi = gray[y:y+h, x:x+w]
#             label = recog.predict(roi)
#             if label[1] < 100:
#                 cv2.putText(frm, f"{labelslist[str(label[0])]} + {int(label[1])}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
#             else:
#                 cv2.putText(frm, "unknown", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
#         cv2.imshow("identify", frm)
#         if cv2.waitKey(1) == 27:
#             cv2.destroyAllWindows()
#             cap.release()
#             break

# def maincall():
#     global input_name, input_id
#     root = tk.Tk()
#     label = tk.Label(root, text="Enter name and ID below:")
#     label.grid(row=0, columnspan=2)
#     label_font = font.Font(size=14, weight='bold', family='Helvetica') 
#     label['font'] = label_font
#     root.title("identify")
#     root.geometry("350x150")
#     input_name_label = tk.Label(root, text="Name:")
#     input_name_label.grid(row=1, column=0)
#     input_name = tk.Entry(root)
#     input_name.grid(row=1, column=1)
#     input_id_label = tk.Label(root, text="ID:")
#     input_id_label.grid(row=2, column=0)
#     input_id = tk.Entry(root)
#     input_id.grid(row=2, column=1)
#     btn_font = font.Font(size=12)
#     button1 = tk.Button(root, text="Add Member ", command=collect_data, height=1, width=20)
#     button1.grid(row=3, column=0, pady=(10,10), padx=(5,5))
#     button1['font'] = btn_font
#     button2 = tk.Button(root, text="Start with known ", command=identify, height=1, width=20)
#     button2.grid(row=3, column=1,pady=(10,10), padx=(5,5))
#     button2['font'] = btn_font
#     root.mainloop()
#     return

# if __name__ == "__main__":
#     maincall()

import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font

# Function to collect face data
def collect_data():
    name = input_name.get()
    ids = input_id.get()
    count = 1

    # Ensure the directory exists
    if not os.path.exists("persons"):
        os.makedirs("persons")
    
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    while True:
        ret, frm = cap.read()
        if not ret:
            continue
        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.4, 4)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = gray[y:y + h, x:x + w]
            cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
            count += 1
            cv2.putText(frm, f"{count}", (20, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            cv2.imshow("Face", roi)
        
        cv2.imshow("Frame", frm)
        
        if cv2.waitKey(1) == 27 or count > 300:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    train()

# Function to train the model
def train():
    print("Training part initiated!")
    recog = cv2.face.LBPHFaceRecognizer_create()
    dataset = 'persons'
    paths = [os.path.join(dataset, im) for im in os.listdir(dataset) if im.endswith('.jpg')]
    faces = []
    ids = []

    for path in paths:
        img = cv2.imread(path, 0)
        filename = os.path.basename(path)
        parts = filename.split('-')
        if len(parts) == 3 and parts[2].endswith('.jpg'):
            try:
                label_id = int(parts[2].split('.')[0])
                faces.append(img)
                ids.append(label_id)
            except ValueError:
                print(f"Skipping file with invalid label ID: {filename}")
        else:
            print(f"Skipping file with unexpected name format: {filename}")
    
    if len(faces) == 0:
        print("No valid training data found.")
        return

    recog.train(faces, np.array(ids))
    recog.save('model.yml')
    print("Training completed!")

# Function to identify faces
def identify():
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    recog = cv2.face.LBPHFaceRecognizer_create()
    recog.read('model.yml')
    
    paths = [os.path.join("persons", im) for im in os.listdir("persons") if im.endswith('.jpg')]
    labelslist = {int(os.path.basename(path).split('-')[2].split('.')[0]): os.path.basename(path).split('-')[0] for path in paths if len(os.path.basename(path).split('-')) == 3}

    while True:
        ret, frm = cap.read()
        if not ret:
            continue
        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = gray[y:y + h, x:x + w]
            label_id, confidence = recog.predict(roi)
            if confidence < 100:
                name = labelslist.get(label_id, "Unknown")
                cv2.putText(frm, f"{name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            else:
                cv2.putText(frm, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        cv2.imshow("Identify", frm)
        
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to create the GUI
def maincall():
    global input_name, input_id
    root = tk.Tk()
    root.title("Face Recognition")
    root.geometry("400x200")

    label_font = font.Font(size=14, weight='bold', family='Helvetica')
    input_font = font.Font(size=12)
    
    label = tk.Label(root, text="Enter name and ID below:", font=label_font)
    label.grid(row=0, columnspan=2, pady=10)
    
    input_name_label = tk.Label(root, text="Name:", font=input_font)
    input_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    input_name = tk.Entry(root, font=input_font)
    input_name.grid(row=1, column=1, padx=10, pady=5)
    
    input_id_label = tk.Label(root, text="ID:", font=input_font)
    input_id_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    input_id = tk.Entry(root, font=input_font)
    input_id.grid(row=2, column=1, padx=10, pady=5)
    
    btn_font = font.Font(size=12, weight='bold')
    button1 = tk.Button(root, text="Add Member", command=collect_data, height=2, width=20, font=btn_font)
    button1.grid(row=3, column=0, pady=10, padx=5)
    
    button2 = tk.Button(root, text="Start Recognition", command=identify, height=2, width=20, font=btn_font)
    button2.grid(row=3, column=1, pady=10, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    maincall()
