def anagram(word):
    if len(word) == 1:
        return [word]
    else:
        results = []
        subanagram = anagram(word[1:])
        for gram in subanagram:
            for i in range(len(gram) + 1):
                results.append(gram[:i] + word[0] + gram[i:])

    return results



print(anagram('abc'))
print(len(anagram('ibrah')))