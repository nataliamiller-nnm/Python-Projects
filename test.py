import math
import time

import numpy as np 
from matplotlib import pyplot as plt

output_file = r"C:\Users\nmiller\OneDrive - EOS DS USA\Documents\output.txt"

#------------------------------------------------------------------------------#
#                           Character Initializations                          #
#------------------------------------------------------------------------------#
character_1 = {
    "id": 2601,
	"steering_behavior": "Continue",
    "steering_behavior_code": "1",
    "inital_position": [0, 0],
	"inital_velocity": [0, 0],
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
    "velocity": (0, 0),
    "linear_acceleration_x": 0,
    "linear_acceleration_z": 0,
    "acceleration": 0,
    "orientation": 0,
    "collision_status": False,
    "position": [0, 0]
}


character_2 = {
	"id": 2602,
	"steering_behavior": "Flee",
    "steering_behavior_code": "7",
	"inital_position": [-30, -50],
	"inital_velocity": [2.0, 7.0],
	"inital_orientation": math.radians(45),
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
    "velocity": (2, 7),
    "linear_acceleration_x": 0,
    "linear_acceleration_z": 0,
    "acceleration": 0,
    "orientation": math.radians(45),
    "collision_status": False,
    "position": [-30, -50],
    "velocity": [2, 7]
}


character_3 = {
	"id": 2603,
	"steering_behavior": "Seek",
    "steering_behavior_code": "6",
	"inital_position":[-50, 40],
	"inital_velocity": [0, 8],
	"inital_orientation": math.radians(270),
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
    "velocity": (0, 8),
    "linear_acceleration_x": 0,
    "linear_acceleration_z": 0,
    "acceleration": 0,
    "orientation": math.radians(270),
    "collision_status": False,
    "position": [-50, 40],
    "veloctiy": [0, 8]
}


character_4 = {
	"id": 2604,
	"steering_behavior": "Arrive",
    "steering_behavior_code": "8",
	"inital_position": (50, 75),
	"inital_velocity": (-9, 4),
	"inital_orientation": math.radians(180),
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
    "velocity": (-9, 4),
    "linear_acceleration_x": 0,
    "linear_acceleration_z": 0,
    "acceleration": 0,
    "orientation": math.radians(180),
    "collision_status": False			 
}


#------------------------------------------------------------------------------#
#                               Vector Functions                               #
#------------------------------------------------------------------------------#
def normalize(vector):
    '''
    Normalizes a vector
    '''
    if (len(vector) != 0):
        normalized_x = vector[0] / len(vector)
        normalized_z = vector[1] / len(vector)
        return [normalized_x, normalized_z]
    else:
        return [0,0]

#------------------------------------------------------------------------------#
#                              Steering Behaviors                              #
#------------------------------------------------------------------------------#
def steering_update(character):
  ''' Updates character’s movement variables
      - Outputs: New values for position, orientation, velocity, rotation
      - Inputs: linear and angular accelerations
      - Inputs generated by movement behaviors
  '''
  position = character["position"]
  velocity = character["velocity"]
  orientation = character["orientation"]
  rotation = [0, 0]
  linear = character["acceleration"]
  angular = [0,0]
  max_velocity = character["max_velocity"]
  time = character["timestep"]

	# Update the position and orientation  
  position += velocity * time  
  orientation += rotation * time  

	# Update the velocity and rotation  
  velocity += linear[0] * time  
  rotation += angular * time  

  # Check for speed above max and clip  
  if len(velocity) > max_velocity:  
    normalized_velocity = normalize(velocity)
    normalized_velocity *= max_velocity
    return position, orientation, normalized_velocity, rotation
  else:
    return position, orientation, velocity, rotation


def steering_continue(character):
    # Continue moving without changing velocity or orientation
    result = [character["velocity_x"], character["velocity_z"], character["orientation"]]
    return result

# NEED UPDATE FUNCTION

def get_steering_seek(character, target):
    character_position = character["position"]
    character_orientation = character["orientation"]
    target_position = target["position"]
    max_acceleration = character["max_acceleration"]
    linear_result = [0, 0]
    angular_result = [0, 0]

    # Get the direction to the target
    linear_result[0] =  character_position[0] - target_position[0]
    linear_result[1] =  character_position[1] - target_position[1]
    print(linear_result)

    # Accelerate at maximum rate
    linear_result = normalize(linear_result)
    print(linear_result)
    linear_result[0] *= max_acceleration
    linear_result[1] *= max_acceleration
    print(linear_result)

    # Output steering
    return linear_result[0], linear_result[1]

def get_steering_flee(character, target):
    character_position = character["position"]
    character_orientation = character["orientation"]
    target_position = target["position"]
    max_acceleration = character["max_acceleration"]
    linear_result = [0, 0]
    angular_result = [0, 0]

    # Get the direction to the target
    linear_result[0] =  character_position[0] - target_position[0]
    linear_result[1] =  character_position[1] - target_position[1]
    print(linear_result)

    # Accelerate at maximum rate
    linear_result = normalize(linear_result)
    print(linear_result)
    linear_result[0] *= max_acceleration
    linear_result[1] *= max_acceleration
    print(linear_result)

    # Output steering
    return linear_result[0], linear_result[1]
    
def output_steering(character):
    with open(output_file, "a") as f:
        print('{}, '.format(character["timestep"]) +
            '{}, '.format(character["id"]) +
            '{}, '.format(character["position_x"]) +
            '{}, '.format(character["position_z"]) +
            '{}, '.format(character["velocity_x"]) +
            '{}, '.format(character["velocity_z"]) +
            '{}, '.format(character["linear_acceleration_x"]) +
            '{},'.format(character["linear_acceleration_z"]) +
            '{}, '.format(character["orientation"]) +
            '{}, '.format(character["steering_behavior_code"]) +
            '{}, '.format(character["collision_status"]), file = f)


#------------------------------------------------------------------------------#
#                                 Main Method                                  #
#------------------------------------------------------------------------------#


# Print initial values
# output_steering(character_1)
output_steering(character_3)

# Run first methods
# character_1["timestep"] += 0.5
character_3["timestep"] += 0.5

# steering_continue(character_1)
character_3["postion_x"], character_3["postion_z"] = get_steering_seek(character_3, character_1)
character_3["postion"] = [character_3["postion_x"], character_3["postion_z"]]
steering_update(character_3)

# Print updated values
# output_steering(character_1)
output_steering(character_3)

'''
for x in range(100):
    
    # character_1["timestep"] += 0.5
    character_3["timestep"] += 0.5

    # Run first methods
    # character_1["postion"] = steering_continue(character_1)
    character_3["postion"], character_3["postion_x"], character_3["postion_z"] = get_steering_seek(character_3, character_1)

    # Print updated values
    # output_steering(character_1)
    output_steering(character_3)
'''
