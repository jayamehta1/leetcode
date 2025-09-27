from collections import Counter, defaultdict


def majority_frequency_group(s: str) -> str:
    if not s:
        return ""
    cnt = Counter(s)
    groups = defaultdict(list)
    for ch, c in cnt.items():
        groups[c].append(ch)
    # pick group with max (number of chars, frequency k)
    best_k, best_chars = max(groups.items(), key=lambda item: (len(item[1]), item[0]))
    return "".join(best_chars)


if __name__ == "__main__":
    print(majority_frequency_group("aaabbbccdddde"))  
