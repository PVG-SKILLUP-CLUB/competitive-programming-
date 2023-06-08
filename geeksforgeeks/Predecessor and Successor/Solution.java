public static void findPreSuc(Node root, int key)
 {
     
  Node curr=root;
    while(curr!=null){
        if(curr.data>key){
            suc=curr;
            curr=curr.left;
        }
        else{
            curr=curr.right;
        }
    }
    curr=root;
    while(curr!=null){
        if(curr.data<key){
            pre=curr;
            curr=curr.right;
        }
        else{
            curr=curr.left;
        }
    }

 }
}
