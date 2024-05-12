import tkinter as tk
import random


dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def roll_dice():
    """Roll the dice the specified number of times and update the output with results and statistics."""
    try:
        num_rolls = int(num_rolls_entry.get())
    except ValueError:
        num_rolls = 1

    for _ in range(num_rolls):
        result = random.randint(1, 6)
        dice_counts[result] += 1

      
        output_message = f"Dice is {result}, "
        output_message += ", ".join(f"{key}={value}" for key, value in dice_counts.items())


        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, output_message + "\n")
        output_text.config(state=tk.DISABLED)
    output_text.yview(tk.END)


def validate_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False


root = tk.Tk()
root.title("Dice Roller")
root.geometry("400x350")

vcmd = root.register(validate_input)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

num_rolls_entry = tk.Entry(control_frame, font=("Arial", 14), validate="key", validatecommand=(vcmd, '%P'))
num_rolls_entry.insert(0, "1")
num_rolls_entry.pack(side=tk.LEFT, padx=(0, 10))


roll_button = tk.Button(control_frame, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.pack(side=tk.LEFT)


output_text = tk.Text(root, height=10, width=50, state=tk.DISABLED, wrap=tk.WORD)
scroll = tk.Scrollbar(root, command=output_text.yview)
output_text.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_text.pack(pady=(0, 10))


root.mainloop()
