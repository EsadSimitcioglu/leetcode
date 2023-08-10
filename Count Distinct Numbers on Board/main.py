class Solution:
    def distinctIntegers(self, n: int) -> int:

        def find_numbers(number):
            board_numbers = []
            for i in range(1, number):
                if number % i == 1:
                    board_numbers.append(i)
            return board_numbers

        distinct_board_numbers = [n]
        numbers = {}
        index = 0

        while index < len(distinct_board_numbers):
            number = distinct_board_numbers[index]
            index += 1
            if number in numbers:
                continue
            else:
                temp_board_numbers = find_numbers(number)
                numbers[number] = True
                distinct_board_numbers.extend(temp_board_numbers)
        
        return len(set(distinct_board_numbers))