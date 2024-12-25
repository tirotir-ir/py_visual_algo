import os
import subprocess


def list_examples():
    """
    List all Python files in the examples directory.
    """
    examples_dir = os.path.join(os.path.dirname(__file__), "../examples")
    if not os.path.exists(examples_dir):
        return []
    return [f for f in os.listdir(examples_dir) if f.endswith(".py")]


def run_example(example_name):
    """
    Run the selected example.
    """
    examples_dir = os.path.join(os.path.dirname(__file__), "../examples")
    example_path = os.path.join(examples_dir, example_name)
    if not os.path.exists(example_path):
        print(f"Error: Example '{example_name}' not found.")
        return

    try:
        print(f"Running example: {example_name}")
        subprocess.run(["python", example_path], check=True)
        print(f"Example '{example_name}' ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Execution Error: Error occurred while running '{example_name}': {e}")
    except Exception as e:
        print(f"Unexpected Error: An unexpected error occurred:\n{e}")


def cli():
    """
    CLI for running embedded examples in the 'examples' directory.
    """
    examples = list_examples()
    if not examples:
        print("No examples available in the 'examples' directory.")
        return

    print("\nAvailable Examples:")
    for i, example in enumerate(examples, start=1):
        print(f"{i}. {example}")

    try:
        choice = int(input("\nEnter the number of the example to run: ")) - 1
        if 0 <= choice < len(examples):
            run_example(examples[choice])
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    cli()
