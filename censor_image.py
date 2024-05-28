import cv2

from utils import detected_and_draw_faces


filepath = 'data/gettyimages-200244581-003-612x612.jpg'
radius = 20
thickness = 2
color = (255, 0, 0)

image = cv2.imread(filepath)
image = detected_and_draw_faces(image)
cv2.imwrite('save/out.jpg', image)
