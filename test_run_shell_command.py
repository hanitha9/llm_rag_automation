from automation_functions import run_shell_command
def main():
    try:
        run_shell_command('dir')
        print("run_shell_command executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
