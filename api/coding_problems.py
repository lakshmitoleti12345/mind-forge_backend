# 50 Must-Solve Technical Interview Coding Challenges (Python, JS, SQL, Data Structures)

CODING_PROBLEMS = [
    # --- ARRAYS & HASHING (1-10) ---
    {
        "title": "1. Two Sum",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
        "language": "python",
        "initial_code": "def two_sum(nums, target):\n    # Write solution here\n    pass",
        "solution_code": "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
        "test_cases": [
            {"input": "([2, 7, 11, 15], 9)", "expected_output": "[0, 1]"},
            {"input": "([3, 2, 4], 6)", "expected_output": "[1, 2]"},
            {"input": "([3, 3], 6)", "expected_output": "[0, 1]"}
        ]
    },
    {
        "title": "2. Contains Duplicate",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "description": "Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.",
        "language": "python",
        "initial_code": "def contains_duplicate(nums):\n    # Write solution here\n    pass",
        "solution_code": "def contains_duplicate(nums):\n    return len(nums) != len(set(nums))",
        "test_cases": [
            {"input": "([1, 2, 3, 1],)", "expected_output": "True"},
            {"input": "([1, 2, 3, 4],)", "expected_output": "False"},
            {"input": "([1, 1, 1, 3, 3, 4],)", "expected_output": "True"}
        ]
    },
    {
        "title": "3. Valid Anagram",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "description": "Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.",
        "language": "python",
        "initial_code": "def is_anagram(s, t):\n    # Write solution here\n    pass",
        "solution_code": "def is_anagram(s, t):\n    return sorted(s) == sorted(t)",
        "test_cases": [
            {"input": "('anagram', 'nagaram')", "expected_output": "True"},
            {"input": "('rat', 'car')", "expected_output": "False"}
        ]
    },
    {
        "title": "4. Group Anagrams",
        "category": "Arrays & Hashing",
        "difficulty": "Medium",
        "description": "Given an array of strings `strs`, group the anagrams together in a list of lists.",
        "language": "python",
        "initial_code": "def group_anagrams(strs):\n    # Write solution here\n    pass",
        "solution_code": "from collections import defaultdict\ndef group_anagrams(strs):\n    ans = defaultdict(list)\n    for s in strs:\n        ans[tuple(sorted(s))].append(s)\n    return list(ans.values())",
        "test_cases": [
            {"input": "(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],)", "expected_output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]"}
        ]
    },
    {
        "title": "5. Top K Frequent Elements",
        "category": "Arrays & Hashing",
        "difficulty": "Medium",
        "description": "Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in any order.",
        "language": "python",
        "initial_code": "def top_k_frequent(nums, k):\n    # Write solution here\n    pass",
        "solution_code": "from collections import Counter\ndef top_k_frequent(nums, k):\n    return [item for item, count in Counter(nums).most_common(k)]",
        "test_cases": [
            {"input": "([1, 1, 1, 2, 2, 3], 2)", "expected_output": "[1, 2]"},
            {"input": "([1], 1)", "expected_output": "[1]"}
        ]
    },
    {
        "title": "6. Product of Array Except Self",
        "category": "Arrays & Hashing",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]` without using division.",
        "language": "python",
        "initial_code": "def product_except_self(nums):\n    # Write solution here\n    pass",
        "solution_code": "def product_except_self(nums):\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
        "test_cases": [
            {"input": "([1, 2, 3, 4],)", "expected_output": "[24, 12, 8, 6]"}
        ]
    },
    {
        "title": "7. Find Missing Number",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "description": "Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.",
        "language": "python",
        "initial_code": "def missing_number(nums):\n    # Write solution here\n    pass",
        "solution_code": "def missing_number(nums):\n    n = len(nums)\n    return n * (n + 1) // 2 - sum(nums)",
        "test_cases": [
            {"input": "([3, 0, 1],)", "expected_output": "2"},
            {"input": "([0, 1],)", "expected_output": "2"},
            {"input": "([9, 6, 4, 2, 3, 5, 7, 0, 1],)", "expected_output": "8"}
        ]
    },
    {
        "title": "8. Move Zeroes",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "description": "Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements in-place.",
        "language": "python",
        "initial_code": "def move_zeroes(nums):\n    # Write solution here\n    pass",
        "solution_code": "def move_zeroes(nums):\n    pos = 0\n    for i in range(len(nums)):\n        if nums[i] != 0:\n            nums[pos], nums[i] = nums[i], nums[pos]\n            pos += 1\n    return nums",
        "test_cases": [
            {"input": "([0, 1, 0, 3, 12],)", "expected_output": "[1, 3, 12, 0, 0]"},
            {"input": "([0],)", "expected_output": "[0]"}
        ]
    },
    {
        "title": "9. Longest Consecutive Sequence",
        "category": "Arrays & Hashing",
        "difficulty": "Medium",
        "description": "Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence in O(n) time.",
        "language": "python",
        "initial_code": "def longest_consecutive(nums):\n    # Write solution here\n    pass",
        "solution_code": "def longest_consecutive(nums):\n    num_set = set(nums)\n    longest = 0\n    for n in num_set:\n        if (n - 1) not in num_set:\n            length = 1\n            while (n + length) in num_set:\n                length += 1\n            longest = max(longest, length)\n    return longest",
        "test_cases": [
            {"input": "([100, 4, 200, 1, 3, 2],)", "expected_output": "4"},
            {"input": "([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],)", "expected_output": "9"}
        ]
    },
    {
        "title": "10. Subarray Sum Equals K",
        "category": "Arrays & Hashing",
        "difficulty": "Medium",
        "description": "Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.",
        "language": "python",
        "initial_code": "def subarray_sum(nums, k):\n    # Write solution here\n    pass",
        "solution_code": "def subarray_sum(nums, k):\n    res, cur_sum = 0, 0\n    prefix_sums = {0: 1}\n    for n in nums:\n        cur_sum += n\n        diff = cur_sum - k\n        res += prefix_sums.get(diff, 0)\n        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1\n    return res",
        "test_cases": [
            {"input": "([1, 1, 1], 2)", "expected_output": "2"},
            {"input": "([1, 2, 3], 3)", "expected_output": "2"}
        ]
    },

    # --- TWO POINTERS & SLIDING WINDOW (11-20) ---
    {
        "title": "11. Valid Palindrome",
        "category": "Two Pointers",
        "difficulty": "Easy",
        "description": "Given a string `s`, return `True` if it is a palindrome after removing non-alphanumeric characters and ignoring case.",
        "language": "python",
        "initial_code": "def is_palindrome(s):\n    # Write solution here\n    pass",
        "solution_code": "def is_palindrome(s):\n    filtered = ''.join(c.lower() for c in s if c.isalnum())\n    return filtered == filtered[::-1]",
        "test_cases": [
            {"input": "('A man, a plan, a canal: Panama',)", "expected_output": "True"},
            {"input": "('race a car',)", "expected_output": "False"}
        ]
    },
    {
        "title": "12. 3Sum",
        "category": "Two Pointers",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that their sum equals 0.",
        "language": "python",
        "initial_code": "def three_sum(nums):\n    # Write solution here\n    pass",
        "solution_code": "def three_sum(nums):\n    nums.sort()\n    res = []\n    for i, a in enumerate(nums):\n        if i > 0 and a == nums[i-1]: continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            threeSum = a + nums[l] + nums[r]\n            if threeSum > 0: r -= 1\n            elif threeSum < 0: l += 1\n            else:\n                res.append([a, nums[l], nums[r]])\n                l += 1\n                while nums[l] == nums[l-1] and l < r: l += 1\n    return res",
        "test_cases": [
            {"input": "([-1, 0, 1, 2, -1, -4],)", "expected_output": "[[-1, -1, 2], [-1, 0, 1]]"}
        ]
    },
    {
        "title": "13. Container With Most Water",
        "category": "Two Pointers",
        "difficulty": "Medium",
        "description": "Given `n` non-negative integers `height` representing vertical lines, find two lines that together with the x-axis form a container holding maximum water.",
        "language": "python",
        "initial_code": "def max_area(height):\n    # Write solution here\n    pass",
        "solution_code": "def max_area(height):\n    l, r = 0, len(height) - 1\n    res = 0\n    while l < r:\n        area = (r - l) * min(height[l], height[r])\n        res = max(res, area)\n        if height[l] < height[r]: l += 1\n        else: r -= 1\n    return res",
        "test_cases": [
            {"input": "([1, 8, 6, 2, 5, 4, 8, 3, 7],)", "expected_output": "49"}
        ]
    },
    {
        "title": "14. Best Time to Buy and Sell Stock",
        "category": "Sliding Window",
        "difficulty": "Easy",
        "description": "Given an array `prices` where `prices[i]` is the price of stock on day `i`, return maximum profit achievable from one buy and one sell.",
        "language": "python",
        "initial_code": "def max_profit(prices):\n    # Write solution here\n    pass",
        "solution_code": "def max_profit(prices):\n    min_price = float('inf')\n    max_prof = 0\n    for p in prices:\n        if p < min_price: min_price = p\n        elif p - min_price > max_prof: max_prof = p - min_price\n    return max_prof",
        "test_cases": [
            {"input": "([7, 1, 5, 3, 6, 4],)", "expected_output": "5"},
            {"input": "([7, 6, 4, 3, 1],)", "expected_output": "0"}
        ]
    },
    {
        "title": "15. Longest Substring Without Repeating Characters",
        "category": "Sliding Window",
        "difficulty": "Medium",
        "description": "Given a string `s`, find the length of the longest substring without repeating characters.",
        "language": "python",
        "initial_code": "def length_of_longest_substring(s):\n    # Write solution here\n    pass",
        "solution_code": "def length_of_longest_substring(s):\n    char_set = set()\n    l = 0\n    res = 0\n    for r in range(len(s)):\n        while s[r] in char_set:\n            char_set.remove(s[l])\n            l += 1\n        char_set.add(s[r])\n        res = max(res, r - l + 1)\n    return res",
        "test_cases": [
            {"input": "('abcabcbb',)", "expected_output": "3"},
            {"input": "('bbbbb',)", "expected_output": "1"},
            {"input": "('pwwkew',)", "expected_output": "3"}
        ]
    },
    {
        "title": "16. Remove Duplicates from Sorted Array",
        "category": "Two Pointers",
        "difficulty": "Easy",
        "description": "Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and return the new length.",
        "language": "python",
        "initial_code": "def remove_duplicates(nums):\n    # Write solution here\n    pass",
        "solution_code": "def remove_duplicates(nums):\n    if not nums: return 0\n    l = 1\n    for r in range(1, len(nums)):\n        if nums[r] != nums[r - 1]:\n            nums[l] = nums[r]\n            l += 1\n    return l",
        "test_cases": [
            {"input": "([1, 1, 2],)", "expected_output": "2"},
            {"input": "([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],)", "expected_output": "5"}
        ]
    },
    {
        "title": "17. Max Consecutive Ones",
        "category": "Sliding Window",
        "difficulty": "Easy",
        "description": "Given a binary array `nums`, return the maximum number of consecutive 1's in the array.",
        "language": "python",
        "initial_code": "def find_max_consecutive_ones(nums):\n    # Write solution here\n    pass",
        "solution_code": "def find_max_consecutive_ones(nums):\n    max_cnt, cur_cnt = 0, 0\n    for n in nums:\n        if n == 1:\n            cur_cnt += 1\n            max_cnt = max(max_cnt, cur_cnt)\n        else:\n            cur_cnt = 0\n    return max_cnt",
        "test_cases": [
            {"input": "([1, 1, 0, 1, 1, 1],)", "expected_output": "3"},
            {"input": "([1, 0, 1, 1, 0, 1],)", "expected_output": "2"}
        ]
    },
    {
        "title": "18. Minimum Size Subarray Sum",
        "category": "Sliding Window",
        "difficulty": "Medium",
        "description": "Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`.",
        "language": "python",
        "initial_code": "def min_sub_array_len(target, nums):\n    # Write solution here\n    pass",
        "solution_code": "def min_sub_array_len(target, nums):\n    l, total = 0, 0\n    res = float('inf')\n    for r in range(len(nums)):\n        total += nums[r]\n        while total >= target:\n            res = min(res, r - l + 1)\n            total -= nums[l]\n            l += 1\n    return res if res != float('inf') else 0",
        "test_cases": [
            {"input": "(7, [2, 3, 1, 2, 4, 3])", "expected_output": "2"},
            {"input": "(4, [1, 4, 4])", "expected_output": "1"}
        ]
    },
    {
        "title": "19. Trapping Rain Water",
        "category": "Two Pointers",
        "difficulty": "Hard",
        "description": "Given `n` non-negative integers representing an elevation map where width of each bar is 1, compute how much water it can trap after raining.",
        "language": "python",
        "initial_code": "def trap(height):\n    # Write solution here\n    pass",
        "solution_code": "def trap(height):\n    if not height: return 0\n    l, r = 0, len(height) - 1\n    leftMax, rightMax = height[l], height[r]\n    res = 0\n    while l < r:\n        if leftMax < rightMax:\n            l += 1\n            leftMax = max(leftMax, height[l])\n            res += leftMax - height[l]\n        else:\n            r -= 1\n            rightMax = max(rightMax, height[r])\n            res += rightMax - height[r]\n    return res",
        "test_cases": [
            {"input": "([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],)", "expected_output": "6"}
        ]
    },
    {
        "title": "20. Permutation in String",
        "category": "Sliding Window",
        "difficulty": "Medium",
        "description": "Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`.",
        "language": "python",
        "initial_code": "def check_inclusion(s1, s2):\n    # Write solution here\n    pass",
        "solution_code": "from collections import Counter\ndef check_inclusion(s1, s2):\n    c1, n1 = Counter(s1), len(s1)\n    c2 = Counter(s2[:n1])\n    if c1 == c2: return True\n    for i in range(n1, len(s2)):\n        c2[s2[i]] += 1\n        c2[s2[i - n1]] -= 1\n        if c2[s2[i - n1]] == 0: del c2[s2[i - n1]]\n        if c1 == c2: return True\n    return False",
        "test_cases": [
            {"input": "('ab', 'eidbaooo')", "expected_output": "True"},
            {"input": "('ab', 'eidboaoo')", "expected_output": "False"}
        ]
    },

    # --- STRINGS & STACK (21-30) ---
    {
        "title": "21. Valid Parentheses",
        "category": "Stack & Strings",
        "difficulty": "Easy",
        "description": "Given a string `s` containing just characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "language": "python",
        "initial_code": "def is_valid(s):\n    # Write solution here\n    pass",
        "solution_code": "def is_valid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top: return False\n        else:\n            stack.append(char)\n    return not stack",
        "test_cases": [
            {"input": "('()',)", "expected_output": "True"},
            {"input": "('()[]{}',)", "expected_output": "True"},
            {"input": "('(]',)", "expected_output": "False"}
        ]
    },
    {
        "title": "22. Reverse String",
        "category": "Stack & Strings",
        "difficulty": "Easy",
        "description": "Write a function that reverses a string value.",
        "language": "javascript",
        "initial_code": "function reverseString(str) {\n    // Write solution here\n}",
        "solution_code": "function reverseString(str) {\n    return str.split('').reverse().join('');\n}",
        "test_cases": [
            {"input": "('hello',)", "expected_output": "'olleh'"},
            {"input": "('Hannah',)", "expected_output": "'hannaH'"}
        ]
    },
    {
        "title": "23. Longest Common Prefix",
        "category": "Strings",
        "difficulty": "Easy",
        "description": "Write a function to find the longest common prefix string amongst an array of strings.",
        "language": "python",
        "initial_code": "def longest_common_prefix(strs):\n    # Write solution here\n    pass",
        "solution_code": "def longest_common_prefix(strs):\n    if not strs: return ''\n    prefix = strs[0]\n    for s in strs[1:]:\n        while not s.startswith(prefix):\n            prefix = prefix[:-1]\n            if not prefix: return ''\n    return prefix",
        "test_cases": [
            {"input": "(['flower', 'flow', 'flight'],)", "expected_output": "'fl'"},
            {"input": "(['dog', 'racecar', 'car'],)", "expected_output": "''"}
        ]
    },
    {
        "title": "24. Roman to Integer",
        "category": "Strings",
        "difficulty": "Easy",
        "description": "Given a roman numeral `s`, convert it to an integer.",
        "language": "python",
        "initial_code": "def roman_to_int(s):\n    # Write solution here\n    pass",
        "solution_code": "def roman_to_int(s):\n    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\n    res = 0\n    for i in range(len(s)):\n        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:\n            res -= roman[s[i]]\n        else:\n            res += roman[s[i]]\n    return res",
        "test_cases": [
            {"input": "('III',)", "expected_output": "3"},
            {"input": "('LVIII',)", "expected_output": "58"},
            {"input": "('MCMXCIV',)", "expected_output": "1994"}
        ]
    },
    {
        "title": "25. First Unique Character in a String",
        "category": "Strings",
        "difficulty": "Easy",
        "description": "Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.",
        "language": "python",
        "initial_code": "def first_uniq_char(s):\n    # Write solution here\n    pass",
        "solution_code": "from collections import Counter\ndef first_uniq_char(s):\n    count = Counter(s)\n    for idx, ch in enumerate(s):\n        if count[ch] == 1: return idx\n    return -1",
        "test_cases": [
            {"input": "('leetcode',)", "expected_output": "0"},
            {"input": "('loveleetcode',)", "expected_output": "2"},
            {"input": "('aabb',)", "expected_output": "-1"}
        ]
    },
    {
        "title": "26. String Compression",
        "category": "Strings",
        "difficulty": "Medium",
        "description": "Given an array of characters `chars`, compress it in-place by replacing consecutive repeating characters with count.",
        "language": "python",
        "initial_code": "def compress(chars):\n    # Write solution here\n    pass",
        "solution_code": "def compress(chars):\n    res = ''\n    i = 0\n    while i < len(chars):\n        ch = chars[i]\n        count = 0\n        while i < len(chars) and chars[i] == ch:\n            count += 1\n            i += 1\n        res += ch + (str(count) if count > 1 else '')\n    return res",
        "test_cases": [
            {"input": "(['a', 'a', 'b', 'b', 'c', 'c', 'c'],)", "expected_output": "'a2b2c3'"}
        ]
    },
    {
        "title": "27. Isomorphic Strings",
        "category": "Strings",
        "difficulty": "Easy",
        "description": "Given two strings `s` and `t`, determine if they are isomorphic (characters in s can be replaced to get t).",
        "language": "python",
        "initial_code": "def is_isomorphic(s, t):\n    # Write solution here\n    pass",
        "solution_code": "def is_isomorphic(s, t):\n    return [s.find(i) for i in s] == [t.find(j) for j in t]",
        "test_cases": [
            {"input": "('egg', 'add')", "expected_output": "True"},
            {"input": "('foo', 'bar')", "expected_output": "False"}
        ]
    },
    {
        "title": "28. Simplify Path (Unix Stack)",
        "category": "Stack & Strings",
        "difficulty": "Medium",
        "description": "Given a Unix-style absolute path for a file, simplify it by evaluating '.' and '..' paths.",
        "language": "python",
        "initial_code": "def simplify_path(path):\n    # Write solution here\n    pass",
        "solution_code": "def simplify_path(path):\n    stack = []\n    for part in path.split('/'):\n        if part == '..':\n            if stack: stack.pop()\n        elif part and part != '.':\n            stack.append(part)\n    return '/' + '/'.join(stack)",
        "test_cases": [
            {"input": "('/home/',)", "expected_output": "'/home'"},
            {"input": "('/../',)", "expected_output": "'/'"},
            {"input": "('/home//foo/',)", "expected_output": "'/home/foo'"}
        ]
    },
    {
        "title": "29. Min Stack",
        "category": "Stack",
        "difficulty": "Medium",
        "description": "Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant $O(1)$ time.",
        "language": "python",
        "initial_code": "def get_min_element(stack_ops):\n    # Write solution here\n    pass",
        "solution_code": "def get_min_element(stack_ops):\n    stack = []\n    min_stack = []\n    for val in stack_ops:\n        stack.append(val)\n        if not min_stack or val <= min_stack[-1]:\n            min_stack.append(val)\n    return min_stack[-1] if min_stack else None",
        "test_cases": [
            {"input": "([-2, 0, -3],)", "expected_output": "-3"}
        ]
    },
    {
        "title": "30. Evaluate Reverse Polish Notation",
        "category": "Stack",
        "difficulty": "Medium",
        "description": "Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).",
        "language": "python",
        "initial_code": "def eval_rpn(tokens):\n    # Write solution here\n    pass",
        "solution_code": "def eval_rpn(tokens):\n    stack = []\n    for t in tokens:\n        if t not in '+-*/':\n            stack.append(int(t))\n        else:\n            b, a = stack.pop(), stack.pop()\n            if t == '+': stack.append(a + b)\n            elif t == '-': stack.append(a - b)\n            elif t == '*': stack.append(a * b)\n            elif t == '/': stack.append(int(a / b))\n    return stack[0]",
        "test_cases": [
            {"input": "(['2', '1', '+', '3', '*'],)", "expected_output": "9"},
            {"input": "(['4', '13', '5', '/', '+'],)", "expected_output": "6"}
        ]
    },

    # --- ALGORITHMS & RECURSION (31-40) ---
    {
        "title": "31. Fibonacci Number",
        "category": "Algorithms & Recursion",
        "difficulty": "Easy",
        "description": "Calculate the n-th Fibonacci number where F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2).",
        "language": "python",
        "initial_code": "def fib(n):\n    # Write solution here\n    pass",
        "solution_code": "def fib(n):\n    if n <= 1: return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b",
        "test_cases": [
            {"input": "(2,)", "expected_output": "1"},
            {"input": "(4,)", "expected_output": "3"},
            {"input": "(10,)", "expected_output": "55"}
        ]
    },
    {
        "title": "32. Climbing Stairs (Dynamic Programming)",
        "category": "Algorithms & Recursion",
        "difficulty": "Easy",
        "description": "You are climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?",
        "language": "python",
        "initial_code": "def climb_stairs(n):\n    # Write solution here\n    pass",
        "solution_code": "def climb_stairs(n):\n    if n <= 2: return n\n    one, two = 1, 2\n    for _ in range(3, n + 1):\n        one, two = two, one + two\n    return two",
        "test_cases": [
            {"input": "(2,)", "expected_output": "2"},
            {"input": "(3,)", "expected_output": "3"},
            {"input": "(5,)", "expected_output": "8"}
        ]
    },
    {
        "title": "33. Maximum Subarray (Kadane's Algorithm)",
        "category": "Algorithms & Recursion",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, find the subarray with the largest sum and return its sum.",
        "language": "python",
        "initial_code": "def max_sub_array(nums):\n    # Write solution here\n    pass",
        "solution_code": "def max_sub_array(nums):\n    max_sum = cur_sum = nums[0]\n    for n in nums[1:]:\n        cur_sum = max(n, cur_sum + n)\n        max_sum = max(max_sum, cur_sum)\n    return max_sum",
        "test_cases": [
            {"input": "([-2, 1, -3, 4, -1, 2, 1, -5, 4],)", "expected_output": "6"},
            {"input": "([1],)", "expected_output": "1"}
        ]
    },
    {
        "title": "34. Binary Search",
        "category": "Algorithms",
        "difficulty": "Easy",
        "description": "Given a sorted array `nums` of integers and a target value, return the index of target if found in O(log n) time, otherwise return -1.",
        "language": "python",
        "initial_code": "def search(nums, target):\n    # Write solution here\n    pass",
        "solution_code": "def search(nums, target):\n    l, r = 0, len(nums) - 1\n    while l <= r:\n        mid = (l + r) // 2\n        if nums[mid] == target: return mid\n        elif nums[mid] < target: l = mid + 1\n        else: r = mid - 1\n    return -1",
        "test_cases": [
            {"input": "([-1, 0, 3, 5, 9, 12], 9)", "expected_output": "4"},
            {"input": "([-1, 0, 3, 5, 9, 12], 2)", "expected_output": "-1"}
        ]
    },
    {
        "title": "35. Coin Change (DP)",
        "category": "Algorithms & DP",
        "difficulty": "Medium",
        "description": "Given an array `coins` representing coin denominations and an integer `amount`, return the fewest number of coins needed to make up that amount.",
        "language": "python",
        "initial_code": "def coin_change(coins, amount):\n    # Write solution here\n    pass",
        "solution_code": "def coin_change(coins, amount):\n    dp = [float('inf')] * (amount + 1)\n    dp[0] = 0\n    for a in range(1, amount + 1):\n        for c in coins:\n            if a - c >= 0:\n                dp[a] = min(dp[a], 1 + dp[a - c])\n    return dp[amount] if dp[amount] != float('inf') else -1",
        "test_cases": [
            {"input": "([1, 2, 5], 11)", "expected_output": "3"},
            {"input": "([2], 3)", "expected_output": "-1"}
        ]
    },
    {
        "title": "36. House Robber (DP)",
        "category": "Algorithms & DP",
        "difficulty": "Medium",
        "description": "Given an integer array `nums` representing the amount of money in each house, return maximum money you can rob tonight without robbing adjacent houses.",
        "language": "python",
        "initial_code": "def rob(nums):\n    # Write solution here\n    pass",
        "solution_code": "def rob(nums):\n    rob1, rob2 = 0, 0\n    for n in nums:\n        temp = max(n + rob1, rob2)\n        rob1 = rob2\n        rob2 = temp\n    return rob2",
        "test_cases": [
            {"input": "([1, 2, 3, 1],)", "expected_output": "4"},
            {"input": "([2, 7, 9, 3, 1],)", "expected_output": "12"}
        ]
    },
    {
        "title": "37. Longest Increasing Subsequence",
        "category": "Algorithms & DP",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, return the length of the longest strictly increasing subsequence.",
        "language": "python",
        "initial_code": "def length_of_lis(nums):\n    # Write solution here\n    pass",
        "solution_code": "def length_of_lis(nums):\n    if not nums: return 0\n    LIS = [1] * len(nums)\n    for i in range(len(nums) - 1, -1, -1):\n        for j in range(i + 1, len(nums)):\n            if nums[i] < nums[j]:\n                LIS[i] = max(LIS[i], 1 + LIS[j])\n    return max(LIS)",
        "test_cases": [
            {"input": "([10, 9, 2, 5, 3, 7, 101, 18],)", "expected_output": "4"},
            {"input": "([0, 1, 0, 3, 2, 3],)", "expected_output": "4"}
        ]
    },
    {
        "title": "38. Flatten Nested Array",
        "category": "JavaScript Manipulation",
        "difficulty": "Easy",
        "description": "Write a JS function `flattenArray(arr)` that recursively flattens a deeply nested array of elements into a single-level array.",
        "language": "javascript",
        "initial_code": "function flattenArray(arr) {\n    // Write solution here\n}",
        "solution_code": "function flattenArray(arr) {\n    return arr.flat(Infinity);\n}",
        "test_cases": [
            {"input": "([1, [2, [3, [4]], 5]],)", "expected_output": "[1, 2, 3, 4, 5]"}
        ]
    },
    {
        "title": "39. Find Peak Element",
        "category": "Algorithms",
        "difficulty": "Medium",
        "description": "A peak element is an element that is strictly greater than its neighbors. Given an array `nums`, find a peak element and return its index.",
        "language": "python",
        "initial_code": "def find_peak_element(nums):\n    # Write solution here\n    pass",
        "solution_code": "def find_peak_element(nums):\n    l, r = 0, len(nums) - 1\n    while l < r:\n        mid = (l + r) // 2\n        if nums[mid] > nums[mid + 1]: r = mid\n        else: l = mid + 1\n    return l",
        "test_cases": [
            {"input": "([1, 2, 3, 1],)", "expected_output": "2"},
            {"input": "([1, 2, 1, 3, 5, 6, 4],)", "expected_output": "5"}
        ]
    },
    {
        "title": "40. Search a 2D Matrix",
        "category": "Algorithms",
        "difficulty": "Medium",
        "description": "Write an efficient algorithm that searches for a `target` value in an `m x n` integer matrix where rows and columns are sorted.",
        "language": "python",
        "initial_code": "def search_matrix(matrix, target):\n    # Write solution here\n    pass",
        "solution_code": "def search_matrix(matrix, target):\n    if not matrix: return False\n    ROWS, COLS = len(matrix), len(matrix[0])\n    l, r = 0, ROWS * COLS - 1\n    while l <= r:\n        mid = (l + r) // 2\n        val = matrix[mid // COLS][mid % COLS]\n        if val == target: return True\n        elif val < target: l = mid + 1\n        else: r = mid - 1\n    return False",
        "test_cases": [
            {"input": "([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)", "expected_output": "True"},
            {"input": "([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)", "expected_output": "False"}
        ]
    },

    # --- SQL & DATABASE PRACTICE (41-50) ---
    {
        "title": "41. Second Highest Salary",
        "category": "SQL Data Query",
        "difficulty": "Medium",
        "description": "Write a SQL query to find the second highest salary from the Employee table.",
        "language": "sql",
        "initial_code": "-- SQL Query\nSELECT DISTINCT age AS SecondHighest \nFROM users \nORDER BY age DESC \nLIMIT 1 OFFSET 1;",
        "solution_code": "SELECT DISTINCT age FROM users ORDER BY age DESC LIMIT 1 OFFSET 1;",
        "test_cases": [
            {"input": "SELECT DISTINCT age FROM users ORDER BY age DESC LIMIT 1 OFFSET 1;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "42. Duplicate Emails",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to report all duplicate emails in a Person table.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT name FROM users GROUP BY name HAVING COUNT(name) > 1;",
        "solution_code": "SELECT name FROM users GROUP BY name HAVING COUNT(name) > 1;",
        "test_cases": [
            {"input": "SELECT name FROM users GROUP BY name HAVING COUNT(name) > 1;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "43. High Earners Query",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to find all users older than 28 years old.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT * FROM users WHERE age > 28;",
        "solution_code": "SELECT * FROM users WHERE age > 28;",
        "test_cases": [
            {"input": "SELECT * FROM users WHERE age > 28;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "44. Count Total Users",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to count the total number of users in the system.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT COUNT(*) FROM users;",
        "solution_code": "SELECT COUNT(*) FROM users;",
        "test_cases": [
            {"input": "SELECT COUNT(*) FROM users;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "45. Average Age of Users",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to find the average age of all users.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT AVG(age) FROM users;",
        "solution_code": "SELECT AVG(age) FROM users;",
        "test_cases": [
            {"input": "SELECT AVG(age) FROM users;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "46. Youngest User Query",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to find the minimum age among all users.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT MIN(age) FROM users;",
        "solution_code": "SELECT MIN(age) FROM users;",
        "test_cases": [
            {"input": "SELECT MIN(age) FROM users;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "47. Oldest User Query",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to find the maximum age among all users.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT MAX(age) FROM users;",
        "solution_code": "SELECT MAX(age) FROM users;",
        "test_cases": [
            {"input": "SELECT MAX(age) FROM users;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "48. Order Users by Name",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to list all users ordered alphabetically by name.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT * FROM users ORDER BY name ASC;",
        "solution_code": "SELECT * FROM users ORDER BY name ASC;",
        "test_cases": [
            {"input": "SELECT * FROM users ORDER BY name ASC;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "49. Select Specific User Columns",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to select only the `id` and `name` columns of all users.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT id, name FROM users;",
        "solution_code": "SELECT id, name FROM users;",
        "test_cases": [
            {"input": "SELECT id, name FROM users;", "expected_output": "Query Results Returned"}
        ]
    },
    {
        "title": "50. Filter Users by Name Pattern",
        "category": "SQL Data Query",
        "difficulty": "Easy",
        "description": "Write a SQL query to find all users whose name starts with 'A'.",
        "language": "sql",
        "initial_code": "-- Write your SQL query here\nSELECT * FROM users WHERE name LIKE 'A%';",
        "solution_code": "SELECT * FROM users WHERE name LIKE 'A%';",
        "test_cases": [
            {"input": "SELECT * FROM users WHERE name LIKE 'A%';", "expected_output": "Query Results Returned"}
        ]
    }
]
