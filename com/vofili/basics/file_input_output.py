import csv

from json import JSONDecodeError

#File reading

#fread = open("/Users/val/PycharmProjects/DataScienceWithPython/com/vofili/basics/10_01_file.txt","r")
#fr = open("10_01_file.txt","r")
#print(fr)
# with open("10_02_us.csv","r") as f:
#      freader = csv.reader(f,delimiter="\t")
#      for line in freader:
#           print(line)




# with open("10_02_us.csv","r") as f:
#      freader = csv.reader(f,delimiter="\t")
#      next(freader)
#      next(freader)
#      for line in freader:
#           print(line)

# with open("10_02_us.csv","r") as f:
#      freader = csv.DictReader(f,delimiter="\t")
#      for line in freader:
#           print(line)

# with open("10_02_us.csv","r") as f:
#      datalist = list(csv.DictReader(f,delimiter="\t"))
#      for item in datalist:
#           print(item)

primes=[]

for n in range(2, 99999):
     for i in (2, (n**0.5)):
          if n % i == 0:
               break
     else:
          primes.append(n)



#File Writing
fw = open("10_01_Output_01.txt","w")
fw.write("explicit is better than implicit\n")
fw.write("loud is better than silent\n")
fw.write("pythonic is better than verbose\n")

fa = open("10_01_output_01.txt","a")
fa.write("simple is better than complex")
fa.close()
fw.close()
