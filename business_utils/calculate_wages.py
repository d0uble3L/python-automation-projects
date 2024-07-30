def calculate_federal_tax(annual_wage):
    brackets = [
        (0, 11000, 0.10),
        (11001, 44725, 0.12),
        (44726, 95375, 0.22),
        (95376, 182100, 0.24),
        (182101, 231250, 0.32),
        (231251, 578125, 0.35),
        (578126, float('inf'), 0.37),
    ]

    tax = 0
    for lower, upper, rate in brackets:
        if annual_wage > lower:
            income_in_bracket = min(annual_wage, upper) - lower
            tax += income_in_bracket * rate
        else:
            break

    return tax

def calculate_state_tax(annual_wage, state_tax_rate=0.0495):
    return annual_wage * state_tax_rate

def calculate_wages_from_hourly(hourly_wage):
    # Constants
    WORK_HOURS_PER_WEEK = 40
    WEEKS_PER_YEAR = 52

    # Calculations
    weekly_wage = hourly_wage * WORK_HOURS_PER_WEEK
    annual_wage = weekly_wage * WEEKS_PER_YEAR
    monthly_wage = annual_wage / 12

    return hourly_wage, weekly_wage, monthly_wage, annual_wage

def calculate_hourly_from_annual(annual_wage):
    # Constants
    WORK_HOURS_PER_WEEK = 40
    WEEKS_PER_YEAR = 52

    # Calculations
    weekly_wage = annual_wage / WEEKS_PER_YEAR
    hourly_wage = weekly_wage / WORK_HOURS_PER_WEEK
    monthly_wage = annual_wage / 12

    return hourly_wage, weekly_wage, monthly_wage, annual_wage

def main():
    # User input to determine conversion type
    print("What would you like to do?")
    print("1. Calculate wages from hourly wage")
    print("2. Calculate hourly wage from annual salary")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        try:
            hourly_wage = float(input("Enter your hourly wage: $"))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            return

        # Calculate wages from hourly wage
        hourly, weekly, monthly, annual = calculate_wages_from_hourly(hourly_wage)
        federal_tax = calculate_federal_tax(annual)
        state_tax = calculate_state_tax(annual)
        total_taxes = federal_tax + state_tax
        net_annual = annual - total_taxes
        net_monthly = net_annual / 12
        net_weekly = net_annual / 52
        net_hourly = net_weekly / 40

        print("\n--- Breakdown of wages from hourly wage ---")
        print(f"{'Hourly Wage:':<20} ${hourly:,.2f}")
        print(f"{'Weekly Wage:':<20} ${weekly:,.2f}")
        print(f"{'Monthly Wage:':<20} ${monthly:,.2f}")
        print(f"{'Annual Wage:':<20} ${annual:,.2f}")
        print()
        print(f"{'Federal Tax:':<20} ${federal_tax:,.2f}")
        print(f"{'State Tax:':<20} ${state_tax:,.2f}")
        print(f"{'Total Taxes:':<20} ${total_taxes:,.2f}")
        print()
        print(f"{'Net Annual Wage:':<20} ${net_annual:,.2f}")
        print(f"{'Net Monthly Wage:':<20} ${net_monthly:,.2f}")
        print(f"{'Net Weekly Wage:':<20} ${net_weekly:,.2f}")
        print(f"{'Net Hourly Wage:':<20} ${net_hourly:,.2f}")

    elif choice == '2':
        try:
            annual_wage = float(input("Enter your annual salary: $"))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            return

        # Calculate hourly wage from annual salary
        hourly, weekly, monthly, annual = calculate_hourly_from_annual(annual_wage)
        federal_tax = calculate_federal_tax(annual)
        state_tax = calculate_state_tax(annual)
        total_taxes = federal_tax + state_tax
        net_annual = annual - total_taxes
        net_monthly = net_annual / 12
        net_weekly = net_annual / 52
        net_hourly = net_weekly / 40

        print("\n--- Breakdown of wages from annual salary ---")
        print(f"{'Hourly Wage:':<20} ${hourly:,.2f}")
        print(f"{'Weekly Wage:':<20} ${weekly:,.2f}")
        print(f"{'Monthly Wage:':<20} ${monthly:,.2f}")
        print(f"{'Annual Wage:':<20} ${annual:,.2f}")
        print()
        print(f"{'Federal Tax:':<20} ${federal_tax:,.2f}")
        print(f"{'State Tax:':<20} ${state_tax:,.2f}")
        print(f"{'Total Taxes:':<20} ${total_taxes:,.2f}")
        print()
        print(f"{'Net Annual Wage:':<20} ${net_annual:,.2f}")
        print(f"{'Net Monthly Wage:':<20} ${net_monthly:,.2f}")
        print(f"{'Net Weekly Wage:':<20} ${net_weekly:,.2f}")
        print(f"{'Net Hourly Wage:':<20} ${net_hourly:,.2f}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
