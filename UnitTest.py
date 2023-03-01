import pandas as pd
import matplotlib.pyplot as plt

# Reads the simulated data into a variable
simulation_data = pd.read_csv("copy of unit_tests_good_one.csv")

#simulation_data['x'].plot()
#simulation_data['y'].plot()
#simulation_data['z'].plot()
#plt.xlabel('Time')
#plt.ylabel('x, y, z')
#plt.title('State vs Sim')
#plt.show()


#simulation_data['x_dot'].plot()
#simulation_data['y_dot'].plot() 
#simulation_data['z_dot'].plot()
#plt.xlabel('Time')
#plt.ylabel('x_dot, y_dot, z_dot')
#plt.title('State vs Sim')
#plt.show()

#simulation_data['phi'].plot()
#simulation_data['theta'].plot()
#simulation_data['psi'].plot()
#plt.xlabel('Time')
#plt.ylabel('phi, theta, psi')
#plt.title('State vs Sim')
#plt.show()

#simulation_data['phi_dot'].plot()
#simulation_data['theta_dot'].plot()
#simulation_data['psi_dot'].plot()
#plt.xlabel('Time')
#plt.ylabel('phi_dot, theta_dot, psi_dot')
#plt.title('State vs Sim')
#plt.show()

#simulation_data['input_x'].plot()
#simulation_data['input_y'].plot()
#plt.xlabel('Time')
#plt.ylabel('input_x, input_y')
#plt.title('State vs Sim')
#plt.show()

# Creates different subplots
fig, axes = plt.subplots(nrows= 3, ncols= 3, figsize = (20,10))

# Plots x,y and z
axes[0][0].plot(simulation_data['Time'], simulation_data['x'], label = 'sim_u')
axes[0][0].plot(simulation_data['Time'], simulation_data['y'], label = 'sim_y')
axes[0][0].plot(simulation_data['Time'], simulation_data['z'], label = 'sim_z')
axes[0][0].legend()
axes[0][0].set_title('x,y,x')

# Hides the second plot in the first
axes[0][1].axis('off')

# Plots x_dot,y_dot, and z_dot
axes[0][2].plot(simulation_data['Time'], simulation_data['x_dot'], label = 'sim_x_dot')
axes[0][2].plot(simulation_data['Time'], simulation_data['y_dot'], label = 'sim_y_dot' )
axes[0][2].plot(simulation_data['Time'], simulation_data['z_dot'], label = 'sim_z_dot')
axes[0][2].legend()
axes[0][2].set_title('x_dot,y_dot,x_dot')

# Hides the first plot in the second row
axes[1][0].axis('off')

# Plots phi, theta, and psi
axes[1][1].plot(simulation_data['Time'], simulation_data['phi'], label = 'sim_phi_dot')
axes[1][1].plot(simulation_data['Time'], simulation_data['theta'], label = 'sim_theta_dot')
axes[1][1].plot(simulation_data['Time'], simulation_data['psi'], label = 'sim_psi_dot')
axes[1][1].legend()
axes[1][1].set_title('phi,theta,psi')

# Hides the third plot in the second row
axes[1][2].axis('off')

# Plots phi_dot, theta_dot, and phsi_dot
axes[2][0].plot(simulation_data['Time'], simulation_data['phi_dot'], label = 'sim_phi_x_dot')
axes[2][0].plot(simulation_data['Time'], simulation_data['theta_dot'], label = 'sim_theta_x_dot')
axes[2][0].plot(simulation_data['Time'], simulation_data['psi_dot'], label = 'sim_psi_x_dot')
axes[2][0].legend()
axes[2][0].set_title('phi_dot,theta_dot,psi_dot')

# Hides the second plot in the third row
axes[2][1].axis('off')

# Plots input_x and input_y
axes[2][2].plot(simulation_data['Time'], simulation_data['input_x'], label = 'sim_input_x')
axes[2][2].plot(simulation_data['Time'], simulation_data['input_y'], label = 'sim_input_y')
axes[2][2].legend()
axes[2][2].set_title('input_x, input_y,')

# Displays the title for all of the subplots and shows the graphs
fig.suptitle('Actual vs Sim')            
plt.show()