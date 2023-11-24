import math

# header

print("investment    - to calculate the amount of interest you'll earn on your investment")             
print("bond          - to calculate the amount you'll have to pay on a home loan")                      
print()         

# defining variables to check users input

bond = "bond"
investment = "investment"
simple = "simple"
compound = "compound"

# requesting input one of two options and changing 

type = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

# requests the series of inputs from the user if he chooses investment

if type in investment:

   deposit = int(input("How much money you want to deposit: "))
   rate_inv = int(input("What is the interest rate: "))
   years = int(input("How many years: "))
   interest = str(input("Do you want 'simple' or 'compound' interest: ")).lower()

# formulas for calculating percetage and both types of intererst

   percentage_inv = (rate_inv / 100 )   
   simple_interest = deposit * (1 + percentage_inv * years) 
   compound_interest = deposit * math.pow((1 + percentage_inv),years)

# displaying the answer depending the type of interest uset chooses  

   if interest in simple:
    print("You will earn:" , round(simple_interest))

   elif interest in compound:
    print("You will earn:" , round(compound_interest)) 

# requests the series of inputs from the user if he chooses bond 

if type in bond:

    house_value = int(input("What is the house value: "))
    rate_bond = int(input("what is the interest rate: "))
    months = int(input("How many months you plan to repay: "))
       
# formulas for percentage and repayment

    percentage_bond = (rate_bond/100)
    monthly_interest = percentage_bond / 12
    repayment = (monthly_interest * house_value)/(1-(1+monthly_interest)**(-months))

# displayig answer after inputing all variables

    print("Your monthly repayment will be:" , round(repayment))

# conditions in which "Invalid input" messege will appear

if type != investment and bond:
  print("Invalid input")

if interest != simple and compound:
  print("Invalid input")




    
    


















    




