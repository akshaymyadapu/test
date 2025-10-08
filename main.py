from operations import saving_account,Business_account



print("1. Saving account")
print("2. Business account")
choose=int(input("choose one option: "))
if choose == 1:
    print("You have chosen saving account")
    saving_account()
elif choose == 2:
    print("You have chosen business account")
else:
    print("Invalid option")
