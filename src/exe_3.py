import os
from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, LpInteger

# Create the maximization problem
model = LpProblem(name="Lucro empresa", sense=LpMaximize)

# Initialize the variables
x = LpVariable(name="Soldado", lowBound=0, cat=LpInteger)
y = LpVariable(name="Trem", lowBound=0, cat=LpInteger)

# Add the constraints to the model. Use += to append expressions to the model
model += (2*x + y <= 100, "Horas de acabamento")
model += (x + y <=  80, "Horas de carpintaria")
model += (x <= 40, "Max. de soldados")

# Objective Function
obj_func = 3*x + 2*y 

# Add Objective function to the model
model += obj_func

status = model.solve()

os.system('clear')
print(model)

print('\n')
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

print('\n')
for var in model.variables():
  print(f"{var.name}: {var.value()}")

print("\n")
for name, constraint in model.constraints.items():
  print(f"{name}: {constraint.value()}")


# For this code this article was used as a reference: https://towardsdatascience.com/how-to-create-your-first-linear-programming-solver-in-python-284e3fe5b811