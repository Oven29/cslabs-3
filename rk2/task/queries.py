def query_one_to_many(browsers, computers):
    return sorted(
        [
            (b.name, b.version, c.name)
            for b in browsers
            for c in computers
            if b.computer_id == c.id
        ],
        key=lambda x: x[0]
    )


def query_computers_with_browser_count(one_to_many):
    result = {}
    for _, _, computer_name in one_to_many:
        result[computer_name] = result.get(computer_name, 0) + 1

    return sorted(result.items(), key=lambda x: x[1])


def query_many_to_many(browsers, computers, browser_computers):
    computer_map = {c.id: c.name for c in computers}
    browser_map = {b.id: b.name for b in browsers}

    pairs = [
        (browser_map[bc.browser_id], computer_map[bc.computer_id])
        for bc in browser_computers
        if bc.browser_id in browser_map and bc.computer_id in computer_map
    ]

    return sorted(
        [(b, c) for b, c in pairs if b.endswith("ов")],
        key=lambda x: x[0]
    )
