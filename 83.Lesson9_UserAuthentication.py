def print_section(title):
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"\n{'='*70}")

print_section("User Authentication System Demo")
has_valid_password = True
account_status = True
is_admin = False

print("Initial Security States:")
print(f"Valid password provided: {has_valid_password}")
print(f"Account is active {account_status}")
print(f"Has admin priviledges {is_admin}")
print("\nPerforming primary authentication check...")

can_login = has_valid_password and account_status
print(f"Can user log in to the system? {can_login}")
print("\nChecking administrative access...")
can_access_admin = can_login and is_admin
print(f"Can access admin panel? {can_access_admin}")
print("\nSimulating account deactivation...")

account_active = False
can_login = has_valid_password and account_active
can_access_admin = can_login and is_admin
print("\nUpdated Security Status:")
print(f"Account is active {account_active}")
print(f"Can user log in? {can_login}")
print(f"Can access admin panel? {can_access_admin}")

if __name__ == "__name__":
    print("\nUser Authentication Demo Completed!")