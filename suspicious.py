import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = None

# Debugging: Check unconnected layers
unconnected_layers = net.getUnconnectedOutLayers()
print("Unconnected Layers:", unconnected_layers)

# Check if unconnected_layers has any elements
if len(unconnected_layers) > 0:
    # Use the first layer in unconnected_layers
    output_layers = [layer_names[i - 1] for i in unconnected_layers.flatten()]
else:
    # If unconnected_layers is empty, try alternative method
    # Alternative method: Get the last layers of the network
    output_layers = [layer_names[i[0]] for i in net.getUnconnectedOutLayers()]

# Load camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break  # Break the loop if frame is None
    
    height, width, channels = frame.shape

    # Detect objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Process detections
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                label = classes[class_id]
                if label == "knife" or label == "gun":
                    # Draw bounding box around the object
                    x, y, w, h = detection[:4] * np.array([width, height, width, height])
                    x, y, w, h = int(x), int(y), int(w), int(h)  # Convert to integers
                    
                    # Ensure coordinates are within bounds
                    x = max(0, x)
                    y = max(0, y)
                    w = min(width - x, w)
                    h = min(height - y, h)
                    
                    # Check if coordinates are valid
                    if w > 0 and h > 0:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
