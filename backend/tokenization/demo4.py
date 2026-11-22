word = input("Enter a word:") or "python"

print("Word=",word)
print("Length=",len(word))

charecters = list(word)
print("Characters in the given word:", charecters)

pairs = list(zip(charecters, charecters[1:]))
print("Adjacent pairs:", pairs)