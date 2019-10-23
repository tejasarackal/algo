from llist import sllist


def palindrome(ls: sllist) -> bool:
    slow, fast = ls.first, ls.first
    stack_ = []

    while fast.next and fast.next.next:
        stack_.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast.next:
        stack_.append(slow.value)
    slow = slow.next

    while stack_ and slow:
        if slow.value != stack_.pop():
            return False
        slow = slow.next

    return len(stack_) == 0


if __name__ == '__main__':
    ls = sllist(['b'])
    print(palindrome(ls))
