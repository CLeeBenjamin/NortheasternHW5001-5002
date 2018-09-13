'''
CS5001
LAB1
FALL 2018
QINGJING GONG  & CASTON BOYD
'''
def main():

    total_bill = float(input("how much was the bill?\n"))
    tip_amount = float(input("what percent will everyone tip? enter a number between 0 and 1\n"))
    split_total = int(input("how many people are spliting?\n"))
    

    amount_per_person = total_bill*(1+tip_amount)/split_total

    new_decimal_amount = round(amount_per_person,2)

    print("Everyone cough up $", new_decimal_amount," please!" ,sep = "")
main()
