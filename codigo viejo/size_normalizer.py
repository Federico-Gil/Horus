from PIL import Image

def normalize_size(img_name,size):
    filename = img_name
    img = Image.open(filename)
    wpercent = (size / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((size, hsize), Image.ANTIALIAS)
    img.save(filename)
