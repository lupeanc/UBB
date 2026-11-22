import json
import random
import re
import os
import sys
import subprocess
from pathlib import Path


def remove_js_comments(text):
    result = []
    i = 0
    in_string = False
    string_char = ""
    escape = False

    while i < len(text):
        char = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""

        if in_string:
            result.append(char)

            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == string_char:
                in_string = False

            i += 1
            continue

        if char in ['"', "'", "`"]:
            in_string = True
            string_char = char
            result.append(char)
            i += 1
            continue

        if char == "/" and nxt == "/":
            while i < len(text) and text[i] != "\n":
                i += 1
            result.append("\n")
            continue

        if char == "/" and nxt == "*":
            i += 2
            while i + 1 < len(text) and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue

        result.append(char)
        i += 1

    return "".join(result)


def extract_questions_array(text):
    """
    Finds the full [ ... ] array after `const questions =`.
    This avoids stopping at the first answers array.
    """
    match = re.search(r"const\s+questions\s*=", text)

    if not match:
        raise ValueError("Could not find `const questions =` in questions.js")

    start_search = match.end()
    start = text.find("[", start_search)

    if start == -1:
        raise ValueError("Could not find opening [ for questions array")

    bracket_count = 0
    in_string = False
    string_char = ""
    escape = False

    for i in range(start, len(text)):
        char = text[i]

        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == string_char:
                in_string = False
            continue

        if char in ['"', "'", "`"]:
            in_string = True
            string_char = char
            continue

        if char == "[":
            bracket_count += 1
        elif char == "]":
            bracket_count -= 1

            if bracket_count == 0:
                return text[start:i + 1]

    raise ValueError("Could not find closing ] for questions array")


def clean_json_like_text(text):
    text = remove_js_comments(text)

    # Remove trailing commas before } or ]
    text = re.sub(r",\s*([\]}])", r"\1", text)

    # Replace raw line breaks inside strings with \n
    cleaned = []
    in_string = False
    string_char = ""
    escape = False

    for char in text:
        if in_string:
            if char == "\n":
                cleaned.append("\\n")
                continue

            cleaned.append(char)

            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == string_char:
                in_string = False

            continue

        if char in ['"', "'", "`"]:
            in_string = True
            string_char = char
            cleaned.append('"')  # normalize string quote to double quote
            continue

        cleaned.append(char)

    return "".join(cleaned)


def load_questions(filename):
    path = Path(filename)

    if not path.exists():
        print(f"Could not find {filename}.")
        print("Make sure quiz.py and the .js file are in the same folder.")
        exit(1)

    js_text = path.read_text(encoding="utf-8")

    try:
        array_text = extract_questions_array(js_text)
        array_text = clean_json_like_text(array_text)
        questions = json.loads(array_text)
    except Exception as e:
        print("Could not load questions file.")
        print("Error:", e)
        exit(1)

    return questions


def normalize_answer(answer):
    answer = answer.lower().strip()
    answer = answer.replace(",", "")
    answer = answer.replace(" ", "")
    answer = answer.replace(".", "")
    return "".join(sorted(set(answer)))


def find_image_path(image_name):
    """
    Looks for the image in the same folder as quiz.py.
    Also works if image_name is already a relative path.
    """
    image_path = Path(image_name)

    if image_path.exists():
        return image_path

    script_folder = Path(__file__).parent
    image_path = script_folder / image_name

    if image_path.exists():
        return image_path

    return None


def open_image(image_name):
    image_path = find_image_path(image_name)

    if image_path is None:
        print(f"\n[Image not found: {image_name}]")
        print("Make sure the image is in the same folder as quiz.py.")
        return

    print(f"\n[Opening image: {image_path}]")

    try:
        if sys.platform.startswith("win"):
            os.startfile(image_path)
        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", str(image_path)])
        else:
            subprocess.run(["xdg-open", str(image_path)])
    except Exception as e:
        print("Could not open image automatically.")
        print("Image path:", image_path)
        print("Error:", e)


def ask_question(question, number, total):
    print("\n" + "=" * 70)
    print(f"Question {number}/{total}")
    print("=" * 70)

    print(question.get("question", "No question text"))

    image_name = question.get("image")
    if image_name:
        open_image(image_name)

    answers = question.get("answers", [])
    letters = "abcdefghijklmnopqrstuvwxyz"

    print()
    for i, ans in enumerate(answers):
        print(f"{letters[i]}. {ans}")

    correct = normalize_answer(question.get("correct", ""))

    user_answer = input("\nYour answer: ")
    user_answer = normalize_answer(user_answer)

    if user_answer == correct:
        print("Correct!")
        return True

    print("Wrong.")
    print(f"Correct answer: {correct.upper()}")

    print("Correct option(s):")
    for letter in correct:
        if letter in letters:
            index = letters.index(letter)
            if index < len(answers):
                print(f"  {letter.upper()}. {answers[index]}")

    return False


def choose_quiz_mode(questions, filename):
    print("\nAI Quiz App")
    print("=" * 70)
    print(f"Loaded {len(questions)} questions from {filename}.")

    print("\nChoose mode:")
    print("1. All questions")
    print("2. Random quiz")
    print("3. Search questions by keyword")
    # print("4. Image questions only")

    choice = input("\nMode: ").strip()

    if choice == "1":
        selected = questions[:]
        random.shuffle(selected)
        return selected

    if choice == "2":
        while True:
            try:
                count = int(input("How many questions? "))
                if count <= 0:
                    print("Enter a positive number.")
                    continue
                break
            except ValueError:
                print("Enter a number.")

        selected = questions[:]
        random.shuffle(selected)
        return selected[:count]

    if choice == "3":
        keyword = input("Keyword: ").lower().strip()

        selected = [
            q for q in questions
            if keyword in q.get("question", "").lower()
            or any(keyword in ans.lower() for ans in q.get("answers", []))
        ]

        if not selected:
            print("No questions found with that keyword.")
            exit(0)

        random.shuffle(selected)
        print(f"Found {len(selected)} questions.")
        return selected

    if choice == "4":
        selected = [q for q in questions if q.get("image")]

        if not selected:
            print("No image questions found.")
            exit(0)

        random.shuffle(selected)
        print(f"Found {len(selected)} image questions.")
        return selected

    print("Invalid mode. Starting random 20-question quiz.")
    selected = questions[:]
    random.shuffle(selected)
    return selected[:20]


def main():
    print("Which file to ask from? DO NOT WRITE .JS")
    questions_file = input().strip()

    if not questions_file.endswith(".js"):
        questions_file += ".js"

    questions = load_questions(questions_file)

    if not questions:
        print("No questions were loaded.")
        exit(1)

    selected_questions = choose_quiz_mode(questions, questions_file)

    score = 0
    answered = 0

    for i, question in enumerate(selected_questions, start=1):
        answered += 1

        if ask_question(question, i, len(selected_questions)):
            score += 1

        if i != len(selected_questions):
            choice = input("\nPress Enter for next question, or type q to quit: ").strip().lower()
            if choice == "q":
                break

    print("\n" + "=" * 70)
    print("Quiz finished")
    print("=" * 70)
    print(f"Score: {score}/{answered}")

    if answered > 0:
        percentage = score / answered * 100
        print(f"Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    main()