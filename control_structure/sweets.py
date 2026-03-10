def select(john, jane, james):
    if john > jane:
        both = john +jane
        print(f"Both john and james have a total of {both} sweets")

        if john > james:
            print("john has more sweets than jane and james")
        else:
            print("john has less sweets than james")    
    elif jane >james:
        print ("jane has more sweets than james")  
    elif james == jane and james == john:
        print("john, jane, and james have the same number of sweets")
    else:
        print("james has more sweets than john and jane")

select(5, 3, 2)



