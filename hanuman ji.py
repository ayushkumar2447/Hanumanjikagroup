# Project: Build Your Own Future
# A motivational program for students without jobs

print("=" * 45)
print("   BUILD YOUR OWN FUTURE")
print("=" * 45)

name = input("Enter your name: ")

print("\nHello,", name)
print("\nYou have not got a job yet.")
print("But remember, your future is not over!")
print("You can learn, create, and build something of your own.")

print("\nWhat is your biggest strength?")
print("1. Programming")
print("2. Creativity")
print("3. Communication")
print("4. Business Ideas")

choice = input("Choose your strength (1-4): ")

if choice == "1":
    skill = "Programming"
    plan = "Build websites, apps, or software projects."
elif choice == "2":
    skill = "Creativity"
    plan = "Create designs, digital art, or creative products."
elif choice == "3":
    skill = "Communication"
    plan = "Develop communication skills and offer useful services."
elif choice == "4":
    skill = "Business Ideas"
    plan = "Research a problem and develop a small business idea."
else:
    skill = "Discovering new skills"
    plan = "Explore different skills and find what you enjoy."

print("\n" + "-" * 45)
print("YOUR FUTURE PLAN")
print("-" * 45)

print("Student Name:", name)
print("Your Strength:", skill)
print("Your First Step:", plan)

print("\nYOUR 30-DAY ACTION PLAN")
print("Day 1-7:   Learn and research.")
print("Day 8-15:  Practise your skills.")
print("Day 16-23: Build a small project.")
print("Day 24-30: Improve and share your work.")

print("\nRemember:")
print("A rejected application does not define your worth.")
print("Start small, keep learning, and improve every day.")
print("Your idea can become an opportunity!")

print("\nGood luck,", name, "!")
print("=" * 45)