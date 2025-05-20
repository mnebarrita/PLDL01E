import tkinter as tk
from tkinter import messagebox, ttk
import random
from datetime import datetime

# ==========================
# --- Core Lotto Logic ---
# ==========================

def pcso_lotto_draw():
    """
    Simulate the 6/58 lotto draw:
    Returns 6 unique numbers between 1 and 58, sorted.
    """
    return sorted(random.sample(range(1, 59), 6))


def generate_jackpot(min_prize=100_000_000, max_prize=50_000_000_000):
    """
    Generate a random jackpot prize within a realistic range.
    """
    return random.randint(min_prize, max_prize)


def count_matches(user, draw):
    """
    Count how many numbers match between user input and draw result.
    """
    return len(set(user).intersection(set(draw)))


def draw_digits(num_digits):
    """
    Generate a list of random digits for digit-based games (3D, 4D, 6D).
    """
    return [random.randint(0, 9) for _ in range(num_digits)]


# ==========================
# --- Auto Win Simulation ---
# ==========================

def auto_win_with_target(target):
    """
    Automatically simulate lotto draws until the target win tier is reached.
    Supports both 6/58 and digit-based games.
    """
    attempts = 0
    selected = lotto_type.get()

    if selected == "6/58":
        target_num = {
            '3 Matches': 3,
            '4 Matches': 4,
            '5 Matches': 5,
            'Jackpot': 6,
            'Win': 6,  # fallback if needed
        }[target]

        while True:
            attempts += 1
            user_nums = sorted(random.sample(range(1, 59), 6))
            draw = pcso_lotto_draw()
            matches = count_matches(user_nums, draw)

            if matches >= target_num:
                jackpot = generate_jackpot()
                if matches == 6:
                    prize = f"🎉 JACKPOT! You win ₱{jackpot:,}!"
                elif matches == 5:
                    prize = "You matched 5 numbers! Consolation Prize: ₱100,000"
                elif matches == 4:
                    prize = "You matched 4 numbers! Consolation Prize: ₱10,000"
                else:
                    prize = "You matched 3 numbers! Consolation Prize: ₱500"

                result_text = (
                    f"📅 Draw Date: {datetime.now().strftime('%B %d, %Y')}\n"
                    f"🎯 Winning Numbers: {draw}\n"
                    f"🎫 Your Numbers:   {user_nums}\n"
                    f"💰 Jackpot Prize: ₱{jackpot:,}\n\n"
                    f"{prize}"
                )
                messagebox.showinfo("Auto Win - 6/58 Result", result_text)
                break

    else:
        digit_count = int(selected[0])
        while True:
            attempts += 1
            user_digits = draw_digits(digit_count)
            draw = draw_digits(digit_count)
            if user_digits == draw:
                result_text = (
                    f"📅 Draw Date: {datetime.now().strftime('%B %d, %Y')}\n"
                    f"🎯 Winning Digits: {''.join(map(str, draw))}\n"
                    f"🎫 Your Entry:     {''.join(map(str, user_digits))}\n\n"
                    f"🎉 You WIN 5000!"
                )
                messagebox.showinfo(f"Auto Win - {digit_count}D Result", result_text)
                break

    return attempts



def open_auto_win_dialog(event=None):
    """
    Popup dialog to select target win tier for auto-win simulation,
    adapting to the selected lotto type.
    """
    selected = lotto_type.get()
    popup = tk.Toplevel(root)
    popup.title("Auto Win Setup")
    popup.geometry("300x200")

    if selected == "6/58":
        tk.Label(popup, text="Select target win tier:").pack(pady=10)

        tiers = ['3 Matches', '4 Matches', '5 Matches', 'Jackpot']
        selected_tier = tk.StringVar(value=tiers[0])

        for tier in tiers:
            ttk.Radiobutton(popup, text=tier, variable=selected_tier, value=tier).pack(anchor='w')

        def start_auto_win():
            target = selected_tier.get()
            popup.destroy()
            attempts = auto_win_with_target(target)
            messagebox.showinfo("Auto Win Result", f"Reached {target} in {attempts} attempts!")

        ttk.Button(popup, text="Start", command=start_auto_win).pack(pady=20)

    else:
        digit_count = int(selected[0])
        tk.Label(popup, text=f"Auto Win for {digit_count}D game").pack(pady=20)

        def start_auto_win_digit():
            popup.destroy()
            attempts = auto_win_with_target("Win")
            messagebox.showinfo("Auto Win Result", f"Auto Win hit after {attempts} attempts!")

        ttk.Button(popup, text="Start Auto Win", command=start_auto_win_digit).pack(pady=20)


# ==========================
# --- Lotto Game Logic ---
# ==========================

def draw_game(autoplay=False):
    """
    Main function to run the lotto game based on selected type.
    Validates user input and shows results with prizes.
    """
    selected = lotto_type.get()

    if selected == "6/58":
        # 6/58 Lotto
        try:
            if autoplay:
                user_nums = sorted(random.sample(range(1, 59), 6))
            else:
                user_nums = [int(entry.get()) for entry in user_inputs]
                if len(set(user_nums)) != 6:
                    raise ValueError("Duplicate numbers are not allowed.")
                if any(n < 1 or n > 58 for n in user_nums):
                    raise ValueError("Numbers must be between 1 and 58.")
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
            return

        draw = pcso_lotto_draw()
        jackpot = generate_jackpot()
        matches = count_matches(user_nums, draw)

        if matches == 6:
            prize = f"🎉 JACKPOT! You win ₱{jackpot:,}!"
        elif matches == 5:
            prize = "You matched 5 numbers! Consolation Prize: ₱100,000"
        elif matches == 4:
            prize = "You matched 4 numbers! Consolation Prize: ₱10,000"
        elif matches == 3:
            prize = "You matched 3 numbers! Consolation Prize: ₱500"
        else:
            prize = "No prize this time."

        result_text = (
            f"📅 Draw Date: {datetime.now().strftime('%B %d, %Y')}\n"
            f"🎯 Winning Numbers: {draw}\n"
            f"🎫 Your Numbers:   {sorted(user_nums)}\n"
            f"💰 Jackpot Prize: ₱{jackpot:,}\n\n"
            f"{prize}"
        )
        messagebox.showinfo("6/58 Draw Result", result_text)

    else:
        # Digit-based games: 3D, 4D, 6D
        digit_count = int(selected[0])
        try:
            if autoplay:
                user_digits = draw_digits(digit_count)
            else:
                user_input = int(user_inputs[0].get())
                user_digits = [int(d) for d in str(user_input).zfill(digit_count)]
                if len(user_digits) != digit_count:
                    raise ValueError(f"Enter exactly {digit_count} digits.")
        except ValueError:
            messagebox.showerror("Invalid Input", f"Enter a valid {digit_count}-digit number.")
            return

        draw = draw_digits(digit_count)
        prize = "🎉 You win 5,000 Pesos" if user_digits == draw else "😢 Try again."

        result_text = (
            f"📅 Draw Date: {datetime.now().strftime('%B %d, %Y')}\n"
            f"🎯 Winning Digits: {''.join(map(str, draw))}\n"
            f"🎫 Your Entry:     {''.join(map(str, user_digits))}\n\n"
            f"{prize}"
        )
        messagebox.showinfo(f"{digit_count}-Digit Draw Result", result_text)


# ==========================
# --- GUI Setup ---
# ==========================

root = tk.Tk()
root.title("PCSO Lotto App")
root.geometry("500x600")
root.resizable(False, False)

# Keybinding Ctrl+A for Auto Win popup
root.bind('<Control-a>', open_auto_win_dialog)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

# --- Variables ---
lotto_type = tk.StringVar(value="6/58")
user_inputs = []

# --- Layout Frames ---
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10)

# --- Helper Functions ---

def reset_inputs():
    """
    Clear all user input fields.
    """
    for entry in user_inputs:
        entry.delete(0, tk.END)


def update_inputs(*args):
    """
    Update input fields dynamically when lotto type changes.
    """
    for widget in input_frame.winfo_children():
        widget.destroy()
    user_inputs.clear()

    selected = lotto_type.get()
    if selected == "6/58":
        ttk.Label(input_frame, text="Enter your 6 numbers (1-58):").pack()
        box_frame = ttk.Frame(input_frame)
        box_frame.pack(pady=5)
        for _ in range(6):
            e = ttk.Entry(box_frame, width=5, justify='center', font=('Arial', 14))
            e.pack(side="left", padx=5)
            user_inputs.append(e)
    else:
        digit_count = int(selected[0])
        ttk.Label(input_frame, text=f"Enter your {digit_count}-digit number:").pack()
        e = ttk.Entry(input_frame, width=digit_count + 2, justify='center', font=('Arial', 20))
        e.pack(pady=10)
        user_inputs.append(e)

    reset_inputs()


# --- Lotto Type Selection ---
ttk.Label(main_frame, text="Choose Lotto Game:").pack()
options = ["6/58", "3D", "4D", "6D"]
for option in options:
    ttk.Radiobutton(main_frame, text=option, variable=lotto_type, value=option, command=update_inputs).pack(anchor="w")

# Initial input fields
update_inputs()

# --- Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

draw_button = ttk.Button(button_frame, text="Draw", command=lambda: draw_game())
draw_button.grid(row=0, column=0, padx=10)

auto_button = ttk.Button(button_frame, text="Lucky Pick", command=open_auto_win_dialog)
auto_button.grid(row=0, column=1, padx=10)

auto_draw_button = ttk.Button(button_frame, text="Auto Draw", command=lambda: draw_game(autoplay=True))
auto_draw_button.grid(row=0, column=2, padx=10)

# --- Hotkey Bindings ---
root.bind('<Return>', lambda event: draw_game())

root.mainloop()
