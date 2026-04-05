from collections import Counter, defaultdict
"""You are given a string s consisting of lowercase English letters.
The frequency group for a value k is the set of characters that appear exactly k times in s.
The majority frequency group is the frequency group that contains the largest number of distinct characters.
Return a string containing all characters in the majority frequency group, in any order. If two or more frequency groups tie for that largest size, pick the group whose frequency k is larger.©leetcode"""

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
    
    
