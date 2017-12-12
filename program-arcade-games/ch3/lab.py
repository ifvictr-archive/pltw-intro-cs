total_questions = 0
total_correct = 0

def prompt(question, correct_answer):
    """
    `question` should be the question to be asked
    `correct_answer` should be the answer expected from the user
    """
    global total_questions
    global total_correct

    inputted_answer = raw_input(question + "\n> ")
    total_questions += 1
    if correct_answer.lower() == inputted_answer.lower():
        total_correct += 1
        print("That's correct! :)")
    else:
        print("That's wrong... :P")

def result():
    """
    Displays the current running totals based on the questions completed
    """
    print("\nCongrats! You got " + str(total_correct) + " question(s) right!")
    print("That's a " + str(int(float(total_correct) / float(total_questions) * 100)) + "%.")

# Main
print("Time for a short quiz!")
# Question 1
prompt("What is 2 + 2?", "4")
# Question 2
prompt("""
What is Google?

a) A company that manufactures goo
b) A search engine that collects a lot of information about you
c) A funny-sounding word
""", "b")
# Question 3
prompt("The Silicon Valley is located in Los Angeles, California. True (T) or false (F)?", "f")
# Question 4
prompt("What does `True and False` equate to?", "false")
# Question 5
prompt("What year was the United States of America founded?", "1776")
result()