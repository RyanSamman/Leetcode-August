class Solution:
	# Naive solution, w/o Combinations formula
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for _ in range(rowIndex + 1):
            row = [row[i - 1] + row[i] if len(row) > i > 0 else 1 for i in range(len(row) + 1)]
        return row
        