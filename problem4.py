def make_beautiful_string(s):
    ugly_substrings = ["pie", "map"]
    result = ""
    i = 0
    while i < len(s):
        if i <= len(s) - 3 and s[i:i+3] in ugly_substrings:
            # Skip the characters causing the ugliness
            i += 3
        else:
            result += s[i]
            i += 1
    return result

