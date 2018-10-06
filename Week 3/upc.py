'''
CS5001
HW3
upc.py
FALL 2018
CASTON BOYD
'''


'''
Barcode#: 312546627543
100
Valid

Barcode#: 032251095160
70
Valid

Barcode#: 032251095106
58
Not Valid

'''



def main():

     upc_input = input("Numbers?\n")
     upc_list = []
     upc_list[:0] = upc_input 
     upc_list = upc_list[::-1]
     upc_len = len(upc_list)

     odd_list = []
     even_list = []

     for i in range(1, upc_len, 2):
        odd = int(upc_list[i]) * 3          
        odd_list.append(odd)
        

     for j in range(0, upc_len, 2):
         even = int(upc_list[j])
         even_list.append(even)
         
         
     even_odd_list = odd_list + even_list
     upc_total = sum(even_odd_list)
     print(upc_total)
        
     if upc_total % 10 == 0:
         print("Valid UPC")
     else:
         print("Not a valid UPC")
        
     main()
    



main()
