class Picture:

    def __init__(self, id, orientation, quantTag, tags, group):
        self.id = id
        self.orientation = orientation
        self.quantTag = quantTag
        self.tags = tags
        self.group = group

    def __str__(self):
        return "Orientation: " + self.orientation + \
               "\nQuantidade de Tags: " + self.quantTag + \
               "\nTags: " + ''.join(self.tags)


class Slide:

    def __init__(self, pics, tags):
        self.pictures = pics
        self.tags = tags


pictures = []
slides = []

file_name = "e_shiny_selfies.txt"


def read_file():
    i = 0
    with open(file_name) as infile:
        next(infile)

        for line in infile:
            line_split = line.split()
            orientation = line_split[0]
            quantity_tags = line_split[1]
            tags = line_split[2:]
            group = set(tags)

            pic = Picture(i, orientation, quantity_tags, tags, group)

            i += 1
            if pic.orientation == 'H':
                pic_a = [pic]
                slide = Slide(pic_a, set(pic.tags))
                slides.append(slide)
            else:
                pictures.append(pic)


def create_slides():
    for i in range(0, len(pictures), 2):
        if i+1 < len(pictures):
            pic1 = pictures[i]
            pic2 = pictures[i+1]
            picture = [pic1, pic2]
            slide = Slide(picture, pic1.group.union(pic2.group))
            slides.append(slide)


def create_relation():
    for i in range(0, len(slides), 2):
        if i + 1 < len(slides):
            slide1 = slides[i].tags
            slide2 = slides[i+1].tags
            intersec = len(slide1.intersection(slide2))
            sld1sld2 = len(slide1.difference(slide2))
            sld2sld1 = len(slide2.difference(slide1))
            value_min = min(intersec, sld1sld2, sld2sld1)


def write_file():
    output_name = "output_"+file_name
    file = open(output_name, "w")
    file.writelines(str(len(slides))+"\n")
    for i in slides:
        line = ""
        for p in i.pictures:
            line += str(p.id) + " "
        file.writelines(line+"\n")
    file.close()


read_file()
create_slides()
create_relation()
write_file()
