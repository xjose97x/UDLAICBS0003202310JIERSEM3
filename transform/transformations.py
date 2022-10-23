
def month_name(month_number):
    """Return the name of the month for the given month number.

    Args:
        month_number (int): The number of the month.

    Returns:
        str: The name of the month.

    Raises:
        ValueError: If the month number is not between 1 and 12.

    """
    if month_number < 1 or month_number > 12:
        raise ValueError("Month number must be between 1 and 12")
    return {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }[month_number]
