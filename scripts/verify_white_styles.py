import sys, asyncio
sys.stdout.reconfigure(encoding="utf-8")
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://127.0.0.1:8766/?refresh=true#/")
        await page.wait_for_timeout(2500)
        await page.screenshot(path="my_tw_coverage_clean_white_verify.png")

        styles = await page.evaluate('''() => {
            return {
                bodyBg: getComputedStyle(document.body).backgroundColor,
                bodyColor: getComputedStyle(document.body).color,
                navBg: getComputedStyle(document.querySelector('.app-nav')).backgroundColor,
                sidebarBg: getComputedStyle(document.querySelector('.sidebar')).backgroundColor,
                h1Color: document.querySelector('h1') ? getComputedStyle(document.querySelector('h1')).color : null,
                brandDisplay: document.querySelector('.tw-nav-brand') ? getComputedStyle(document.querySelector('.tw-nav-brand')).display : null
            };
        }''')
        print("Computed Styles:", styles)
        await browser.close()
        print("Captured my_tw_coverage_clean_white_verify.png successfully!")

asyncio.run(run())
