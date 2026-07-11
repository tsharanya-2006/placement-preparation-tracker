# ==========================================
# Placement Preparation Tracker
# Developed by Talasani Sharanya
# Language: Python
# ==========================================
dsa_problems = []
projects = []
goals_completed = 0

def view_progress():
    print("\n===== YOUR PROGRESS =====")
    print("\nDSA Problems:")
    if len(dsa_problems) == 0:
        print("No DSA Problems Added.")
    else:
        for problem in dsa_problems:
            print("-", problem)

    print("\nProjects:")
    if len(projects) == 0:
        print("No Projects Added.")
    else:
        for project in projects:
            print("-", project)

    print(f"\nGoals Completed: {goals_completed}")
def mark_goal_completed():
    global goals_completed
    goals_completed += 1
    print("Goal Marked as Completed!")
def delete_dsa_problem():
    problem = input("Enter DSA Problem Name to Delete: ")

    if problem in dsa_problems:
        dsa_problems.remove(problem)
        print(f"'{problem}' deleted successfully!")
    else:
        print("Problem not found!")
def delete_project():
    project = input("Enter Project Name to Delete: ")

    if project in projects:
        projects.remove(project)
        print(f"'{project}' deleted successfully!")
    else:
        print("Project not found!")
def add_dsa_problem():
    problem = input("Enter DSA Problem Name: ")
    dsa_problems.append(problem)

    with open("placement_data.txt", "a") as file:
        file.write("DSA: " + problem + "\n")

    print(f"'{problem}' added successfully!")
def add_project():
    project = input("Enter Project Name: ")
    projects.append(project)

    with open("placement_data.txt", "a") as file:
        file.write("Project: " + project + "\n")

    print(f"'{project}' added successfully!")
def view_saved_data():
    print("\n===== SAVED DATA =====")

    with open("placement_data.txt", "r") as file:
        print(file.read())
def search_dsa_problem():
    problem = input("Enter DSA Problem to Search: ")

    if problem in dsa_problems:
        print(f"'{problem}' Found!")
    else:
        print(f"'{problem}' Not Found!")
def statistics():
    print("\n========== STATISTICS ==========")
    print(f"Total DSA Problems : {len(dsa_problems)}")
    print(f"Total Projects     : {len(projects)}")
    print(f"Goals Completed    : {goals_completed}")
    print("================================")
def edit_dsa_problem():
    old_problem = input("Enter the DSA Problem to Edit: ")

    if old_problem in dsa_problems:
        new_problem = input("Enter the New DSA Problem Name: ")

        index = dsa_problems.index(old_problem)
        dsa_problems[index] = new_problem

        print(f"'{old_problem}' updated to '{new_problem}' successfully!")

    else:
        print("Problem Not Found!")
def search_project():
    project = input("Enter Project Name to Search: ")

    if project in projects:
        print(f"'{project}' Found!")
    else:
        print(f"'{project}' Not Found!")
def edit_project():
    old_project = input("Enter the Project Name to Edit: ")

    if old_project in projects:
        new_project = input("Enter the New Project Name: ")

        index = projects.index(old_project)
        projects[index] = new_project

        print(f"'{old_project}' updated to '{new_project}' successfully!")

    else:
        print("Project Not Found!")
while True:
    print("\n===== WELCOME TO PLACEMENT TRACKER =====")
    print("1. Add DSA Problem")
    print("2. Add Project")
    print("3. View Progress")
    print("4. Mark Goal Completed")
    print("5. Delete DSA Problem")
    print("6. Delete Project")
    print("7. View Saved Data")
    print("8. Search DSA Problem")
    print("9. Statistics")
    print("10. Search Project")
    print("11. Edit DSA Problem")
    print("12. Edit Project")
    print("13. Exit")
    choice=int(input("Enter the choice"))
    if choice == 1:
        add_dsa_problem()
    elif choice == 2:
     add_project()
    elif choice == 3:
        view_progress()
    elif choice == 4:
        mark_goal_completed()

    elif choice == 5:
        delete_dsa_problem()
    elif choice == 6:
        delete_project()

    elif choice == 7:
        view_saved_data()
    elif choice==8:
        search_dsa_problem()
    elif choice==9 :
        statistics()
    elif choice==10:
        search_project()
    elif choice == 11:
        edit_dsa_problem()
    elif choice == 12:
        edit_project()

    elif choice == 13:
        print("Thank you for using Placement Preparation Tracker!")
        break
    else:
        print("Invalid Choice!")
    