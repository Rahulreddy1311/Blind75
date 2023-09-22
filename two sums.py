class Sol:
    def twoSum(self, number: List[int], target: int) -> List[int]:
                n = len(number)
                for i in range(n - 1):
                    for j in range(i + 1, n):
                        if number[i] + number[j] == target:
                            return [i, j]
                return []