import pickle
def pingenerate():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        cusacc=int(input("\tEnter Customer Account Number:"))
        res=False
        for index in range(len(records)):
            if records[index][0]==cusacc and  records[index][3]== None:
                res=True
                break
        print("-"*70)
        if res:
            pin=input("\tEnter Pin Number(Pin Number Must Be 6 Digits):")#int has no length so to make our pin 6 digit we take pin as str
            if pin.isdigit() and len(pin)==6:
                pin=int(pin)
                records[index][3]=pin
                with open("bankcust.data","wb") as fp:
                    for record in records:
                        pickle.dump(record,fp)
                    print("\tPin Number Generated Successfully.")
            else:
                print("\tDon't Enter Alphabets and Symbol For Pin (Pin Must Be 6 Digits).")
        else:
            print("\tEither Customer Account Number In-Valid or Pin Number Already Generated.")
        print("-"*70)


def pinupdate():
    with open("bankcust.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        custacc=int(input("\tEnter Customer Account Number:"))
        res=False
        for index in range(len(records)):
            if records[index][0]==custacc and records[index][3]!= None:
                res=True
                break
        if res:
            updatepin=input("\tEnter Pin Number(Pin Number Must Be 6 Digits):")
            if updatepin.isdigit() and len(updatepin)==6 and int(updatepin)!=records[index][3]:
                updatepin=int(updatepin)
                records[index][3]=updatepin
                with open("bankcust.data","wb") as fp:
                    for record in records:
                        pickle.dump(record,fp)
                    print("\tPin Number Updated Successfully.")
            else:
                print("\tDon't Enter Alphabets,Symbol For Pin And Don't Enter Old Pin As New Pin (Pin Must Be 6 Digits) .")
        else:
            print("\tEither Customer Account Number In-valid or Pin Number Not Generated.")
