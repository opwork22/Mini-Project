import data
import preprocessing
import calculation
import visualisation
def run_menu():
    """
    Docstring for run_menu
    calling the menu and running it
    """
    data.Menu()

def run_preprocessing():
    """
    Docstring for run_preprocessing
    """
    preprocessing.data_cleaning()

def run_calculation():
    """
    Docstring for run_calculation
    Calculating the total marks, percentage, Grade, 
    """
    calculation.calculate_result_grade()

def run_graph():
    """
    Docstring for run_graph
    """
    visualisation.graph()

while True:
   
    choice=input("Enter the choice:")
    if choice=="menu":
        print(run_menu())
    if choice=="preprocess":
        print(run_preprocessing())
    if choice=="calculation":
        print(run_calculation())
    if choice=="graph":
        print(run_graph())
    if choice=="Exit":
        break


#logging
