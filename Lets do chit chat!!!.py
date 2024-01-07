print("Welcome to a unique chit chat!!!")
int=0
prize=2000
Question=[["Q1. Who invented the first flying airplane","A. Wright Brothers","B. John Brothers","C. Pathan Brothers","D. Mehta Brothers",'A'],
   ["Q2. First person to step on the moon","A. Edwin Aldrin","B. Kalpana Chawla","C. Neil Armstrong","D. Shilpa Sharma","C"],
   ["Q3. First Prime Minister of India","A. Dr. Rajendra Prasad","B. Sardar Vallabhai Patel","C. Mahatma Gandhi","D. Dr. Jawaharlal Nehru","D"]
   ]
while True:
    c=Question[int]    
    for i in c:
        print(i)
    b=input("Choose the correct option A-Z ")
    b=b.upper()
    if b==c[5]:
        print("CORRECT ANSWER!!\nYou have won Rs.",prize,"\nNext Question:")
    else:
        print("Incorrect answer :(\nTry Again next time!")
        break
    if prize==6000:
        print("Congratulations You have won the Game!!")
        break
    int=int+1
    prize=prize+2000