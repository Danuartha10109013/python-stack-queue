# Percobaan 3: Membalikkan Kata/Kalimat (Stack) 
def reverse_sentence (sentence): 
    stack = [] 
    reversed_sentence = ""
    for word in sentence.split(): 
        stack.append(word) 
    while len(stack) > 0: 
        reversed_sentence += stack.pop() + " " 
    return reversed_sentence.strip() 
sentence = "Selamat pagi, bagaimana kabar Anda?" 
print(reverse_sentence(sentence)) 