import os
from pulp import LpMinimize, LpProblem, LpStatus, LpVariable, LpInteger

# Create the maximization problem
model = LpProblem(name="Minimização", sense=LpMinimize)

# Initialize the variables
xa = LpVariable(name="Quant. do produto A que será produzido", lowBound=0, cat=LpInteger)
xat = LpVariable(name="Quant. do produto A que será terceirizado", lowBound=0, cat=LpInteger)

xb = LpVariable(name="Quant. do produto B que será produzido", lowBound=0, cat=LpInteger)
xbt = LpVariable(name="Quant. do produto B que será terceirizado", lowBound=0, cat=LpInteger)


# Add the constraints to the model. Use += to append expressions to the model
model += (xa + xat == 30000)
model += (xb + xbt == 15000)
model += (0.20*xa + 0.40*xb <= 10000)
model += (0.30*xa + 0.50*xb <= 15000)
model += (0.10*xa + 0.10*xb <= 5000)


# Objective Function
obj_func = 55*xa + 67*xat + 85*xb + 95*xbt
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