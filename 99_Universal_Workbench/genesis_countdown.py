import datetime
import time

def system_check():
    # Ustawienie celu: 1 Stycznia 2026
    target_date = datetime.datetime(2026, 1, 1, 0, 0, 0)
    now = datetime.datetime.now()
    
    # Obliczenie czasu, który został
    remaining = target_date - now
    
    # Rozbicie na dni, godziny i minuty
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Output w stylu Terminala
    print("\n" + "="*40)
    print(" 🐍 GENESIS PROTOCOL: SYSTEM STATUS")
    print("="*40)
    print(f" [DATE] Current:  {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" [GOAL] Deploy:   2026-01-01 00:00:00")
    print("-" * 40)
    print(f" ⏳ COUNTDOWN:    {days} days, {hours}h {minutes}m")
    print("-" * 40)
    
    if remaining.total_seconds() > 0:
        print(" >> STATUS: PREPARING MODULES...")
        print(" >> MOTTO:  Biology was the past. Code is the future.")
    else:
        print(" >> STATUS: DEPLOYMENT ACTIVE! 🚀")
    print("="*40 + "\n")

if __name__ == "__main__":
    system_check()
