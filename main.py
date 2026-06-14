# Quiz Application

score = 0

print("===== Welcome to Python Quiz =====")

# Question 1
print("\n1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
print("d) Chennai")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Delhi.")

# Question 2
print("\n2. Who developed Python?")
print("a) James Gosling")
print("b) Dennis Ritchie")
print("c) Guido van Rossum")
print("d) Bjarne Stroustrup")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Guido van Rossum.")

# Question 3
print("\n3. Which keyword is used to create a function in Python?")
print("a) function")
print("b) define")
print("c) def")
print("d) fun")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is def.")

# Question 4
print("\n4. Which data type stores True or False?")
print("a) int")
print("b) string")
print("c) float")
print("d) bool")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is bool.")

# Question 5
print("\n5. Which symbol is used for comments in Python?")
print("a) //")
print("b) #")
print("c) /*")
print("d) --")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is #.")

# Final Score
print("\n===== Quiz Finished =====")
print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent! 🎉")
elif score >= 3:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 📚")