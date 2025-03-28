from automation_functions import create_text_file
def main():
    try:
        create_text_file('example.txt')
        print("create_text_file executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
