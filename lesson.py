import requests
import time
import threading
import json

urls = [
    "https://dummyjson.com/users",
    "https://dummyjson.com/products",
    "https://dummyjson.com/posts",
    "https://dummyjson.com/carts",
    "https://dummyjson.com/comments",
    "https://dummyjson.com/quotes",
    "https://dummyjson.com/todos",
    "https://dummyjson.com/recipes",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
]


def download(url, index, filename=None):
    print(f"[{index}] Yuklanmoqda: {url}")
    response = requests.get(url)
    data = response.json()

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"[{index}] Tugadi: {len(response.content)} bayt")


threads = []

start_time = time.time()

for index, url in enumerate(urls):
    thraed = threading.Thread(target=download, args=(url, index, f"data_{index}.json"))
    threads.append(thraed)
    thraed.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"\n⏱️ Umumiy vaqt: {end_time - start_time:.2f} soniya")