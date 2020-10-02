import cv2
import numpy as np
import glob
import random
import time
import keyboard

cap = cv2.VideoCapture(0)

net = cv2.dnn.readNet("yolov3-tiny-obj_7000.weights", "yolov3-tiny-obj.cfg")


classes = ["Fist", "Palm"]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
Color_Text = (0, 255, 0)
Color_Highlight = (0, 0, 255)
left_color, right_color, forward_color, backward_color = Color_Text, Color_Text, Color_Text, Color_Text
isFist = False
flag = 0
while True:
    start = time.time()
    ret, imgg = cap.read()
    img = imgg
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)

    height, width, channels = img.shape


    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)


    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:

                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)


                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    where = "Nowhere"
    for i in range(1): #len(boxes)
        left_color, right_color, forward_color, backward_color = Color_Text, Color_Text, Color_Text, Color_Text
        isFist = False

        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            point =  (x + int(w/2), y + int(h/2))
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 2)
            cv2.circle(img, point, 3, (255, 255, 255), -1)
            p_x = x + int(w/2)
            p_y = y + int(h/2)
            if label == "Fist":
                flag = 1
                isFist = True
            if(155 <= p_x <= 450 and 68 <= p_y <= 181):
                where = "Forward"
            elif(155 <= p_x <= 450 and 312 <= p_y <= 417):
                where = "Backward"
            elif(12 <= p_x <= 220 and 186 <= p_y <= 307):
                where = "Left"
            elif(390 <= p_x <= 625 and 186 <= p_y <= 307):
                where = "Right"
            if flag == 1 and isFist == False:
                flag = 2


    if not isFist:
        if flag == 2:
            keyboard.press_and_release("u")
            flag = 0
        elif(where == "Forward"):
            forward_color = Color_Highlight
            keyboard.press_and_release('w')
        elif(where == "Backward"):
            backward_color = Color_Highlight
            keyboard.press_and_release('s')
        elif(where == "Left"):
            left_color = Color_Highlight
            keyboard.press_and_release('a')
        elif(where == "Right"):
            right_color = Color_Highlight
            keyboard.press_and_release('d')

    # img = cv2.resize(img, (840, 640))
    forward_start = (155, 68)
    forward_end = (450, 181)
    cv2.rectangle(img, forward_start, forward_end, forward_color, 2)

    backward_start = (155, 312)
    backward_end = (450, 417)
    cv2.rectangle(img, backward_start, backward_end, backward_color, 2)

    left_start = (12, 186)
    left_end = (220, 307)
    cv2.rectangle(img, left_start, left_end, left_color, 2)

    right_start = (390, 186)
    right_end = (625, 307)
    cv2.rectangle(img, right_start, right_end, right_color, 2)
    img = cv2.flip(img, 1)
    cv2.imshow("Image", img)
    print(f"Time = {time.time() - start} seconds")
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
