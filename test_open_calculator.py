from automation_functions import open_chrome
def main():
    try:
        open_chrome()
        print("open_chrome executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
