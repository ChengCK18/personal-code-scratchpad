class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # each number represents a unique subject
        # if the prerequisite subject is not listed meaning no prereq required.
        # numCourses = target num of subjects to take

        # might work???? to try
        # graph based approach, each node represents a subject
        # the node represents the prereq of the child nodes
        # TBC