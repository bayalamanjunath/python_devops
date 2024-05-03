def replace_word(input_file, old_word, new_word):
    with open(input_file, 'r') as f:
        # print(f)
        content = f.read()
        print(content)
        replace_content = content.replace(old_word, new_word)
        print(replace_content)
    with open(input_file, 'w') as f:
        new_content = f.write(replace_content)
        print(new_content)
replace_word("practice.py", "branchA", "branchB")

