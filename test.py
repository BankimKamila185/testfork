# Simple MCQ Exam in Python (Easy Mode)

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
        "correct_answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "correct_answer": "B"
    }
]


# Initialize score
score = 0

# Function to ask a question and check the answer
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    user_answer = input("Your answer (A, B, C, or D): ").upper()
    
    if user_answer == question["correct_answer"]:
        print("Correct!")
        return 1
    else:
        print(f"Sorry, the correct answer was {question['correct_answer']}.")
        return 0

# Main exam loop
print("Welcome to the Easy MCQ Exam!")
print("Please answer the following questions:\n")

for question in questions:
    score += ask_question(question)
    print()  # Add a blank line between questions

# Display final score
total_questions = len(questions)
print(f"Exam completed! Your score: {score}/{total_questions}")
print(f"Percentage: {(score/total_questions)*100:.2f}%")
