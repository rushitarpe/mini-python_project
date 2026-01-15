
import random
import os

# ==================== HANGMAN ASCII ART ====================
HANGMAN_STAGES = [
    # Stage 0: Empty
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    # Stage 1: Head
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    # Stage 2: Body
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    # Stage 3: Left Arm
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    # Stage 4: Right Arm
    """
       ------
       |    |
       |    O
       |   /|\
       |
       |
    --------
    """,
    # Stage 5: Left Leg
    """
       ------
       |    |
       |    O
       |   /|\ 
       |   /
       |
    --------
    """,
    # Stage 6: Right Leg (Game Over)
    """
       ------
       |    |
       |    O
       |   /|\ 
       |   / \ 
       |
    --------
    """
]
# Total 50 Python Programming questions
QUESTIONS = {
    "Python Basics": [
        {"question": "Who created Python?", "options": ["A) James Gosling", "B) Guido van Rossum", "C) Dennis Ritchie", "D) Bjarne Stroustrup"], "answer": "B"},
        {"question": "What is the correct file extension for Python files?", "options": ["A) .python", "B) .pl", "C) .py", "D) .p"], "answer": "C"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["A) function", "B) def", "C) fun", "D) define"], "answer": "B"},
        {"question": "Which of these is NOT a Python data type?", "options": ["A) list", "B) dictionary", "C) tuple", "D) array"], "answer": "D"},
        {"question": "What symbol is used for comments in Python?", "options": ["A) //", "B) /* */", "C) #", "D) --"], "answer": "C"},
        {"question": "Which method is used to add an element to a list?", "options": ["A) add()", "B) append()", "C) insert()", "D) push()"], "answer": "B"},
        {"question": "What is the output of: print(type([]))?", "options": ["A) <class 'list'>", "B) <class 'array'>", "C) <class 'tuple'>", "D) <class 'dict'>"], "answer": "A"},
        {"question": "Which operator is used for exponentiation in Python?", "options": ["A) ^", "B) **", "C) //", "D) %"], "answer": "B"},
        {"question": "What does 'len()' function do?", "options": ["A) Deletes elements", "B) Returns length", "C) Sorts items", "D) Reverses order"], "answer": "B"},
        {"question": "Which statement is used to exit a loop?", "options": ["A) exit", "B) stop", "C) break", "D) end"], "answer": "C"},
    ],
    "Python Data Structures": [
        {"question": "Which data structure is immutable in Python?", "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"], "answer": "D"},
        {"question": "How do you create an empty dictionary?", "options": ["A) []", "B) {}", "C) ()", "D) <>"], "answer": "B"},
        {"question": "Which method removes and returns the last element of a list?", "options": ["A) remove()", "B) delete()", "C) pop()", "D) clear()"], "answer": "C"},
        {"question": "What is the output of: [1,2,3] + [4,5,6]?", "options": ["A) [1,2,3,4,5,6]", "B) [5,7,9]", "C) Error", "D) [15]"], "answer": "A"},
        {"question": "Which method is used to get all keys from a dictionary?", "options": ["A) values()", "B) items()", "C) keys()", "D) getkeys()"], "answer": "C"},
        {"question": "What does 'set()' create?", "options": ["A) List", "B) Tuple", "C) Set", "D) Dictionary"], "answer": "C"},
        {"question": "How do you access the first element of a list 'mylist'?", "options": ["A) mylist[0]", "B) mylist[1]", "C) mylist.first()", "D) mylist(0)"], "answer": "A"},
        {"question": "Which data structure doesn't allow duplicate values?", "options": ["A) List", "B) Tuple", "C) Set", "D) Dictionary"], "answer": "C"},
        {"question": "What is the output of: len({'a':1, 'b':2})?", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "B"},
        {"question": "Which slicing operation gives the last element?", "options": ["A) list[0]", "B) list[-1]", "C) list[last]", "D) list.end()"], "answer": "B"},
    ],
    "Python Control Flow": [
        {"question": "Which keyword is used for conditional statements?", "options": ["A) switch", "B) if", "C) case", "D) when"], "answer": "B"},
        {"question": "What does 'elif' stand for?", "options": ["A) else if", "B) elseif", "C) electric if", "D) eliminate if"], "answer": "A"},
        {"question": "Which loop is used to iterate over a sequence?", "options": ["A) while", "B) do-while", "C) for", "D) loop"], "answer": "C"},
        {"question": "What does 'continue' do in a loop?", "options": ["A) Exits loop", "B) Skips current iteration", "C) Restarts loop", "D) Pauses loop"], "answer": "B"},
        {"question": "Which statement is used to handle exceptions?", "options": ["A) try-except", "B) catch-throw", "C) error-handle", "D) do-catch"], "answer": "A"},
        {"question": "What is the output of: 5 == 5.0?", "options": ["A) False", "B) True", "C) Error", "D) None"], "answer": "B"},
        {"question": "Which keyword is used to create a loop that runs indefinitely?", "options": ["A) for", "B) while True", "C) loop", "D) infinite"], "answer": "B"},
        {"question": "What does 'pass' statement do?", "options": ["A) Exits function", "B) Does nothing", "C) Raises error", "D) Breaks loop"], "answer": "B"},
        {"question": "Which operator is used for logical AND?", "options": ["A) &&", "B) &", "C) and", "D) AND"], "answer": "C"},
        {"question": "What is the output of: not False?", "options": ["A) False", "B) True", "C) 0", "D) 1"], "answer": "B"},
    ],
    "Python Functions & Modules": [
        {"question": "What keyword is used to return a value from a function?", "options": ["A) return", "B) give", "C) output", "D) send"], "answer": "A"},
        {"question": "How do you import a module named 'math'?", "options": ["A) include math", "B) import math", "C) using math", "D) require math"], "answer": "B"},
        {"question": "What is a lambda function?", "options": ["A) Named function", "B) Anonymous function", "C) Class method", "D) Built-in function"], "answer": "B"},
        {"question": "Which keyword is used to create a default parameter?", "options": ["A) default", "B) =", "C) :", "D) ->"], "answer": "B"},
        {"question": "What does '*args' do in a function?", "options": ["A) Multiply arguments", "B) Accept variable arguments", "C) Required argument", "D) Return multiple values"], "answer": "B"},
        {"question": "How do you import only 'sqrt' from math module?", "options": ["A) import sqrt from math", "B) from math import sqrt", "C) import math.sqrt", "D) using math.sqrt"], "answer": "B"},
        {"question": "What is the purpose of '__init__' method?", "options": ["A) Delete object", "B) Initialize object", "C) End program", "D) Import module"], "answer": "B"},
        {"question": "Which function converts a string to integer?", "options": ["A) str()", "B) float()", "C) int()", "D) num()"], "answer": "C"},
        {"question": "What does 'global' keyword do?", "options": ["A) Delete variable", "B) Access global variable", "C) Create constant", "D) Import module"], "answer": "B"},
        {"question": "How do you create a docstring?", "options": ["A) // comment", "B) /* comment */", "C) # comment", "D) '''comment'''"], "answer": "D"},
    ],
    "Python OOP & Advanced": [
        {"question": "Which keyword is used to create a class?", "options": ["A) class", "B) define", "C) object", "D) create"], "answer": "A"},
        {"question": "What is inheritance in OOP?", "options": ["A) Hiding data", "B) Deriving from parent class", "C) Creating objects", "D) Deleting classes"], "answer": "B"},
        {"question": "Which method is called when an object is created?", "options": ["A) __new__", "B) __init__", "C) __create__", "D) __start__"], "answer": "B"},
        {"question": "What does 'self' represent in a class?", "options": ["A) Class name", "B) Instance of class", "C) Method name", "D) Parent class"], "answer": "B"},
        {"question": "Which decorator is used for static methods?", "options": ["A) @static", "B) @staticmethod", "C) @classmethod", "D) @method"], "answer": "B"},
        {"question": "What is encapsulation?", "options": ["A) Data hiding", "B) Data sharing", "C) Data deletion", "D) Data sorting"], "answer": "A"},
        {"question": "How do you create a private variable in Python?", "options": ["A) private var", "B) _var", "C) __var", "D) var_"], "answer": "C"},
        {"question": "What is polymorphism?", "options": ["A) One form", "B) Many forms", "C) No form", "D) Two forms"], "answer": "B"},
        {"question": "Which method is used to convert object to string?", "options": ["A) __str__", "B) __string__", "C) toString()", "D) str()"], "answer": "A"},
        {"question": "What does 'super()' function do?", "options": ["A) Delete parent", "B) Call parent class", "C) Create superclass", "D) Override method"], "answer": "B"},
    ]
}
#======================Adding helper funtions=====================
def clear_screen():
    """Clear the console screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(wrong_count):
    """Display the hangman ASCII art based on wrong answers"""
    print(HANGMAN_STAGES[wrong_count])

def display_header(lives, score, category):
    """Display game header with current stats"""
    print("=" * 60)
    print(" " * 20 + "QUIZ HANGMAN GAME")
    print("=" * 60)
    print(f"Category: {category} | Lives Remaining: {lives} | Score: {score}")
    print("=" * 60)

def get_all_questions():
    """Combine all questions from all categories into a single list"""
    all_questions = []
    for category, questions in QUESTIONS.items():
        for question in questions:
            question_with_category = question.copy()
            question_with_category['category'] = category
            all_questions.append(question_with_category)
    return all_questions

def ask_question(question_data, question_number, total_questions):
    """Display a question and get user's answer"""
    print(f"\nQuestion {question_number}/{total_questions}")
    print(f"Category: {question_data['category']}")
    print(f"\n{question_data['question']}")
    print()
    
    for option in question_data['options']:
        print(f"  {option}")
    
    print()
    
    # Input validation
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input! Please enter A, B, C, or D.")

def display_result(is_correct, correct_answer):
    """Display whether the answer was correct or wrong"""
    if is_correct:
        print("\n✓ CORRECT! Well done!")
    else:
        print(f"\n✗ WRONG! The correct answer was: {correct_answer}")
    print()

def display_game_over(won, score, total_questions):
    """Display the final game over screen"""
    clear_screen()
    print("\n" + "=" * 60)
    
    if won:
        print(" " * 20 + "🎉 CONGRATULATIONS! 🎉")
        print("=" * 60)
        print(f"\nYou answered all questions correctly!")
        print(f"Final Score: {score}/{total_questions}")
        print("\nYou saved the hangman! 🎊")
    else:
        print(" " * 22 + "GAME OVER")
        print("=" * 60)
        display_hangman(6)
        print(f"\nThe hangman is complete... You lost!")
        print(f"Final Score: {score}/{total_questions}")
    
    print("=" * 60)
    # ==================== MAIN GAME LOGIC ====================

def play_game():
    """Main game loop"""
    MAX_LIVES = 6
    MAX_QUESTIONS = 15  # Limit to 15 questions per game
    lives = MAX_LIVES
    score = 0
    wrong_count = 0
    
    # Get and shuffle questions
    all_questions = get_all_questions()
    random.shuffle(all_questions)
    
    # Select only 15 random questions from the 50
    selected_questions = all_questions[:MAX_QUESTIONS]
    total_questions = len(selected_questions)
    
    clear_screen()
    print("\n" + "=" * 60)
    print(" " * 15 + "WELCOME TO QUIZ HANGMAN!")
    print("=" * 60)
    print("\nRules:")
    print("• Answer multiple-choice quiz questions correctly to survive")
    print("• Each wrong answer adds a body part to the hangman")
    print(f"• You have {MAX_LIVES} lives (wrong answers allowed)")
    print(f"• You will answer {MAX_QUESTIONS} random questions from 50 available")
    print("• Answer all questions correctly to WIN!")
    print("• Complete the hangman figure and you LOSE!")
    print("\nGood luck! 🍀")
    print("=" * 60)
    input("\nPress Enter to start the game...")
    
    # Main game loop
    for i, question_data in enumerate(selected_questions, 1):
        clear_screen()
        
        # Display current game state
        display_header(lives, score, question_data['category'])
        display_hangman(wrong_count)
        
        # Ask question and get answer
        user_answer = ask_question(question_data, i, total_questions)
        
        # Check if answer is correct
        is_correct = (user_answer == question_data['answer'])
        
        if is_correct:
            score += 1
            display_result(True, question_data['answer'])
        else:
            lives -= 1
            wrong_count += 1
            display_result(False, question_data['answer'])
        
        # Check if game over
        if lives == 0:
            input("Press Enter to see final result...")
            display_game_over(False, score, total_questions)
            return False
        
        # Wait for user before continuing
        if i < total_questions:
            input("Press Enter to continue to next question...")
    
    # Player answered all questions with lives remaining - WIN!
    display_game_over(True, score, total_questions)
    return True

def main():
    """Main program entry point"""
    while True:
        play_game()
        
        # Ask if player wants to play again
        print("\n" + "=" * 60)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if play_again not in ['yes', 'y']:
            clear_screen()
            print("\n" + "=" * 60)
            print(" " * 15 + "Thanks for playing!")
            print(" " * 12 + "Quiz Hangman Game v1.0")
            print("=" * 60 + "\n")
            break

# ==================== PROGRAM EXECUTION ====================

if __name__ == "__main__":
    main()