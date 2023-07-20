# test_web_tools.py

import time
import web

# Example URLs for testing
url1 = "https://www.example.com"
url2 = "https://www.google.com"
url3 = "https://www.github.com"

def test_get_page():
    # Fetch the same URL multiple times to check caching behavior
    for i in range(5):
        content = web.get_page(url1)
        print(f"Access {i + 1}: {content}")

    # Fetch different URLs to check separate caching
    content2 = web.get_page(url2)
    content3 = web.get_page(url3)

    # Wait for the cache to expire (10 seconds) and fetch the same URL again
    time.sleep(11)
    content1_cached = web.get_page(url1)
    print(f"Cached content: {content1_cached}")

    # Check the number of requests made to the URLs
    request_count_url1 = web.redis_client.get(f'count:{url1}')
    request_count_url2 = web.redis_client.get(f'count:{url2}')
    request_count_url3 = web.redis_client.get(f'count:{url3}')

    print(f"Number of requests to {url1}: {int(request_count_url1)}")
    print(f"Number of requests to {url2}: {int(request_count_url2)}")
    print(f"Number of requests to {url3}: {int(request_count_url3)}")

if __name__ == "__main__":
    test_get_page()
