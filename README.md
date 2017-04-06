# RLMap

The focus of thsiassignment is to explore the use of modules in reinforcement learn- ing. You ahould create a driving environment that consists of a four lane road with two lanes in each direction. Make the environment circular so that cars going over the end of the road appear at the beginning of the other end.
Your environment should have:

1. Traffic lights with a yellow-red-green pattern
2. Cars traveling in both directions at different speeds and lane changing ability
3. Parking
4. Pedestrians who cross the road at random points and times- giving gars some warning

You should solve this problem by giving reinforcement modules that learn by expe- rience.
Each module that you choose should use a version of Q-Learning. SARSA is a pop- ular option where you follow the best policy, with a schedule of picking a random alternative.

A. First train up your modules individually and demonstrate their performance.

B. Next construct a protocol to allow them to work together when they are simulta- neously active. The weighted average of Q values is one alternative. The highest Q value is another.

C. Next see if you can construct a protocol that will allow the mix of active modules to vary according to the environmental demand (approaching cars, pedestrains etc). You can add a sensing ability to the cars for this stage.
