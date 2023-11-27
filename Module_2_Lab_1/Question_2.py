class CustomStack:
    """
    class implementing a text editor functionality using a stack of operations.
    """
    def __init__(self):
        """Initializes the CustomStack class with an empty text and an empty operations stack."""
        self.text = ""          # Represents the text
        self.operations = []    # Stack to keep track of operations for undo

    def insert(self, value):
        """Inserts a string of characters at the current cursor position in the text."""
        self.text += value
        self.operations.append((1, value))  # Pushes the insert operation for potential undo

    def deleteChars(self, value):
        """Deletes the last specified characters from the text starting from the current cursor position."""
        deletedChars = self.text[-value:]
        self.text = self.text[:-value]
        self.operations.append((2, deletedChars))  # Pushes the delete operation for potential undo

    def getChar(self, index):
        """Retrieves the character at a specific index from the text and displays it."""
        result = self.text[index - 1]
        print(result)
        self.operations.append((3, result))  # Pushes the getChar operation for potential undo
        return result

    def undo(self):
        """Reverts the last executed command on the text."""
        if self.operations:
            operation = self.operations.pop()
            if operation[0] == 1:
                self.text = self.text[:-len(operation[1])]
            elif operation[0] == 2:
                self.text += operation[1]
            elif operation[0] == 3:
                pass


# Main
editor = CustomStack()
input_str = input()
commands = input_str.split(",")
for command in commands:
    command, value = command.split()
    if command == "1":
        editor.insert(value)
    elif command == "3":
        intValue = int(value)
        editor.getChar(intValue)
    elif command == "2":
        intValue = int(value)
        editor.deleteChars(intValue)
    elif command == "4":
        editor.undo()
                                                                                                                            