def reverse_text(text):
    reverse_list = []
    text_split = text.split()
    for i in range(len(text_split)+1):
        if i == 0:
            pass
        else:
            reverse_list.append(text_split[-i])
    return " ".join(reverse_list)
        
         

if __name__ == "__main__":
    text = input('Write a text: ')
    print(reverse_text(text))