from ultralytics import YOLO

# Model
model = YOLO('yolov5n.pt')  # load an official model
# Predict with the model
results = model('./test/automatic1111/night_stand/2023-10-31/00000-1337.png')  # predict on an image

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    
    
    print(boxes)
