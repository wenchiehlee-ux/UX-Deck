import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://127.0.0.1:8766/#/")
        await page.wait_for_timeout(2000)

        data = await page.evaluate('''() => {
            const body = document.body;
            const nav = document.querySelector('.app-nav');
            const sidebar = document.querySelector('.sidebar');
            const h2 = document.querySelector('h2');
            const content = document.querySelector('.content');
            const link = document.querySelector('.markdown-section a');
            return {
                bodyBg: getComputedStyle(body).backgroundColor,
                bodyColor: getComputedStyle(body).color,
                navBg: nav ? getComputedStyle(nav).backgroundColor : null,
                sidebarBg: sidebar ? getComputedStyle(sidebar).backgroundColor : null,
                h2Color: h2 ? getComputedStyle(h2).color : null,
                contentBg: content ? getComputedStyle(content).backgroundColor : null,
                linkCol: link ? getComputedStyle(link).color : null,
                fontFamily: getComputedStyle(body).fontFamily
            };
        }''')
        print(data)
        await browser.close()

asyncio.run(run())
