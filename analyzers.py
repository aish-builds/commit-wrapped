def calculate_language_breakdown(repos):
    total = len(repos)
    if not repos:
        return {}
    language_dict = {}
    for repo in repos:
        if repo["language"] not in language_dict:
            language_dict[repo["language"]] = 1
        else:
            language_dict[repo["language"]] += 1
    for lang in language_dict:
        percent = (language_dict[lang]/total) * 100
        language_dict[lang] = round(percent, 1)
    sorted_language_dict = dict(sorted(language_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_language_dict