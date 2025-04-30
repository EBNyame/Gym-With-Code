# Check if a person is eligible to vote (age ≥ 18).

def eligible(age):
   
    if age < 18:
        remaining = 18 - age
        print(f"Heyy you're not eligible to vote now, wait for {remaining} more year(s)")
    else:
        print(f"You're currently {age} years old and you're eligible to vote")


age = int(input("your age: "))
eligible(age)