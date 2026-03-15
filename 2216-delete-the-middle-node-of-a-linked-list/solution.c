/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode *trailer, *slow, *fast;
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    trailer = &dummy;
    slow = head;
    fast = head;

    while (fast != NULL && fast -> next != NULL)
    {
        trailer = trailer -> next;
        slow = slow -> next;
        fast = fast -> next -> next;
    }

    trailer -> next = trailer -> next -> next;
    free(slow);

    return dummy.next;
}
