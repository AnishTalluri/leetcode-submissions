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

    ListNode* reverse(ListNode* head) {
        ListNode* temp = nullptr;
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr != nullptr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        head = prev;

        return head;
    }

    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }

        if (fast != nullptr) {
            slow = slow->next;
        }

        slow = reverse(slow);
        fast = head;

        while (slow != nullptr) {
            if (fast->val != slow->val) {
                return false;
            }
            
            fast = fast->next;
            slow = slow->next;
        }
        return true;
    }
};