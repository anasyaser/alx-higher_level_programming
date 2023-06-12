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
 * reverse_list - reverse list
 *
 * @curr: pointer to head to start reverse
 * Return: pointer to head of reveresed linked list
 */

listint_t *reverse_list(listint_t *curr)
{
	listint_t *prev = NULL;
	listint_t *tmp;

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
	listint_t *last_node;
	listint_t *cmp_second;

	if (length == 1 || length == 0)
		return (1);
	if (length == 2)
		return (cmp_first->n == cmp_first->next->n);
/* not that we can remove above condtitions and still works well*/
	cmp_second = get_nth_node(cmp_first, middle);
	cmp_second = reverse_list(cmp_second);
	last_node = cmp_second;
	while (middle)
	{
		if (cmp_first->n != cmp_second->n)
		{
			reverse_list(last_node);
			return (0);
		}
		cmp_first = cmp_first->next;
		cmp_second = cmp_second->next;
		middle--;

	}
	reverse_list(last_node);
	return (1);
}
