from optparse import OptionParser

parser = OptionParser( description="GridFile Creator v0.2.kutsukos This tool is creating a tab-delimited file, that contains positions inside a specified range."
                                   "It can be used as input in some programs like SweeD or OmegaPlus."
                                   "\nThe format of this file is \"chr <tab> pos\". It is like a bed file, but it is not defining areas of interest, but points, inside an area." )
parser.add_option("-c", "--chr", dest="chr",
                  help="the number of the chr that will be written in output")
parser.add_option("-s", "--start", dest="start",
                  help="the starting position of this range. It is included in the file")
parser.add_option("-e", "--end", dest="end",
                  help="the ending position of this range. It is included in the file")
parser.add_option("-n", "--num", dest="num",default=0,
                  help="the number of positions you want in this range")
parser.add_option("-d", "--dist", dest="dist",
                  help="alternative to num, dist is the distance between the points. If -dist is used, -num will be ignored", default=0)

(options, args) = parser.parse_args()

chr=options.chr    #chromosome
numOfPoints=int(options.num)
rangeEnd=int(options.end)
rangeStart=int(options.start)
userdist=int(options.dist)

diff=rangeEnd-rangeStart+2
if(diff<=0):
    print "Error! Please check your input"
if(userdist == 0 and numOfPoints==0):
    print "Error! Please check your input"
else:
    if(userdist != 0):
        step=userdist
        numOfPoints=(diff/step) +1
    else:
        step = (diff / (numOfPoints - 1));  upoloipo=diff%(numOfPoints - 1)
        if (upoloipo > 5):
            step = step + 1
        if (step < 1):
            step = 1
    x=rangeStart
    positions=[]

    test=range(rangeStart, rangeEnd+1,step)
    for item in test:
        if (positions.count(item) == 0 and len(positions)<(numOfPoints-1)):
            positions.append(item)

    if(positions.count(rangeEnd)==0):
        positions.append(rangeEnd)

    # sort positions
    positions.sort()

    #time to export our data
    outputfile="points."+chr+"."+str(rangeStart)+"."+str(rangeEnd)+".out"
    outFile = open(outputfile, "w")
    # print positions
    for item in positions:
        outFile.write("chr" + chr+"\t" + str(item) + "\n")
    outFile.close()

    #print statistics for debugging
    print "[Creating points completed]"
    print "Area: "+str(rangeStart)+" - "+str(rangeEnd)
    print "Distance:" + str(step)
    print "[DEBUGGING MSG] "+str(len(positions))+"/"+str(numOfPoints)+" points created and exported to " +outputfile
