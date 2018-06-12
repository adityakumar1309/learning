"""
You can win three kinds of basketball points, 1 point, 2 points, and 3 points. Given a total score n, print out all the combination to compose n.

Examples:

For n = 1, the program should print following:
1

For n = 2, the program should print following:
1 1
2

For n = 3, the program should print following:
1 1 1
1 2
2 1 
3

For n = 4, the program should print following:
1 1 1 1
1 1 2
1 2 1
1 3
2 1 1
2 2
3 1

and so on ...
"""

POINT_SET = [1,2,3]

def get_combination(cur_sum,  desired_sum, collected_points_array, i):
    if cur_sum == desired_sum:
        call_print(collected_points_array, i)

    elif cur_sum < desired_sum:
        for point in POINT_SET:
            collected_points_array[i] = str(point)
            got_sum = get_combination(cur_sum+point, desired_sum, collected_points_array, i+1)

def call_print(arr, i):
    st = ""
    for index, ele in enumerate(arr):
        if index != i:
            st = st + " " + ele
        else:
            print st

sum_reqd = 4
gathered_points_array = [''] * sum_reqd
get_combination(0, sum_reqd, gathered_points_array, 0)


