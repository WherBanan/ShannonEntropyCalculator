# Made by Lasse Ruokokoski
# Github.com/WherBanan

import math
from collections import Counter

def shannon_entropy(probabilities):
    if probabilities != 0:
        entropy = -sum(i * math.log2(i) for i in probabilities)
        return entropy
    else:
        return 0
    
# TO BE DONE
def joint_entropy(probabilitiesX, probabilitiesY):
    entropy = 0
    if probabilitiesX !=0 and probabilitiesY != 0:
        for prob_X in probabilitiesX:
            for prob_Y in probabilitiesY:
                joint_prob = prob_X * prob_Y
                entropy -= joint_prob * math.log2(joint_prob)
        return entropy
    else:
        return 0



probabilitiesX = [0.26, 0.22, 0.28, 0.24]
probabilitiesY = [0.18, 0.26, 0.28, 0.28]

print("Shannon Entropy of data1:", shannon_entropy(probabilitiesX))
print("Shannon Entropy of data2:", shannon_entropy(probabilitiesY))
print("Joint Entropy of data1 and data2:", joint_entropy(probabilitiesX, probabilitiesY))