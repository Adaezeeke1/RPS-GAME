def get_valid_input(prompt, valid_choices, enum_type=None):
    while True:
        try:
            user_input = input(prompt)
            if enum_type:
                user_choice = enum_type(int(user_input))
            else:
                user_choice = int(user_input)

            if user_choice not in valid_choices:
                raise ValueError(f"Invalid input. Please enter one of {list(valid_choices)}.")
            return user_choice

        except ValueError:
            print(f"Invalid input. Please enter a valid number.")
