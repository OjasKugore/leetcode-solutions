/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) 
{
    struct ListNode *trailer, *leader, *temp1, *temp2;
    int storage;

    trailer = head;
    leader = head;

    for (int i = 0; i<k-1; i++)
    {
        leader = leader -> next;
    }

    temp1 = leader;

    while (leader -> next != NULL)
    {
        leader = leader -> next;
        trailer = trailer -> next;
    }
    
    temp2 = trailer;

    storage = temp1 -> val;
    temp1 -> val = temp2 -> val;
    temp2 -> val = storage;

    return head;
}
