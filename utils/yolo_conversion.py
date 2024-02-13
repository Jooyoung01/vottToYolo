def convert_to_yolo(size, box):
    dw = 1. / size['width']
    dh = 1. / size['height']
    x = (box['x'] + box['w'] / 2.0) * dw
    y = (box['y'] + box['h'] / 2.0) * dh
    w = box['w'] * dw
    h = box['h'] * dh
    return x, y, w, h