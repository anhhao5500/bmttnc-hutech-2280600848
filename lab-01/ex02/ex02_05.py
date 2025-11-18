work_time = float(input ("Enter the number of hours worked per week:"))
salary = float(input("standard hourly wage:"))
hour = 44
overtime = max(0, work_time - hour)
pay = hour * salary + overtime * salary *1.5
print(f"employee's weekly pay is: {pay}")
