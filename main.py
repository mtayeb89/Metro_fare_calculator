# cairo_metro_fare_calculator.py

def calculate_metro_fare(stations):
    """
    Function to calculate the fare for the Cairo Metro based on the number of stations traveled.

    Parameters:
    stations (int): Number of stations traveled by the user.

    Returns:
    int: The fare in Egyptian Pounds (EGP) based on the number of stations.
    """
    if stations <= 0:
        return "Invalid input. The number of stations must be greater than 0."

    # Define fare bands for Cairo Metro
    if stations <= 9:
        return 8  # Fare for 1-9 stations is 5 EGP
    elif stations <= 16:
        return 10  # Fare for 10-16 stations is 7 EGP
    else:
        return 15  # Fare for more than 16 stations is 10 EGP


def main():
    """
    Main function to interact with the user, get the number of stations, and display the fare.
    """
    try:
        # User input for the number of stations
        stations = int(input("Enter the number of stations you're traveling: "))
        # Calculate the fare
        fare = calculate_metro_fare(stations)
        print(f"Your metro fare is: {fare} EGP")
    except ValueError:
        print("Invalid input. Please enter a valid number of stations.")


if __name__ == "__main__":
    main()
