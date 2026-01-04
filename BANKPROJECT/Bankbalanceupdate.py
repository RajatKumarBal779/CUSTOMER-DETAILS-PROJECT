import pickle
import sys
sys.path.append("D:\\ADVANCE  FUNCTION PYTHON(COACHING)\\9ATMproject")
from ATMexcept import DepositError,WithDrawError,InSufficientFundError
def Withdrarw():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        print("-"*70)
        CusAccno=int(input("\tEnter the Customer Account Number:"))
        pinno=int(input("\tEnter the Pin No:"))
        res=False
        for index in range(len(records)):
            if records[index][0]==CusAccno and records[index][3]==pinno:
                res=True
                bal=records[index][2]
                break
        if res:
            Withdrawl=float(input("\tEnter The Withdrawl Amount:"))
            if Withdrawl<=0:
                raise WithDrawError
            else:
                if Withdrawl+500>bal:
                    raise InSufficientFundError
                else:
                    bal-=Withdrawl
                    records[index][2]=bal
                    with open("bankcust.data","wb") as fp:
                        for record in records:
                            pickle.dump(record,fp)
                        print(f"\tYour Account Number {CusAccno} debited with INR {Withdrawl}")
                        print(f"\tNow Your Account Balance After Withdrawl {bal}")
        else:
            print("\tYou Entered Wrong Customer Account Number/Pin No--Try Again.")
        print("-"*70)
def Deposit():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        print("-"*70)
        CusAccNo=int(input("\tEnter Customer Account No:"))
        res=True
        for index in range (len(records)):
            if records[index][0]==CusAccNo:
                res=False
                bal=records[index][2]
                break
        if not res:
            Damt=float(input("\tEnter Deposit Amount:"))
            if Damt<=0:
                raise DepositError
            else:
                bal+=Damt
                records[index][2]=bal
                with open("bankcust.data","wb") as fp:
                    for record in records:
                        pickle.dump(record,fp)
                    print(f"\tYour Account No:{CusAccNo} Credited With INR {Damt}")
                    print(f"\tNow Your Account Balance After Deposit {bal}")
        else:
            print("\tCustomer Account Number Is Not Valid--Try Again.")
        print("-"*70)

