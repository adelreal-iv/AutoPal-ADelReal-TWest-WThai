import requests
import json

def InterestCalculator(LoanAmount, term, interest, Last_Payment,tax):

    LoanAmount = float(LoanAmount)
    interest = float(interest)
    term = int(term)
    Last_Payment = 0
    tax = tax * .01

    LoanAmount = LoanAmount + (LoanAmount * tax)
    monthly_payment, interest_charge, final_amount, Last_Payment = ProjectLoan(LoanAmount, interest, term, Last_Payment)

    monthly_payment = round(monthly_payment, 2)
    interest_charge = round(interest_charge, 2)
    final_amount = round(final_amount, 2)
    Last_Payment = round(Last_Payment,2)


    return monthly_payment, interest_charge, final_amount, Last_Payment, LoanAmount
    


def ProjectLoan(LoanAmount, interest, term, Last_Payment):
    balance = LoanAmount
    apr = interest * .01
    period_rate = (apr / 12)
    Last_Payment = 0

    Payment_Calculation = (LoanAmount * (period_rate * pow((1+period_rate), term))) / (pow((1+period_rate), term) - 1)  #This is the formula to calculate the monthly payment of an APR based loan
    Payment_Calculation = round(Payment_Calculation,2)                                                                              #Rounds payment to 2 decimal places
    print(Payment_Calculation)
    

    FinanceCharge = 0
    LoanAmount = balance
    year = 1
    NewLoanAmount = balance
    payment = Payment_Calculation
        

    for i in range(0, term):
        paid_interest = (period_rate * NewLoanAmount)
        principal = payment - round (paid_interest,2)
        paid_interest = round(paid_interest,2)
        
        

        if payment > NewLoanAmount:
            principal = NewLoanAmount
            payment = principal + paid_interest
            NewLoanAmount = 0

        NewLoanAmount = LoanAmount - principal
        LoanAmount = NewLoanAmount
        FinanceCharge = FinanceCharge + paid_interest
        
        i += 1
    
    
        Last_Payment = payment
        TotalPayments = FinanceCharge + balance     
    

    return Payment_Calculation, FinanceCharge, TotalPayments, Last_Payment       

        
#This function might be converted to JavaScript instead, it would run much faster on the browser
def AmortizationCalculator(LoanAmount, term, interest): 
    LoanAmount = float(LoanAmount)
    interest = float(interest)
    term = int(term)

    balance = LoanAmount
    apr = interest * .01
    period_rate = (apr / 12)

    Payment_Calculation = (LoanAmount * (period_rate * pow((1+period_rate), term))) / (pow((1+period_rate), term) - 1)  #This is the formula to calculate the monthly payment of an APR based loan
    Payment_Calculation = round(Payment_Calculation,2)                                                                              #Rounds payment to 2 decimal places
    print(Payment_Calculation)

    FinanceCharge = 0
    LoanAmount = balance
    year = 1
    NewLoanAmount = balance
    payment = Payment_Calculation

    
    for i in range(0, term):
        paid_interest = (period_rate * NewLoanAmount)
        principal = payment - round (paid_interest,2)
        paid_interest = round(paid_interest,2)
        
        

        if payment > NewLoanAmount:
            principal = NewLoanAmount
            payment = principal + paid_interest
            NewLoanAmount = 0

        NewLoanAmount = LoanAmount - principal

                         
        if i % 12 == 0:
            year += 1

        LoanAmount = NewLoanAmount
        FinanceCharge = FinanceCharge + paid_interest


def TaxAPI(city):
    url = 'https://www.cdtfa.ca.gov/dataportal/api/odata/Effective_Sales_Tax_Rates?%24select=city%2Crate'
    response = requests.get(url)
    response = response.json()
    cityrates = []
    cityrates = response['value']
    usertax = 0
    
#    print("\nCALIFORNIA TAX RATE API")
#    print("-" * 150)

    cityinput = city #input('\nPlease enter your city: ')
    cityinput = cityinput.title()    

    for i in range(len(cityrates)):
        if cityinput == (cityrates[i]['City']):
            usertax = (cityrates[i]['Rate'])
            break
        else:
            i += 1

    usertax = usertax * 100
    usertax = round(usertax, 2)

    return cityinput, usertax


#    print("Your tax rate will be: %.2f%%\n"% usertax)

    
