if __name__ == "__main__":
    num = int(input("Enter the number: ").strip())
    bNum = bin(num)[2:]
    num_list = str(bNum).split('0')
    len_list = [len(num) for num in num_list]
    print(max(len_list))


# Samples:

# Enter the number: 100
# 2

# Enter the number: 9784
# 3

# Enter the number: 7
# 3