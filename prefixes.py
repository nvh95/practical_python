def all_prefixes(prefix):
    prefixes = set()
    for i in range(1, len(prefix)+1):
        prefixes.add(prefix[0:i])
    return prefixes
# print all_prefixes('hung')