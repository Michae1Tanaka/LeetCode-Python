def isPalindrome(x: int) -> bool:
    int_as_str = str(x)
    if len(int_as_str) == 1:
        return True
    if int_as_str.startswith("-"):
        return False
    else:
        int_as_list = [int(num) for num in int_as_str]
        reversed_list = int_as_list[::-1]
        if int_as_list == reversed_list:
            return True
        else:
            return False
