def solution(s):
    stack = []
    for idx in range(len(s)):
        alpha = s[idx]
        if stack:
            last = stack[-1]
            if last == alpha:
                stack.pop()
            else:
                stack.append(alpha)
        else:
            stack.append(alpha)
    if stack:
        return 0
    return 1