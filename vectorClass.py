# Natalia Miller

''' The following code has been adapted from psuedocode code:
    I. Millington, Artificial Intelligence for Games, Third Edition,
    CRC Press, Boca Raton FL, 2019
'''

import numpy as np 
from matplotlib import pyplot as plt

'''
10 int values, 1 bool value in vector for plotting
1. simulation time
2. character id (numeric)
3. position x (meters)
4. position z (meters)
5. velocity x (meters per second)
6. velocity z (meters per second)
7. linear acceleration x (meters per second per second)
8. linear acceleration z (meters per second per second)
9. orientation (radians)
10. steering behavior code (1=Continue, 6=Seek, 7=Flee, 8=Arrive)
11. collision status (TRUE if collided, FALSE if not collided; always FALSE for Program 1)
'''



# From https://www.digitalocean.com/community/tutorials/vectors-in-python

# Horizontal Vector



lst = [10,20,30,40,50] 

vctr = np.array(lst) 

vctr = np.array(lst) 

print("Vector created from a list:") 
print(vctr)

# Vertical Vector

lst = [[2], 
        [4], 
        [6],
          [10]]  

vctr = np.array(lst) 

vctr = np.array(lst) 

print("Vector created from a list:") 
print(vctr)

# dot product
vctr_dot = vctr1.dot(vctr2)


# Movement behaviors (Seek, Flee, Arrive, Continue)

#------------------------------------------------#
#                Movement Behaviors              #
#------------------------------------------------#

class DynamicSeek:
  ''' Seek: Match character position to target position
      - Determine direction to target
      - Accelerate in that direction at max rate up to max speed

      character: Kinematic      # position and orientation for character
      target: Kinematic         # position and orientation for target
      maxAcceleration: float    # maximum acceleration rate for character
  '''
  def __init__(self):
    character = 0 
    target = 0
    max_acceleration = 0 

  def get_steering() -> SteeringOutput:
    # Create output structure
    result = new SteeringOutput()

    # Get the direction to the target
    result.linear = target.position – character.position

    # Accelerate at maximum rate
    result.linear.normalize()
    result.linear *= max_acceleration

    # Output steering
    result.angular = 0
    return result

class DynamicFlee:
  ''' Flee: Negate character position to target position
      - Determine direction to target
      - Accelerate in opposite direction at max rate up to max speed

      character: Kinematic      # position and orientation for character
      target: Kinematic         # position and orientation for target
      maxAcceleration: float    # maximum acceleration rate for character
  '''
  def __init__(self):
      character = 0 
      target = 0
      max_acceleration = 0 

  def getSteering() -> SteeringOutput:
    # Create output structure
    result = new SteeringOutput()

    # Get the direction to the target
    result.linear = character.position – target.position

    # Accelerate at maximum rate
    result.linear.normalize()
    result.linear *= maxAcceleration

    # Output steering
    result.angular = 0
    return result

class DynamicArrive:
  ''' Arrive: Uses two distance raddii to solve the issue that accelerating
      at max rate to max speed causes, i.e. overshooting or orbiting target
      - Slowing-down radius; distance to target below -> character slows down
      - Arrival radius; distance to target below -> character stops

      Direction
        - Desired direction calculated directly toward target
      Speed
        - Outside slowing-down radius, desired speed set to max speed
        - Between radii, desired speed interpolated between max and 0
        - Inside arrival radius, desired speed set to 0
      Velocity
        - Direction and speed combined to give desired velocity
        - Acceleration set to change current velocity to desired velocity

      character: Kinematic        # position and orientation for character
      target: Kinematic           # position and orientation for target
      maxAcceleration: float      # maximum acceleration rate for character
      maxSpeed: float             # maximum speed for character
      targetRadius: float         # arrival radius
      slowRadius: float           # slowing-down radius
      timeToTarget: float = 0.1   # time over which to achieve target speed
  '''
  def __init__(self):
    character = 0
    target = 0
    max_acceleration = 0
    max_speed = 0
    target_radius = 0
    slow_radius = 0
    time_to_target = 0

  def getSteering() -> SteeringOutput:
    result = new SteeringOutput()

    # Get the direction and distance to the target
    direction = target.position – character.position
    distance = direction.length()
    # Test for arrival
    if distance < target_radius:
      return null

    # Outside slowing-down (outer) radius, move at max speed
    if distance > slow_radius:
      target_speed = max_speed

    # Between radii, scale speed to slow down
    else:
      targetSpeed = max_speed * distance / slow_radius

    # Target velocity combines speed and direction
    target_velocity = direction
    target_velocity.normalize()
    target_velocity *= target_speed

    # Accelerate to target velocity
    result.linear = target_velocity – character.velocity
    result.linear /= time_to_target

    # Test for too fast acceleration
    if result.linear.length() > max_acceleration:
      result.linear.normalize()
      result.linear *= max_acceleration

    # Output steering
    result.angular = 0
    return result