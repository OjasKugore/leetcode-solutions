/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) 
{
    struct ListNode* P, *Tmp;
    P = head;

    while (P != NULL && P -> next != NULL)
    {
        if (P -> val == P -> next -> val)
        {
            Tmp = P -> next;
            P -> next = P -> next -> next;
            free(Tmp);
        }
        else
        {
            P = P-> next;
        }
    }
    return head;
}
