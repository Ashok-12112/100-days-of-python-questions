class FrequencyCounter:
    def count_occurrences(self, numbers):
        frequency_map = {}
        for idx in range(0,len(numbers)):
            frequency_map[numbers[idx]] = frequency_map.get(numbers[idx],0)+1
        return frequency_map

obj = FrequencyCounter()
numbers = [1, 2, 3, 3, 4, 6, 4, 3, 2, 4, 6, 8, 8, 6, 53, 2]
print(obj.count_occurrences(numbers))