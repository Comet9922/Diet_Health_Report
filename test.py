guess_me = 7
number = 1 
while True:
    if number < guess_me:
        print("too low")
    if number == guess_me:
        print("fount it! number is ", number)
        break
    if number >= guess_me:
        print("oops")
        break
    number += 1
    
        
        