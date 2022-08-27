def new_code(prefix, code_list):
    max_code = 0
    for i in code_list:
        code_number = int("".join([j for j in [*i] if j.isnumeric()]))
        if max_code < code_number:
            max_code = code_number

    return f"{prefix}{max_code + 1}"
