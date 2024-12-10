def print_section(title):
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"\n{'='*70}")

print_section("Basic Bolean Operations - Day Off Checker")

is_weekend = True
is_holiday = False
print("Current status:")
print(f"Is it a weekend?: {is_weekend}")
print(f"Is it a holiday?: {is_holiday}")
get_day_off = is_weekend or is_holiday
print("\nFinal Decision")
print(f"Does the employee get a day off? {get_day_off}")
print(f"\nLet's simulate a holiday during a workday...")
is_weekend = False
is_holiday = True
get_day_off = is_weekend or is_holiday
print(f"Is it a weekend? {is_weekend}")
print(f"Is it a holiday? {is_holiday}")
print(f"Does the employee get a day off? {get_day_off}")

if __name__ == "__name__":
    print("\nBasic Bolean Demo Completed!")