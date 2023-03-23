 bank_ac = {'acno':'12345','password':'Pass#00',
            'name':'Shrikant Tiwari',
            'balance':10000,
            'transactions':{'deposit' :[],
                            'withdraw':[]}}

acno = input('Please enter your account number here :  ')
if acno == bank_ac['acno']:
  password = input('Please enter your password number here : ')
  if password == bank_ac['password']:
    while True:
      print('\n','_'*20 + 'Welcome',bank_ac['name'],'_'*20)
      print("Press '1' to see your bank account.")
      print("Press '2' to credit your amount in your account.")
      print("Press '3' to withdraw your amount from your account.")
      print("Press '4' to log out.")
      press = input('Please press your response here : ')

      if press == '1':
        print(f"***\nHello {bank_ac['name']}, you have Rs.{bank_ac['balance']} left in your bank account number {bank_ac['acno']}.")

      elif press == '2':
        try:
          credit = int(input('Please enter the amount to deposit here (Rs.): '))
          bank_ac['balance'] = bank_ac['balance'] + credit 
          bank_ac['transactions']['deposit'].append(credit)
          print('***\nTransaction completed successfully.')
          print('Your transaction amount = Rs.', bank_ac['transactions']['deposit'][-1])
          print('New balance = Rs.',bank_ac['balance'])              
        except ValueError as e:
          print('You did not enter valid amount to deposit.')

      elif press == '3':
        try:
          debit = int(input('Please enter the amount to withdraw here : '))
          bank_ac['balance'] = bank_ac['balance'] - debit 
          bank_ac['transactions']['withdraw'].append(debit)
          print('***\nTransaction completed successfully.')
          print('Your transaction amount = Rs.', bank_ac['transactions']['withdraw'][-1])
          print('New balance = Rs.',bank_ac['balance'])
        except ValueError as e:
          print('You did not enter valid amount to deposit.')
          
      elif press == '4':
        print('\n...Thank you, visit again...')
        break
        
      else:
        print('Invalid response entered !')
  else:
    print('Invalid password entered !')
else:
  print('Invalid bank account entered !')
