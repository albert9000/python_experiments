arr = [
    ["R", "G", "G"],
    ["R", "R", "B"],
    ["B", "B", "B"]
]

moves = ["0 1", "2 2", "2 2"]


def board(arr, moves):
    col = 0
    row = 0

    for i in range(len(arr)):
        print(arr[i])

    for j in range(0, len(moves)):
        count = 0
        score = 0
        col = int(moves[j].strip().split(" ")[0])
        row = int(moves[j].strip().split(" ")[1])

        temp = arr[row][col]
        top = "_"
        right = "_"
        bottom = "_"
        left = "_"

        if row - 1 <= 0:
            top = arr[row-1][col]

        if col + 1 <= 2:
            right = arr[row][col+1]

        if row + 1 <= 2:
            bottom = arr[row+1][col]

        if col -1 <= 0:
            left = arr[row][col-1]

        arr[row][col] = "_"
        count += 1

        if top == temp and row-1 >= 0:
            arr[row - 1][col] = "_"
            count += 1


        if top != "_":
            arr[row][col] = arr[row - 1][col]

        if right == temp and col+1 <= 2:
            arr[row][col+1] = "_"
            count += 1
            if drop(arr, row, col+1) != "_":
                arr[row][col + 1] = drop(arr, row, col+1)
                arr[row-1][col +1] = "_"

        if left == temp and col-1 >= 0:
            arr[row][col - 1] = "_"
            count += 1
            if drop(arr, row, col-1) != "_":
                arr[row][col - 1] = drop(arr, row, col - 1)
                arr[row-1][col - 1] = "_"


        if bottom == temp:
            arr[row][col-1] = "_"
            count += 1
            arr[row][col - 1] = drop(arr, row, col-1)

        score = pow(2, 3)

        #for k in range(len(arr)):
         #   print(arr[k])

        print(score)


    for i in range(len(arr)):
        print(arr[i])


def drop(arr, r, c):
    if r-1 >= 0:
        #print(str(r-1) + " " + str(c))
        if arr[r-1][c] != "_":
         #   print("hello")
            return arr[r - 1][c]
        else:
            return "_"

    #elif arr[r-1][c] != "_":

    else:
        return "_"


board(arr, moves)