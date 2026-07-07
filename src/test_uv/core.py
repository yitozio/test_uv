def greet(name: str = "1") -> str:
    """一个简单的问候函数"""
    return f"Hello, {name}!"


def add_numbers(a: int = 1, b: int = 2) -> int:
    """两数相加"""
    return a + b
