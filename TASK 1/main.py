
#Guess The No:

# import random
# rand_num=[2,5,-1,10,8,13,20,25]
# random_no=random.choice(rand_num)

# while True:
        
#     guess=int(input("enter the minimum and maximum num :"))
#     if guess > random_no:
#         print("Too high")
#     elif guess < random_no:
#         print("Too low")
#     else: 
#         print("correct")      
#         break


#WORD SCRAMBLE
import random
words=["python","javascript","java","automation","selenium","guvi","selenium"]
rand=random.choice(words)
letter=list(rand)
random.shuffle(letter)
unscramble_words =''.join(letter)
print("unscrambled word:", unscramble_words )
while True:
    guess=(input("enter the word :"))
    if guess == rand:
        print("correct")
        break
    else:
        print("Try again")

