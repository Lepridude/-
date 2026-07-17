import pandas as pd
import requests


MY_CODE = "2164745"


def get_group_info(url):

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    r.raise_for_status()

    result = {
        "direction": "МТУСИ",
        "my": None
    }

    tables = pd.read_html(r.text)

    print("ТАБЛИЦ НАЙДЕНО:", len(tables))

    for i, df in enumerate(tables):

        print("ТАБЛИЦА", i)
        print(df.head())

        text = df.to_string()

        if MY_CODE in text:

            print("НАШЕЛ МОЙ КОД")

            row = df[df.astype(str).apply(
                lambda x: x.str.contains(MY_CODE).any(),
                axis=1
            )].iloc[0]


            values = row.tolist()

            print(values)


            result["my"] = {
                "place": values[0],
                "id": MY_CODE,
                "scores": values[3] if len(values) > 3 else "-",
                "priority": values[-1] if len(values) else "-"
            }

            break


    return result
