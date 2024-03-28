def add_binary(str1, str2):

    ptr1 = len(str1) - 1
    ptr2 = len(str2) - 1
    result = ""
    carry = 0
    for i in range(max(len(str2), len(str1))):
        if ptr1 < 0:
            dgt1 = 0
            dgt2 = int(str2[ptr2])
        elif ptr2 < 0:
            dgt1 = int(str1[ptr1])
            dgt2 = 0
        else:
            dgt1 = int(str1[ptr1])
            dgt2 = int(str2[ptr2])
        added = dgt1 + dgt2 + carry
        print(dgt1, dgt2, added)
        if added == 0:
            carry = 0
            result += "0"
        elif added == 1:
            carry = 0
            result += "1"
        elif added == 2:
            carry = 1
            result += "0"
        elif added == 3:
            carry = 1
            result += "1"

        ptr1 -= 1
        ptr2 -= 1
    if carry == 1:
        result += "1"
    # Replace this placeholder return statement with your code
    return result[::-1]
