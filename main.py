def get_group_info(group_id):
    r = requests.get(
        "https://abitrating.rea.ru/rest/v1/competitive_groups",
        headers=headers,
        params={
            "select": "*",
            "id": f"eq.{group_id}"
        },
        timeout=30
    )

    r.raise_for_status()

    data = r.json()

    if data:
        return data[0]

    return None
