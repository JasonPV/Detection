import cv2
import numpy as np
from matplotlib import pyplot as plt


def template_matching(path1, path2):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img_rgb = cv2.imread(path1)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(path2, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # cv2.imwrite('res.png', img_rgb)
    return img_rgb
    # cv2.imshow("Matched image", img_rgb)
    # while True:
    #     k = cv2.waitKey(0) & 0xFF
    #     if k == 27:
    #         cv2.destroyAllWindows()
    #         break


if __name__ == '__main__':
    path1 = 'image_with_cats.png'
    path2 = 'template.png'
    template_matching(path1, path2)