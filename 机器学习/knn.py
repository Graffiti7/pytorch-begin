import numpy as np
import math
import operator

def knn(trainData,testData,labels,k):
    rowSize = trainData.shape[0]
    diff = np.tile(testData,(rowSize,1)) - trainData
    sqrDiff = diff**2
    sqrDiffSum = sqrDiff.sum(axis = 1)
    distance = sqrDiffSum**0.5
    sortDistance = distance.argsort()

    count = {}

    for i in range(k):
        vote = labels[sortDistance[i]]
        count[vote] = count.get(vote, 0) + 1
    # 对类别出现的频数从高到低进行排序
    sortCount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    
    return sortCount[0][0] 


if __name__ == "__main__":
    trainData = np.array([[0, 4],[5, 1], [4, 0], [1, 3] ])
    labels = ['动作片', '动作片', '爱情片', '爱情片']
    testData = [3, 2]
    X = knn(trainData, testData, labels, 3)
    print(X)
        
        
    