#import random to be able to pull random sequences 
#import io helps for data extraction and IOError
import random 
import io
#nucleo_list is our variable name for our sequences, which are the DNA sequences AGCT
nucleo_list = ("A","G","C","T")
#DNA_sequence is definied with these variables since it will help us select random sequences and then we are able to combine them
def DNA_sequence():
  subset1 = ''
  subset2 = ''
  for i in range(0, 76):
    subset1 += random.choice(nucleo_list)
  for i in range(150- len(subset1)):
    subset2 += random.choice(nucleo_list)
  full_sequence = subset1 + subset2 + subset1 + subset2
  return(full_sequence)
#spidroin is same value as DNA_sequence but named
spidroin = DNA_sequence()
#this will help us create new files 
filename = input("File name is: ")
file_header = input("File Header is:")
#this will create fasta files and check for errors
def spidroinFile(filename, file_header):
  try:
    with open(filename + ".fasta", "w") as spidroinFile_handle:
      spidroinFile_handle.write(">"+file_header)
      spidroinFile_handle.write(spidroin)
  except IOError as err:
    print("there's an error")
  return spidroinFile_handle

spidroinFile(filename, file_header) 

