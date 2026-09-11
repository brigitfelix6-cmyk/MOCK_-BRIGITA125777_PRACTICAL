number_of_cow=int(input("enter the number of cows"))
milk_per_cow=float(input("enter the average amount of milk produced per cow per day in liters"))
cost_per_liter=float(input("enter the cost of production per liter of milk"))
total_amount_milk=milk_per_cow*number_of_cow
total_cost=total_amount_milk*cost_per_liter
print("total milk per day:",total_amount_milk)
print("total cost of milk production per day:",total_cost)
