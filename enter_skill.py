def check_skill(skill):

    with open("resume.txt", "r") as file:
        resume = file.read()

    if skill.lower() in resume.lower():
        print("✅ Skill Found")
    else:
        print("❌ Skill not found")


skill = input("Enter a skill to check: ")

check_skill(skill)