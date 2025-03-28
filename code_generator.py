# code_generator.py
class CodeGenerator:
    @staticmethod
    def generate_code(function_name, params=None):
        template = """from automation_functions import {function_name}
def main():
    try:
        {execution}
        print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
        execution = f"{function_name}()"
        if params:
            param_str = ", ".join([f"'{p}'" if isinstance(p, str) else str(p) for p in params])
            execution = f"{function_name}({param_str})"
        
        return template.format(function_name=function_name, execution=execution)

# Temporary test code
if __name__ == "__main__":
    generator = CodeGenerator()
    code = generator.generate_code("open_chrome")
    print(code)
