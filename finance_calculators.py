# importing math module
import math

# drafting initial user message 
# with program description and 
# initial program instructions
initial_prompt = '''
-----------------------------------------------------------------------------------
Choose either 'investment' or 'bond' from the menu below to proceed:

investment          - to calculate your total investment after earning interest
bond                - to calculate the amound you'll have to pay on a home loan
-----------------------------------------------------------------------------------
'''

# instantiate variable for user input
calculator_selection = input(initial_prompt + ': ').lower()

# branch for investment calculation
if calculator_selection == 'investment':
    try:
        # requesting deposit amount
        deposit_prompt = '''
        -----------------------------------------------------------------------------------
        Please enter the principle amount being invested.
        -----------------------------------------------------------------------------------
        '''
        deposit_amount = round(float(input(deposit_prompt + ': ')), 2)

        # requesting interes rate
        interest_rate_prompt = '''
        -----------------------------------------------------------------------------------
        Please enter the investment's interest rate.
        -----------------------------------------------------------------------------------
        '''
        interest_rate = int(input(interest_rate_prompt + ': '))

        # request investment period
        investment_period_prompt = '''
        -----------------------------------------------------------------------------------
        How many years do you plan on investing the principle amount for?
        -----------------------------------------------------------------------------------
        '''
        investment_period = int(input(investment_period_prompt + ': '))

        # request type of interest calculation
        interest_type_prompt = '''
        -----------------------------------------------------------------------------------
        Choose either 'simple' or 'compound' interest to complete your calculation:
        -----------------------------------------------------------------------------------
        '''
        interest_type = input(interest_type_prompt + ': ').lower()

        # nested branch to complete interest calculation
        if interest_type == 'simple':
            # simple interest formula/calculation
            interest = deposit_amount * (1 + (interest_rate / 100) * investment_period)

            # output result for simple interest
            interest_result = f'''
            -----------------------------------------------------------------------------------
            Your investment standing, after accumulating simple interest for {investment_period} years
            at {interest_rate}% interest, is R{round(interest, 2)}
            -----------------------------------------------------------------------------------
            '''

            # output result
            print(interest_result)
        
        elif interest_type == 'compound':
            # compound interest formula/calculation
            interest = deposit_amount * math.pow(1 + (interest_rate / 100), investment_period)

            # output result for simple interest
            interest_result = f'''
            -----------------------------------------------------------------------------------
            Your investment standing, after accumulating compound interest for {investment_period} years
            at {interest_rate}% interest, is R{round(interest, 2)}
            -----------------------------------------------------------------------------------
            '''

            # output result
            print(interest_result)
        
        else:
            # request user re-run program
            calculator_selection_error = '''
            -----------------------------------------------------------------------------------
            You chose neither 'simple' nor 'compound' interest from the menu above.

            To proceed you'll need to re-run the program and ensure your inputs are valid.
            -----------------------------------------------------------------------------------
            '''

            #output error message
            print(calculator_selection_error)

    except:
        # error handling for initial parameters
        initial_parameters_error = '''
        -----------------------------------------------------------------------------------
        One or more of the initial parameters you entered for your interest calculation
        is invalid.

        To proceed you'll need to re-run the program and ensure your inputs are valid.
        -----------------------------------------------------------------------------------
        '''

        # output error message
        print(initial_parameters_error)

# branch for bond payment calculation
elif calculator_selection == 'bond':
    try:
        # requesting value of home
        home_value_prompt = '''
        -----------------------------------------------------------------------------------
        Please enter the present value of the home you'd like to purchase.
        -----------------------------------------------------------------------------------
        '''
        home_value = round(float(input(home_value_prompt + ': ')), 2)

        # requesting interes rate
        interest_rate_prompt = '''
        -----------------------------------------------------------------------------------
        Please enter the bond's interest rate.
        -----------------------------------------------------------------------------------
        '''
        interest_rate = int(input(interest_rate_prompt + ': '))

        # request investment period
        repayment_period_prompt = '''
        -----------------------------------------------------------------------------------
        Over how many months do you plan on repaying your bond?
        -----------------------------------------------------------------------------------
        '''
        repayment_period = int(input(repayment_period_prompt + ': '))

        # instantiate i value to simplify calc statement
        i = (interest_rate / 100) / 12

        # repayment value calculation
        repayment = (i * home_value) / (1 - (1 + i) ** (-repayment_period))

        # output result for bond repayment
        repayment_result = f'''
            -----------------------------------------------------------------------------------
            Your monthly repayment on your bond, over {repayment_period} months at {interest_rate}% interest
            is R{round(repayment, 2)}
            -----------------------------------------------------------------------------------
            '''

        # output result
        print(repayment_result)

    except:
        # error handling for parameter inputs 
        initial_parameters_error = '''
        -----------------------------------------------------------------------------------
        One or more of the initial parameters you entered for your bond repayment
        calculation is invalid.

        To proceed you'll need to re-run the program and ensure your inputs are valid.
        -----------------------------------------------------------------------------------
        '''

        # output error message
        print(initial_parameters_error)

# instance where neither input is 
# investment nor bond
else:
    # request user re-run program
    calculator_selection_error = '''
    -----------------------------------------------------------------------------------
    You chose neither 'investment' nor 'bond' from the menu above.

    To proceed you'll need to re-run the program and ensure your inputs are valid.
    -----------------------------------------------------------------------------------
    '''

    #output error message
    print(calculator_selection_error)
    