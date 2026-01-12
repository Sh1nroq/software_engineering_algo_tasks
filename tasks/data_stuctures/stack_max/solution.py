class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> str | None:
        if not self.stack:
            return "error"

        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()

        return None

    def get_max(self) -> int | str | None:
        if not self.stack:
            return "None"
        return self.max_stack[-1]

solution = StackMax