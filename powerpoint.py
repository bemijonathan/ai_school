import fitz

class PowerPoint:
    def __init__(self, filepath):
        self.filepath = filepath
        pass
    # find the file path find a library to disintegrate the pdf paper into different pages and then summaris
    def disintegrate_powerpoint(self):
        print(self.filepath)

        doc = fitz.open(self.filepath)

        return doc

    def convert_to_images(self, doc):
        images = []
        for page in doc:
            pix = page.get_pixmap()
            pic_title = f"./image/{self.filepath}_{page.number}.png"
            pix.save(pic_title)
            images.append(pic_title)

        return images