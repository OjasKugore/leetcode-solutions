/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) 
{
    struct ListNode *trailer, *leader, *tmp;
    
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    trailer = &dummy;
    leader = head;

    for (int i = 0; i<n; i++)
    {
        leader = leader -> next;
    }

    while (leader != NULL)
    {
        leader = leader -> next;
        trailer = trailer -> next;
    }

    tmp = trailer -> next;
    trailer ->next = tmp -> next;
    free(tmp);

    return dummy.next;
}
