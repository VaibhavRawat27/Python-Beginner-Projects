from datetime import datetime, timedelta
import time

def get_lifetime_stats(birthdate):
    now = datetime.now()
    age = now - birthdate

    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30

    total_days = age.days
    total_seconds = int(age.total_seconds())
    total_hours = total_seconds // 3600
    total_minutes = total_seconds // 60

    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": total_days,
        "total_hours": total_hours,
        "total_minutes": total_minutes,
        "total_seconds": total_seconds
    }

def get_milestones(birthdate):
    milestones = [1000, 5000, 10000, 20000]
    upcoming = []

    now = datetime.now()
    for day in milestones:
        milestone_date = birthdate + timedelta(days=day)
        if milestone_date > now:
            upcoming.append((day, milestone_date.strftime('%Y-%m-%d')))
    return upcoming

def compare_fun_facts(total_days, total_seconds):
    moon_cycle_days = 27.3
    heartbeats = total_seconds // 0.8  # avg 75 bpm
    breaths = total_seconds // 4       # avg 15 breaths/min

    return {
        "full_moons": round(total_days / moon_cycle_days),
        "heartbeats": int(heartbeats),
        "breaths": int(breaths)
    }

def main():
    print("👶 Welcome to the Lifetime Clock!")
    birth_input = input("📅 Enter your birthdate (YYYY-MM-DD): ")

    try:
        birthdate = datetime.strptime(birth_input, "%Y-%m-%d")
    except:
        print("❌ Invalid date format.")
        return

    stats = get_lifetime_stats(birthdate)
    fun = compare_fun_facts(stats['total_days'], stats['total_seconds'])
    milestones = get_milestones(birthdate)

    print("\n🕰️ Your Lifetime Stats So Far:")
    print(f"➡️ {stats['years']} years, {stats['months']} months, {stats['days']} days old")
    print(f"📆 Total days lived: {stats['total_days']}")
    print(f"⏱️ Total hours: {stats['total_hours']}")
    print(f"⏱️ Total minutes: {stats['total_minutes']}")
    print(f"⏱️ Total seconds: {stats['total_seconds']}")

    print("\n🌕 Fun Life Comparisons:")
    print(f"🌝 You've lived through about {fun['full_moons']} full moons")
    print(f"❤️ Estimated heartbeats: {fun['heartbeats']:,}")
    print(f"💨 Estimated breaths: {fun['breaths']:,}")
    print(f"💸 If ₹1 per second — you've 'earned': ₹{stats['total_seconds']:,}")

    print("\n🎯 Upcoming Milestones:")
    if milestones:
        for m in milestones:
            print(f"📌 Day {m[0]} → On: {m[1]}")
    else:
        print("✅ You’ve passed all major milestones we track!")

    print("\n✨ Keep making every second count!")

if __name__ == "__main__":
    main()
