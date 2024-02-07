# TODO: Define kinematic type??
# TODO: Get function definitons from slide

# TODO: See 1 Support r file for vector class example
# TODO: Possibly write my own plotter? sounds hard tho

# Make functions separate
# and then output to character file -> use list??
# teamStep
# need continue function?? -> check R code 
# For this assignment, the Continue character’s initial velocity and rotation will
# all be 0, so the Continue character should not move at all

# Natalia Miller

'''
The following code has been adapted from psuedocode:
    I. Millington, Artificial Intelligence for Games, Third Edition,
    CRC Press, Boca Raton FL, 2019
''' 

import math
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

# File for output
output = open("output.txt","w+")
output.write("hello world")

#------------------------------------------------------------------------------#
#                               Vector Functions                               #
#------------------------------------------------------------------------------#
def normalize(vector):
  '''
   Normalizes a vector using the NumPy module
  '''
  normalized_vector = vector / np.linalg.norm(vector)
  return normalized_vector

#------------------------------------------------------------------------------#
#                           Character Initializations                          #
#------------------------------------------------------------------------------#

character_1 = {
  "id": 2601,
	"steering_behavior": "Continue",
	"inital_position": (0, 0),
	"inital_velocity": (0, 0),
	"inital_orientation": 0,
	"max_velocity": 0,
	"max_acceleration": 0,
	"target": 0,				 
  "arrival_radius": 0,
  "slowing_radius": 0,
  "time_to_target": 0,
  "timestep": 0,
  "position_x": 0,
  "position_z": 0,
  "velocity_x": 0,
  "velocity_z": 0,
  "linear_acceleration_x": 0,
  "linear_acceleration_z": 0,
  "orientation": 0,
  "collision_status": False
}

character_2 = {
	"id": 2602,
	"steering_behavior": "Flee",
	"inital_position": (-30, -50),
	"inital_velocity": (2, 7),
	"inital_orientation": np.pi/4,
	"max_velocity": 8,
	"max_acceleration": 1.5,
	"target": 1,				 
  "arrival_radius": 0,
  "slowing_radius": 0,
  "time_to_target": 0,		
  "timestep": 0,
  "position_x":-30,
  "position_z": -50,
  "velocity_x": 2,
  "velocity_z": 7,
  "linear_acceleration_x": 0,
  "linear_acceleration_z": 0,
  "orientation": np.pi/4,
  "collision_status": False
}

character_3 = {
	"id": 2603,
	"steering_behavior": "Seek",
	"inital_position": (-50, 40),
	"inital_velocity": (0, 8),
	"inital_orientation": (3(np.pi))/2,
	"max_velocity": 8,
	"max_acceleration": 2,
	"target": 1,				 
  "arrival_radius": 0,
  "slowing_radius": 0,
  "time_to_target": 0,
  "timestep": 0,
  "position_x": -50,
  "position_z": 40,
  "velocity_x": 0,
  "velocity_z": 8,
  "linear_acceleration_x": 0,
  "linear_acceleration_z": 0,
  "orientation": (3(np.pi))/2,
  "collision_status": False
}

character_4 = {
	"id": 2604,
	"steering_behavior": "Arrive",
	"inital_position": (50, 75),
	"inital_velocity": (-9, 4),
	"inital_orientation": np.pi,
	"max_velocity": 10,
	"max_acceleration": 2,
	"target": 1,				 
  "arrival_radius": 4,
  "slowing_radius": 32,
  "time_to_target": 1,
  "timestep": 0,
  "position_x": 50,
  "position_z": 75,
  "velocity_x": -9,
  "velocity_z": 4,
  "linear_acceleration_x": 0,
  "linear_acceleration_z": 0,
  "orientation": np.pi,
  "collision_status": False			 
}

#------------------------------------------------------------------------------#
#                              Steering Behaviors                              #
#------------------------------------------------------------------------------#
class SteeringOutput:
  ''' 
   Inputs to steering behaviors:
    - Character data (position, orientation)  
    - Target data needed for steering behavior (e.g., position, velocity)  
   Outputs from steering behaviors:
    - Linear acceleration (vector, rate of change of velocity)  
    - Angular acceleration (scalar, rate of change of rotation)  
  '''
  def __init__(self):
    '''
     Args:
      linear: linear acceleration -> vector
      angular: angular acceleration, scalar -> float
    '''
    self.linear = 0 
    self.angular = 0

# TODO: Does this belong in a class?
def steering_update(steering: SteeringOutput, max_speed: float, time: float):
  ''' Updates character’s movement variables
      - Outputs: New values for position, orientation, velocity, rotation
      - Inputs: linear and angular accelerations
      - Inputs generated by movement behaviors
  '''
	# Update the position and orientation  
  position += velocity * time  
  orientation += rotation * time  

	# Update the velocity and rotation  
  velocity += steering.linear * time  
  rotation += steering.angular * time  

  # Check for speed above max and clip  
  if velocity.length() > max_speed:  
    normalized_velocity = normalize(velocity)
    normalized_velocity *= max_speed

def steering_continue(character):
  # Continue moving without changing velocity or orientation
  result = [character["velocity_x"], character["velocity_z"], character["orientation"]]
  return result

#------------------------------------------------------------------------------#
#                              Movement Behaviors                              #
#------------------------------------------------------------------------------#

class DynamicSeek:
  ''' 
  Move directly towards target as fast as possible

  Seek: Match character position to target position
    - Determine direction to target
    - Accelerate in that direction at max rate up to max speed
  '''
  def __init__(self, character):
    '''
    Args:
      character: position and orientation for character -> kinematic
      target: position and orientation for target -> kinematic
      max_acceleration: maximum acceleration rate for character -> float 
    '''
    self.kinematic = (character["inital_position"], character["inital_orientation"])
    self.target = (steering.position, steering.orientation)
    self.max_acceleration = character["max_acceleration"]
    self.result = (steering.linear, steering.angular)

  def get_steering(self) -> SteeringOutput:
    # Create output structure
    result = SteeringOutput()

    # Get the direction to the target
    result[0] = self.target[0] - self.kinematic[0]

    # Accelerate at maximum rate
    result[0] = normalize(result[0])
    result[1] *= self.max_acceleration

    # Output steering
    result[1] = 0
    output.write(result)
    return result

class DynamicFlee:
  ''' 
  Move directly away from target as fast as possible

  Flee: Negate character position to target position
    - Determine direction to target
    - Accelerate in opposite direction at max rate up to max speed
  '''
  def __init__(self, character):
    '''
    Args:
      character: position and orientation for character -> kinematic
      target: position and orientation for target -> kinematic
      max_acceleration: maximum acceleration rate for character -> float 
    '''
    self.kinematic = (character["inital_position"], character["inital_orientation"]) 
    self.target = (steering.position, steering.orientation)
    self.max_acceleration = steering.max_acceleration
    self.result = (steering.linear, steering.angular)

  def getSteering(self) -> SteeringOutput:
    # Create output structure
    result = SteeringOutput()

    # Get the direction to the target
    result.linear = self.kinematic[0] - self.target[0]

    # Accelerate at maximum rate
    result.linear.normalize()
    result.linear *= self.max_acceleration

    # Output steering
    result.angular = 0
    return result

class DynamicArrive:
  ''' 
  Move directly towards target, slowing down when near.

  Arrive: Uses two distance raddii to solve the issue that accelerating
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
  '''
  def __init__(self):
    '''
    Args:
      character: position and orientation for character -> Kinematic        
      target: position and orientation for target -> Kinematic          
      maxAcceleration: maximum acceleration rate for character-> float
      maxSpeed: maximum speed for character -> float            
      targetRadius: arrival radius -> float         
      slowRadius: slowing-down radius -> float          
      timeToTarget: time over which to achieve target speed -> float = 0.1 
    '''
    self.character = 0
    self.target = 0
    self.max_acceleration = 0
    self.max_speed = 0
    self.target_radius = 0
    self.slow_radius = 0
    self.time_to_target = 0

  def getSteering(self) -> SteeringOutput:
    result = SteeringOutput()

    # Get the direction and distance to the target
    direction = self.target.position - self.character.position
    distance = direction.length()
    # Test for arrival
    if distance < self.target_radius:
      return None

    # Outside slowing-down (outer) radius, move at max speed
    if distance > self.slow_radius:
      target_speed = self.max_speed

    # Between radii, scale speed to slow down
    else:
      self.targetSpeed = self.max_speed * distance / self.slow_radius

    # Target velocity combines speed and direction
    target_velocity = direction
    target_velocity.normalize()
    target_velocity *= target_speed

    # Accelerate to target velocity
    result.linear = target_velocity - self.character.velocity
    result.linear /= self.time_to_target

    # Test for too fast acceleration
    if result.linear.length() > self.max_acceleration:
      result.linear.normalize()
      result.linear *= self.max_acceleration

    # Output steering
    result.angular = 0
    return result

output.close()
