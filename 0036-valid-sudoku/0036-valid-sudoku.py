class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # rows
        for r in range(9):
            seen = set()

            for c in range(9):
                x = board[r][c]

                if x == ".":
                    continue

                if x in seen:
                    return False

                seen.add(x)

        # columns
        for c in range(9):
            seen = set()

            for r in range(9):
                x = board[r][c]

                if x == ".":
                    continue

                if x in seen:
                    return False

                seen.add(x)

        # 3x3 boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):

                seen = set()

                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):

                        x = board[r][c]

                        if x == ".":
                            continue

                        if x in seen:
                            return False

                        seen.add(x)

        return True