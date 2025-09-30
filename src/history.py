# src/history.py

class BrowserHistory:
    def __init__(self):
        self._back_stack = []
        self._forward_stack = []
        self._current = "home"

    def current(self):
        return self._current

    def visit(self, url: str):
        # don't store the initial "home" in back history
        if self._current != "home":
            self._back_stack.append(self._current)
        self._current = url
        # visiting clears forward history
        self._forward_stack.clear()

    def back(self):
        if not self._back_stack:
            raise IndexError("No pages in back history")
        # move current to forward stack
        self._forward_stack.append(self._current)
        # pop previous page as current
        self._current = self._back_stack.pop()
        return self._current

    def forward(self):
        if not self._forward_stack:
            raise IndexError("No pages in forward history")
        # don't push "home" into back history
        if self._current != "home":
            self._back_stack.append(self._current)
        self._current = self._forward_stack.pop()
        return self._current
