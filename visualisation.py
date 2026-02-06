import pandas as pd
import plotly.express as px
import os
import logging

# BASE DIRECTORY
BASE_DIR = "/home/om-panchpatkar/Desktop/Python/Mini project"

# FILE PATHS
CSV_FILE = os.path.join(BASE_DIR, "student.csv")
LOG_FILE = os.path.join(BASE_DIR, "student.log")
GRAPH_DIR = os.path.join(BASE_DIR, "graphs")

# LOGGING SETUP
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# PARENT FUNCTION
def graph():
    try:
        logging.info("Graph generation started")

        # READ DATA
        df = pd.read_csv(CSV_FILE)

        marks_cols = ["Science", "Maths", "English", "History", "Computer"]

        # CREATE GRAPH FOLDER
        if not os.path.exists(GRAPH_DIR):
            os.mkdir(GRAPH_DIR)
            logging.info("Graphs folder created")

        # GRAPH 1 — SUBJECT AVERAGE MARKS
        subject_avg = []

        for subject in marks_cols:
            avg = df[subject].mean()
            subject_avg.append(avg)

        avg_df = pd.DataFrame({
            "Subject": marks_cols,
            "Average Marks": subject_avg
        })

        fig1 = px.bar(
            avg_df,
            x="Subject",
            color="Subject",
            y="Average Marks",
            text="Average Marks",
            title="Subject Wise Average Marks"
        )

        fig1.update_traces(
            textposition="outside",
            textangle=0
        )

        fig1.write_image(os.path.join(GRAPH_DIR, "subject_average.png"))
        logging.info("Subject average graph saved")

        # GRAPH 2 — GRADE DISTRIBUTION
        grade_count = df["Grade"].value_counts().reset_index()
        grade_count.columns = ["Grade", "Count"]

        fig2 = px.pie(
            grade_count,
            names="Grade",
            values="Count",
            title="Grade Distribution"
        )

        fig2.write_image(os.path.join(GRAPH_DIR, "grade_distribution.png"))
        logging.info("Grade distribution graph saved")

        # GRAPH 3 — PASS FAIL COUNT
        result_count = df["Result"].value_counts().reset_index()
        result_count.columns = ["Result", "Count"]

        fig3 = px.bar(
            result_count,
            x="Result",
            y="Count",
            text="Count",
            title="Pass vs Fail Students"
        )

        fig3.update_traces(
            textposition="outside",
            textangle=0
        )

        fig3.write_image(os.path.join(GRAPH_DIR, "pass_fail.png"))
        logging.info("Pass Fail graph saved")

        print("\nAll graphs generated successfully")
        print("Saved inside 'graphs' folder")

        logging.info("All graphs created successfully")

    except Exception as e:
        logging.error("Error while generating graphs")
        logging.error(str(e))
        print("Error:", e)


if __name__=="__main__":
    graph()