# Dfined rates of currencies

rates = {
    '$' : 80,
    '€' : 90,
    '£' : 100,
    '₹' : 1
}

# Function to Calculate Tax

def Calculate_Tax(inr_rates,currency):
    try:
        rate = rates.get(currency,1)
        print('rate',rate)
        tax_percent = 0
        Tax, Inhand = 0,0
        if inr_rates <= 0:
            print("Salary cannot be zero or negative")
        elif inr_rates <=10000:
            inhand = inr_rates
            print("You do'nt have to pay tax")
        elif inr_rates >10000 and inr_rates <=20000:
            tax_percent = 10
            Tax = 0.10 * inr_rates
            Inhand = inr_rates - Tax
            # print("Tax on your salary is 10% i.e", Tax)
            # print(f"Your Inhand salary is {Salary} - {Tax} i.e", Inhand)
        elif inr_rates >20000 and inr_rates <=30000:
            tax_percent = 20
            Tax = 0.20 * inr_rates
            Inhand = inr_rates - Tax
            # print("Tax on your salary is 20% i.e", Tax)
            # print(f"Your Inhand salary is {Salary} - {Tax} i.e", Inhand)
        elif inr_rates >30000 and inr_rates <=40000:
            tax_percent = 30
            Tax = 0.30 * inr_rates
            Inhand = inr_rates - Tax
        elif inr_rates >40000:
            tax_percent = 40
            Tax = 0.40 * inr_rates
            Inhand = inr_rates - Tax
            # print("Tax on your salary is 30% i.e", Tax)
            # print(f"Your Inhand salary is {Salary} - {Tax} i.e", Inhand)

        # Converting ₹ to $, ₹ to €, ₹ to £

        Tax_currency = Tax / rate
        Inhand_currency = Inhand / rate
        Salary_currency = inr_rates / rate

        #Printing Tax

        if tax_percent > 0:
            print(f"Tax on your Salary is {tax_percent}% i.e {Tax_currency:} {currency}")
        print(f"In-hand salary:  {Salary_currency} - {Tax_currency} = {Inhand_currency}{currency}")
            
        return Tax_currency,Inhand_currency

    except NameError as e:
        print("Error in Calculate Tax Function")

#This function is for checking input

def Check_Input():
    Salary = input("Enter your Salary : (e.g. $100...100$....E333...R)")
    currency = None
    amount = None
    try:
        try:
            # if Salary > 0:
                
            Salary = Salary.replace(" ","")
            # Tax, Inhand = Calculate_Tax(Salary)
            
            # if Salary.endswith("USD"):
            #     return USD_to_INR(Salary)
                 
            # elif Salary.endswith("EUR"):
            #     return EUR_to_INR(Salary)
                
            # elif Salary.endswith("GDP"):
            #     return GDP_to_INR(Salary)
                
            # else:
                # print("Unknown Currency")        
    
            currency = Salary[-1]
            amount = float(Salary[:-1])
            
            if currency in rates:
                print('Currency found in salary')
                if currency == '₹':
                    print('INR entered by user')
                    inr_salary = amount
                    
                    Tax, Inhand = Calculate_Tax(inr_salary, '₹')
                elif currency == '$':
                    inr_salary = USD_to_INR(amount)
                    print('INR SALRY',inr_salary)
                    Tax, Inhand = Calculate_Tax(inr_salary, '$')
                elif currency == '€':
                    inr_salary, Tax, Inhand = EUR_to_INR(amount)
                elif currency == '£':
                    inr_salary, Tax, Inhand = GDP_to_INR(amount)
                else:
                    print("Unknown currency. Please use $, €, £, or ₹.")
            else:
                print('Currency not found in salary')
                print('Considering ₹ as default Currency')
                inr_salary = float(Salary)
                Tax, Inhand = Calculate_Tax(inr_salary, '₹')
                               
                # if currency not in rates:
                #     print("Unknown currency please use $, €, £, or ₹")
        
                # Tax, Inhand = Calculate_Tax(Salary)
    
            # else:
            #     print("Salary cannot be negative or zero")
        except ValueError as e:
            print("Salary Cannot be Character")
            
    except NameError as e:
        print("Error in Function check_input",e)
    
    # except Exception as ee:
    #     print("###### error",ee)
    # return Calculate_Tax(inr_rates)





# Converting $ to ₹

def USD_to_INR(Salary):
    try:
        inr_salary = Salary * rates['$']
        return inr_salary
    except NameError as e:
        Print("Error in USD_to_INR Function",e)

# Converting € to ₹
    
def EUR_to_INR(Salary):
    try:
        inr_salary = Salary * rates['€']
        Tax, Inhand = Calculate_Tax(inr_salary, '€')
        return inr_salary, Tax, Inhand
    except NameError as e:
        Print("Error in EUR_to_INR Function",e)

# Converting £ to ₹
    
def GDP_to_INR(Salary):
    try:
        inr_salary = Salary * rates['£']
        Tax, Inhand = Calculate_Tax(inr_salary, '£')
        return inr_salary, Tax, Inhand
    except NameError as e:
        Print("Error in GDP_to_INR Function",e)

# Converting ₹ to $

def INR_to_USD(Salary):
    try:
        usd_value = Salary / rates['$']
        return usd_value
    except NameError as e:
        Print("Error in INR_to_USD Function",e)
    
# Converting ₹ to €
    
def INR_to_EUR(Salary):
    try:
        eur_value = Salary / rates['€']
        return eur_value
    except NameError as e:
        Print("Error in INR_to_EUR Function",e)

#Converting ₹ to £
    
def INR_to_GDP(Salary):
    try:
        gdp_value = Salary / rates['£']
        return gdp_value
    except NameError as e:
        Print("Error in INR_to_GDP Function",e)

Check_Input()