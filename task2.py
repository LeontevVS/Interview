from task1 import Stack

def check_brackets_balance(sequence: str) -> str:
    stack = Stack()
    sequence_len = len(sequence)
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    for i in range(sequence_len):
        elem = sequence[i]
        if elem in brackets:
            stack.push(elem)
        else:
            try:
                last_opening = brackets[stack.pop()]
            except IndexError:
                return 'Несбалансированно'
            if last_opening != elem:
                return 'Несбалансированно'
    else:
        return 'Сбалансированно'