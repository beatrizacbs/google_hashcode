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


file_name = "c_memorable_moments.txt"



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


def create_relationVertical():
    for v in range(0, len(pictures), 1):
        greaterintersection = 0
        currentIntersec = 0
        block = 1
        currentId = 0

        if (len(pictures) == 0 and block > 1):
            break

        for v2 in range(0, len(pictures), 1):
            if v != v2:
                p1 = set(pictures[v].tags)
                p2 = set(pictures[v2].tags)
                currentIntersec = len(p1.intersection(p2))
                if currentIntersec > greaterintersection:
                    currentId = v2
                    greaterintersection = currentIntersec

        picRelation = [pictures[v], pictures[v2]]
        slideRelation = Slide(picRelation, p1.union(p2))
        slides.append(slideRelation)
        pictures.remove(pictures[v2])
        v = v-1
        pictures.remove(pictures[v])
        # block += 1
        # if(len(pictures) == 0 and block > 1):
        #     break



def create_slides():
    for i in range(0, len(pictures), 2):
        if i+1 < len(pictures):
            pic1 = pictures[i]
            pic2 = pictures[i+1]
            picture = [pic1, pic2]
            slide = Slide(picture, pic1.group.union(pic2.group))
            slides.append(slide)


def calculate_min(slide1, slide2):
    if slide1 is not None and slide2 is not None:
        slide1 = slide1.tags
        slide2 = slide2.tags
        intersec = len(slide1.intersection(slide2))
        sld1sld2 = len(slide1.difference(slide2))
        sld2sld1 = len(slide2.difference(slide1))
        value_min = min(intersec, sld1sld2, sld2sld1)
        return value_min
    else:
        return 0


list_final = []


def calculate_relation():
    max_min = 0
    index_max_min = -1
    list_final.append(slides[0])
    del slides[0];
    while len(slides) != 0:
        for sld in list(slides):
            min = calculate_min(sld, list_final[-1])
            if min > max_min:
                max_min = min
                index_max_min = sld
        print("Length: "+ str(len(slides)))
        print(index_max_min)
        slides.remove(sld)
        list_final.append(sld)


def write_file():
    output_name = "output_"+file_name
    file = open(output_name, "w")
    file.writelines(str(len(list_final))+"\n")
    for i in list_final:
        if i is not None:
            line = ""
            for p in i.pictures:
                line += str(p.id) + " "
            file.writelines(line+"\n")
    file.close()


read_file()
create_relationVertical()
calculate_relation()
print(len(list_final))
write_file()
