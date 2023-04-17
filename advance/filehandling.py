while(True):
    rate = float(input("rate: "))
    action = input("press y for next and n for end")

    with open("gr.txt", "a") as f:
        data = f"rate:{rate}:"
        f.write(data)
    if action == "n":
        break
rate = 0
with open("gr.txt","r") as f:
    data = f.read()

    data_list = data.split(":")
    print(data_list)
    for i in data_list:
        if not i == "rate" and len(i)>1:
            print(i)
            rate += float(i)
print("Total: ",rate)
