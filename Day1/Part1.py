if __name__ == "__main__":
    with open("input", "r") as input_file:
        nums = [num.strip() for num in input_file]
        last_seen = nums[0]
        number_of_increases = 0
        for num in nums[1:]:
            if num > last_seen:
                number_of_increases += 1
            last_seen = num
        if nums[-1] > nums[-2]:
            number_of_increases += 1
        print(number_of_increases)