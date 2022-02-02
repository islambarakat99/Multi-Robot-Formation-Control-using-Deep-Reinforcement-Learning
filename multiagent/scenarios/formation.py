
import numpy as np
from multiagent.core import World, Agent, Landmark
from multiagent.scenario import BaseScenario

class Scenario(BaseScenario):
    def make_world(self):
        world = World()
        # world characteristics
        world.dim_c = 2
        num_agents = 3
        world.num_agents = num_agents
        num_landmarks = num_agents + 1
        # adding agents
        world.agents = [Agent() for i in range(num_agents)]
        for i, agent in enumerate(world.agents):
            agent.name =  'agent %d' % i
            agent.collide = False
            agent.silent = True
            agent.size = 0.05
        # adding landmarks
        world.landmarks = [Landmark() for i in range(num_landmarks)]
        for i, landmark in enumerate(world.landmarks):
            landmark.name = 'landmark %d' % i
            landmark.collide = False
            landmark.movable = False
            landmark.size = 0.07 
        # Initial Conditions
        self.reset_world(world)
        return world
    
    def reset_world(self, world):
        # Landmarks characteristics
        for landmark in world.landmarks:
            landmark.color = np.array([0.15, 0.15, 0.15])
            landmark.state.p_pos = np.random.uniform(-1, +1, world.dim_p)
            landmark.state.p_vel = np.zeros(world.dim_p)
        goal = world.landmarks[0]
        goal.color = np.array([0.15, 0.65, 0.15])
        goal.state.p_pos = [-0.8, -0.8]            
        # Leader characteristics
        world.agents[0].color = np.array([0.85, 0.35, 0.35])
        world.agents[0].adversary = True
        world.agents[0].goal_a = goal     
        # Followers
        for i in range(1, world.num_agents):
            world.agents[i].color = np.array([0.35, 0.35, 0.85])
            world.agents[i].adversary = False    
        # Random intial states
        for agent in world.agents:  
            agent.state.p_pos = np.random.uniform(0.1, 0.9, world.dim_p)
            agent.state.p_vel = np.zeros(world.dim_p)
            agent.state.c = np.zeros(world.dim_c)   
       
    def benchmark_data(self, agent, world):
        # returning data for benchmark purposes
        if agent.adversary:
            return np.sum(np.square(agent.state.p_pos - agent.goal_a.state.p_pos))
        else:
            dists = []
            for l in world.landmarks:
                dists.append(np.sum(np.square(agent.state.p_pos - l.state.p_pos)))
            dists.append(np.sum(np.square(agent.state.p_pos - world.agents[0].state.p_pos)))
            return tuple(dists)

    def reward(self, agent, world):
        reward = self.outside(agent, world) + self.collosion(agent, world)
        if agent.adversary:
            reward -= np.sqrt(np.sum(np.square(agent.state.p_pos - agent.goal_a.state.p_pos)))
        else:
            reward -= np.sqrt(np.sum(np.square(agent.state.p_pos - world.agents[0].state.p_pos)))
        return reward
      
    def collosion(self, agent, world):
        col_rew = 0
        for ag in world.agents:
            if not ag.name == agent.name:
                if np.sqrt(np.sum(np.square(agent.state.p_pos - ag.state.p_pos))) < 2* agent.size:
                    col_rew -= 15
        for i in range(1, len(world.landmarks)):
            if np.sqrt(np.sum(np.square(agent.state.p_pos - world.landmarks[i].state.p_pos))) < 2* agent.size:
                col_rew -= 15
        return col_rew
    
    def outside(self, agent, world):
        out_rew = 0
        if np.sum(np.absolute(agent.state.p_pos)) > 2:
            out_rew -= 20
        return out_rew

    def observation(self, agent, world):
        # position of the landmarks w.r.t the agent
        landmark_pos = []
        for landmark in world.landmarks:
            landmark_pos.append(landmark.state.p_pos - agent.state.p_pos)
        # position of the other agents w.r.t this agent
        other_pos = []
        for other in world.agents:
            if other is agent: continue
            other_pos.append(other.state.p_pos - agent.state.p_pos)

        if not agent.adversary:
            return np.concatenate([agent.state.p_pos - world.agents[0].state.p_pos] + landmark_pos + other_pos)
        else:
            return np.concatenate([agent.goal_a.state.p_pos - agent.state.p_pos] + landmark_pos)