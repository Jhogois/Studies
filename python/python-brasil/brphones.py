from multiprocessing.connection import answer_challenge
import re

class BrPhone:
    def __init__(self, phone) -> None:
        if self.phone_validation(phone):
            self.number = phone
        else:
            raise ValueError("Incorrect number")

    def __str__(self) -> str:
        return self.format_number()

    def phone_validation(self, phone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, phone)
        if answer:
            return True
        else:
            return False

    def format_number(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.number)
        formatted_number = f"+{answer.group(1)} ({answer.group(2)}) {answer.group(3)}-{answer.group(4)}"
        return formatted_number


