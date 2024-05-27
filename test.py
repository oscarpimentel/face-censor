import cv2

from utils import get_bboxes, Face

path = '/home/oscar/repos/face-detector/gettyimages-200244581-003-612x612.jpg'
radius = 20
thickness = 2
color = (255, 0, 0)

image = cv2.imread(path)
bboxes = get_bboxes(path)
for bbox in bboxes:
    face = Face(bbox)
    image = face.draw_lines(image)
cv2.imwrite('out.jpg', image)
