#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list) {
    listint_t *slow, *fast, *temp;

    if (!list)
        return 0;

    slow = list;
    fast = list;

    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            slow = list;
            while (slow != fast) {
                temp = fast->next;
                fast = temp;
            }
            return 1;
        }
    }

    return 0;
}
