class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dict = {}

        for num_index in range(0, len(nums)):

            selected_number = nums[len(nums)-1-num_index]
            length_list = []
            counter_list = []
            counter = 0

            for j in range(len(nums)-num_index, len(nums)):
                next_number = nums[j]
                selected_number_counter, selected_number_length = dict[j]
                if next_number > selected_number:
                    length_list.append(selected_number_length)
                    counter_list.append(selected_number_counter)

            if len(length_list) == 0:
                dict[len(nums)-1-num_index] = [1, 1]
                continue

            max_length = max(length_list)
            for l in range(len(length_list)):
                if length_list[l] == max_length:
                    counter += counter_list[l]
            dict[len(nums)-1-num_index] = [counter, max_length + 1]

        max_length = 0
        for key in dict:
            if dict[key][1] > max_length:
                max_length = dict[key][1]

        counter = 0
        for key in dict:
            if dict[key][1] == max_length:
                counter += dict[key][0]

        return counter
                

