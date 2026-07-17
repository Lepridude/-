from playwright.sync_api import sync_playwright

MY_CODE = "2164745"


def get_group_info(url):

    result = {
        "direction": "МТУСИ",
        "my": None
    }


    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )


        page.locator(f"td:has-text('{MY_CODE}')").first.wait_for(timeout=30000)


        rows = page.locator("tr")

        count = rows.count()

        print("TR COUNT:", count)


        for i in range(count):

            row = rows.nth(i)

            text = row.inner_text()


            if MY_CODE in text:

                cols = row.locator("td").all_inner_texts()

                print("MTUCI FOUND:", cols)


                result["my"] = {
                    "place": cols[0],
                    "id": cols[7],
                    "scores": cols[3],
                    "priority": cols[9]
                }


                break


        browser.close()


    return result
