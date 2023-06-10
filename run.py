import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gaeilge_group')

NAME = ""
SCORE = 0

quiz_questions = [
    {"question": "1. What does 'Go tobann! mean?",
     "answers": {"a": "Suddenly",
                 "b": "No!",
                 "c": "Get out!",
                 "d": "Amazing!"},
     "correct_answer": "a"},
    {"question": "2. How would you say 'the weather is lovely'?",
     "answers": {"a": "Sea sea sea",
                 "b": "Is maith liom tae.",
                 "c": "Tá an ghrian ag scoilteadh na gcloch.",
                 "d": "Ní thuigim."},
     "correct_answer": "c"},
    {"question": "3. Finish this line of Géibheann by Caitlín Maude,\n"
                 "Ainmhí mé, ainmhí allta as __________",
     "answers": {"a": "Port Láirge",
                 "b": "an Aifric",
                 "c": "an abhainn",
                 "d": "na teochreasa"},
     "correct_answer": "d"},
    {"question": "4. Who wrote the book A Thigh ná Tit Orm?",
     "answers": {"a": "Caitlín Maude",
                 "b": "Des Bishop",
                 "c": "Daithí Ó Sé",
                 "d": "Maidhc Dainín Ó Sé"},
     "correct_answer": "a"},
    {"question": "5. What is 'rí rá agus ruaille buaille'?",
     "answers": {"a": "Controlled substances",
                 "b": "Fun and excitement",
                 "c": "Rinner and drinks",
                 "d": "Cats and dogs"},
     "correct_answer": "b"},
    {"question": "6. How do you say 'Hi, how are you?'",
     "answers": {"a": "Ciúnas bóthar cailín bainne?",
                 "b": "Conas atá tú?",
                 "c": "Póg mo thón",
                 "d": "Ní thuigim"},
     "correct_answer": "b"},
    {"question": "7. What is Cácá Milis",
     "answers": {"a": "A sweet cake",
                 "b": "A movie about a blind man on a train eating cake.",
                 "c": "A bird",
                 "d": "Ribena"},
     "correct_answer": "b"},
    {"question": "8. How would you say St. Patrick's Day as Gaeilge?",
     "answers": {"a": "Lá Féile Pádraig",
                 "b": "St Patty's Day",
                 "c": "Ag imirt peile",
                 "d": "Ag feachaint ar an teilifís"},
     "correct_answer": "a"},
    {"question": "9. What does 'ar meisce' mean?",
     "answers": {"a": "Drunk",
                 "b": "Happy",
                 "c": "Silly",
                 "d": "Mean"},
     "correct_answer": "a"},
    {"question": "10. Which of these sentences is correct",
     "answers": {"a": "Is é Corcaigh príomhchathair na hÉireann",
                 "b": "Ní maith linn tae",
                 "c": "Bíonn an ghrian ag taitneamh go minic",
                 "d": "Is breá linn na Sasanaigh"},
     "correct_answer": "a"},
]


def enter_username():
    """
    Welcome message and asks user for username before beginning.
    """
    global NAME
    NAME = input("Hello! Enter your name and click the enter key to begin:\n")
    if NAME == "":
        print("Name is required to begin.")
        enter_username()
    else:
        start_quiz()


def start_quiz():
    """
    Provides instructions and loads quiz if user agrees, or else returns to
    name input.
    """
    print(f"Hello {NAME}! Welcome to the Gaeilge quiz, just do your best.\n")
    print("This is a multiple choice quiz with 10 questions, and 4 answer"
          " options. When you are ready to answer, you can enter either 'a',"
          " 'b', 'c', or 'd' and click the enter key to submit your answer.\n"
          "You will be asked at the end of each question if you would like "
          "to proceed to the next question. Click 'y' and enter for yes, or"
          " 'n' and enter for no.")
    ready_to_begin = input(f"OK {NAME}, are you ready to try it? (y/n):\n")

    while ready_to_begin != "y":
        enter_username()

    if ready_to_begin == "y":
        load_questions(quiz_questions)


def load_questions(data):
    """
    Runs through the questions
    """
    score = 0

    for answer in quiz_questions:
        users_answer = ""
        correct_answer = answer['correct_answer']

        while users_answer not in ['a', 'b', 'c', 'd']:
            print(f"{answer['question']}\n")

            for key, value in answer['answers'].items():
                print(f"{key}: {value}")

            users_answer = input("\nAnswer(a, b, c, d): \n")
            users_answer = users_answer.lower()
        
        if users_answer == answer['correct_answer']:
            print(f"\nWell done {NAME}! That is the right answer.\n")
            score = score + 1
            print(f"Score: {score}")

        elif users_answer != answer['correct_answer']:
            print(f"That was not the right answer {NAME}")
            print(f"The answer is {correct-answer}./n")


def main():
    """
    Runs all program functions
    """
    enter_username()


main()
