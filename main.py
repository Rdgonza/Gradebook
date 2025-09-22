def letter_grade(score):
    """Return letter grade for a numeric average."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    name = input("Enter student name: ")
    g1 = float(input("Enter grade 1: "))
    g2 = float(input("Enter grade 2: "))
    g3 = float(input("Enter grade 3: "))
    g4 = float(input("Enter grade 4: "))
    g5 = float(input("Enter grade 5: "))
    grades = [g1, g2, g3, g4, g5]

    avg = sum(grades) / 5
    avg_str = f"{avg:.1f}"

    print(name)
    print()
    print(f"Average: {avg_str}")
    print()
    print(f"Letter Grade: {letter_grade(avg)}")
if __name__ == "__main__":
    main()