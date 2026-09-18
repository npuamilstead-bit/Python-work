
def tuition_calculator(credit_s,cost_per_credit):
    base_tuition = credit_s * cost_per_credit
    if credit_s >= 12:
        base_tuition += 250
    else:
        base_tuition += 100
    return base_tuition
fall_tuition = tuition_calculator(15, 600)
spring_tuition = tuition_calculator(6, 600)
total_year = fall_tuition + spring_tuition

print(f"Fall: {fall_tuition:,.2f}, Spring: {spring_tuition:,.2f}, Total Cost: {total_year:,.2f}")


