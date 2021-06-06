def equation(xy1, xy2):
    x1 = int(xy1.split(";")[0])
    y1 = int(xy1.split(";")[1])
    x2 = int(xy2.split(";")[0])
    y2 = int(xy2.split(";")[1])
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(k, b)
equation("0;0", "1;1")