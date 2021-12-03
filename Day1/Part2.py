if __name__ == "__main__":
    with open("input", "r") as input_file:
        nums = [int(num.strip()) for num in input_file]
        if len(nums) > 5:
            last_window = nums[0] + nums[1] + nums[2]
            number_of_increases = 0
            i = 1
            while i + 2 < len(nums):
                this_window = nums[i] + nums[i+1] + nums[i+2]
                if this_window > last_window:
                    number_of_increases += 1
                last_window = this_window
                i += 1
            print(number_of_increases)