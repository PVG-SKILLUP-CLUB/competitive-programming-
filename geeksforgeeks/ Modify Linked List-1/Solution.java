class Solution
{
    static int count;
    static Node root;
    static Node call(Node temp){
        if(temp.next == null){
            return temp;
        }
        Node nVal = call(temp.next);
        if(count>0 ){
            int mom = nVal.data;
            nVal.data = root.data;
            root.data = mom - root.data;
            count--;
            root = root.next;
        }
        return temp;
    }
    public static Node modifyTheList(Node head)
    {
        Node temp = head;
        int size =0;
        while(temp!= null){
            size++;
            temp = temp.next;
        }
        if(size == 1)return head;
        temp = head;
        root = head;
        count = size/2;
        call(temp);
        return head;
        
    }
    
}
