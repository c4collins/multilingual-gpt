def ask_user(question: str) -> str:
    return input(f"{question} ")


def ask_user_boolean(
    question: str, true_value: str = "Y", false_value: str = "n"
) -> bool:
    if not question.endswith("?"):
        question = f"{question}?"
    return (
        ask_user(f"{question} ({true_value}/{false_value})") or true_value
    ) == true_value
