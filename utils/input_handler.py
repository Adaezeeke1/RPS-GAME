def get_valid_input(prompt, valid_choices, enum_type=None):
    while True:
        user_input = input(prompt)

        if enum_type:
            try:
                user_choice = enum_type(int(user_input))
                if user_choice in valid_choices:
                    return user_choice
                else:
                    print(
                        f"Invalid input. Please enter one of {list(valid_choices)}.")
            except (ValueError, KeyError):
                print(f"Invalid input. Please enter a valid number.")
        else:
            if user_input.lower() in valid_choices:
                return user_input.lower()
            else:
                print(f"Invalid input. Please enter one of {valid_choices}.")
