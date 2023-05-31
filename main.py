import math
def convert_rads_to_degrees(rad):
    degree = (180 / math.pi) * rad
    return degree

def return_area(l, h):
    area = (l * h)
    return area

def calculate_avsqrt(list):
    summ = 0
    for number in list:
        summ = summ + number
    av = summ / len(list)
    summsqrt = 0
    for number in list:
        summsqrt = summsqrt + math.pow(number - av, 2)
    avgsqrt = math.sqrt(summsqrt)
    return avgsqrt
#math.sqrt((x1 - xaver)^2 + (x2 - xaver)^2 + ... + (xn - aver)^2)
#math.sqrt
#math.pow(x, 2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 123, 123, 11, 22, 22, 33, 44]
    print(calculate_avsqrt(X))


