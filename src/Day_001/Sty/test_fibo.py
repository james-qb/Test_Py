import math
import operator
from functools import reduce

import cv2
import numpy
from PIL import Image
from PIL import ImageChops
from skimage.metrics import structural_similarity as ssim


def fibo(n):
    a, b = 0, 1
    i, result = 0, []
    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


def calculate(image1, image2):
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def classify_hist_with_split(image1, image2, size=(256, 256)):
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))


def compare(pic1, pic2):
    """
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    """
    try:
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
    except (FileNotFoundError, IOError) as e:
        print(e)
    else:
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        print(differ)
        return differ


compare(r'D:\360Downloads\IMG_0020.JPG', r'D:\360Downloads\IMG_0023.JPG')
compare_images(r'D:\360Downloads\IMG_0020.JPG', r'D:\360Downloads\IMG_0023.JPG', r'D:\360Downloads\IMG_0026.JPG')
# fibo(6)
# ll = 'jjjjjj'
# print(ll.__contains__('jj'))
# d = u.connect_usb()
# d.wait_activity
# d(text='卡包').click()
# d.window_size()
image_a = cv2.imread(r'D:\360Downloads\IMG_0020.JPG')
image_b = cv2.imread(r'D:\360Downloads\IMG_0023.JPG')
gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)
(score, diff) = ssim(gray_a, gray_b, full=True)
print(f"SSIM: {score}")
ll = classify_hist_with_split(r'D:\360Downloads\IMG_0020.JPG', r'D:\360Downloads\IMG_0023.JPG')
print(ll)
# print(calculate(r'D:\360Downloads\IMG_0020.JPG', r'D:\360Downloads\IMG_0023.JPG'))
