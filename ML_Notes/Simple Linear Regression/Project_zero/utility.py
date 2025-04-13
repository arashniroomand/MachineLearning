import shutil
import time

import pandas as  pd
import matplotlib.pyplot as plt 

from constant import LOSS_OPTIONS
data = pd.read_csv('Data/xy_100_scores.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))
    
    
def check_values(start_m, end_m, start_b, end_b):
    losses = []
    for m in range(start_m,end_m):
        for b in range(start_b,end_b):
            print(m,b)
            print(loss_function(m, b, data))
            losses.append([m, b, loss_function(m, b, data)])
    sorted_data = sorted(losses, key=lambda x: x[2]) 
    return sorted_data[0]


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = float(len(points))
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return m, b

def find_best_values(m, b, L, epochs): 
    for _ in range(epochs):
        m, b = gradient_descent(m, b, data, L)

    print(f"Optimized m: {m}, Optimized b: {b}")
    print(f"Final Loss: {loss_function(m, b, data)}")

def show_menu():
    result = input("DO YOU WANT TO QUIT OR GO TO MENU:(Q: QUIT , M:MENU):").lower()
    if result == 'q':
        return False
    elif result == 'm':
        return True
    else:
        print("ENTER Q OR M. YOU ENTERED INVALID VALUE!!")
        show_menu()
        
        
def set_values(temp):
    terminal_width = shutil.get_terminal_size().columns  # Get terminal width dynamically

    if temp == 'loss':
        print(LOSS_OPTIONS.center(terminal_width))  # Center LOSS_OPTIONS
        print()
        option = input("WRITE YOUR CHOICE HERE: ".center(terminal_width))  # Centered input prompt
        if option == '1':
            try:
                start_m, end_m = map(int, input("ENTER THE START AND THE END OF SPAN FOR m: ".center(terminal_width)).split())
                start_b, end_b = map(int, input("ENTER THE START AND THE END OF SPAN FOR b: ".center(terminal_width)).split())
                best_m, best_b, final_result = check_values(start_m, end_m, start_b, end_b)
                print()
                print(f"{'Optimized m:':<5}{best_m}, {'Optimized b:':<5}{best_b}. {'The loss is':<5}{final_result}".center(terminal_width))
                result = show_menu()
                time.sleep(2) 
                print(result)
                return result
            except ValueError:
                print("Invalid input! Please enter two integer values separated by a space.".center(terminal_width))

        elif option == '2':
            print()
            m = int(input("PLEASE ENTER THE m VALUE: ".center(terminal_width)))
            b = int(input("PLEASE ENTER THE b VALUE: ".center(terminal_width)))
            loss = loss_function(m, b, data)
            print(f"Loss with {m}*x + {b} is {loss}".center(terminal_width))
            result = show_menu()
            time.sleep(2) 
            return result
        
        elif option == '3':
            print("Exiting...".center(terminal_width))
            time.sleep(2)
            return

    elif temp == 'Gradient':
        print("*****WE SUGGEST YOU TO SET M AND B ZERO AT THE FIRST STEP BUT YOU SHOULD CONSIDER YOUR DATA FIRST****".center(terminal_width))
        print()
        m = int(input("PLEASE ENTER THE M VALUE: ".center(terminal_width)))
        b = int(input("PLEASE ENTER THE B VALUE: ".center(terminal_width)))
        L = float(input("ENTER LEARNING RATE (USUALLY BETWEEN 0 AND 1 LIKE 0.01): ".center(terminal_width)))
        epochs = int(input("ENTER THE NUMBER OF ITERATIONS: ".center(terminal_width)))
        best_m, best_b = gradient_descent(m, b, L, epochs) 
        print(f"{'Optimized m:':<20}{best_m}, {'Optimized b:':<20}{best_b}.".center(terminal_width))
