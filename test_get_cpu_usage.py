from automation_functions import get_cpu_usage
def main():
    try:
        get_cpu_usage()
        print("get_cpu_usage executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
