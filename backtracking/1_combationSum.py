#IN PROGRESSSSS, NOT COMPLETE

class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfsSearch(cand,tgt,tempResult):
            if(tgt<0):
                return False
            if(tgt==0):
                output.append(tempResult)
                return True

            cand = [cd for cd in cand if cd <= tgt]
       

            if(len(cand)==0 and tgt != 0):
                return False

            for x in cand:
                tempResult.append(x)
                result = dfsSearch(cand,tgt-x,tempResult)
                if(not result):
                    tempResult.pop()
                

        for cand in candidates:
            tempResult = [cand]
            dfsSearch(candidates,target-cand,tempResult)
            

        print(output)




