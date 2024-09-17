def snail(snail_map):
    numbers = []

    n = len(snail_map[0]) - 1
    if n >= 0:
        g = 0
        if n % 2 == 0:
            gt = n / 2
        else:
            gt = (n / 2) + 0.5
        while g <= gt:
            for num in snail_map[g][g:n]:
                numbers.append(num)

            for num in snail_map[g:n]:
                numbers.append(num[n])

            for i in range(len(snail_map[n-g])-g-1, g-1, -1):
                numbers.append(snail_map[n][i])

            for num in range(n-1,g,-1):
                numbers.append(snail_map[num][g])

            n-=1
            g+=1

        return numbers
    else:
        return []