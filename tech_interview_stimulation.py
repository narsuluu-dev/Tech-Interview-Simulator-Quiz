from datetime import datetime

# Get current date and time
now = datetime.now()
print(f"Date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

#  Main function
def main():
    # Welcoming message 
    print("Welcome to the Tech Interview Simulator!")
    print("Let's get to know more about you!\n") 

    # Get user's name and last name 
    name = input("Enter your name: ")
    last = input("Enter your last name: ")
    age = int(input("Enter your age: ")) 

    print(f"\nAlright {name} {last}, we are about to start!\n")  

    score, a1, a2, a3, a4 = interview_questions()

    show_results(score)

    save_to_file(score, a1, a2, a3, a4, name, last, age)

#  Ask questions & calculate score
def interview_questions():   
    score = 0

    # Q1
    answer1 = input( 
        "1. Why do you want to work in tech?\n"
        "a) I want to grow my skills and solve real-world problems.\n" 
        "b) I heard tech pays well.\n"
        "c) I don’t really know yet.\n> "
    )

    if answer1 == "a": 
        score += 2 
    elif answer1 == "b":
        score += 1 
   

    # Q2
    answer2 = input(
        "\n2. What do you do when you're stuck on a coding problem?\n"
        "a) Give up and blame the bug.\n"
        "b) Search online, then ask for help if needed.\n"
        "c) Wait until someone else solves it.\n> "
    )

    if answer2 == "b":
        score += 2
    elif answer2 == "c":
        score += 1  

    

    # Q3
    answer3 = input(
        "\n3. What’s more important to you?\n"
        "a) Always getting things right on the first try.\n"
        "b) Learning and improving consistently.\n"
        "c) Avoiding mistakes at all cost.\n> "
    )

    if answer3 == "b":
        score += 2
    elif answer3 == "c":
        score += 1 
  
    # Q4
    answer4 = input(
        "\n4. You’re given a task in a language you’ve never used. What do you do?\n"
        "a) Refuse the task — you’re not ready.\n"
        "b) Start learning the basics immediately and give it a try.\n"
        "c) Ask someone else to do it for you.\n> "
    )

    if answer4 == "b":
        score += 2
    elif answer4 == "c":
        score += 1

    return score, answer1, answer2, answer3, answer4 

#  Show results based on score
def show_results(score):  
    print(f"\nYour total score: {score}/8")
     
    if score >= 7: 
        print("🎉 You are hired!")
    elif score >= 5:  
        print("👍 Not bad — you're on the right track.")
    else:
        print("💡 Don't worry. With hard work, you can succeed!")

#  Save interview summary to file
def save_to_file(score, answer1, answer2, answer3, answer4, name, last, age):
    now = datetime.now()

    with open("tech_interview_simulation.txt", "a", encoding="utf-8") as file: 
        file.write(f"-- Completed on {now.strftime('%Y-%m-%d %H:%M:%S')} --\n")
        file.write(f"Name: {name} {last}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Question 1: {answer1}\n")
        file.write(f"Question 2: {answer2}\n")
        file.write(f"Question 3: {answer3}\n")
        file.write(f"Question 4: {answer4}\n")
        file.write(f"Final Score: {score}/8\n")
        file.write("-" * 40 + "\n\n")  

# Run the app
main()  




  













    



