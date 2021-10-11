Leetcode 1047 — Remove All Adjacent Duplicates In String

## Solution
This problem can be solved by Stack. We can put all characters one by on into stack
While we put character to stack with check the top of stack. If the top of stack equal to the
current value, we don't put the current to stack and pop the top value of stack.
After loop through all string, we pop all element in stack and then we can get the reverse of a string.
That is the result
