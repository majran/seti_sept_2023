import seti_converter
import sys

for index, arg in enumerate(sys.argv):
    print(f"Z lini polecen przekazano: {index}: {arg} ==> {type(arg)}")

for arg in sys.argv[1:]:
    print(seti_converter.decimal_to_binary(int(arg)))




# print("---")
# print(seti_converter.decimal_to_binary(6768768))