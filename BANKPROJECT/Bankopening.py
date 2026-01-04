import pickle
import sys
sys.path.append("D:\\ADVANCE  FUNCTION PYTHON(COACHING)\\8 custom Exceptions and raise keyword")
from nameexcept import ZeroNameLengthError,SpaceError,InvalidNameError
from namevalidation import validate
def uniqueacno(lst):
    with open ("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        res=True
        for record in records:
            if record[0]==lst[0]:
                res=False
                break
        return res
def addnc():
    with open("bankcust.data","ab") as fp:
        while True:
            try:
                print("-"*70)
                acno=int(input("\tEnter Customer Account No:"))
                custname=input("\tEnter Customer Name:")
                cn=validate(custname)
                bal=500.00
                pin=None
                print("-" * 70)
                lst=[]
                lst.append(acno)
                lst.append(cn)
                lst.append(bal)
                lst.append(pin)
                if uniqueacno(lst):
                    pickle.dump(lst,fp)
                    print("\tCustomer Data Saved As Record In File Successfully.")
                else:
                    print("\tCustomer Account Number Already Exist-Try With Unique Account Number.")
                print("-"*70)
                ch=input("\tDo You Want To Enter Another Customer Account Details?(Yes/No):")
                if ch.lower()=="no":
                    break
                print("-" * 70)
            except ValueError:
                print("\tDon't Enter Alnums,Str and Symbol For Account Number.")
            except ZeroNameLengthError:
                print("\tPlease Enter Your Name")
            except SpaceError:
                print("\tDon't Enter Space For Your Name")
            except InvalidNameError:
                print("\tInvalid Name--Try Again.")


