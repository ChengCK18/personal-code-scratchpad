
class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfsSearch(cand,tgt,tempResult):
            if(tgt<0):
                return False

            cand = [cd for cd in cand if cd <= tgt]
       
            if(len(cand)==0 and tgt != 0):
                return False

            tempResult = sorted(tempResult)
            if(tgt==0 and tempResult not in output):
                
                output.append(tempResult.copy())
                return True

           

            for x in cand:
                tempResult.append(x)
                result = dfsSearch(cand,tgt-x,tempResult) 
                tempResult.pop()
                
                

        for cand in candidates:
            tempResult = [cand]
            dfsSearch(candidates,target-cand,tempResult)
            

        return output