import numpy as np
import cv2
import matplotlib.pyplot as plt
import csv

header = ["k","x_values","y_values"]
header_g = ["m","x_values","y_values"]
header_b = ["n","x_values","y_values","angle"]

k = 0
m = 0
n = 0

with open('test.csv', 'w', encoding='UTF8', newline='') as f:
    csv_writer = csv.DictWriter(f,fieldnames=header)
    csv_writer.writeheader()
with open('test_g.csv', 'w', encoding='UTF8', newline='') as g:
    csv_writer_g = csv.DictWriter(g,fieldnames=header_g)
    csv_writer_g.writeheader()

with open('test_b.csv', 'w', encoding='UTF8', newline='') as b:
    csv_writer_b = csv.DictWriter(b,fieldnames=header_b)
    csv_writer_b.writeheader()

    # write the header




#using video from file
webcam = cv2.VideoCapture("input.mp4")
while True:
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    timer = cv2.getTickCount()
    print(timer)
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for red color and
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for green color and
    # define mask
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask = red_mask)

    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = blue_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)



    # Reading the video from the
    # webcam in image frames
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 0, 255), 2)

            cv2.putText(imageFrame, "Red Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))
            print(x,y)
            k+=1

            with open('test.csv', 'a') as f:
                csv_writer = csv.DictWriter(f,fieldnames=header)
                #csv_writer.writeheader()
                info = {
                "k":k,
                "x_values": x,
                "y_values": y

                }

                csv_writer.writerow(info)






    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x_g, y_g, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x_g, y_g),
                                       (x_g + w, y_g + h),
                                       (0, 255, 0), 2)

            cv2.putText(imageFrame, "Green Colour", (x_g, y_g),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

            m += 1

            with open('test_g.csv', 'a') as g:
                csv_writer_g = csv.DictWriter(g,fieldnames=header_g)
                #csv_writer.writeheader()
                info_g = {
                "m":m,
                "x_values": x_g,
                "y_values": y_g
                }

                csv_writer_g.writerow(info_g)

    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x_b, y_b, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x_b, y_b),
                                       (x_b + w, y_b + h),
                                       (255, 0, 0), 2)

            cv2.putText(imageFrame, "Blue Colour", (x_b, y_b),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

            n += 1

            with open('test_b.csv', 'a') as b:
                csv_writer_b = csv.DictWriter(b,fieldnames=header_b)
                #csv_writer.writeheader()
                info_b = {
                "n":n,
                "x_values": x_b,
                "y_values": y_b,
                
                }

                csv_writer_b.writerow(info_b)





    # Program Termination
    cv2.putText(imageFrame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    cv2.imshow("Pendulum tracker", imageFrame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()

        break
