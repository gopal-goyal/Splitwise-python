# main.py

import sys
import os
from splitwise import Splitwise

def main():
    splitwise_instance = Splitwise()
    
    # Read sample input file
    sample_input_path = os.path.join(os.path.dirname(__file__), '../sample_inputs/sample_input.txt')
    with open(sample_input_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            description = parts[0]
            amount = float(parts[1])
            paid_by = parts[2]
            participants = parts[3:]
            splitwise_instance.add_expense(description, amount, paid_by, participants)
    
    splitwise_instance.print_balances()

if __name__ == "__main__":
    main()
