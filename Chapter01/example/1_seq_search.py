from json.tool import main


def seqsearch(lst, x):
    index = 0
    while index < len(lst) and lst[index] != x:
        index += 1
    if index == len(lst):
        index = -1
    return index

if __name__ == "__main__":
    lst = [5, 7, 8, 10, 11, 13]
    print(seqsearch(lst, 10))