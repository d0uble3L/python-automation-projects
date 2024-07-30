def calculate_insights(revenue, number_of_sales, visits):
    # Ensure we have valid input
    if number_of_sales <= 0 or visits <= 0:
        raise ValueError("Number of sales and visits must be greater than zero.")
    
    # Calculate average revenue per sale
    avg_revenue_per_sale = revenue / number_of_sales
    
    # Calculate average revenue per visit
    avg_revenue_per_visit = revenue / visits
    
    # Calculate conversion rate
    conversion_rate = (number_of_sales / visits) * 100
    
    return avg_revenue_per_sale, avg_revenue_per_visit, conversion_rate

def main():
    try:
        # Request user input
        revenue = float(input("Enter the total revenue ($): "))
        number_of_sales = int(input("Enter the number of sales: "))
        visits = int(input("Enter the number of visits: "))
        
        # Calculate insights
        avg_revenue_per_sale, avg_revenue_per_visit, conversion_rate = calculate_insights(revenue, number_of_sales, visits)
        
        # Print results
        print(f"Average Revenue Per Sale: ${avg_revenue_per_sale:.2f}")
        print(f"Average Revenue Per Visit: ${avg_revenue_per_visit:.2f}")
        print(f"Conversion Rate: {conversion_rate:.2f}%")
    
    except ValueError as e:
        print(f"Input error: {e}")

# Run the main function
if __name__ == "__main__":
    main()