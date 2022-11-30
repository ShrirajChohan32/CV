# Technical CV

candiate = {
    "name": "Shriraj Chohan",
    "DOB": "16/12/1996",
    "Contact": "+64211840925",
    "Email": "shrirajchohan@yahoo.com",
}
s = []

help = (
    "\nFor Canidate's Name = name \n"
    "For Candidate's phone = contact \n"
    "For Candidate's email = email \n"
    "For Candiadate's DOB = dob \n"
    "For Candidate's Skills = skills \n"
    "To close the CV = exit or close \n"
)

Cloudskills = ["AWS", "Python Scripting", "Linux", "Windows", "CDK", "Terraform"]
NetworkingSkills = ["Cisco/Juniper/HP", "Aruba", "Firewall (Foretinet)", "TCP/IP"]

# print(candiate["name"])

print("Welcome to my Technical CV")

while input != "exit" or "close":
    question = input("\n What would you like to know about the candiate? ")

    if question.lower() == "email":
        print("\n")
        print(candiate["Email"])

    elif question.lower() == "name":
        print("\n")
        print(candiate["name"])

    elif question.lower() == "contact":
        print("\n")
        print(candiate["Contact"])

    elif question.lower() == "dob":
        print("\n")
        print(candiate["DOB"])

    elif question.lower() == "help":
        print("\n")
        print(help)

    elif question.lower() == "skills":
        skills_question = input(
            "For Cloud Skills enter 1, for Networking skills press 2 and for all skills press 0: \n"
        )
        if skills_question == "1":
            print(" \n ")
            for skills in Cloudskills:
                print(skills),
            print("\n")
        elif skills_question == "2":
            print("\n")
            for n_skills in NetworkingSkills:
                print(n_skills)
            print("\n")
        elif skills_question == "0":
            print("\n")
            for i in Cloudskills:
                s.append(i)
            for j in NetworkingSkills:
                s.append(j)
            for all in s:
                print(all)
            print("\n")
            s = []

        else:
            print(
                "\nChoose from following options \n"
                "Networking Skills: 1 \n"
                "Cloud Skills: 2 \n"
                "All Skills: 0 \n"
            )

    elif question.lower() == "exit" or question.lower() == "close":
        break

    else:
        print("Type help for instructions")
