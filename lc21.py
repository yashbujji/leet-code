class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(list1, list2):
    # Initialize a placeholder for the result
    prehead = ListNode(-1)

    prev = prehead
    while list1 and list2:
        if list1.val <= list2.val:
            print(f"Adding {list1.val} from list1 to the merged list")
            prev.next = list1
            list1 = list1.next
        else:
            print(f"Adding {list2.val} from list2 to the merged list")
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    # At this point, we have one non-null list and one null, append the non-null list to merged list
    if list1 is not None:
        print(f"Adding the rest of list1 to the merged list")
    else:
        print(f"Adding the rest of list2 to the merged list")

    prev.next = list1 if list1 is not None else list2

    return prehead.next

def printList(node):
    while node is not None:
        print(node.val, end = " ")
        node = node.next
    print()

# Creating two sorted linked lists
node1 = ListNode(1)
node2 = ListNode(2)
node4 = ListNode(4)
node1_2 = ListNode(1)
node3 = ListNode(3)
node4_2 = ListNode(4)

node1.next = node2
node2.next = node4
node1_2.next = node3
node3.next = node4_2

print("List 1:")
printList(node1)
print("List 2:")
printList(node1_2)

print("\nMerging the lists...\n")
merged_head = mergeTwoLists(node1, node1_2)

print("\nMerged List:")
printList(merged_head)
