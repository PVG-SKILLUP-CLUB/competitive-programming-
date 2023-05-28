class Solution
{
    //Function to find the data of nth node from the end of a linked list.
    int getNthFromLast(Node head, int n)
    {
    	int reqNode = getLength(head) - n;
    	
    	if(reqNode < 0) return -1;
    	
    	Node curr = head;
    	for(int idx=0; idx < reqNode; idx++, curr = curr.next);
    	
    	return curr.data;
    }
    
    int getLength(Node head)
    {
        int length = 0;
        for(Node curr = head; curr != null; curr = curr.next)
        {
            length++;
        }
        return length;
    }
}
