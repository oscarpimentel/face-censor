from __future__ import annotations

import math
import random
from typing import List

import cv2
from yolov8face import get_bbox


def get_bboxes(path) -> List[dict]:
    bboxes = []
    results = get_bbox(path)
    for bbox, score in zip(results.xyxy, results.conf):
        bboxes.append({
            'xyxy': bbox.numpy().tolist(),
            'score': score.item(),
        })
    return bboxes


def random_point_in_circle(cx, cy, r):
    angle = random.uniform(0, 2 * math.pi)
    distance = math.sqrt(random.uniform(0, r ** 2))
    x = cx + distance * math.cos(angle)
    y = cy + distance * math.sin(angle)
    return x, y


class Line:
    @staticmethod
    def get_lines(cx: int, cy: int, r: int, n: int) -> List[Line]:
        """
        Get n random lines that lies inside a circle of center (cx, cy) and radious r. The extremes of the lines are consecutive.
        """
        lines = []
        x1, y1 = random_point_in_circle(cx, cy, r)

        for _ in range(n):
            x2, y2 = random_point_in_circle(cx, cy, r)
            lines.append(Line(x1, y1, x2, y2))
            x1, y1 = x2, y2

        return lines

    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)


class Face:
    def __init__(self, bbox) -> None:
        self.bbox = bbox

    def get_center(self):
        cx = int((self.bbox['xyxy'][0] + self.bbox['xyxy'][2]) / 2)
        cy = int((self.bbox['xyxy'][1] + self.bbox['xyxy'][3]) / 2)
        return cx, cy

    def get_width(self):
        width = int(abs(self.bbox['xyxy'][0] - self.bbox['xyxy'][2]))
        return width

    def draw_lines(self, image,
                   thickness = 1,
                   ns = [50, 100],
                   color = (255, 255, 255),
                   ):
        radius = int(self.get_width() * 0.9)
        cx, cy = self.get_center()
        lines = Line.get_lines(cx, cy, radius, random.randint(ns[0], ns[1]))
        for line in lines:
            image = cv2.line(image, (line.x1, line.y1), (line.x2, line.y2), color, thickness)
        if 0:
            image = cv2.circle(image, (cx, cy), radius, color, thickness)
        return image
