//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class Node {
    char data;
    Node next;

    Node(char x) {
        data = x;
        next = null;
    }

    public static Node inputList(BufferedReader br) throws IOException {
        int n = Integer.parseInt(br.readLine().trim()); // Length of Linked List

        String[] s = br.readLine().trim().split(" ");
        Node head = new Node((s[0].charAt(0))), tail = head;
        for (int i = 1; i < s.length; i++)
            tail = tail.next = new Node((s[i].charAt(0)));

        return head;
    }

    public static void printList(Node node, PrintWriter out) {
        while (node != null) {
            out.print(node.data + " ");
            node = node.next;
        }
        out.println();
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            Node head = Node.inputList(br);

            String S = br.readLine().trim();

            Solution obj = new Solution();
            ArrayList<Node> res = obj.findAnagrams(head, S);

            for (Node node : res) {
                Node temp = node;
                Node.printList(temp, out);
            }
            if (res.size() == 0) {
                out.println("-1");
            }
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java
/*

Definition for singly Link List Node
class Node
{
    char data;
    Node next;

    Node(char x){
        data = x;
        next = null;
    }
}

You can also use the following for printing the link list.
Node.printList(Node node);
*/

class Solution {
    public static ArrayList<Node> findAnagrams(Node head, String s) {
      
        ArrayList<Node> a = new ArrayList<>();
        Node prev = head;
        Node curr = head;
        int arr[]=new int[26];

        for(int i=0; i<s.length(); i++)arr[s.charAt(i)-'a']++;
        int j=0;
        int n= s.length();
 
        while(curr!=null)
        {
            int[] arr2 = new int[26];
            while(j<n && curr!=null)
            {
                arr2[curr.data-'a']++;
                curr=curr.next;
                j++;
            }
            boolean ana = true;
            
            for(int i=0; i<26; i++)
            {
                if(arr[i]!=arr2[i])
                {
                    ana = false;
                    break;
                }
            }
            
            if(ana==false)
            {
                curr=prev.next;
                prev = curr ;
                j=0;
                continue;
            }
            else 
            {
                
                Node nh = new Node('x');
                Node temp = nh;
                while(j>0)
                {
                    Node nh2 = new Node(prev.data);
                    prev=prev.next;
                    temp.next =nh2;
                    temp = nh2;
                    j--;
                }
                a.add(nh.next);
                curr = prev;
            }
        }
        return a;
    }
}
