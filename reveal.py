from PIL import Image
from sys import argv


def reveal(img):
    img = img.convert("RGBA")#.copy()
    dat = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r,g,b,a = dat[x,y]
            dat[x,y] = r,g,b,255
            
    return img

if __name__=="__main__":
    CIPHER = argv[1] if len(argv)>1 else "tst/plain_secret.cipher.png"
    PLAIN = argv[2] if len(argv)>2 else CIPHER[:CIPHER.rfind(".")]+".plain.png"
    reveal(Image.open(CIPHER)).save(PLAIN)

