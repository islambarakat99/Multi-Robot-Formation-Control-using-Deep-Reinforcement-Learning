# Multi-Robot-Formation-Control-using-Deep-Reinforcement-Learning


In this project deep reinforcement learning is used to train multi-agent robotic systems to perfrom leader-follower formation control . The OpenAI's MADDPG environment is used after some modifications have been added for agent training.

## Framework

The Framework used in this project is Python 3.6.9 installed on Ubuntu 18.04 LTS. Alongside with Numpy, Tensorflow.

<p align="center">
  <img  src="https://user-images.githubusercontent.com/42684592/123695973-82063300-d85b-11eb-8349-84dadbda6b69.png">
</p>


## Environment

The  environment  is  the  single  most  important  element  in  the  Reinforcement  Learningprocess since it presents the physical world that the agent interacts with.  In this project the environment used is [Multi-Agent Particle Environments (MPE)](https://github.com/openai/multiagent-particle-envs).
based on OpenAI work. OpenAI is artificial intelligence research laboratory that develops free open-source tools and libraries that helps the Artificial Intelligence developers community in the Research and Industry fields. The original environment is a 2D world with a continuous observation and discreteaction space, along with some basic simulated physics.  It was developed such that the agents are divided into 2 groups: Good Agents, Adversary Agents. Such that the good agents try to cooperate to cover certain goal landmarks so that the adversary agents can not cover these goals. Many modifications are made to this environment in this project so that it can be used in the Leader-Follower Formation Control favor, including:

<p align="center">
  <img  src="https://user-images.githubusercontent.com/42684592/123695976-829ec980-d85b-11eb-8d5f-a7f1391d9418.png">
</p>

1.  The agents are divided into:  One Leader Agent, Two Follower Agents.
2.  The goal is an individual landmark its location is fixed, unlike being assigned randomly  in  the  original  environment,  in  the  left  down  corner  of  the  environment, specifically at location (-0.8, -0.8) with respect to the coordination plane which has a center of (0, 0) right at the middle of the screen.
3.  The landmarks representing obstacles are assigned randomly.
4.  All of the agents initial positions are assigned randomly constrained to be at the first quadrant of the coordination system unlike being completely random at the original environment.
5.  The maximum speed of the agents is set to 0.2 unlike the original environments. The size of the agents is reduced and the landmarks size is magnified compared tothe original environment.
