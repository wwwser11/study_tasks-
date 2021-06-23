def number_of_unique_letters(some_string):
    return len({
        x.lower() for x in some_string
        if x.isalpha()
    })

print(number_of_unique_letters("AaBbCcDd"))
print(number_of_unique_letters("\\(O_o)/"))