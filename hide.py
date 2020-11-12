from PIL import Image
from sys import argv


def reveal(img):
    img = img.convert("RGBA")#.copy()
    dat = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r,g,b,a = dat[x,y]
            dat[x,y] = r,g,b,0
            
    return img

if __name__=="__main__":
    PLAIN = argv[1] if len(argv)>1 else "tst/plain_secret.png"
    CIPHER = argv[2] if len(argv)>2 else PLAIN[:PLAIN.rfind(".")]+".cipher.png"
    reveal(Image.open(PLAIN)).save(CIPHER)

