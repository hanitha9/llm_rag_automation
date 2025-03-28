from automation_functions import open_calculator
def main():
    try:
        open_calculator()
        print("open_calculator executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
