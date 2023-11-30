
# VERY SLOW ALGO xD just by using brute force. NOT RECOMMENDED AT ALL
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # each number represents a unique subject
        # if the prerequisite subject is not listed meaning no prereq required.
        # numCourses = target num of subjects to take

        uniqueNode = {}
        corePrereq = set()
        for course,prereq in prerequisites: 
            course,prereq = str(course), str(prereq)
            if(course not in uniqueNode):
                uniqueNode[course] = set([prereq])
                corePrereq.add(course)
                if(prereq not in uniqueNode):
                    uniqueNode[prereq] = set()
            else:
                uniqueNode[course].add(prereq)
                if(prereq not in uniqueNode):
                    uniqueNode[prereq] = set()


        subsTaken = set()
        while True:
            newlyTaken = []
            for course in uniqueNode.keys():
                if(len(uniqueNode[course]) == 0): # no more prereq
                    subsTaken.add(course)
                    newlyTaken.append(course)

                else:
                    prereqTaken = []
                    for prereq in uniqueNode[course]: # try to fulfill prereq with taken subs
                        if(prereq in subsTaken):
                            prereqTaken.append(prereq) # prereq fulfilled
                    for prereqTake in prereqTaken:
                        uniqueNode[course].remove(prereqTake)
                    if(len(uniqueNode[course]) == 0):
                        subsTaken.add(course)
                        newlyTaken.append(course)

            if(len(newlyTaken)==0):
                break
            else:
                for taken in newlyTaken:
                    uniqueNode.pop(taken)
            if(len(uniqueNode.keys())==0):
                break
               
      
        for sub in subsTaken:
            if(sub in corePrereq):
                corePrereq.remove(sub)
        

        if(len(subsTaken)>= numCourses or len(corePrereq) == 0):
            return True
        else:
            return False


        
                    
            

                


                    

            

                





      