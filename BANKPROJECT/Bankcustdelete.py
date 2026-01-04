import pickle

def deletecustomer():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        print("-"*70)
        cusaccno=int(input("\tEnter Customer Account Number:"))
        res=False
        for index in range(len(records)):#take this logic for updation and deletion ease to access index.
            if records[index][0]==cusaccno:
                res=True
                recindex=index
                break
        print("-"*70)
        if res:
            del records[recindex]
            with open("bankcust.data","wb") as fp:
                for record in records:
                    pickle.dump(record,fp)
                print("\tCustomer Records Deleted Successfully.")
        else:
            print("\tCustomer Account Number Not Found.")
        print("-"*70)


