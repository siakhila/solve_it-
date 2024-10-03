import random
import time 

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL = 5


def problem_generator():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left)+ " " +operator + " " + str(right)
    answer = eval(expr)
    return expr,answer



expr, answer = problem_generator()
print(expr, answer)


for i in range(TOTAL):
    expr, answer = problem_generator()
    
    start_time = time.time()  # Start timing
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        
        if guess == str(answer):
            end_time = time.time()  # End timing
            time_taken = end_time - start_time
            print(f"Correct! Time taken: {time_taken:.2f} seconds\n")
            break  # Exit the loop after the correct answer
        else:
            print("Incorrect. Try again!\n")  # Provide immediate feedback

print("All problems completed!")

