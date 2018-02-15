import numpy as np
import matplotlib.pyplot as plot
import matplotlib.colors as colors

def add_annotation(start, end, length, colour, comment):
    ann = []

    #0 2 4 6 8 10 14 15

    #light blue 1
    #light orange 3
    #light green 5
    #light red 7
    #light purple 9
    #light brown 11
    #pink 12
    #light pink 13
    #yellowGreen 16
    #light yellowGreen 17
    #aqua 18
    #light aqua 19

    if colour == "lightBlue":
        colourn = 1
    elif colour == "lightOrange":
        colourn = 3
    elif colour == "lightGreen":
        colourn = 5
    elif colour == "lightRed":
        colourn = 7
    elif colour == "lightPurple":
        colourn = 9
    elif colour == "lightBrown":
        colourn = 11
    elif colour == "Pink":
        colourn = 6
    elif colour == "YellowGreen":
        colourn = 16
    elif colour == "lightYellow":
        colourn = 17
    elif colour == "aqua":
        colourn = 18
    elif colour == "lightAqua":
        colourn = 19
    else:
        raise TypeError("Invalid colour, please choose from 'yellow', 'brown', or 'pink'.")

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

    ref.append(6)

    space = []

    for i in range(0,len(template_n)):
        space.append(2)


    for i in range (0,50):
        template_show.append(space)

    if annotations != False:
        labels = []
        for ann in annotations:
            start = ann[0]
            end = ann[1]
            comment = ann[2]
            colour = ann[3]
            length = len(template_n)
            labels.append(add_annotation(start, end, length, colour, comment))
        for l in labels:
            for i in range(0,80):
                template_show.append(l)
            for i in range(0,20):
                template_show.append(space)

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

    cmap = colors.LinearSegmentedColormap.from_list("", ["red", "green", "white", "blue", "yellow", "orange", "deeppink"])

    plot.imshow(template_show, cmap=cmap)

    plot.show()
