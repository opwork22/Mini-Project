import pandas as pd
import re
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


def data_cleaning():
    try:
        logging.info("Data cleaning process started")

        # READ CSV FILE
        df = pd.read_csv(CSV_FILE)
        print("\nStudent Data Loaded Successfully\n")

        marks_cols = ["Science", "Maths", "English", "History", "Computer"]

        # FIX DUPLICATE ROLL NUMBERS
        print("\nChecking Duplicate Roll Numbers...\n")
        logging.info("Checking duplicate roll numbers")

        max_roll = df["Roll No"].max()
        used_rolls = []

        for index, row in df.iterrows():
            roll = row["Roll No"]

            if roll in used_rolls:
                max_roll += 1

                print("Duplicate Roll Found:", roll)
                print("Assigned New Roll:", max_roll)

                logging.warning(
                    f"Duplicate roll {roll} found. New roll assigned: {max_roll}"
                )

                df.at[index, "Roll No"] = max_roll
            else:
                used_rolls.append(roll)

        # FIX MISSING / INVALID MARKS
        print("\nChecking Marks...\n")
        logging.info("Checking missing and invalid marks")

        for index, row in df.iterrows():
            for subject in marks_cols:
                value = row[subject]

                if pd.isna(value):
                    print(f"\nMissing {subject} marks for {row['Name']}")
                    logging.warning(
                        f"Missing {subject} marks for {row['Name']}"
                    )

                    new_value = float(input(f"Enter {subject} marks: "))
                    df.at[index, subject] = new_value
                else:
                    value = float(value)

                    if value < 0 or value > 100:
                        print(f"\nInvalid {subject} marks for {row['Name']}")
                        logging.warning(
                            f"Invalid {subject} marks for {row['Name']}"
                        )

                        new_value = float(
                            input(f"Enter correct {subject} marks: ")
                        )
                        df.at[index, subject] = new_value

        # FIX CITY COLUMN
        print("\nChecking City Column...\n")
        logging.info("Cleaning City column")

        for index in range(len(df)):
            city = str(df.at[index, "City"])

            city = re.sub(r"\s+", " ", city)
            city = city.strip()

            if city == "" or city.lower() == "nan":
                print(f"\nMissing City for {df.at[index,'Name']}")
                logging.warning(
                    f"Missing City for {df.at[index,'Name']}"
                )

                city = input("Enter City Name: ")

            df.at[index, "City"] = city

        # FIX SPORTS COLUMN
        print("\nChecking Sports Column...\n")
        logging.info("Cleaning Sports column")

        for index in range(len(df)):
            sport = str(df.at[index, "Sports"]).strip()

            if sport == "" or sport.lower() == "nan":
                print(f"\nMissing Sports for {df.at[index,'Name']}")
                logging.warning(
                    f"Missing Sports for {df.at[index,'Name']}"
                )

                sport = input("Enter Sports Name: ")

            sport = sport.lower().capitalize()
            df.at[index, "Sports"] = sport

        # SAVE UPDATED DATA
        df.to_csv(CSV_FILE, index=False)

        logging.info("Data cleaning completed successfully")
        print("\nPreprocessing Completed Successfully")
        print("student.csv UPDATED")

    except FileNotFoundError:
        logging.error("student.csv file not found")
        print("student.csv file not found")

    except Exception as e:
        logging.error(f"Error occurred during preprocessing: {e}")
        print("Error:", e)
