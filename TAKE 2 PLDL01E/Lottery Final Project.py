import random
from datetime import datetime

def pcso_lotto_draw():
    # Generate 6 unique random numbers between 1 and 58
    winning_numbers = random.sample(range(1, 59), 6)
    winning_numbers.sort()
    return winning_numbers

def generate_jackpot(min_prize=100_000_000, max_prize=500_000_000):
    # Random jackpot within range
    return random.randint(min_prize, max_prize)

def display_draw(draw_date, numbers, jackpot):
    print("\n🎉 PCSO 6/58 LOTTO DRAW RESULT 🎉")
    print(f"📅 Draw Date: {draw_date.strftime('%B %d, %Y')}")
    print("🏆 Winning Numbers:", ' - '.join(f"{num:02d}" for num in numbers))
    print(f"💰 Jackpot Prize: ₱{jackpot:,}")

if __name__ == "__main__":
    draw_date = datetime.now()
    draw_result = pcso_lotto_draw()
    jackpot = generate_jackpot()

    display_draw(draw_date, draw_result, jackpot)
    