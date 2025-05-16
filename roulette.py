import random

def spin_roulette():
    numbers = list(range(37))  # 0 to 36
    colors = ['Red', 'Black'] * 18 + ['Green']  # 18 Red, 18 Black, 1 Green
    pockets = list(zip(numbers, colors))
    
    spin_result = random.choice(pockets)
    return spin_result

def calculate_payout(bet_type, bet_value, result_number, result_color, bet_amount):
    if bet_type == 'number' and bet_value == result_number:
        return bet_amount * 35  # Payout 35:1
    elif bet_type == 'color' and bet_value == result_color:
        return bet_amount * 2  # 1:1 payout
    elif bet_type == 'odd_even' and ((bet_value == 'Odd' and result_number % 2 == 1) or (bet_value == 'Even' and result_number % 2 == 0 and result_number != 0)):
        return bet_amount * 2
    elif bet_type == 'high_low' and ((bet_value == 'High' and 19 <= result_number <= 36) or (bet_value == 'Low' and 1 <= result_number <= 18)):
        return bet_amount * 2
    elif bet_type == 'dozen' and ((bet_value == '1st' and 1 <= result_number <= 12) or (bet_value == '2nd' and 13 <= result_number <= 24) or (bet_value == '3rd' and 25 <= result_number <= 36)):
        return bet_amount * 3
    elif bet_type == 'column' and ((bet_value == '1st' and result_number % 3 == 1) or (bet_value == '2nd' and result_number % 3 == 2) or (bet_value == '3rd' and result_number % 3 == 0 and result_number != 0)):
        return bet_amount * 3
    elif bet_type == 'split' and result_number in bet_value:
        return bet_amount * 17
    elif bet_type == 'corner' and result_number in bet_value:
        return bet_amount * 8
    elif bet_type == 'street' and result_number in bet_value:
        return bet_amount * 11
    else:
        return -bet_amount

def main():
    print("Welcome to Advanced Python Roulette!")
    balance = 100  # Starting balance
    
    while balance > 0:
        print(f"Your current balance: ${balance}")
        try:
            bet_amount = int(input("Enter your bet amount (0 to quit): "))
            if bet_amount == 0:
                break
            if bet_amount > balance:
                print("You don't have enough balance!")
                continue
            
            print("Betting options: 'number', 'color', 'odd_even', 'high_low', 'dozen', 'column', 'split', 'corner', 'street'")
            bet_type = input("Choose your bet type: ").strip().lower()
            
            if bet_type == 'number':
                bet_value = int(input("Enter a number (0-36): "))
                if bet_value not in range(37):
                    print("Invalid number! Try again.")
                    continue
            elif bet_type == 'color':
                bet_value = input("Bet on 'Red' or 'Black': ").strip().capitalize()
                if bet_value not in ['Red', 'Black']:
                    print("Invalid color! Try again.")
                    continue
            elif bet_type == 'odd_even':
                bet_value = input("Bet on 'Odd' or 'Even': ").strip().capitalize()
                if bet_value not in ['Odd', 'Even']:
                    print("Invalid choice! Try again.")
                    continue
            elif bet_type == 'high_low':
                bet_value = input("Bet on 'High' (19-36) or 'Low' (1-18): ").strip().capitalize()
                if bet_value not in ['High', 'Low']:
                    print("Invalid choice! Try again.")
                    continue
            elif bet_type == 'dozen':
                bet_value = input("Bet on '1st' (1-12), '2nd' (13-24), or '3rd' (25-36): ").strip()
                if bet_value not in ['1st', '2nd', '3rd']:
                    print("Invalid choice! Try again.")
                    continue
            elif bet_type == 'column':
                bet_value = input("Bet on '1st' (left), '2nd' (middle), or '3rd' (right) column: ").strip()
                if bet_value not in ['1st', '2nd', '3rd']:
                    print("Invalid choice! Try again.")
                    continue
            elif bet_type == 'split':
                bet_value = list(map(int, input("Enter two numbers separated by a space: ").split()))
                if len(bet_value) != 2 or any(num not in range(37) for num in bet_value):
                    print("Invalid numbers! Try again.")
                    continue
            elif bet_type == 'corner':
                bet_value = list(map(int, input("Enter four numbers forming a square (separated by spaces): ").split()))
                if len(bet_value) != 4 or any(num not in range(37) for num in bet_value):
                    print("Invalid numbers! Try again.")
                    continue
            elif bet_type == 'street':
                bet_value = list(map(int, input("Enter three consecutive numbers in a row (separated by spaces): ").split()))
                if len(bet_value) != 3 or any(num not in range(37) for num in bet_value):
                    print("Invalid numbers! Try again.")
                    continue
            else:
                print("Invalid bet type! Try again.")
                continue
            
            # Spin the roulette
            result_number, result_color = spin_roulette()
            print(f"Roulette spun... {result_number} ({result_color})")
            
            # Calculate winnings or losses
            payout = calculate_payout(bet_type, bet_value, result_number, result_color, bet_amount)
            balance += payout
            
            if payout > 0:
                print(f"You won ${payout - bet_amount}! 🎉")
            else:
                print("You lost! 😢")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
    
    print("Thanks for playing! Your final balance:", balance)

if __name__ == "__main__":
    main()
