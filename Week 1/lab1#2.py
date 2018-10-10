'''
CS5001
Lab 1
Fall 2018
Caston Boyd and Qingjing Gong
'''
'''
Problem 2: Buying a house in Boston
'''

def main():

    cost_house = float(input("How much does your dreamhouse cost?\n"))
    annual_salary = float(input("How much do you make per year?\n"))
    saving_pct_per_month = float(input("What percent do you save each month? Enter a number between 0 and 1\n"))

    down_payment = float(.25 * cost_house)
    down_payment_format = format( down_payment,".2f")
    saves_per_month = float(annual_salary / 12 * saving_pct_per_month)
    saves_per_month_format = format(saves_per_month, ".2f")
    
    months_for_down_payment = int(down_payment // saves_per_month)
    year = int(months_for_down_payment // 12)
    months = int(months_for_down_payment % 12)

    print("You need to save $", down_payment_format, " before you can buy the place.", sep = "")
    print("You save $", saves_per_month_format, " per month", sep = "")
    print("It will take you", months_for_down_payment, " months to save that much.")
    print("Which is", year, "years and", months, "months.")

main()
