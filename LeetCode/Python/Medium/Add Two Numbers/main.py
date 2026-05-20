class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numbers:list[int] = []
        rest = 0
        while True:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            number = val1 + val2 + rest
            if number >= 10:
                numbers.append(number % 10)
                rest = 1
            else:
                numbers.append(number)
                rest = 0

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None:
                if rest != 0:
                    numbers.append(rest)
                break

        numbers.reverse()

        current_node: ListNode = None
        for number in numbers:
            node = ListNode(number, current_node)
            current_node = node

        return current_node
