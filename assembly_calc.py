import sys

def ratioCalc(massBack,lengthIns,lengthBack,ratio): #ratio = [insert,backbone]
	ratioStr = str(ratio[0])+":"+str(ratio[1])
	print("Ratio:",ratioStr)
	return(((massBack*lengthIns)/lengthBack)*(ratio[0]/ratio[1]))

if len(sys.argv) != 4:
	print("Insert Length (bp) | Backbone Mass (ng) | Backbone Length (bp)")
	quit()

lengthIns = float(sys.argv[1])
massBack = float(sys.argv[2])
lengthBack = float(sys.argv[3])

pmolsBack = (massBack*1000)/(lengthBack*650)

#print("pMols Backbone:", pmolsBack)

ratioList = [[1,1],[1,3],[1,5],[3,1],[5,1]]
print("\n")
for i in ratioList:
	print(ratioCalc(massBack,lengthIns,lengthBack,i),"ng","\n")
