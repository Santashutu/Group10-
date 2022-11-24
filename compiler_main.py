print(f'// To exit, press "."')

brackets_list = []
outcasts_list = []

brackets_dict = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

# an infinite loop
i = 1
while True:

    code = input(f'{i}:\t')

    # looping individual characters for brackets
    for char in code:

        if '{' == char or '(' == char or '[' == char or '<' == char:

            if len(brackets_list) > 0:
                if brackets_list[-1] == '<' and char != '>':
                    outcasts_list.append(char)

            brackets_list.append(char)

        elif '}' == char or ')' == char or ']' == char or '>' == char:
            if len(brackets_list) > 0:
                if brackets_dict[brackets_list[-1]] == char:
                    brackets_list.pop()
                else:
                    outcasts_list.append(char)
            else:
                outcasts_list.append(char)

    # exit
    if code == '.':
        break

    i += 1

if len(brackets_list) == 0 and len(outcasts_list) == 0:
    print("Brackets are nested correctly, now running the program...")

elif len(brackets_list) > 0 or len(outcasts_list) > 0:
    print("Sorry, brackets not nested correctly...")
