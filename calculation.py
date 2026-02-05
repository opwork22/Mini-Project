import pandas as pd
import logging
import os

# BASE DIRECTORY
BASE_DIR = "/home/om-panchpatkar/Desktop/Python/Mini project"

# FILE PATHS
CSV_FILE = os.path.join(BASE_DIR, "student.csv")
LOG_FILE = os.path.join(BASE_DIR, "student.log")

# LOGGING CONFIGURATION
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_result_grade():
    try:
        logging.info("Result & Grade calculation started")

        # READ CSV FILE
        df = pd.read_csv(CSV_FILE)

        marks_cols = ["Science", "Maths", "English", "History", "Computer"]

        # TOTAL MARKS
        df["Total"] = df[marks_cols].sum(axis=1)

        # PERCENTAGE
        df["Percent"] = (df["Total"] / 500) * 100
        df["Percent"] = df["Percent"].round(2)

        # RESULT
        df["Result"] = df["Percent"].apply(lambda x: "P" if x >= 45 else "F")

        # GRADE
        def grade(percent):
            if percent >= 90:
                return "A"
            elif percent >= 75:
                return "B"
            elif percent >= 60:
                return "C"
            else:
                return "D"

        df["Grade"] = df["Percent"].apply(grade)

        # SAVE BACK
        df.to_csv(CSV_FILE, index=False)

        logging.info("Result, Percent and Grade added successfully")

        print("\nResult, Percent and Grade Added Successfully")
        print("student.csv Updated")

    except FileNotFoundError:
        logging.error("student.csv file not found")
        print("Error: student.csv file not found")

    except Exception as e:
        logging.error(f"Error during result calculation: {e}")
        print("Error:", e)
