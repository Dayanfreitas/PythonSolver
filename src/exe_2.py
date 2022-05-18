import os
from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, LpInteger

# Create the maximization problem
model = LpProblem(name="Lucro empresa cadeira e mesa", sense=LpMaximize)

# Initialize the variables
x = LpVariable(name="Quant. de Cadeiras", lowBound=0, cat=LpInteger)
y = LpVariable(name="Quant. de Mesas", lowBound=0, cat=LpInteger)

# Add the constraints to the model. Use += to append expressions to the model
model += (5*x + 20*y <= 400)
model += (10*x + 15*y <= 450)

# Objective Function
obj_func = 180*x + 320*y

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