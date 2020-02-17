from PIL import ImageTk, Image, ImageDraw


class MyImage:
    def __init__(self, path):
        self.path = path

    def open(self):
        pillow_img = Image.open(self.path)
        image = ImageTk.PhotoImage(pillow_img)

        return image
        panel.configure(image=img2)
        panel.image = img2