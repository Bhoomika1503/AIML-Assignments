tasks = {
    "Resume": {
        "weak": "Write a resume",
        "strong": "Write a professional resume for a Computer Science student skilled in Python, Machine Learning and Web Development"
    },
    "Business Idea": {
        "weak": "Give business idea",
        "strong": "Give a low-investment tech startup idea for college students in India"
    },
    "Study Plan": {
        "weak": "Make study plan",
        "strong": "Create a 4-week study plan to learn Machine Learning with Python for beginners"
    }
}

for task in tasks:
    print("\nTask:", task)
    print("Weak Prompt:", tasks[task]["weak"])
    print("Strong Prompt:", tasks[task]["strong"])