import cv2
import mediapipe as mp
import ctypes



# Read the image
image = cv2.imread('Arnold_Schwarzenegger_2019.jpg')
height,width,_=image.shape
print('Height ,Width',height,width)

#face mesh
ma_face = mp.solutions.face_mesh
face_mesh = ma_face.FaceMesh()



result =face_mesh.process(image)


## rgb to bgr

rgb_img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#facila landmark
result=face_mesh.process(rgb_img)






for facial_landmark in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmark.landmark[i]  # Use i here, not 0
        x = pt1.x * width
        y = pt1.y * height
        print("x, y:", x, y)
        cv2.circle(image, (int(x), int(y)), 2, (100, 100, 0), -1)
        cv2.putText(image, str(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)



















# Get screen resolution using ctypes (Windows)
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Resize the image to fit screen while maintaining aspect ratio
image_height, image_width = image.shape[:2]
aspect_ratio = image_width / image_height

# Fit the image to screen
if image_width > screen_width or image_height > screen_height:
    if aspect_ratio > screen_width / screen_height:
        new_width = screen_width
        new_height = int(screen_width / aspect_ratio)
    else:
        new_height = screen_height
        new_width = int(screen_height * aspect_ratio)
    image = cv2.resize(image, (new_width, new_height))











# Show image
cv2.imshow('IMAGE', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
