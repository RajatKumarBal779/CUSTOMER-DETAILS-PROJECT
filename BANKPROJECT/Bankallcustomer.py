import pickle
def viewcd():
    with open("bankcust.data","rb") as fp:
        records=[]#here we have to access index so that, we create an empty list for storing records.
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        print("-"*70)
        custaccno=int(input("\tEnter Customer Account Number:"))
        res=False
        for record in records:
            if record[0]==custaccno:
                res=True
                break
        if res:
            print("\tCustomer Account Number:{}".format(record[0]))
            print("\tCustomer Name:{}".format(record[1]))
            print("\tCustomer Account Balance:{}".format(record[2]))
            print("\tCustomer Account Pin:{}".format(record[3]))
        else:
            print("\tCustomer Account Number Doesn't Exist.")
        print("-"*70)

def viewallcd():
    with open("bankcust.data","rb") as fp:
        print("-"*70)
        print("\tACNO\tCUSTNAME\tBALANCE\tPIN")
        print("-" * 70)
        while True:
            try:
                record=pickle.load(fp)#load one by one list
                for val in record:#iterate one by one value in list
                    print("\t{}".format(val),end=" ")
                print()
            except EOFError:
                print("-"*70)
                break




