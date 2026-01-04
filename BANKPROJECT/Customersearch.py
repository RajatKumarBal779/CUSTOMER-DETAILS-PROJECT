import pickle
def searchcust():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        custaccno=int(input("Enter Customer Account Number:"))
        res=True
        for record in records:
            if record[0]==custaccno:
                res=False
                break
        print("-"*70)
        if not res:
            print("\tCustomer Account Number Found And Valid.")
        else:
            print("\tCustomer Account Number Doesn't Exist, In-Valid.")
        print("-"*70)
