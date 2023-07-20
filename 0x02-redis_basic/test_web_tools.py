# test_web_tools.py

import time
import web

# Example URLs for testing
url1 = "http://slowwly.robertomurray.co.uk"

def test_get_page():
    # Fetch the same URL multiple times to check caching behavior
    for i in range(5):
        content = web.get_page(url1)
        print(f"Access {i + 1}: {content}")

    # Wait for the cache to expire (10 seconds) and fetch the same URL again
    time.sleep(11)
    content1_cached = web.get_page(url1)
    print(f"Cached content: {content1_cached}")

    # Check the number of requests made to the URLs
    request_count_url1 = web.redis_client.get(f'count:{url1}')

if __name__ == "__main__":
    test_get_page()
