from playwright.sync_api import sync_playwright

MY_CODE = "2164745"


def get_group_info(url):

    result = {
        "direction": "МТУСИ",
        "my": None
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url, wait_until="networkidle")

        html = page.content()

        print("CODE:", MY_CODE in html)

        rows = page.locator("tr").all()

        for row in rows:
            text = row.inner_text()

            if MY_CODE in text:
                cols = row.locator("td").all_inner_texts()

                print("НАЙДЕНА:", cols)

                result["my"] = {
                    "place": cols[0],
                    "code": cols[1],
                    "sum": cols[3],
                    "priority": cols[-1]
                }

                break

        browser.close()

    return result
