import cv2

density = list("MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. ")
LEN = len(density)

def image_print(image, wid=30):
    #gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(image, (int(wid*2),int(wid)))
    for i in range(resized.shape[0]):
        s = ""
        for j in range(resized.shape[1]):
            b, g, r = resized[i][j]
            s += "\033[48;2;{};{};{}m ".format(r, g, b)
            #s += density[(LEN-1)-resized[i][j]//(256//LEN)]
        print(s+"\033[0m")


if __name__ == '__main__':
    img = cv2.imread("lenna.png")
    image_print(img, 30)

