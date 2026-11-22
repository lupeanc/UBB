# The sequence a1, ..., an of distinct integer numbers is given. Display all subsets with a mountain aspect.
# A set has a mountain aspect if the elements increase up to a point and then they decrease.
# E.g. 10, 16, 27, 18, 14, 7.

def is_mnt(l):
    """
    :param l: list that is checked for mountain aspect
    :return: if list has mountain aspect
    """
    if len(l)<3:
        return 0

    peak = 0
    peak_pos=-1 #position of the peak so there are no cases where it's on the first/last position

    for i in range(1, len(l)):
        if peak == 0:
            if l[i-1] > l[i]:
                peak = 1
                peak_pos = i-1
            elif l[i-1] < l[i]:
                continue
            else:
                return 0
        else: #checks if the peak is on the last position
            if l[i] < l[i-1]:
                continue
            else:
                return 0

    if peak_pos == 0: #checks if the peak is on the first position
        return 0

    return peak

#Time complexity: O(n*2^n) - 2^n subsets ; n from is_mnt
#recursive
def backrec(index, subset, l):
    """
    :param index: keeps track of where to continue checking the list
    :param subset: where the subsets will be built
    :param l: complete list
    """
    if subset and is_mnt(subset):
        print(subset)

    for j in range(index, len(l)):
        subset.append(l[j])
        backrec(j + 1, subset, l)
        subset.pop()

#iterative
def backit(l):
    stack = [(0, [])]

    while stack:
        index, subset = stack.pop()

        for j in range(index, len(l)):
            new_subset = subset + [l[j]]
            stack.append((j + 1, new_subset))

        if subset and is_mnt(subset):
            print(subset)

# print("Backtracking recursive")
# backrec(0, [], [10, 16, 27, 18, 14, 7])
#
# print()
# print("Backtracking iterative")
# backit([10, 16, 27, 18, 14, 7])

#Dynamic Programming
# Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q],
# where m, n, p, q are array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40], the maximum value is 32
# obtained as 40 - 18 + 15 - 5. Display both the maximum value as well as the expression used to calculate it.


def prob6(l):
    smax = -9999
    a = [0, 0, 0, 0]
    for m in range(len(l)-1, 2, -1):

        for n in range(m-1, 1, -1):

            for p in range(n-1, 0, -1):

                for q in range(p-1, -1, -1):

                    if l[m] - l[n] + l[p] - l[q] > smax:
                        smax = l[m] - l[n] + l[p] - l[q]
                        a[0] = l[m]
                        a[1] = l[n]
                        a[2] = l[p]
                        a[3] = l[q]
    print(a[0], " - ", a[1], " + ", a[2], " - ", a[3], " = ", smax)

def dp6(A):
    n = len(A)

    # Initialize arrays
    min_q = [2 ** 100] * n
    max_p_minus_q = [-2 ** 100] * n
    max_m = [0] * n
    max_m_minus_n = [0] * n
    max_m_minus_n_plus_p_minus_q = -2 ** 100

    values_p_and_q = [[0, 0]] * n  # values_p_and_q[i] = values for the maximum difference A[p]-A[q] where p and q are 0 and i respectively
    values_m_and_n = [[0, 0]] * n

    # minimum values of q, min_q[i] = minimum value from sequence 0, 1, ..., n-1 from the array
    min_q[0] = A[0]
    for i in range(1, n):
        min_q[i] = min(min_q[i - 1], A[i])

    max_p_minus_q[0]=0
    max_p_minus_q[1] = A[1] - A[0]  # lowest possible combination for p>q
    for i in range(2, n):
        if max_p_minus_q[i - 1] >= A[i] - min_q[i - 1]:
            max_p_minus_q[i] = max_p_minus_q[i - 1]
        else:
            max_p_minus_q[i] = A[i] - min_q[i - 1]
            values_p_and_q[i] = [A[i], min_q[i - 1]]

    print("Min values of q: ", min_q)
    print("Values for p and q: ", values_p_and_q)
    print("Max for difference: ", max_p_minus_q)
    print()

    max_m[n - 2] = A[n - 1]
    for i in range(n - 3, -2, -1):
        max_m[i] = max(max_m[i + 1], A[i + 1])

    max_m_minus_n[n - 3] = A[n - 1] - A[n - 2]  # highest possible combination for m>n
    for i in range(n - 4, -1, -1):
        if max_m_minus_n[i + 1] >= -A[i + 1] + max_m[i + 1]:
            max_m_minus_n[i] = max_m_minus_n[i + 1]
        else:
            max_m_minus_n[i] = -A[i + 1] + max_m[i + 1]
            values_m_and_n[i] = [max_m[i + 1], A[i + 1]]

    print("Max value of m: ", max_m)
    print("Values for m and n: ", values_m_and_n)
    print("Max for difference: ", max_m_minus_n)
    print()

    values_of_sum = [0, 0, 0, 0] #save the values for the sum
    for i in range(1, n - 1):  # begin from 1 (q=0, p=1 lowest values) and go to n-2 (m=n-1, n=n-2 highest values)
        if max_m_minus_n_plus_p_minus_q < max_p_minus_q[i] + max_m_minus_n[i]:  # value changes
            max_m_minus_n_plus_p_minus_q = max_p_minus_q[i] + max_m_minus_n[i]
            values_of_sum = [values_m_and_n[i][0], values_m_and_n[i][1], values_p_and_q[i][0], values_p_and_q[i][1]]

    print(values_of_sum[0], "-", values_of_sum[1], "+", values_of_sum[2], "-", values_of_sum[3], " = ", max_m_minus_n_plus_p_minus_q)

l = [30, 5, 15, 18, 30, 40]
prob6(l)
dp6(l)