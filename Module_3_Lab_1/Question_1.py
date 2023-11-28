import sys
def maximum_subsequence_count(text, pattern):
    res, cnt1, cnt2 = 0, 0, 0

    for c in text:
        if c == pattern[1]:
            res += cnt1
            cnt2 += 1
        if c == pattern[0]:
            cnt1 += 1

    return res + max(cnt1, cnt2)

if __name__ == "__main__":
    text = input()
    pattern = input()
    print(maximum_subsequence_count(text, pattern))
                                                                                                                            