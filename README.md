# Wheeled-Robots
Robotics Programs -Differential Drive Robot, Mecanum Drive robot

Problem No – 1

Given a differential drive robot starting from (0,0,0) find the final position when wheel velocities are
given by:
t=0 to t=5: 𝜔1 = 2, 𝜔2 = 2
t=5 to t=6: 𝜔1 = 3, 𝜔2 = 4
t=6 to t=10: 𝜔1 = 1, 𝜔


Solution –

Full Problem Solution – The problem statement is divided into three different time slots (t0-t1, t1-t2, t2- t3). So there are three different problem statements and solved one by one. Each time slot is divided into 50 different points and sampled them. Nine blank arrays assigned (xp1,2,3 yp1,2,3 th1,2,3) which stores position and orientation information of differential drive robot. Six different wheel speeds assign in order to get the movement of the robot mentioned in the problem statement. In three different ‘for’ loops made in order to get three arrays which have information about the robot’s movement. Combine three strings and plot using matplot library (path of the robot fig.1).

PROBLEM NO – 1 

Assume that you have a rectangular Mechanum robot with L1=0.30m, L2=0.20m and r=0.08 Find the path of the robot for the given wheel rotations: ϕ˙1=0.75∗cos(t/3.0), ϕ˙2=1.5∗cos(t/3.0), ϕ˙3=−1.0, ϕ˙4=0.5. Start with x,y,θ=0 and set t=0, Δt=0.05. Run the simulation for 200 iterations (or for 10 seconds). Keeping the x and y locations in an array is an easy way to generate a plot of the robot’s path. If x, y are arrays of x-y locations then try
Showing the orientation takes a bit more work. Matplotlib provides a vector plotting method. You need to hand it the location of the vector and the vector to be plotted, (x,y,u,v), where (x,y) s the vector location and (u,v) are the x and y components of the vector. You can extract those from θ using u=s∗cos(θ) and v=s∗sin(θ) where ss is a scale factor (to give a good length for the image, e.g. 0.075). The vector plot commands are then

Solution – 

In the solution 200 points generated using linspace command which is equally spaced between 0to10 time frame. Blank array for Xp, Yp and Th generated in order to store the location of the mechanum wheel robot. Parameter of the robot is already provided in the problem statement. A B and C are the vehicle equation used from the textbook which is used to generate state co-ordinates of the robot. The array of x,y, and th parameters generate and store into the above blank arrays. Plot the points with the help of matplotlib library. The quiver function is used from matplotlib in order to generate the orientation of the robot and plot. Display all the plotted points using show command.

