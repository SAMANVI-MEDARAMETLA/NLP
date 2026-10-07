#Experiment 4: Basic Regular Expression Operations

import re

patterns = {
    "a*": ["", "a", "aaa", "b"],
    "a+": ["a", "aaa", "b"],
    "a?": ["", "a", "aa"],
    "[abc]": ["a", "b", "c", "d"],
    "[^abc]": ["d", "x", "a"],
    "^Hello": ["Hello", "Hello World", "Hi"],
    "World$": ["World", "Hello World", "Hello"]
}

for pattern, strings in patterns.items():
    print("\nPattern:", pattern)
    for s in strings:
        print(s, "->", "Yes" if re.fullmatch(pattern, s) else "No")
