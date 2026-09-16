import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
        }

        for item in tokens:
            if item not in ops:
                eval_stack.append(item)
            else:
                operation = ops.get(item)
                operand_right = int(eval_stack.pop())
                operand_left = int(eval_stack.pop())
                res = operation(operand_left, operand_right)
                eval_stack.append(res)
 

        return int(eval_stack[0])
                





        