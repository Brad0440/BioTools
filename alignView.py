import numpy as np
import matplotlib.pyplot as plot
import matplotlib.colors as colors

def add_annotation(start, end, length, colour, comment):
    ann = []

    #orangered 5
    #deeppink 6
    #aqua 7
    #slategrey 8
    #lime 9
    #navy 10
    #teal 11
    #black 12
    #indigo 13

    if colour == "orangered":
        colourn = 5
    elif colour == "deeppink":
        colourn = 6
    elif colour == "aqua":
        colourn = 7
    elif colour == "slategray" or colour == "slategrey":
        colourn = 8
    elif colour == "lime":
        colourn = 9
    elif colour == "navy":
        colourn = 10
    elif colour == "teal":
        colourn = 11
    elif colour == "black":
        colourn = 12
    elif colour == "indigo":
        colourn = 13
    else:
        raise TypeError("Invalid colour, please choose from 'orangered', 'deeppink', 'aqua', 'slategrey', 'lime', 'navy', 'teal', 'black', or 'indigo'.")

    for i in range(0, start):
        ann.append(2)

    for j in range(start, end):
        ann.append(colourn)

    for k in range(end, length):
        ann.append(2)

    print("Annotation (" + colour + "): " + comment)

    return(ann)




def show_align(alignment, annotations = False):

    file = open(alignment)
    print('\n')
    line = 0
    names_pos = []
    for i in file:
        if i[0] == ">":
            print(i)
            names_pos.append(line)
        line = line + 1

    file.close()
    file = open(alignment)

    count = -1
    seq = []
    for x in file:
        count = count + 1
        #print(count)
        if count > names_pos[0] and count < names_pos[1]:
            seq.append(x)

    file.close()
    file = open(alignment)

    count = -1
    read1 = []
    for x in file:
        count = count + 1
        #print(count)
        if count > names_pos[1] and count < names_pos[2]:
            read1.append(x)

    file.close()
    file = open(alignment)

    count = -1
    read2 = []
    for x in file:
        count = count + 1
        #print(count)
        if count > names_pos[2]:
            read2.append(x)


    file.close()

    outpos = 0
    for y in seq:
        pos = 0
        for w in y:
            if w == '\n':
                seq[outpos] = seq[outpos][0:len(seq[outpos])-1]
            pos = pos + 1
        outpos = outpos + 1

    seq_str = ''

    outpos = 0
    for y in read1:
        pos = 0
        for w in y:
            if w == '\n':
                read1[outpos] = read1[outpos][0:len(read1[outpos])-1]
            pos = pos + 1
        outpos = outpos + 1

    read1_str = ''

    outpos = 0
    for y in read2:
        pos = 0
        for w in y:
            if w == '\n':
                read2[outpos] = read2[outpos][0:len(read2[outpos])-1]
            pos = pos + 1
        outpos = outpos + 1

    read2_str = ''

    for n in seq:
        seq_str = seq_str + n

    for n in read1:
        read1_str = read1_str + n

    read1_str = read1_str.lower()

    for n in read2:
        read2_str = read2_str + n

    read2_str = read2_str.lower()

    #print(seq_str)

    template = []

    align1 = []

    align2 = []


    for a in seq_str:
        template.append(a)

    for a in read1_str:
        align1.append(a)

    for a in read2_str:
        align2.append(a)

    template_n = []
    for t in template:
        if t == 'a':
            template_n.append(3)
        elif t == 'c':
            template_n.append(4)
        elif t == 'g':
            template_n.append(4)
        elif t == 't':
            template_n.append(3)
        elif t == '-':
            template_n.append(2)
        else:
            print("ERROR: " + t)
            break

    align1_n = []
    count = 0
    for t in align1:
        if t == '-':
            align1_n.append(2)
        elif t == template[count]:
            align1_n.append(1)
        else:
            align1_n.append(0)
            #print(t + '---' + template[count])
        count = count + 1

#print(align1_n)

    align2_n = []
    count = 0
    for t in align2:
        if t == '-':
            align2_n.append(2)
        elif t == template[count]:
            align2_n.append(1)
        else:
            align2_n.append(0)
            #print(t + '---' + template[count])
        count = count + 1

        #print(template_n)


    template_show = []

    ref = []
    for i in range(0,len(template_n)-1):
        ref.append(0)

    ref.append(13)

    space = []

    for i in range(0,len(template_n)):
        space.append(2)


    for i in range (0,50):
        template_show.append(space)

    height = [0]

    if annotations != False:
        labels = []
        for i in range(0,80):
            template_show.append(space)
        for ann in annotations:
            start = ann[0]
            end = ann[1]
            comment = ann[2]
            colour = ann[3]
            length = len(template_n)
            labels.append(add_annotation(start, end, length, colour, comment))
        c = 0
        for l in labels:
            for i in range(0,80):
                template_show.append(space)
            for i in range(0,80):
                template_show.append(l)
            for i in range(0,80):
                template_show.append(space)
            height.append(height[len(height)-1]+200)
            plot.text(annotations[c][0] + 40, height[c+1], annotations[c][2])
            c = c + 1

    for i in range (0,30):
        template_show.append(space)

    for i in range (0,1):
        template_show.append(ref)

    for q in range(0,200):
        template_show.append(template_n)

    for i in range (0,50):
        template_show.append(space)

    for i in range (0,200):
        template_show.append(align1_n)

    for i in range (0,50):
        template_show.append(space)

    for i in range (0,200):
        template_show.append(align2_n)

    for i in range (0,50):
        template_show.append(space)

    template_show = np.asarray(template_show)

    cmap = colors.LinearSegmentedColormap.from_list("", ["red", "grey", "white", "blue", "darkorange", "orangered", "deeppink", "aqua", "slategrey", "lime", "navy", "teal", "black", "indigo"])

    plot.imshow(template_show, cmap=cmap)

    plot.show()
