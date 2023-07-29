class Solution:
    def reverse(self, head, k):
        i, prev, curr = k, None, head
        while curr and i > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i -= 1
        if curr:
            head.next = self.reverse(curr, k)
        return prev
