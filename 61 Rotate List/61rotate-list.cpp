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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) {
            return head;
        }
        int len = 1;
        ListNode* tail = head;

        while (tail->next != nullptr) {
            tail = tail->next;
            len += 1;
        }

        k = k % len;

        if (k == 0) {
            return head;
        }

        ListNode* curr = head;
        for (int i = 0; i < len - k - 1; i++) {
            curr = curr->next;
        }

        ListNode* newHead = curr->next;
        curr->next = nullptr;
        tail->next = head;

        return newHead;
    }
};