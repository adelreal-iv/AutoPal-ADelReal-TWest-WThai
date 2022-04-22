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

def BudgetAssistant(monthly_income,monthly_debt):
    dti = 0 
    dti_tier = 0   
    dti_range = [35.99, 49.99]
    tier_text = " "

    monthly_income = round(float(monthly_income),2)
    monthly_debt = round(float(monthly_debt), 2)
    
    if monthly_income != 0 or monthly_debt != 0:
        dti_tier, dti, tier_text = (calculate_dti(monthly_income, monthly_debt, dti_range))

    return dti, dti_tier, tier_text


def calculate_dti(monthly_income, monthly_debt, dti_range):
    dti = 0
    monthly_income = monthly_income 
    dti = monthly_debt / monthly_income
    dti = dti * 100
    dti = round(dti,2)

    tier1_text = "Being at a Tier 1 DTI signifies that you most likely have money left over for savings and monthly expenses, lenders view lower DTI ratios as favorable."
    tier2_text = "A Tier 2 DTI shows that you are managing your debt adequately, but needs work. You may consider lowering your monthly debt as this would help in the event of unexpected expenses. Additionally, lenders may ask for additional eligibility factors such as co-borrowers or down payments."
    tier3_text = "A Tier 3 DTI signifies that more than half your income goes to monthly expenses, leaving you with limited funds that restrict you from handling unexpected expenses and saving. Your borrowing options may be limited as since lenders tend to see this ratio as more of a liability."

    
    if dti <= dti_range[0]: 
        return 1, dti, tier1_text
    elif dti >= dti_range[0] and dti <= dti_range[1]:
        return 2, dti, tier2_text
    elif dti > dti_range[1]:
        return 3, dti, tier3_text    

