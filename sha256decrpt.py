import hashlib
target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddf56d4c77c9cc31757"  # Hash of "password"

dictionary = ["123456", "password", "hello", "qwerty", "letmein"]


for word in dictionary:
    # Hash the word
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    
    # Compare it to the target hash
    if hashed_word == target_hash:
        print(f"Match found! The original word is: {word}")
        break
else:
    print("No match found.")
