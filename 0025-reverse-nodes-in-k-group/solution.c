/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) 
{
    if (head == NULL || k == 1)
    {
        return head;
    }

    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    //count how many nodes are there in the list
    int counter = 0;
    struct ListNode *p = head;
    while (p != NULL)
    {
        p = p -> next;
        counter++;
    }
    struct ListNode *prevgroupend = &dummy, *curr, *Next;

    while (counter >= k)
    {
        curr = prevgroupend -> next;

        Next = curr -> next;

        for (int i = 0; i< k-1; i++)
        {
            curr -> next = Next -> next;
            Next -> next = prevgroupend -> next;
            prevgroupend -> next = Next;

            Next = curr -> next;
        }

        prevgroupend = curr;
        counter -= k;
    }

    return dummy.next;
}
