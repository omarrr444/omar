import time

accounts={
    "mohamed":2000,
    "ahmad":5000,
    "alaa":1500,
    "yousef":3000
    
    }

def withdraw(balance,amount):
    if balance >= amount :
        balance-=amount
        return balance
    else :
        print("invalid")
        
def deposit():
   amount= int(input("enter the deposit amount "))
   print("process succses")
   return amount
   

def transformation(balance,account,to_account,trans_amount,accounts):
    if to_account in accounts:
        if balance >= trans_amount :
            accounts[to_account] += trans_amount
            accounts[account] -= trans_amount
            return accounts
        else :
            print("you have no enougth money")
    else:
        print("invalid")
        
        

def balance_info(balance):
    print(f"your balance is {balance}")

counter = 0
while True:
    account=input("We have 4 accounts, enter your user name ")
    
    for key,value in accounts.items():
        if account == key:
            balance = value

            process = input("""which process do you need withdraw, deposit,transformation, balance information """)

            if process == "withdraw":

                amount = int(input("enter the amount you need "))
                new_balance = withdraw(balance,amount)
                
                accounts[key] = new_balance
                
                print(new_balance)
                
            elif process == "deposit":
                new_balance = deposit()
                accounts[key]+= new_balance
                
            elif process == "transformation":
                to_account = input("the account you want to transfer to ")
                trans_amount = int(input("how mush mony do you need "))
                
                new_accounts = transformation(balance,account,to_account,trans_amount,accounts)
                accounts = new_accounts
                
                
            else:
                balance_info(balance)
                





            
            
        
