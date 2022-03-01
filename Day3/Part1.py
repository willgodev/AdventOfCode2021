if __name__ == "__main__":
    with open("input", "r") as input_file:
        nums = [num.strip() for num in input_file]
        occurrence_list = []
        for num in nums[0]:
            occurrence_list.append(0)
        for num in nums:
            for i in range(len(num)):
                if num[i] == '0':
                    occurrence_list[i] -= 1
                else:
                    occurrence_list[i] += 1
        gamma_rate = ''
        for occurrence in occurrence_list:
            if occurrence >= 0:
                gamma_rate += '1'
            else:
                gamma_rate += '0'
        epsilon_rate = ''.join('1' if c == '0' else '0' for c in gamma_rate)
        gamma_rate = int(gamma_rate, 2)
        epsilon_rate = int(epsilon_rate, 2)
        answer = gamma_rate * epsilon_rate
        print(answer)