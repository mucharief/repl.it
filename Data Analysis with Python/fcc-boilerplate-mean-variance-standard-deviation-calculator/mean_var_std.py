import numpy as np

def calculate(inList):
  if len(inList) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    outMat = np.array(inList).reshape(3,3)
    outMean, outVar, outStd = [list(outMat.mean(axis=0)), list(outMat.mean(axis=1)), outMat.mean()], [list(outMat.var(axis=0)), list(outMat.var(axis=1)), outMat.var()], [list(outMat.std(axis=0)), list(outMat.std(axis=1)), outMat.std()]
    outMax, outMin, outSum = [list(outMat.max(axis=0)), list(outMat.max(axis=1)), outMat.max()], [list(outMat.min(axis=0)), list(outMat.min(axis=1)), outMat.min()], [list(outMat.sum(axis=0)), list(outMat.sum(axis=1)), outMat.sum()]
    
    calculations = {'mean':outMean, 'variance':outVar, 'standard deviation':outStd, 'max':outMax, 'min':outMin, 'sum':outSum}

    return calculations