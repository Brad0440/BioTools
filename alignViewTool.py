import alignView as av
import sys


if len(sys.argv) == 1:
    print("")
    print("Format: python3 alignViewTool [Alignment File]")
    print("")
    print("Alignment File:" + "\t" + "Location of the alignment file to visualise. Must be in FASTA format. Supports output from Benchling")
    print("")
    print("To learn about other options, run 'python3 alignViewTool -h' or 'python3 alignViewTool --help'")
    print("")
    exit()

elif sys.argv[1] == '-h' or sys.argv == '--help':
    print("")
    print("Format: python3 alignViewTool [Alignment File]")
    print("")
    print("Alignment File:" + "\t" + "Location of the alignment file to visualise. Must be in FASTA format. Supports output from Benchling")
    print("")
    print("Adding Annotations: \n")
    print("For each annotation to add, use either a '-a' or '--annotation' flag. \n Annotations are declared in the following format:")
    print("\t python3 alignViewTool alignment_example.fasta -a [start position] [end position] [annotation text] [annotation colour]")
    print("Example:")
    print("\t python3 alignViewTool alignment_example.fasta -a 1244 2003 'My new annotation' lightBlue -a 200 998 'My second annotation' Pink")
    print("")
    exit()

elif len(sys.argv) < 2:
    print("")
    print("Format: python3 alignViewTool [Alignment File]")
    print("")
    print("Alignment File:" + "\t" + "Location of the alignment file to visualise. Must be in FASTA format. Supports output from Benchling")
    print("")
    print("To learn about other options, run 'python3 alignViewTool -h' or 'python3 alignViewTool --help'")
    print("")
    exit()

else:
    alignfile = sys.argv[1]
    annotations = []
    for i in range(0,len(sys.argv)):
        if sys.argv[i] == '-a' or sys.argv[i] == '--annotation':
            annotations.append([int(sys.argv[i+1]), int(sys.argv[i+2]), sys.argv[i+3], sys.argv[i+4]])
    if annotations == []:
        av.show_align(alignfile)
    else:
        av.show_align(alignfile, annotations)
