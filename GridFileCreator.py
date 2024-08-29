INFILE = 'data.dat'

# function to create and write the points to files
def points_creator(data_list):
    print(f"Grid File Creator: Writing on output file/s")

    for (chromos, A, B, num_intervals) in data_list:
        fileout_name = "points." + chromos + "." + ".".join(map(str, [A, B, num_intervals])) + ".out"
        
        # Generate the points betweem A and B
        num_intervals    = num_intervals + 1 
        step_size        = (B - A) / num_intervals

        with open(fileout_name,"w") as file1:
            file1.write(f"chr{chromos}\t{A}\n")
            for i in range(1, num_intervals):
                point = int(A + i * step_size)
                file1.write(f"chr{chromos}\t{point}\n")
            file1.write(f"chr{chromos}\t{B}\n")

def print_error():
    print(f"Something went wrong")
    return 0

def main():
    print(f"Grid File Creator")
    data_list = []
    print(f"Grid File Creator: Reading input file")
    # check the input file if the data is valid
    with open(INFILE,'r') as file0:
        for line in file0:
            tokens = line.split('\n')[0].split(' ')
            if len(tokens) != 4:
                return print_error()
            if False in list(filter(lambda x:x.isdigit(),tokens)):
                return print_error()
            chromosome  = tokens[0]
            rangeStart  = int(tokens[1])
            rangeEnd    = int(tokens[2])
            numOfPoints = int(tokens[3])

            # check input validity
            if rangeEnd < rangeStart or numOfPoints == 0 or not chromosome.isdigit():
                return print_error()

            data_list.append((chromosome, rangeStart, rangeEnd, numOfPoints))
    
    points_creator(data_list)
    print(f"Grid File Creator: Creating points completed")
    return 1

if __name__ == "__main__":
        main()