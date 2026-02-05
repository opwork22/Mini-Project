import pandas as pd
import logging

# LOGGING CONFIGURATION

logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_result_grade():

    try:

        logging.info("Result & Grade calculation started")

        # READ CSV FILE
        df = pd.read_csv("student.csv")

        marks_cols = ["Science", "Maths", "English", "History", "Computer"]

        # TOTAL MARKS
        df["Total"] = df[marks_cols].sum(axis=1)

        # PERCENTAGE
        df["Percent"] = (df["Total"] / 500) * 100
        df["Percent"] = df["Percent"].round(2)

        # RESULT COLUMN (PASS / FAIL)

        result_list = []

        for percent in df["Percent"]:

            if percent >= 45:
                result_list.append("P")
            else:
                result_list.append("F")

        df["Result"] = result_list

        # GRADE COLUMN

        grade_list = []

        for percent in df["Percent"]:

            if percent >= 90:
                grade_list.append("A")

            elif percent >= 75:
                grade_list.append("B")

            elif percent >= 60:
                grade_list.append("C")

            else:
                grade_list.append("D")

        df["Grade"] = grade_list

        # SAVE BACK TO SAME FILE
        df.to_csv("student.csv", index=False)

        logging.info("Result, Percent and Grade added successfully")

        print("\nResult, Percent and Grade Added Successfully")
        print("student.csv Updated")

    except FileNotFoundError:

        logging.error("student.csv file not found")
        print("Error: student.csv file not found")

    except Exception as e:

        logging.error("Error during result calculation")
        print("Error:", e)
