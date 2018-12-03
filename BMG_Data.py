import sys
import csv

fname = sys.argv[1] # get filename from argument
reading = sys.argv[2]



def metadata(file): # Input file_stored
    all_meta = []
    for i in file:
        meta = i.split(",")[0]
        if meta != "Well":
            all_meta.append(meta)
        else:
            break
    return(all_meta)

def returnReadingTypes(file):
    for i in file:
        if i.split(",")[0] == "Well":
            reading_row = i.split(",")
            break
    reading_types = []
    for r in reading_row:
        if r != "Well" and r != "Content" and r != "Group":
            if not r.split("\n")[0] in reading_types:
                reading_types.append(r)
    return(reading_types)

def returnGroupNames(file):
    check = False
    for i in file:
        if i.split(",")[2] == "Group":
            check = True
            break
    if not check:
        return("No Groups Found!")
    data_only = []
    at_data = False
    for do in file:
        if not at_data:
            if do.split(",")[1] == "Time":
                at_data = True
            continue
        data_only.append(do.split(","))

    group_names = []
    for g in data_only:
        if not g[2] in group_names:
            group_names.append(g[2])
    return(group_names)

def exportReadingData(file,fname,rTitle):
    reading_types = returnReadingTypes(file)
    check = False
    number = 0
    for r in reading_types:
        if rTitle in r:
            full_rTitle = r
            check = True
            number += 1
    if not check or number > 1:
        print("Reading Not Found!")
        for i in returnReadingTypes(file):
            print(i)
        return()
    slice_start = False
    slice_end = 0
    n = 0
    for i in file:
        if i.split(",")[0] == "Well":
            for t in i.split(","):
                if t == full_rTitle:
                    if not slice_start:
                        slice_start = n
                    else:
                        slice_end = n+1
                n += 1
            break
    print(slice_start)
    print(slice_end)
    data_slice = []
    data_start = False
    for i in file:
        if not data_start:
            if i.split(",")[0] == "Well":
                data_start = True
                data_slice.append(i.split(",")[0:3] + i.split(",")[slice_start:slice_end])
            continue
        data_slice.append(i.split(",")[0:3] + i.split(",")[slice_start:slice_end])

    to_write = []
    for d in data_slice:
        row = ""
        for e in d:
            row += e + ", "
        to_write.append(row[0:len(row)-2])
    sName_rTitle = ""
    for i in full_rTitle:
        if len(sName_rTitle) == 0 and i == " ":
            continue
        if i == " ":
            sName_rTitle += "_"
        elif i == "/":
            sName_rTitle += "_and_"
        else:
            sName_rTitle += i
    if "/" in fname:
        fname = fname.split("/")
        fname = fname[len(fname)-1]
    output_file = open(fname.split(".")[0] + "-" + sName_rTitle + ".csv","w+")

    for r in to_write:
        output_file.write(r+"\n")
    output_file.close()
    return(to_write)

data = open(fname, "r") # Open file from BMG (export as table) and store in a list
file_stored = []
for i in data:
    file_stored.append(i)
data.close()

ds = exportReadingData(file_stored,fname,reading)
