print("""Hi Friends. I would Like To Play a Game With You 
            The Rule Of The Game Is To Prediction Your Final Answer With, Your Question. 
            The Question Must Contain ONLY NUMBERS Of 4 Digits.
             
            You Must Have To Give 3 Sets Of 4 Digit Number.
            Then I Give 2 Sets Of 4 Digits Number Each Time Its Completed.
            Your WORK is to ADD Every Thing Except My PREDICTION
            Come Let's Start""")
try:
    def main():

        while True:
            in1 = int(input("Enter Any 4 Digit Numbers That's Come's In Your Mind:- "))
            sin1 = str(in1)
            if len(sin1) == 4:
                A = 20000 + in1
                print("My PREDICTION is ", str(A))
                break

            else:
                print("Enter 4 Digit Number Only")
        while True:
            arr = [1,2]

            for i in arr:
                in2 = int(input("Enter Any 4 Numbers:- "))
                sin2 = str(in2)
                if len(sin2) == 4:
                    B = 10000 - in2
                    B1 = str(B)
                    if len(B1) == 3:
                        print("Now My Turn. My Answer Of %d"%i,end="")
                        print(" Number Is 0", str(B))

                    elif len(B1) == 2:
                        print("Now My Turn. My Answer Of %d"%i,end="")
                        print(" Number Is 00", str(B))

                    elif len(B1) == 1:
                        print("Now My Turn. My Answer Of %d"%i,end="")
                        print(" Number Is 000", str(B))

                    else:
                        print("Now My Turn. My Answer Of %d"%i,end="")
                        print(" Number Is ", str(B))


                else:
                    print("Enter 4 Digit Number Only")
                    break

            if i == 2:
                break
    main()

except Exception:
    print("Your Entered Wrong Input. Only Numbers")


