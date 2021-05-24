from PIL import Image

def resizeimage(path):

    if '.png' in str(path):
        image = Image.open(path)
        size = image.size
        correct_sizes = [48, 48]
        #
        # if correct_sizes == size:
        #     return -1


        image = image.resize((48, 48), Image.ANTIALIAS)
        image.save(fp=path)
