################## START HELP ##################
def sum_rec(n):
    if n == 0:
        return 1

    def sum_rec_in(n, i=0, sum=0):
        if i == n:
            return sum
        return sum_rec_in(n, i + 1, sum + sum_rec(n-1-i))

    return sum_rec_in(n)


print([sum_rec(i) for i in range(9)])
##################  END HELP  ##################


def catalan_rec(n, memo=None):
    if memo == None:
        memo = {0: 1}
    if n not in memo:
        def catalan_rec_in(n, memo, i=0, acc=0):
            if i == n:
                return acc
            return catalan_rec_in(n, memo, i+1, acc + catalan_rec(i, memo) * catalan_rec(n-1-i, memo))

    memo[n] = catalan_rec_in(n, memo)
    return memo[n]


print([catalan_rec(i) for i in range(15)])
