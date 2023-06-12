#include "lists.h"

/**
 * linked_list_length - get length of linked list
 *
 * @head: pointer to head of linked list
 * Return: (int) length of linked list
 */

int linked_list_length(listint_t *head)
{
	int cnt = 0;

	while (head)
	{
		head = head->next;
		cnt++;
	}
	return (cnt);

}

/**
 * get_nth_node - get nth node of linked list
 *
 * @head: pointer to head of linked list
 * @nth: required lenght (starting from 0 and assuming valid number)
 * Return: pointer to required node
 */

listint_t *get_nth_node(listint_t *head, int nth)
{
	while (nth--)
	{
		head = head->next;
	}

	return (head);
}

/**
 * reverse_linded_list - reverse list
 *
 * @head: pointer to head of linked list
 * Return: pointer to head of reveresed linked list
 */

listint_t *reverse_linked_list(listint_t *prev, listint_t *curr)
{
	lintint_t *tmp;

	while (curr)
	{
		tmp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = tmp;
	}
	return (prev);

}


/**
 * is_palindrome - check if linked list is palindrome
 *
 * @head: pointer to head of linked list
 * Return: (int) 1 if it is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	int length = linked_list_length(*head);
	int middle = length / 2;
	listint_t *cmp_first = *head;
	lintint_t *cmp_second;
	int i;
	if (length == 1 || length == 0)
		return (1);
	if (length == 2)
		return (cmp_first->n == cmp_first->next->n);

	cmp_second = get_nth_node(middle);
	cmp_second = reverse_linked_list(cmp_second, cmp_second->next);
	while (middle)
	{
		if (cmp_first->n != cmp_second->n)
			return (0);
		cmp_first = cmp_first->next;
		cmp_second = cmp_second->prev;
		middle--;

	}
	return (1);
}
