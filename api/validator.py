def validate_data(request) -> dict | bool:
    total = request.json.get("total", "")
    used = request.json.get("used", "")
    used_percentage = request.json.get("used_percentage", "")
    free = request.json.get("free", "")
    shared = request.json.get("shared", "")
    cache = request.json.get("cache", "")

    if not all((total, used, used_percentage, free, shared, cache)):
        return False

    return True
