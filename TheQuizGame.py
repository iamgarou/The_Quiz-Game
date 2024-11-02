def opt_sort(user_opt):
    updated_opt_list = []
    new_opt_list = user_opt.split(",")
    for opt in new_opt_list:
        opt_strip = opt.strip()
        updated_opt_list.append(opt_strip.title())
    
    return updated_opt_list

def all_clear():
    print("\nCaution: This Action will delete all save Questions. Are you sure:")
    print("1. Yes")
    print("2. No")
    try:
        user_action = int(input("Your choice: "))
        if user_action<1 or user_action>2:
            return print("\nChoose a number from 1/2.")
    except ValueError:
        return print("\nInput should be a integer.")
    
    if user_action == 1:
        for filename in ["quiz_questions.txt", "quiz_options.txt", "quiz_answers.txt"]:
            open(filename, "w").close()
        print("\nAll questions have been deleted.")

    elif user_action == '2':
                print("Action cancelled.")

def question_list():
    with open("quiz_questions.txt", "r") as questions,\
            open("quiz_answers.txt", "r") as answers,\
                open("quiz_options.txt", "r") as options:
            
            print("\nQustions:")
            for ind, question in enumerate(questions):
                print(f"{ind+1}. {question}", end="")
            
            print("\nOptions:")
            for ind, option in enumerate(options):
                print(f"{ind+1}. {option}", end="")

            print("\nAnswers:")
            for ind,answer in enumerate(answers):
                print(f"{ind+1}. {answer}", end="")
            

def sp_line_find (file_name, user_action):
    with open(file_name, "r") as f:
        file_line = ""
        for ind, line in enumerate(f, start=1):
            if user_action == ind:
                file_line+= line
    
    return file_line


def sp_del(file_name, del_line):
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        for line in lines:
            if line.strip("\n") != del_line.strip():
                f.write(line)

print("Welcome to the Quiz Game\n")
print("Add your cutom question and play with your friends")

while True:
    print("\n1. Start Game.")
    print("2. Add a Question.")
    print("3. Remove a Specific Question.")
    print("4. Clear all Question.")
    print("5. All Questions list.")

    try:
        user_choice = int(input("Your choice: "))
        if user_choice<1 or user_choice>5:
            print("Choose a number from 1/2/3/4.")
            continue
    except ValueError:
        print("Input should be a integer.")
        continue

    if user_choice == 1:
        prize_money = 0
        total_ques_count = 0
        total_answers = 0
        try:
            with open("quiz_questions.txt", "r") as questions,\
                open("quiz_answers.txt", "r") as answers,\
                    open("quiz_options.txt", "r") as options:
                
                for question in questions:
                    total_ques_count += 1
                    print(f"{question}", end="")
                    iter_opt = opt_sort(options.readline())
                    for  opt_no, option in enumerate(iter_opt, start= 1):
                        print(f"{opt_no}. {option}")
                    
                    try:
                        user_ans_no = int(input("Your choice: "))
                        if user_ans_no<1 or user_ans_no>4:
                            print("Choose a number from 1/2/3/4.")
                            continue
                    except ValueError:
                        print("Input should be a integer.")
                        continue
                    
                    user_ans = iter_opt[user_ans_no-1]
                    correct_ans = answers.readline().strip().title()

                    if user_ans == correct_ans:
                        print("\nCorrect Answer.")
                        prize_money = (prize_money+1000)*1.8
                        total_answers += 1
                        print(f"Your current prize money: {prize_money}")
                        continue

                    else:
                        print("\nIncorrect Answer.")
                        prize_money = prize_money*.66
                        print(f"Your Score: {total_answers}/{total_ques_count}")
                        print(f"Your current prize money: {prize_money}")
                        continue

                    


        except FileNotFoundError:
            print("\nOne or more files are missing. Please add questions first.\n")
            continue

    if user_choice == 2:
        user_question = input("Your Question: ")
        if user_question == "":
            print("Question input can't be empty.")
            continue

        user_options = input("Options (o1, o2, o3, o4): ")
        option_list = opt_sort(user_options)
        opt_title = user_options.title().strip()
        if len(option_list) != 4:
            print("Options should be 4.")
            continue

        user_answer = input("Answer: ")
        ans_title = user_answer.title().strip()
        if ans_title not in option_list:
            print("Answer should be from the given options")
            continue

        with open("quiz_questions.txt", "a") as questions,\
            open("quiz_answers.txt", "a") as answers,\
                open("quiz_options.txt", "a") as options:
            
            questions.write(f"{user_question.capitalize()}\n")
            options.write(f"{opt_title}\n")
            answers.write(f"{ans_title}\n")

    if user_choice == 3:
        print("\nTo remove a specific Question from the list Enter it's index number:")
        print("\nQuestion list:")
        que_count = 0
        with open("quiz_questions.txt", "r") as questions:
            for ind, question in enumerate(questions):
                    print(f"{ind+1}. {question}", end="")
                    que_count+= 1

            try:
                user_action = int(input("Your choice: "))
                if user_action<1 or user_action>que_count:
                    print("\nChoose your Question index number.")
                    continue
            except ValueError:
                print("\nInput should be a integer.")
                continue
            print("Are you sure you want to delete this question?")
            print("1. Yes")
            print("2. No")
            try:
                user_action2 = int(input("Your choice: "))
                if user_action<1 or user_action>2:
                    print("\nChoose a number from 1/2.")
            except ValueError:
                print("\nInput should be a integer.")
            
            if user_action2==1:
                del_question = sp_line_find("quiz_questions.txt",user_action)
                del_option = sp_line_find("quiz_options.txt",user_action)
                del_answer = sp_line_find("quiz_answers.txt",user_action)

                    
                sp_del("quiz_questions.txt", del_question)
                sp_del("quiz_options.txt", del_option)
                sp_del("quiz_answers.txt", del_answer)

                print(f"\nQuestion no. {user_action} has been removed.")

            elif user_action == '2':
                print("Action cancelled.")
                continue

    if user_choice == 4:
        all_clear()
        continue
        
    if user_choice == 5:
        question_list()
        continue