import random
import sys
import time
import winsound

def spin_sound():
    winsound.Beep(900, 80)   # same sound, same speed

def win_sound():
    winsound.Beep(1200, 200)
    winsound.Beep(1500, 300)

def jackpot_sound():
    for f in [1000, 1300, 1600, 1900]:
        winsound.Beep(f, 200)

def lose_sound():
    winsound.Beep(400, 500)

player_balance=1000
bet_limit=5000
symbols=["☘️","💫","🍒"]

def payout(symbol,amount):
    if symbol == "☘️":
        return amount * 10
    elif symbol == "💫":
        return amount * 5
    elif symbol == "🍒":
        return amount * 3
    else:
        return 0

def spin(amount):
    global player_balance
    print("SPINNING THE REELS...") 

    start_time = time.time()
    while time.time() - start_time < 10:

        reel1=random.choice(symbols)
        reel2=random.choice(symbols)
        reel3=random.choice(symbols)
        sys.stdout.write(f"\r🎰 {reel1} | {reel2} | {reel3}")
        sys.stdout.flush()
        spin_sound()
        time.sleep(0.1)
    print()

    if reel1==reel2 and reel2==reel3:
        win_amount=payout(reel1,amount)

        if reel1=="☘️":    
            print("JACKPOT!!! YOU WON THE MAXIMUM PRIZE")
            print("🏆CONGRATULATIONS YOU ARE A LUCKY WINNER") 
            print(f"🏆 YOU WON ₹{win_amount}")

        else:
            print("🥳HURRIE YOU WON! PLAY AGAIN TO EARN MORE")
        player_balance += win_amount
        print(f"YOUR BALANCE IS {player_balance}")

    else:
        print("😔SORRY YOU LOSE THE ROUND")
        player_balance=player_balance-amount
    print(f"YOUR BALANCE IS {player_balance}")
  
is_running=True

while is_running:
    print("\n----🎰 SLOT MACHINE ----")
    print("PLAY THE GAME DOUBLE THE EXCITMENT")
    print(f"Balance: ₹{player_balance}")
    print("1. 💫Spin")
    print("2. 💤Exit")
    print("**************************")
    choice = input("Choose an option: ")
    print("**************************")

    if choice=="1":
        amount=input("PLACE YOUR BET AMOUNT: ")

        if not amount.isdigit():
            print("❌ ONLY DIGITS ARE ALLOWED")
            continue
        amount=int(amount)

        if amount <= 0:
            print("❌ BET AMOUNT MUST BE GREATER THAN 0")
        elif amount > player_balance:
            print("INSUFFICIENT FUNDS")
        elif amount > bet_limit:
            print(f"BET AMOUNT SHOULD NOT EXCEED {bet_limit}")
        else:
            spin(amount)
    elif choice=="2":
        print("🙏THANK YOU FOR PLAYING THE GAME")
        is_running=False
    else:
        print("❌ INVALID OPTION!")
    if player_balance <= 0:
        print("💀 GAME OVER! NO BALANCE LEFT")
        is_running = False
print("---------VISIT AGAIN----------")

  

        
        
    






