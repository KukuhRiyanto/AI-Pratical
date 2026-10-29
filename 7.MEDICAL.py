# ---------------------------------------------------------
# EXPERT SYSTEM FOR MEDICAL DIAGNOSIS
# ---------------------------------------------------------

def get_answer(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def medical_diagnosis():
    print("=" * 55)
    print("       MEDICAL DIAGNOSIS EXPERT SYSTEM")
    print("=" * 55)
    print("Answer the following questions with yes or no.\n")

    # Collect symptoms
    fever = get_answer("Do you have fever?")
    cough = get_answer("Do you have cough?")
    sore_throat = get_answer("Do you have a sore throat?")
    runny_nose = get_answer("Do you have a runny nose?")
    headache = get_answer("Do you have a headache?")
    body_pain = get_answer("Do you have body pain?")
    fatigue = get_answer("Do you feel tired or weak?")
    sneezing = get_answer("Are you sneezing frequently?")
    breathing_problem = get_answer("Do you have difficulty breathing?")
    stomach_pain = get_answer("Do you have stomach pain?")
    vomiting = get_answer("Are you vomiting?")
    diarrhea = get_answer("Do you have diarrhea?")

    print("\n" + "=" * 55)
    print("                 DIAGNOSIS")
    print("=" * 55)

    # -----------------------------------------------------
    # RULES
    # -----------------------------------------------------

    # Rule 1: Common Cold
    if runny_nose and sneezing and sore_throat and not fever:
        diagnosis = "Common Cold"
        explanation = (
            "Runny nose, sneezing and sore throat are commonly "
            "associated with a common cold."
        )

    # Rule 2: Flu
    elif fever and cough and body_pain and fatigue:
        diagnosis = "Influenza (Flu)"
        explanation = (
            "Fever, cough, body pain and fatigue can occur with "
            "influenza."
        )

    # Rule 3: Possible throat infection
    elif fever and sore_throat and headache:
        diagnosis = "Possible Throat Infection"
        explanation = (
            "Fever, sore throat and headache may occur with "
            "a throat infection."
        )

    # Rule 4: Possible respiratory infection
    elif cough and fever and breathing_problem:
        diagnosis = "Possible Respiratory Infection"
        explanation = (
            "Cough, fever and breathing difficulty can occur "
            "with respiratory infections."
        )

    # Rule 5: Possible gastroenteritis
    elif stomach_pain and vomiting and diarrhea:
        diagnosis = "Possible Gastroenteritis"
        explanation = (
            "Stomach pain, vomiting and diarrhea are commonly "
            "associated with gastroenteritis."
        )

    # Rule 6: Possible food poisoning
    elif stomach_pain and vomiting and diarrhea and fever:
        diagnosis = "Possible Food Poisoning"
        explanation = (
            "Stomach symptoms together with fever can occur "
            "after contaminated food."
        )

    # Rule 7: Headache-related symptoms
    elif headache and fatigue and not fever:
        diagnosis = "Possible Tension Headache"
        explanation = (
            "Headache and fatigue can occur with tension-type "
            "headaches."
        )

    # Rule 8: Mild viral illness
    elif fever and fatigue and headache:
        diagnosis = "Possible Viral Infection"
        explanation = (
            "Fever, fatigue and headache can occur in several "
            "viral illnesses."
        )

    # No matching rule
    else:
        diagnosis = "No Clear Diagnosis"
        explanation = (
            "The symptoms do not match the rules in this "
            "expert system."
        )

    print("\nPossible Condition:", diagnosis)
    print("Reason:", explanation)

    # Emergency warning
    if breathing_problem:
        print("\nWARNING:")
        print("Difficulty breathing can require urgent medical attention.")
        print("Please seek professional medical care promptly.")

    print("\nNote: This system is for educational purposes only.")
    print("It should not replace examination or advice from a qualified doctor.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

medical_diagnosis()