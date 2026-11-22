text=input("Enter a sentence:") or "I love Learning python"

print("Length=",len(text))
print("Charecters in the given text:")

for ch in text:
    print(ch, end=",")
    