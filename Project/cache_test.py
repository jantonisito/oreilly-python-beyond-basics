from requests_cache import CachedSession
import time
import os

HEADERS = {'User-Agent': 'Mozilla/5.0'}
# session = CachedSession(
#     'test_cache',
#     backend='filesystem',
#     expire_after=3600,         # your preferred expiry
#     cache_control=False,       # this disables obeying Cache-Control from server
#     stale_if_error=True,
#     allowable_codes=(200,),
#     allowable_methods=('GET',)
# )
session = CachedSession(
    'test_cache',
    backend='sqlite',
    # expire_after=60 * 60 * 24 * 30,  # 30 days
    expire_after=60,
    refresh=False,
    allow_expired=False,
    #cache_control=False,
    #stale_if_error=True,
    #allowable_codes=(200,),
    #allowable_methods=('GET',)
)
print(session.cache)
print('Cached URLS:')
print('\n'.join(session.cache.urls()))

resolved_url_cache = {}

def get_url(url):
    response = session.get(url, headers=HEADERS)
    resolved_url = response.url
    # 🔧 Force reading body content so it's cached
    _ = response.text  # or response.content

    print(f"{'[CACHE]' if getattr(response, 'from_cache', False) else '[FETCH]'} {url} → {resolved_url}")
    print(f"Cache key: {session.cache.create_key(response.request)}")
    print(f"Expires: {getattr(response, 'expires', 'N/A')}")
    # print(f"Cached?    {session.cache.has_url(url)}")
    # print(f"Cached file present: {os.path.exists(os.path.join('test_cache', session.cache.create_key(response.request)[:2], session.cache.create_key(response.request) + '.json'))}")

    return response.text

#session.cache.clear()
#print("Cache cleared.")

for i in range(5):
    #url = "https://en.wikipedia.org/wiki/Germany"
    url = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

    resp = get_url(url)
    if i == 0:
        print("Waiting to allow cache write...")
        time.sleep(10)
    else:
        time.sleep(2)
