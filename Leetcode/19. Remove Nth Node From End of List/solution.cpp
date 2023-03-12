/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *curr=head;
        int count=0;
        if(head==NULL) return head;
        if(head->next == NULL){
            return NULL;
        }
        while(curr!= NULL){
            count++;
            curr=curr->next;
        }
        int pos=count-n;
        if(pos==0){
            curr=head->next;
            delete head;
            return curr;
        }
        ListNode *curr1= head;
        ListNode *temp=curr1->next;
        for(int i=0;i<pos-1;i++){
            curr1=curr1->next;
            temp=temp->next;
        }
        curr1->next=temp->next;
        delete temp;
        return head;
    }
};
