import random 
import io

nucleo_list = ("A","G","C","T")

def DNA_sequence():
  subset1 = ''
  subset2 = ''
  for i in range(0, 76):
    subset1 += random.choice(nucleo_list)
  for i in range(150- len(subset1)):
    subset2 += random.choice(nucleo_list)
  full_sequence = subset1 + subset2 + subset1 + subset2
  return(full_sequence)

spidroin = DNA_sequence()

filename = input("File name is: ")
file_header = input("File Header is:")

def spidroinFile(filename, file_header):
  try:
    with open(filename + ".fasta", "w") as spidroinFile_handle:
      spidroinFile_handle.write(">"+file_header)
      spidroinFile_handle.write(spidroin)
  except IOError as err:
    print("there's an error")
  return spidroinFile_handle

spidroinFile(filename, file_header) 

