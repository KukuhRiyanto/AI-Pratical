# ============================================================
# AGRICULTURE PROBLEM DIAGNOSIS EXPERT SYSTEM
# Rule-Based Expert System - 10 Rules
# ============================================================

def get_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def get_choice(question, options):
    while True:
        print("\n" + question)

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")


def agriculture_expert_system():

    print("=" * 60)
    print("      AGRICULTURE PROBLEM DIAGNOSIS EXPERT SYSTEM")
    print("=" * 60)

    # --------------------------------------------------------
    # INPUT INFORMATION
    # --------------------------------------------------------

    crop = input("\nEnter crop name: ")

    soil_moisture = get_choice(
        "Select soil moisture:",
        ["Low", "Normal", "High"]
    )

    temperature = get_choice(
        "Select temperature:",
        ["Low", "Moderate", "High"]
    )

    rainfall = get_choice(
        "Select rainfall:",
        ["Low", "Moderate", "High"]
    )

    irrigation = get_yes_no(
        "Is irrigation available?"
    )

    yellow_leaves = get_yes_no(
        "Are the leaves turning yellow?"
    )

    brown_spots = get_yes_no(
        "Are there brown spots on the leaves?"
    )

    leaf_curling = get_yes_no(
        "Are the leaves curling?"
    )

    insects = get_yes_no(
        "Are insects visible on the plant?"
    )

    dry_leaves = get_yes_no(
        "Are the leaves dry or wilting?"
    )

    slow_growth = get_yes_no(
        "Is the plant growth slow?"
    )

    poor_drainage = get_yes_no(
        "Is there a drainage problem?"
    )

    # --------------------------------------------------------
    # KNOWLEDGE BASE / RULE BASE
    # --------------------------------------------------------

    problems = []

    # RULE 1
    if soil_moisture == "Low" and dry_leaves and not irrigation:
        problems.append(
            ("Water Deficiency",
             "The crop may not be receiving enough water.",
             "Provide suitable irrigation and monitor soil moisture.")
        )

    # RULE 2
    if soil_moisture == "High" and poor_drainage and yellow_leaves:
        problems.append(
            ("Overwatering / Waterlogging",
             "Excess water and poor drainage may be affecting the crop.",
             "Improve drainage and avoid excessive irrigation.")
        )

    # RULE 3
    if yellow_leaves and slow_growth:
        problems.append(
            ("Possible Nutrient Deficiency",
             "Yellow leaves and slow growth may indicate a nutrient problem.",
             "Consider soil testing before applying fertilizer.")
        )

    # RULE 4
    if brown_spots and rainfall == "High":
        problems.append(
            ("Possible Fungal Disease",
             "Leaf spots under wet conditions may be associated with fungal disease.",
             "Reduce excess moisture and consult an agricultural expert.")
        )

    # RULE 5
    if insects and leaf_curling:
        problems.append(
            ("Possible Pest Attack",
             "Insects together with leaf curling suggest possible pest damage.",
             "Inspect the plant and identify the pest before treatment.")
        )

    # RULE 6
    if insects and brown_spots:
        problems.append(
            ("Possible Insect Damage",
             "Insects and damaged leaves may indicate pest activity.",
             "Inspect leaves carefully and consider integrated pest management.")
        )

    # RULE 7
    if temperature == "High" and dry_leaves and soil_moisture == "Low":
        problems.append(
            ("Heat Stress",
             "High temperature and low soil moisture can stress plants.",
             "Maintain adequate soil moisture and monitor plants during heat.")
        )

    # RULE 8
    if temperature == "Low" and slow_growth:
        problems.append(
            ("Possible Cold Stress",
             "Low temperature may be slowing plant growth.",
             "Monitor temperature and follow crop-specific protection practices.")
        )

    # RULE 9
    if poor_drainage and soil_moisture == "High":
        problems.append(
            ("Poor Drainage",
             "Excess water may remain around the plant roots.",
             "Improve field drainage and avoid unnecessary irrigation.")
        )

    # RULE 10
    if (
        not yellow_leaves
        and not brown_spots
        and not leaf_curling
        and not insects
        and not dry_leaves
        and not slow_growth
    ):
        problems.append(
            ("No Major Problem Detected",
             "No major problem matches the rules in this system.",
             "Continue regular monitoring of the crop.")
        )

    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("                  DIAGNOSIS RESULT")
    print("=" * 60)

    print(f"\nCrop: {crop}")

    if len(problems) == 0:
        print("\nNo matching agricultural problem was detected.")

    else:
        for i, problem in enumerate(problems, 1):

            name, explanation, recommendation = problem

            print(f"\nProblem {i}: {name}")
            print("-" * 60)
            print("Explanation :", explanation)
            print("Recommendation:", recommendation)

    print("\n" + "=" * 60)
    print("Total Rules Matched:", len(problems))
    print("=" * 60)

    print("\nNote:")
    print("This is an educational expert system.")
    print("For actual crop diagnosis, consult a qualified")
    print("agricultural expert and use appropriate testing.")


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

agriculture_expert_system()