class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            courseDict[prereq[0]].append(prereq[1])

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if courseDict[crs] == []:
                return True
            
            visiting.add(crs)
            for newCrs in courseDict[crs]:
                if not dfs(newCrs):
                    return False
            visiting.remove(crs)
            courseDict[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True