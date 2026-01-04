#This is one of my most dangerous (pseudo)viruses, haha!
import time
import subprocess
Q=(1)
print("Haha! You're got an M-landish language virus! Would You like to learn alphabet? (YES/NO)")
A=input()
if A=="NO":
    print("OK, goodbye! See You next time...")
if A!="YES" and A!="NO":
    print("I think that You're have gone crazy...anyways goodbye")

#DANGER ZONE!!!

B=(10)
if A=="YES":
    print("OK. Wait 10 sec...")
    print(B)
    for counter in range(10):
        B=B-1
        print(B)
        time.sleep(1)
    print("LET'S BEGIN!!!")
    Y="""
    while True:
        print("a ä â f ḟ x × k ḱ n ń m ḿ í î e ë ê l ĺ o ö ô u ü û d ḋ ð")
        """
    CODE="""
    Q=Q+1
    filename=(Q)
    with open(filename, "w", ecoding="utf-8") as file:
        file.write(Y)
    result = subprocess.run(["python", filename], capture_output=True, text=True)
    """
    
    while True:
        print("a ä â f ḟ x × k ḱ n ń m ḿ í î e ë ê l ĺ o ö ô u ü û d ḋ ð")
        filename=(Q)
        with open(filename, "w", ecoding="utf-8") as file:
            file.write(CODE)
        result = subprocess.run(["python", filename], capture_output=True, text=True)
#The end. I hope You enjoy my work!
