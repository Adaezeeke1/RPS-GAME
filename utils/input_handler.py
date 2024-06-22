def get_valid_input(prompt, valid_choices, enum_type=None):
    while True:
        try:
            user_input = input(prompt)
            if enum_type:
                user_choice = enum_type(int(user_input))
            else:
                user_choice = int(user_input)

            if user_choice in valid_choices:
                return user_choice
            else:
                print(
                    f"Invalid input. Please enter one of {list(valid_choices)}.")

                return None

        except ValueError:
            print(f"Invalid input. Please enter a valid number.")
            return None
