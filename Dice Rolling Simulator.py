import random

start_input = input('Type "play" to roll the die: ')

if start_input == 'play':
    low = 1; high = 6
    ran_number = random.uniform(low, high)
    print (int(ran_number))
    
func_input = input('Role Again? ')

while func_input == 'yes':
    if ran_number > 0 and func_input == 'yes':
        low = 1; high = 6
        ran_number = random.uniform(low, high)
        print (int(ran_number))
        func_input = input('Role Again? ')
    
    if ran_number > 0 and func_input == 'no':
        print("Thanks for playing!")
        break
        
       
        
            
        
    


    
