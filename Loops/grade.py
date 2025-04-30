# Create a simple grade calculator (A, B, C, D, F based on percentage).



"""
A1: 75%-100%
B2: 70%-74%
B3: 65%-69%
C4: 60%-64%
C5: 55%-59%
C6: 50%-54%
D7: 45%-49%
E8: 40%-45%
F9: 0%-39%
"""


def grade_check(grade):
    if grade >= 75:
        print("A1") 
    
    elif grade >69 and grade <= 74:
        print("B2") 
    
    elif grade >= 65 and grade <= 69:
        print("B3") 
    
    elif grade >= 60 and grade <= 64:
        print("C4") 
    
    elif grade >= 55 and grade <= 59:
        print("C5") 
    
    elif grade >= 50 and grade <= 54:
        print("C6") 
    
    elif grade >= 45 and grade <= 49:
        print("D7") 
    
    elif grade >= 40 and grade <= 45:
        print("E8") 
    
    else:
        print("Oh snr why F9?") 
    
grade = int(input("Score: "))
grade_check(grade)