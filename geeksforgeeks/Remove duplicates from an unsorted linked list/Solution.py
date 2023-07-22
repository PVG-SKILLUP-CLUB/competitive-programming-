class Solution:
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head

        values = {head.data}
        current = head

        while current.next is not None:
            if current.next.data in values:
                current.next = current.next.next
            else:
                values.add(current.next.data)
                current = current.next

        return head
