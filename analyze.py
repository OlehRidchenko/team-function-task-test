def analyze_numbers(numbers):
    if not numbers:
        return {
            "sum": 0,
            "average": None,
            "maximum": None,
            "minimum": None,
            "even_count": 0,
            "odd_count": 0
        }

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = len(numbers) - even_count

    return {
        "sum": total,
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "even_count": even_count,
        "odd_count": odd_count
    }