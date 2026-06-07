class Check:
    def number(self, numbers, query_numbers):
        frequency = {}

        for num in numbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for item in query_numbers:
            print(item, ":", frequency.get(item, 0))

obj = Check()

numbers = [1, 2, 3, 4, 5, 6, 87, 8]
query_numbers = [2, 3, 5]

obj.number(numbers, query_numbers)