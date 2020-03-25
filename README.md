# Wheeled-Robots
Robotics Programs -Differential Drive Robot, Mecanum Drive robot

Problem No – 4
Given a differential drive robot starting from (0,0,0) find the final position when wheel velocities are
given by:
t=0 to t=5: 𝜔1 = 2, 𝜔2 = 2
t=5 to t=6: 𝜔1 = 3, 𝜔2 = 4
t=6 to t=10: 𝜔1 = 1, 𝜔


Solution –
Full Problem Solution – The problem statement is divided into three different time slots (t0-t1, t1-t2, t2- t3). So there are three different problem statements and solved one by one. Each time slot is divided into 50 different points and sampled them. Nine blank arrays assigned (xp1,2,3 yp1,2,3 th1,2,3) which stores position and orientation information of differential drive robot. Six different wheel speeds assign in order to get the movement of the robot mentioned in the problem statement. In three different ‘for’ loops made in order to get three arrays which have information about the robot’s movement. Combine three strings and plot using matplot library (path of the robot fig.1).

