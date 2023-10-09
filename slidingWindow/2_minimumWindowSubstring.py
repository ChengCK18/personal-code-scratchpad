class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t) == 0):
            return ""

        wantDict = {}
        searchWindowDict = {}

        for charac in t:
            wantDict[charac] = 1 +wantDict.get(charac,0)


        # Each unique character represents a condition
        # once a condition is met with its count, have +=1
        have, need = 0 , len(wantDict)

        minResult = [-1,-1]
        minResultLen = float("infinity")

        leftPtr = 0

        for rightPtr in range(len(s)):
            #get charac
            charac = s[rightPtr]
            searchWindowDict[charac] = 1 + searchWindowDict.get(charac,0)
            if(charac in wantDict and searchWindowDict[charac] == wantDict[charac]):
                have +=1

            # found at least 1 window fulfilling the wantDict, loop through by popping from leftptr to rightptr to search for any other window that fufill the wantDict
            while have == need:  
                tempResultLen = rightPtr - leftPtr +1
                if(tempResultLen < minResultLen):
                    minResult = [leftPtr,rightPtr]
                    minResultLen = tempResultLen
                
                # remove from left
                searchWindowDict[s[leftPtr]] -= 1
                # if removal affected the fulfillment
                if(s[leftPtr] in wantDict and searchWindowDict[s[leftPtr]]<wantDict[s[leftPtr]]):
                    have -=1
                leftPtr +=1


        if(minResultLen == float("infinity")): # no match found
            return ""
        else:
            return s[minResult[0]:minResult[1]+1]