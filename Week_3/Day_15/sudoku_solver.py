# ==========================================
# PART 1: The Board Setup (0 represents empty)
# ==========================================
board = [
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# ==========================================
# PART 2: Constraint Checking
# ==========================================
def is_valid(bo, num, pos):
    row, col = pos

    # Check Row
    for i in range(9):
        if bo[row][i] == num and col != i:
            return False

    # Check Column
    for i in range(9):
        if bo[i][col] == num and row != i:
            return False

    # Check 3x3 Box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# ==========================================
# PART 3: The Backtracking Algorithm
# ==========================================
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def solve(bo):
    # 1. BASE CASE: No empty spots left? We are done!
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    # 2. RECURSIVE STEP: Try numbers 1-9
    for i in range(1, 10):
        # Check constraints (Pruning)
        if is_valid(bo, i, (row, col)):
            # A. Choose
            bo[row][col] = i

            # B. Explore (Recurse)
            if solve(bo):
                return True

            # C. Un-choose (Backtrack)
            # If we get here, it means solve(bo) returned False.
            # So the choice 'i' was wrong. Reset to 0 and try next number.
            bo[row][col] = 0

    return False

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- Original Board ---")
    print_board(board)
    
    print("\n--- Solving... ---")
    solve(board)
    
    print("--- Solved Board ---")
    print_board(board)