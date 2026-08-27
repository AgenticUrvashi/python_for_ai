import time

def stream_responce(text):
    for word in text.split():
        time.sleep(0.05)
        yield word

with open("week11_advance_python_for_ai/code/history_of_india_hw.txt","r") as f:
    data = f.read()

gen_streamer = stream_responce(data)

for word in gen_streamer:
    print(word,end=" ",flush=True)
