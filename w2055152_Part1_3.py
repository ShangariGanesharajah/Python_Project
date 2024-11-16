# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2021001
# UoW ID: w2055152
# Date: 11.12.2023

from graphics import *

# Defining variables
continue_loop = False
total_marks = 0
accepted_marks = [0, 20, 40, 60, 80, 100, 120]
progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0
bar_spacing = 50
user_pass_marks = 0
user_defer_marks = 0
user_fail_marks = 0
big_list = []

# Prompt for credits at pass, defer and fail and validation
while not continue_loop:
    validation_loop = False

    question_loop = False
    small_list = []
    while not validation_loop:
        pass_loop = False
        defer_loop = False
        fail_loop = False
        user_pass_marks = 0
        user_defer_marks = 0
        user_fail_marks = 0

        while not pass_loop:
            user_pass_marks = input("Enter your pass marks:")
            try:
                user_pass_marks = int(user_pass_marks)
            except ValueError:
                print("integer required")
                continue
            if user_pass_marks in accepted_marks:
                pass_loop = True
                break
            else:
                print("out of range")

        while not defer_loop:
            user_defer_marks = input("Enter your defer marks:")
            try:
                user_defer_marks = int(user_defer_marks)
            except ValueError:
                print("integer required")
                continue
            if user_defer_marks in accepted_marks:
                defer_loop = True
                break
            else:
                print("out of range")

        while not fail_loop:
            user_fail_marks = input("Enter your fail marks:")
            try:
                user_fail_marks = int(user_fail_marks)
            except ValueError:
                print("integer required")
                continue
            if user_fail_marks in accepted_marks:
                fail_loop = True
                break
            else:
                print("out of range")

        total_marks = user_pass_marks + user_defer_marks + user_fail_marks
        if total_marks == 120:
            validation_loop = True
            break
        else:
            print('Total incorrect')

    if user_pass_marks == 120:
        print("progress")
        progress_count += 1
        small_list.append("progress")
        small_list.append(user_pass_marks)
        small_list.append(user_defer_marks)
        small_list.append(user_fail_marks)
        big_list.append(small_list)
    elif user_pass_marks == 100:
        print("progress (module trailer)")
        trailer_count += 1
        small_list.append("progress (module trailer)")
        small_list.append(user_pass_marks)
        small_list.append(user_defer_marks)
        small_list.append(user_fail_marks)
        big_list.append(small_list)
    elif 60 <= user_pass_marks <= 80:
        print("Do not progress (module retriever)")
        retriever_count += 1
        small_list.append("Do not progress (module retriever)")
        small_list.append(user_pass_marks)
        small_list.append(user_defer_marks)
        small_list.append(user_fail_marks)
        big_list.append(small_list)
    elif user_pass_marks <= 40:
        if user_fail_marks >= 80:
            print("exclude")
            exclude_count += 1
            small_list.append("exclude")
            small_list.append(user_pass_marks)
            small_list.append(user_defer_marks)
            small_list.append(user_fail_marks)
            big_list.append(small_list)
        else:
            print("do not progress (module retriever)")
            retriever_count += 1
            small_list.append("Do not progress (module retriever)")
            small_list.append(user_pass_marks)
            small_list.append(user_defer_marks)
            small_list.append(user_fail_marks)
            big_list.append(small_list)
    while not question_loop:
        continue_input = input("would you like to continue type 'y' for yes or type 'q' for quit and view results:")
        if continue_input == "q":
            with open('lists.txt', 'w') as file:
                file.write(f"{big_list}")
            print("")
            print("part 2")
            for sublist in big_list:
                print(f"{sublist[0]} - {sublist[1]}, {sublist[2]},{sublist[3]}")
            print("")
            print("part 3")
            with open('lists.txt', 'r') as file:
                file_content = file.read()
                nested_list = eval(file_content)
                for sublist in nested_list:
                    print(f"{sublist[0]} - {sublist[1]}, {sublist[2]},{sublist[3]}")
            win = GraphWin("Histogram", 800, 800)
            line = Line(Point(50,500), Point(750,500))
            line.draw(win)
            title = Text(Point(150, 50), "Histogram result")
            title.setSize(18)
            title.draw(win)

            y1 = 500 - (progress_count * 50)
            bar = Rectangle(Point(70, y1), Point(220, 500))
            bar.setFill("purple")
            bar.draw(win)
            progress_num = Text(Point(145, 515), f"Progress - {progress_count}")
            progress_num.draw(win)
            
            y1 = 500 - (trailer_count * 50)
            bar = Rectangle(Point(240, y1), Point(390, 500))
            trailer_num = Text(Point(315, 515), f"Trailer - {trailer_count}")
            bar.setFill("blue")
            trailer_num.draw(win)
            bar.draw(win)
            

            y1 = 500 - (retriever_count * 50)
            bar = Rectangle(Point(410, y1), Point(560, 500))
            retriever_num = Text(Point(485, 515), f"Retriever - {retriever_count}")
            bar.setFill("red")
            retriever_num.draw(win)
            bar.draw(win)
            

            y1 = 500 - (exclude_count * 50)
            bar = Rectangle(Point(580, y1), Point(730, 500))
            exclude_num = Text(Point(655, 515), f"Exclude - {exclude_count}")
            bar.setFill("green")
            exclude_num.draw(win)
            bar.draw(win)
            

            total_marks_graph = Text(Point(350, 650), f"{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.")
            total_marks_graph.setSize(36)
            total_marks_graph.draw(win)
            win.getMouse()
            win.close()
        elif continue_input == "y":
            question_loop = True
        else:
            print("Invalid input")
