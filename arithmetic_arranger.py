def arithmetic_arranger(problems, solve = False):

    if len(problems) > 5:
        return "Error: Too many problems."
# create a lambda function to check operators only '+' or '-'
    operators = {
        '+': lambda pair: str(pair[0] + pair[1]),
        '-': lambda pair: str(pair[0] - pair[1]),
    }
    arranged_problems = []
    top = []
    bottom = []
    lines = []
    results = []

    for problem in problems:
        nums = problem.split()
        max_len = len(max(nums, key=len))

        if not all([i.isnumeric() for i in nums[::2]]):
            return "Error: Numbers must only contain digits."
        elif nums[1] not in operators.keys():
            return "Error: Operator must be '+' or '-'."
        elif max_len > 4:
            return "Error: Numbers cannot be more than four digits."

        line_len = max_len + 2

        line = '-' * line_len  # set it to 2 to get space and allignment correct
        first_num = nums[0].rjust(line_len, ' ')
        second_num = f"{nums[1]}{' ' * (line_len - len(nums[2]) - 1)}{nums[2]}"

        top.append(first_num)
        bottom.append(second_num)
        lines.append(line)

        if solve:
            res = operators[nums[1]]([int(i) for i in nums[::2]])
            results.append(f"{res.rjust(line_len, ' ')}")

    arranged_problems = '\n'.join(['    '.join(i)
                                   for i in (top, bottom, lines)])

    if results:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems