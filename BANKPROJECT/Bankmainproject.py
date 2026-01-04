from Bankmenu import menu
from Bankopening import addnc
from Bankallcustomer import viewallcd,viewcd
from Customersearch import searchcust
from Bankcustdelete import deletecustomer
from Bankpin import pingenerate,pinupdate
from Bankbalanceupdate import Deposit,Withdrarw
import sys
sys.path.append("D:\\ADVANCE  FUNCTION PYTHON(COACHING)\\9ATMproject")
from ATMexcept import DepositError,WithDrawError,InSufficientFundError
while True:
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match ch:
            case 1:
                addnc()
            case 2:
                deletecustomer()
            case 3:
                try:
                    Withdrarw()
                except WithDrawError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR WITHDRAW.")
                except InSufficientFundError:
                    print("\tYOUR ACCOUNT DOES NOT HAVE SUFFICIENT FUND.")
            case 4:
                try:
                    Deposit()
                except DepositError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR DEPOSITS.")
            case 5:
                viewcd()
            case 6:
                viewallcd()
            case 7:
                searchcust()
            case 8:
                pingenerate()
            case 9:
                pinupdate()
            case 10:
                print("\tThanks For Using This Project.")
                break
            case _:
                print("\tYour Choice Of Selection Is Wrong--Try Again.")
    except ValueError:
        print("\tDon't Enter Alnums,Str And Symbol For Choice.")