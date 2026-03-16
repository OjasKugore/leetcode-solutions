/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head)
{
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    struct ListNode *p = &dummy, *trailer, *leader, *temp;

    while (p -> next != NULL && p -> next -> next != NULL)
    {
        trailer = p -> next;
        leader = p -> next -> next;
        temp = leader -> next;

        leader -> next = trailer;
        p -> next = leader;
        trailer -> next = temp;

        p = trailer;
    }

    return dummy.next;
}
