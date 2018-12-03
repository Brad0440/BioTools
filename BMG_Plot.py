import sys
import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1] # get filename from argument
samples = []
for s in sys.argv[2:len(sys.argv)]:
    samples.append(s)

data = open(fname, "r") # Open file from BMG (export as table) and store in a list
file_stored = []
for i in data:
    file_stored.append(i.split(","))
data.close()

Sample_names = []
y = []
check = False
for i in file_stored:
    if check:
        Sample_names.append(i[1] + i[2])
        y.append(i[3:len(i)-1] + [i[len(i)-1].split("\n")[0]])
    elif i[1] == " Time":
        check = True
        continue
for i in Sample_names:
    print(i)


times = file_stored[1]
times = times[3:len(times)]

x = []

for i in times:
    st = i.split(" ")
    if st[3] == "":
        x.append(int(st[1])*60)
    else:
        x.append(int(st[1])*60 + int(st[3]))

x_int = []
for i in x:
    x_int.append(int(i))

y_int = []
for i in y:
    ySub_int = []
    for j in i:
        ySub_int.append(int(j))
    y_int.append(ySub_int)

Sample_Ids = []
Sample_rep_n = []
for i in Sample_names:
    if not i in Sample_Ids:
        Sample_Ids.append(i)
        Sample_rep_n.append(Sample_names.count(i))

y_Av = []
y_Std = []

for i in Sample_Ids:
    reps = []
    reps_Av = []
    reps_Std = []
    for j in range(0,len(Sample_names)):
        if Sample_names[j] == i:
            reps.append(y_int[j])
    for r in range(0,len(reps[0])):
        avs  = []
        for z in range(0,len(reps)):
            avs.append(float(reps[z][r]))
        reps_Av.append(np.average(avs))
        reps_Std.append(np.std(avs))
    y_Av.append(reps_Av)
    y_Std.append(reps_Std)


#### Average

sample_show = []

n = 0
leg = []
for i in Sample_Ids:
    for j in samples:
        if j in i:
            sample_show.append(n)
            leg.append(i)
    n += 1

colors = []

for i in sample_show:
    a = plt.errorbar(x,y_Av[i],yerr=y_Std[i],capsize=2)
    for c in range(0,Sample_rep_n[i]):
        colors.append(a.lines[0].get_color())
plt.legend(leg)
sample_show_scatter = []

n = 0
for i in Sample_names:
    for j in samples:
        if j in i:
            sample_show_scatter.append(n)
    n += 1
m = 0
for i in sample_show_scatter:
    plt.scatter(x,y_int[i], facecolor = colors[m])
    m += 1


plt.show()

#### Raw Data

# sample_show = []
#
# n = 0
# for i in Sample_names:
#     for j in samples:
#         if j in i:
#             sample_show.append(n)
#     n += 1
#
# for i in sample_show:
#     plt.plot(x,y_int[i])
# plt.show()
