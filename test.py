def log_event(event, cache=[], max_size=1):
    cache.append(event)

    if len(cache) > max_size:
        cache[:] = cache[1:]

    print(cache)


log_event("start")
log_event("finish", max_size=2)