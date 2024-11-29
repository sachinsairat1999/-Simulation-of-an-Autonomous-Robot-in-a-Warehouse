import numpy as np
import matplotlib.pyplot as plt

# Warehouse dimensions
warehouse_length = 10
warehouse_width = 10

# Robot settings
robot_speed = 0.1
movement_step = 0.1
robot_pause = 2

# Starting and destination positions
start_position = np.array([0, 0], dtype=float)
destination_position = np.array([7, 9], dtype=float)

# Function to plot the warehouse and robot's position
def plot_warehouse(robot_position, destination):
 plt.imshow(np.zeros((warehouse_length, warehouse_width)), cmap='Blues', origin='lower')
 plt.plot(robot_position[1], robot_position[0], 'ro', label='Robot')
 plt.plot(destination[1], destination[0], 'gx', label='Destination')
 plt.title(f"Robot's Position: {robot_position}")
 plt.legend()
 plt.grid(True)
 
# Function to move the robot
def move_robot(start, destination):
 current_position = start.copy()

 # Create the plot figure
 plt.figure(figsize=(6, 6))

 # Continue until the robot reaches the destination
 while not np.allclose(current_position, destination, atol=0.1):
 # Calculate the direction vector (normalized)
 direction = destination - current_position
 distance = np.linalg.norm(direction)

 # Normalize the direction vector and move the robot by 0.1 meters per step
 if distance > movement_step:
 direction /= distance
 current_position += direction * movement_step
 else:
 # If the robot is very close, move it directly to the destination
 current_position = destination.copy()

 # Ensure the robot stays within the warehouse boundaries
 current_position = np.clip(current_position, [0, 0], [warehouse_length - 1, warehouse_width - 1])

 # Visualize the movement
 plot_warehouse(current_position, destination)
 plt.pause(0.1) # Update the plot for smooth movement

 # Pause for 2 seconds to simulate the robot stopping
 plt.pause(robot_pause)


 print("Robot has reached the destination!")
 plot_warehouse(current_position, destination)
 plt.show()
move_robot(start_position, destination_position)