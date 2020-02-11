from PIL import ImageTk, Image, ImageDraw


class MyImage:
    def __init__(self, path):
        self.path = path

    def open(self):
        pillow_img = Image.open(self.path)
