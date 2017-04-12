from lightsRL import lightsRL
from scipy import stats
import matplotlib.pyplot as plt

class rl:
    def __init__(self, agent):
        self.iterator = 0
        self.epsilon = 0.1
        self.lights_module = lightsRL(agent)
    
    def rl_main(self):
        if (self.iterator < 500):
            mean_reward = self.lights_module.run_simulation(epsilon)
            plt.scatter(i, mean_reward)
        
        self.iterator += 1

        if (self.iterator % 500 == 0):
            plt.show()