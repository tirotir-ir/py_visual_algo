import tkinter as tk
from tkinter import messagebox
import os
import subprocess


def list_examples():
    """
    List all Python files in the examples directory.
    """
    examples_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../examples")
    )
    if not os.path.exists(examples_dir):
        return []
    return [f for f in os.listdir(examples_dir) if f.endswith(".py")]


def run_example(example_name):
    """
    Run the selected example.
    """
    examples_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../examples")
    )
    example_path = os.path.join(examples_dir, example_name)
    print(f"Attempting to run: {example_path}")  # Debugging statement

    if not os.path.exists(example_path):
        messagebox.showerror("Error", f"Example '{example_name}' not found.")
        return

    try:
        subprocess.run(["python", example_path], check=True)
        messagebox.showinfo("Success", f"Example '{example_name}' ran successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Execution Error", f"Error occurred while running '{example_name}':\n{e}"
        )
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred:\n{e}")


def launch_gui():
    """
    Launch the GUI for running examples.
    """
    examples = list_examples()
    print(f"Examples found: {examples}")  # Debugging statement

    if not examples:
        messagebox.showerror("Error", "No examples found in the 'examples' directory.")
        return

    def on_run_button_click():
        selected_example = example_listbox.get(tk.ACTIVE)
        print(f"Selected Example: {selected_example}")  # Debugging statement
        if selected_example:
            run_example(selected_example)
        else:
            messagebox.showwarning("Warning", "Please select an example to run.")

    # Create the main window
    window = tk.Tk()
    window.title("py_visual_algo Examples")

    # Adjust window size to fit content
    window.geometry("600x500")
    window.resizable(True, True)

    # Create a frame for better layout control
    frame = tk.Frame(window, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Title label
    tk.Label(frame, text="Available Examples", font=("Helvetica", 16)).grid(
        row=0, column=0, columnspan=2, pady=(0, 20)
    )

    # Example listbox
    example_listbox = tk.Listbox(frame, height=20, width=50, font=("Helvetica", 12))
    example_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    for example in examples:
        example_listbox.insert(tk.END, example)

    # Scrollbar for the listbox
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=example_listbox.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    example_listbox.config(yscrollcommand=scrollbar.set)

    # Run button
    run_button = tk.Button(
        frame, text="Run Example", font=("Helvetica", 14), command=on_run_button_click
    )
    run_button.grid(row=2, column=0, columnspan=2, pady=(20, 0), sticky="ew")

    # Adjust grid weights for resizing
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Run the GUI event loop
    window.mainloop()


if __name__ == "__main__":
    launch_gui()
