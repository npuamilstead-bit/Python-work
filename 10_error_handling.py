def safe_divide(numerator, denominator):
    try:
        return numerator/denominator
    except ZeroDivisionError:
        print("can't divide by zero.")
        return None
    except TypeError:
        print("Must be numbers.")
        return None
    
safe_divide(10, 0)
safe_divide(10, "zero")

def normalize_grade(score, max_score):
    
    try:
        
        if score < 0 or score > max_score:
                raise ValueError("Score out of acceptable range")
        percentage = (score / max_score) * 100
    except ZeroDivisionError:
        print("Max score cannot be zero.")
        return 0.0
    except ValueError:
        print("Score out of acceptable range")
        return 0.0
    else:
        print(f"Grade normalized: {percentage:.1f}%")
        return percentage
    finally:
        print("--- Calculation attempted ---")

normalize_grade(85, 100)
normalize_grade(105, 100)
normalize_grade(50, 0)

        
            
