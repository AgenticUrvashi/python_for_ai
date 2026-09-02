import time
import functools
from dataclasses import dataclass
from typing import Callable, Iterator


@dataclass
class Message:
    role: str
    content: str


def timer(func: Callable) -> Callable:
    """Decorator: print how long a function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[{func.__name__} took {time.time() - start:.3f}s]")
        return result
    return wrapper


@timer
def build_messages(texts: list[str]) -> list[Message]:
    """Turn raw strings into typed Message objects."""
    return [Message(role="user", content=t) for t in texts]


def stream_words(message: Message) -> Iterator[str]:
    """Stream a message's content word-by-word (like an LLM)."""
    for word in message.content.split():
        yield word
        time.sleep(0.05)


# --- demo ---
messages = build_messages(["Hello world", "How are you"])
print(messages)             # [Message(role='user', content='Hello world'), ...]

print("Streaming first message: ", end="")
for token in stream_words(messages[0]):
    print(token, end=" ", flush=True)
print()