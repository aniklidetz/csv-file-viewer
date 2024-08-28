import pandas as pd
from enum import Enum

# Enum for file choices
class FileChoice(Enum):
    NEWS_DECLINE = "1"
    SNAKES_COUNT = "2"
    TREES = "3"

# Enum for commands with single-letter options
class Command(Enum):
    HEAD = "H"
    TAIL = "T"
    DF = "D"

# Class to manage file operations
class FileManager:
    def __init__(self):
        self.files = {
            FileChoice.NEWS_DECLINE: 'news_decline.csv',
            FileChoice.SNAKES_COUNT: 'snakes_count_10.csv',
            FileChoice.TREES: 'trees.csv'
        }
    
    def display_file_content(self, file_name, command):
        # Reading the CSV file into a DataFrame
        df = pd.read_csv(file_name)
        
        print(f"\n--- Contents of {file_name} ---\n")
        
        if command == Command.HEAD:
            # Display the first 5 rows of the file (by default)
            print("First 5 rows (head):")
            print(df.head())
        elif command == Command.TAIL:
            # Display the last 5 rows of the file (by default)
            print("Last 5 rows (tail):")
            print(df.tail())
        elif command == Command.DF:
            # Display the entire file content
            print(f"\nFull content of {file_name}:")
            print(df)
        else:
            print("Invalid command. Please use 'H', 'T', or 'D'.")
        

    def display_menu(self):
        print("Please choose a file to view:")
        for choice in FileChoice:
            file_name = self.files[choice]
            print(f"{choice.value} - {file_name}")
        
        print("\nAvailable commands:")
        for command in Command:
            print(f"{command.value} - {command.name.lower()}")

    def handle_choice(self, choice):
        try:
            file_choice = FileChoice(choice)
            file_name = self.files[file_choice]
            
            command_input = input("Enter the command (H for head, T for tail, D for df): ").strip().upper()
            command = Command(command_input)
            
            if file_choice in self.files:
                self.display_file_content(file_name, command)
            else:
                print("Invalid file choice. Please run the script again and select a valid option.")
        except (ValueError, KeyError):
            print("Invalid input. Please enter a valid option letter for command and a number for file.")

if __name__ == "__main__":
    file_manager = FileManager()
    
    # Display menu
    file_manager.display_menu()
    
    # Get user input
    choice = input("Enter the number of the file you want to view: ")
    
    # Handle user choice
    file_manager.handle_choice(choice)
