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


        # ждём пока появятся строки
        page.wait_for_timeout(3000)


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
                    "id": cols[1],
                    "scores": cols[3],
                    "priority": cols[-1]
                }


                break


        browser.close()


    return result
