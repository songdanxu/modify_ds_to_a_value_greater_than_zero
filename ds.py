import argparse

parser = argparse.ArgumentParser(description="Input and output file path.")
parser.add_argument('--input',type=str,help="The input file path")
parser.add_argument('--output',type=str,help="The output file path")

args=parser.parse_args()

file1=open(args.input,'r')
file2=open(args.output,'w')

# file1 = open("D:\\python_files\\ds\\ds.txt", 'r')
# file2 = open('D:\\python_files\\ds\\ds_xiugai.txt', 'w')
data = []
new_data = []
without_zero_data = []
# Read the value of each line in the file and save it to a list.
for line in file1.readlines():
    data.append(line.strip())
print(data)
# Convert the value in the list from a string to a floating point.
for i in data:
    new_data.append(float(i))
print(new_data)
# Del the zero value in the list,and then use min() to find the min value.
for j in new_data:
    if j != 0:
        without_zero_data.append(j)
min_value = min(without_zero_data)
# print(min_value)

# Add the minimum value to each of the value in the list.
for i, k in enumerate(new_data):
    new_data[i] += min_value
print(new_data)

for z in range(0, len(new_data)):
    file2.write(str(new_data[z]) + "\n")
file1.close()
file2.close()
