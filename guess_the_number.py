import random
#r_n=random.randint(0,2000)            #random number generator..
#print("random number:",r_n)
#str_r_n=str(r_n)
#
def rule():
         print("\t\t\t\tFIND THE HIDDEN NUMBER")   
         print("rule-1:in this game you have to find the hidden number that computer generated")
         print("rule-2:you will have only 7 guess's ")
         print("rule-3:in this game 'liza'(the computer ) will help you a bit.. \n have  a good luck.")

ran_1=random.randint(2,3)
                              # random number generator with specific digits ..
def random_num_gen(ran_1):
    range_start=10**(ran_1-1)
    range_end=(10**ran_1)-1

    guess_num= random.randint(range_start,range_end)
    # print("its is ",ran_1," digit number :",guess_num)
    return guess_num
    

random_num_gen(ran_1)

def guessing(guess_n):
    if ran_1<3:
        print("liza : your guess numbers is ",ran_1,"digit number ")
        i=0
        
        while(5==5):
            i=i+1

            my_ans=int(input("your ans plz \n-->"))
            if my_ans==guess_n:
                print("liza : congratulation, you are the winner ") 
                print("liza : complete guessing in only",i,"guess's")
                break
            elif (i==7):
                print("GAME OVER")
                print("liza : THE HIDDEN NUMBER WAS :",guess_n,)
                break    
                
            elif my_ans<guess_n:
                print("liza : move forward")
                print("liza : guess's  reamining :" ,7-i)
            elif my_ans>guess_n:
                print("liza : move backward")
                print("liza : guess's  reamining :" ,7-i)
            

            

    #for 3 digits 
    if ran_1>2 :
        print("your guess numbers is ",ran_1,"digit number ")
        i=0
        str_guess_num=str(guess_n)
        first_str_guess_num=int(str_guess_num[0])*100
        
        print("HINT : your guess number is in between",first_str_guess_num, "and",first_str_guess_num+100)
        while(5==5):
            i=i+1

            my_ans=int(input("your ans plz \n-->"))
            if my_ans==guess_n: 
                print("liza : congratulation, you are the winner ")
                print("liza : complete guessing in only",i,"guess's")
                break
            elif (i==7):
                print("GAME OVER")
                print("liza : THE HIDDEN NUMBER WAS :",guess_n,)
                break    
                
            elif my_ans<guess_n:
                print("liza : move forward")
                print("liza : guess's  reamining :" ,7-i)
            elif my_ans>guess_n:
                print("liza : move backward")
                print("liza : guess's  reamining :" ,7-i)
            

 

#guessing(guess_num)
def main():
    rule()
    guess_n=random_num_gen(ran_1)
    guessing(guess_n)

main()