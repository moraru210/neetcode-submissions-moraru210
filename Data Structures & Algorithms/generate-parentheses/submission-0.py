class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
        stack = []
        def backtrack(opened, closed):
            if opened == closed == n:
                solution.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                backtrack(opened+1, closed)
                stack.pop()
            
            if opened > closed:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()

            return

        backtrack(0,0)
        return solution
