
def entry():
    print("Enter W to Withdraw or D for Deposit Followed by a space and Amount")
    i = str(input())
    return i
def transact():
    try:
        j = entry()
        category_input = j.split(' ')[0]
        amount = int(j.split(' ')[1])
        Balance = 0
        if(category_input == 'D'):
            Balance+=amount
            return Balance
        elif(category_input == 'W'):
            Balance-=amount
            return Balance
        else:
            print("Invalid Entry")
    except:
        pass

def status():
    print("Balance is: {}",transact())


obj = status()
print(obj)


''' 
Initialize User account and User Balance
Request User to provide Transaction variables
Split and Categorize variable by transaction type
Create aggregate functions to add or subtract to Balance
'''
