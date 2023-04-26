# Convert between fahreneheit and celcius using two functions.

def f_to_c(f_temp):
  c_temp = (f_temp - 32)*(5/9)
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp *(9/5) + 32
  return f_temp

f100_in_celsius = f_to_c(100)
print("100 degrees farenheit is", f100_in_celsius, "degrees celcius")

c0_in_fahrenheit = c_to_f(0)
print("0 degrees celcius is", c0_in_fahrenheit, "degrees farenheit")



# make force, energy, and work calculations based on the properties of an object.

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

def get_energy(mass, c = 3*10**8):
  energy = mass * c**2
  return energy

#This function assumes the force and velocity vectors present on the train are always parallel to each other.
def get_work(mass, acceleration, distance):
  work = mass*acceleration*distance
  return work
  

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies", train_force, "Newtons of force.")

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules of energy. (This is untrue even if it was a nuclear bomb. The entire mass of the bomb will never be converted into energy unless the bomb was using matter/antimatter annihilation as its method of energy generation.)")

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters of travel.")

