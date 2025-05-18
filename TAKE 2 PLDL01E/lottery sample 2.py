import random
from datetime import datetime


def pcso_lotto_draw():
    return sorted(random.sample(range(1, 59), 6))


def generate_jackpot(min_prize=100_000_000, max_prize=50_000_000_000):
    return random.randint(min_prize, max_prize)


def get_user_numbers():
    print("\n🎫 Enter your 6 unique numbers (1-58):")
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            num = int(input(f"Enter number {len(user_numbers) + 1}: "))
            if num < 1 or num > 58:
                print("❌ Number must be between 1 and 58.")
            elif num in user_numbers:
                print("❌ You already entered that number.")
            else:
                user_numbers.add(num)
        except ValueError:
            print("❌ Invalid input. Enter a number.")
    return sorted(user_numbers)


def check_winner(user, draw):
    return user == draw


def display_result(draw_date, draw, user, jackpot):
    print("\n🎉 PCSO 6/58 LOTTO DRAW RESULT 🎉")
    print(f"📅 Draw Date: {draw_date.strftime('%B %d, %Y')}")
    print("🏆 Winning Numbers:", ' - '.join(f"{n:02d}" for n in draw))
    print("🎫 Your Numbers:   ", ' - '.join(f"{n:02d}" for n in user))
    print(f"💰 Jackpot Prize: ₱{jackpot:,}")

    if check_winner(user, draw):
        print("\n🎊 CONGRATULATIONS! YOU HIT THE JACKPOT! 🎊")
    else:
        print("\n😢 Sorry, you didn't win. Try again!")

def main():
    while True:
        draw_date = datetime.now()
        draw = pcso_lotto_draw()
        user = get_user_numbers()
        jackpot = generate_jackpot()

        display_result(draw_date, draw, user, jackpot)

        again = input("\n🔁 Would you like to draw again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Thank you for playing. Good luck next time!")
            break


if __name__ == "__main__":
    main()
