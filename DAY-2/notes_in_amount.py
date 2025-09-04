def notes(amount):
    notes=[2000,1000,500,200,100,50,20,10,5,2,1]
    notes_count={}
    for note in notes:
        if amount>=note:
            count=amount//note
            notes_count[note]=count
            amount=amount%note
    return notes_count
n=int(input("Enter amount: "))
print(f"number of notes in {n}rupees is {notes(n)}")