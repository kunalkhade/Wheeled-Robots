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

Problem No - 2

Assume that you have a rectangular Mechanum robot with L1=0.30m, L2=0.20m and r=0.08 Find the path of the robot for the given wheel rotations: ϕ˙1=0.75∗cos(t/3.0), ϕ˙2=1.5∗cos(t/3.0), ϕ˙3=−1.0, ϕ˙4=0.5. Start with x,y,θ=0 and set t=0, Δt=0.05. Run the simulation for 200 iterations (or for 10 seconds). Keeping the x and y locations in an array is an easy way to generate a plot of the robot’s path. If x, y are arrays of x-y locations then try
Showing the orientation takes a bit more work. Matplotlib provides a vector plotting method. You need to hand it the location of the vector and the vector to be plotted, (x,y,u,v), where (x,y) s the vector location and (u,v) are the x and y components of the vector. You can extract those from θ using u=s∗cos(θ) and v=s∗sin(θ) where ss is a scale factor (to give a good length for the image, e.g. 0.075). The vector plot commands are then

Solution – 

In the solution 200 points generated using linspace command which is equally spaced between 0to10 time frame. Blank array for Xp, Yp and Th generated in order to store the location of the mechanum wheel robot. Parameter of the robot is already provided in the problem statement. A B and C are the vehicle equation used from the textbook which is used to generate state co-ordinates of the robot. The array of x,y, and th parameters generate and store into the above blank arrays. Plot the points with the help of matplotlib library. The quiver function is used from matplotlib in order to generate the orientation of the robot and plot. Display all the plotted points using show command.

Problem No - 3

Real motion and measurement involves error and this problem will introduce the concepts. Assume that you have a differential drive robot with wheels that are 20cm in radius and L is 12cm. Using the differential drive code (forward kinematics) from the text, develop code to simulate the robot motion when the wheel velocities are ϕ˙1=0.25t2, ϕ˙2=0.5t. The starting location is [0,0] with θ=0. 
Plot the path of the robot on 0≤t≤. It should end up somewhere near [50,60]. 


Solution  – 

In the solution equal 100 points generated from 0 to 5. Dotphi1 and dotphi2 velocities are provided in order to compute the robot motion. Blank array Xp Yp and Th are made in order to store x y and th coordinates. Using for loop co-ordinates will be generated and store into blank arrays. Plot and show all the coordinates using matplotlib commands.


Solution (2nd and 3rd problem) –
Continue to the first solution, in this problem noise is added into the velocities and accordingly, 10 different paths plotted with nose in red color. All paths then concatenate with each other using numpy function. Blue path indicates the noise-free path which is the exact path of the robot that has to take from source to destination.




