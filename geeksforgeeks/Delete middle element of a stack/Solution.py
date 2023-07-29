class Solution:
    
    def deleteMid(self, s, sizeOfStack):
        
        if sizeOfStack == 0:
            return

        mid = sizeOfStack // 2

        def deleteMiddle(stack, current):

            if current == mid:
                stack.pop()
                return

            top = stack.pop()
            deleteMiddle(stack, current + 1)

            stack.append(top)

        deleteMiddle(s, 0)
