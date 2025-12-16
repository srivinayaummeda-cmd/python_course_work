questions = [
{
"question": "What is the output of print(2 ** 3)?",
"options": {
"a": "6",
"b": "8",
"c": "9",
"d": "Error"
},
"answer": "b"
},
{
"question": "Which data type stores key-value pairs?",
"options": {
"a": "list",
"b": "tuple",
"c": "dictionary",
"d": "set"
},
"answer": "c"
},
{
"question": "What does range(5) return?",
"options": {
"a": "[1,2,3,4,5]",
"b": "[0,1,2,3,4]",
"c": "[1,2,3,4]",
"d": "Error"
},
"answer": "b"
},
{
"question": "Which keyword is used to handle exceptions?",
"options": {
"a": "catch",
"b": "error",
"c": "try",
"d": "handle"
},
"answer": "c"
},
{
"question": "What is the output of print(len('Python'))?",
"options": {"a": "5", "b": "6", "c": "7", "d": "Error"},
"answer": "b"
},
{
"question": "Which symbol is used for comments in Python?",
"options": {"a": "//", "b": "<!--", "c": "#", "d": "**"},
"answer": "c"
},
{
"question": "Which function is used to take input from the user?",
"options": {"a": "scan()", "b": "read()", "c": "input()", "d": "get()"},
"answer": "c"
},
{
"question": "What is the output of print(10 % 3)?",
"options": {"a": "1", "b": "3", "c": "0", "d": "Error"},
"answer": "a"
},
{
"question": "Which keyword is used to define a function?",
"options": {"a": "function", "b": "define", "c": "def", "d": "fun"},
"answer": "c"
},
{
  "question": "What is the output of print(type(5))?",
  "options": {
    "a": "<class 'float'>",
    "b": "<class 'int'>",
    "c": "<class 'str'>",
    "d": "Error"
  },
  "answer": "b"
},
{
  "question": "Which of the following is a valid variable name in Python?",
  "options": {
    "a": "1value",
    "b": "value-1",
    "c": "_value",
    "d": "value 1"
  },
  "answer": "c"
},
{
  "question": "What is the output of print(2 ** 3)?",
  "options": {
    "a": "6",
    "b": "8",
    "c": "9",
    "d": "Error"
  },
  "answer": "b"
},
{
  "question": "Which data type is used to store True or False values?",
  "options": {
    "a": "int",
    "b": "str",
    "c": "bool",
    "d": "float"
  },
  "answer": "c"
},
{
  "question": "What is the output of print(len([1, 2, 3, 4]))?",
  "options": {
    "a": "3",
    "b": "4",
    "c": "5",
    "d": "Error"
  },
  "answer": "b"
},
{
  "question": "Which keyword is used to check a condition in Python?",
  "options": {
    "a": "for",
    "b": "while",
    "c": "if",
    "d": "check"
  },
  "answer": "c"
},
{
  "question": "What is the output of print(5 // 2)?",
  "options": {
    "a": "2.5",
    "b": "3",
    "c": "2",
    "d": "Error"
  },
  "answer": "c"
},
{
  "question": "Which bracket is used to define a list?",
  "options": {
    "a": "()",
    "b": "{}",
    "c": "[]",
    "d": "<>"
  },
  "answer": "c"
},
{
  "question": "What is the correct file extension for Python files?",
  "options": {
    "a": ".pt",
    "b": ".py",
    "c": ".pyt",
    "d": ".python"
  },
  "answer": "b"
},
{
  "question": "Which function is used to display output in Python?",
  "options": {
    "a": "show()",
    "b": "display()",
    "c": "print()",
    "d": "output()"
  },
  "answer": "c"
},
{
  "question": "What is the output of print(type('10'))?",
  "options": {
    "a": "<class 'int'>",
    "b": "<class 'float'>",
    "c": "<class 'str'>",
    "d": "Error"
  },
  "answer": "c"
}


]




def run_quiz():
    score = 0
    print("🧪 Welcome to the Python Quiz Game!\n")


    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")


        for key, value in q["options"].items():
            print(f"{key}) {value}")


        user_answer = input("Your answer (a/b/c/d): ").lower()


        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is '{q['answer']}'\n")


    print("🎯 Quiz Completed!")
    print(f"Your Final Score: {score}/{len(questions)}")




run_quiz()
