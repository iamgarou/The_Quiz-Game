def opt_sort(user_opt):
    updated_opt_list = []  # Initialize an empty list for updated options
    new_opt_list = user_opt.split(",")  # Split the user input string into a list
    for opt in new_opt_list:
        opt_strip = opt.strip()  # Remove leading and trailing whitespace
        updated_opt_list.append(opt_strip.title())  # Capitalize each option and add to the updated list
    
    return updated_opt_list  # Return the list of formatted options

def all_clear():
    # Warn the user about deleting all saved questions
    print("\nCaution: This Action will delete all save Questions. Are you sure:")
    print("1. Yes")
    print("2. No")
    try:
        user_action = int(input("Your choice: "))  # Get user confirmation
        if user_action < 1 or user_action > 2:
            return print("\nChoose a number from 1/2.")  # Validate input
    except ValueError:
        return print("\nInput should be a integer.")  # Handle non-integer input
    
    if user_action == 1:
        # Clear the contents of the specified files
        for filename in ["quiz_questions.txt", "quiz_options.txt", "quiz_answers.txt"]:
            open(filename, "w").close()
        print("\nAll questions have been deleted.")  # Confirm deletion

    elif user_action == 2:
        print("Action cancelled.")  # Handle cancellation

def question_list():
    # Read and display questions, options, and answers from files
    with open("quiz_questions.txt", "r") as questions,\
            open("quiz_answers.txt", "r") as answers,\
                open("quiz_options.txt", "r") as options:
            
            print("\nQuestions:")
            for ind, question in enumerate(questions):
                print(f"{ind+1}. {question}", end="")  # Print each question with its index
            
            print("\nOptions:")
            for ind, option in enumerate(options):
                print(f"{ind+1}. {option}", end="")  # Print each option with its index

            print("\nAnswers:")
            for ind, answer in enumerate(answers):
                print(f"{ind+1}. {answer}", end="")  # Print each answer with its index

def sp_line_find(file_name, user_action):
    # Find and return a specific line in the file based on the user's action
    with open(file_name, "r") as f:
        file_line = ""
        for ind, line in enumerate(f, start=1):
            if user_action == ind:
                file_line += line  # Append the line that matches the user's choice
    
    return file_line  # Return the found line

def sp_del(file_name, del_line):
    # Delete a specific line from the specified file
    with open(file_name, "r") as f:
        lines = f.readlines()  # Read all lines from the file
    with open(file_name, "w") as f:
        for line in lines:
            if line.strip("\n") != del_line.strip():
                f.write(line)  # Write back lines that don't match the one to delete

print("Welcome to the Quiz Game\n")
print("Add your custom question and play with your friends")

while True:
    # Display menu options for the user
    print("\n1. Start Game.")
    print("2. Add a Question.")
    print("3. Remove a Specific Question.")
    print("4. Clear all Questions.")
    print("5. All Questions list.")

    try:
        user_choice = int(input("Your choice: "))  # Get user's choice
        if user_choice < 1 or user_choice > 5:
            print("Choose a number from 1/2/3/4.")
            continue  # Validate input
    except ValueError:
        print("Input should be a integer.")  # Handle non-integer input
        continue

    if user_choice == 1:
        prize_money = 0  # Initialize prize money
        total_ques_count = 0  # Initialize total question count
        total_answers = 0  # Initialize total correct answers
        try:
            # Open files to read questions, answers, and options
            with open("quiz_questions.txt", "r") as questions,\
                open("quiz_answers.txt", "r") as answers,\
                    open("quiz_options.txt", "r") as options:
                
                for question in questions:
                    total_ques_count += 1  # Increment question count
                    print(f"{question}", end="")  # Display the current question
                    iter_opt = opt_sort(options.readline())  # Get and sort options
                    for opt_no, option in enumerate(iter_opt, start=1):
                        print(f"{opt_no}. {option}")  # Display options
                    
                    try:
                        user_ans_no = int(input("Your choice: "))  # Get user's answer choice
                        if user_ans_no < 1 or user_ans_no > 4:
                            print("Choose a number from 1/2/3/4.")
                            continue
                    except ValueError:
                        print("Input should be a integer.")
                        continue
                    
                    user_ans = iter_opt[user_ans_no-1]  # Get the selected answer
                    correct_ans = answers.readline().strip().title()  # Get the correct answer

                    if user_ans == correct_ans:
                        print("\nCorrect Answer.")
                        prize_money = (prize_money + 1000) * 1.8  # Update prize money for correct answer
                        total_answers += 1  # Increment correct answer count
                        print(f"Your current prize money: {prize_money}")
                        continue

                    else:
                        print("\nIncorrect Answer.")
                        prize_money = prize_money * .66  # Deduct prize money for incorrect answer
                        print(f"Your Score: {total_answers}/{total_ques_count}")
                        print(f"Your current prize money: {prize_money}")
                        continue

        except FileNotFoundError:
            print("\nOne or more files are missing. Please add questions first.\n")
            continue  # Handle missing files

    if user_choice == 2:
        user_question = input("Your Question: ")  # Get new question from user
        if user_question == "":
            print("Question input can't be empty.")  # Validate empty question
            continue

        user_options = input("Options (o1, o2, o3, o4): ")  # Get options from user
        option_list = opt_sort(user_options)  # Sort and format options
        opt_title = user_options.title().strip()  # Title case for options
        if len(option_list) != 4:
            print("Options should be 4.")  # Validate number of options
            continue

        user_answer = input("Answer: ")  # Get the correct answer
        ans_title = user_answer.title().strip()  # Format answer
        if ans_title not in option_list:
            print("Answer should be from the given options")  # Validate answer
            continue

        # Write new question, options, and answer to files
        with open("quiz_questions.txt", "a") as questions,\
            open("quiz_answers.txt", "a") as answers,\
                open("quiz_options.txt", "a") as options:
            
            questions.write(f"{user_question.capitalize()}\n")  # Write question
            options.write(f"{opt_title}\n")  # Write options
            answers.write(f"{ans_title}\n")  # Write answer

    if user_choice == 3:
        print("\nTo remove a specific Question from the list Enter its index number:")
        print("\nQuestion list:")
        que_count = 0  # Initialize question count
        with open("quiz_questions.txt", "r") as questions:
            for ind, question in enumerate(questions):
                    print(f"{ind+1}. {question}", end="")  # Display each question
                    que_count += 1

            try:
                user_action = int(input("Your choice: "))  # Get user's choice for question removal
                if user_action < 1 or user_action > que_count:
                    print("\nChoose your Question index number.")
                    continue  # Validate input
            except ValueError:
                print("\nInput should be a integer.")
                continue
            
            print("Are you sure you want to delete this question?")  # Confirmation prompt
            print("1. Yes")
            print("2. No")
            try:
                user_action2 = int(input("Your choice: "))  # Get confirmation choice
                if user_action2 < 1 or user_action2 > 2:
                    print("\nChoose a number from 1/2.")
            except ValueError:
                print("\nInput should be a integer.")
            
            if user_action2 == 1:
                # Find and delete the specified question, option, and answer
                del_question = sp_line_find("quiz_questions.txt", user_action)
                del_option = sp_line_find("quiz_options.txt", user_action)
                del_answer = sp_line_find("quiz_answers.txt", user_action)

                sp_del("quiz_questions.txt", del_question)  # Delete question
                sp_del("quiz_options.txt", del_option)  # Delete option
                sp_del("quiz_answers.txt", del_answer)  # Delete answer

                print(f"\nQuestion no. {user_action} has been removed.")  # Confirmation of removal

            elif user_action2 == 2:
                print("Action cancelled.")  # Handle cancellation
                continue

    if user_choice == 4:
        all_clear()  # Clear all questions
        continue
        
    if user_choice == 5:
        question_list()  # Display all questions
        continue
