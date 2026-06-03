from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 配置 Chrome 选项，降低被检测为自动化工具的风险
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 初始化浏览器驱动
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# 隐藏 webdriver 属性
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

try:
    # 直接导航到百度搜索结果页（绕过首页交互和人机验证）
    keyword = "Python RPA"
    search_url = f"https://www.baidu.com/s?wd={keyword}"
    driver.get(search_url)
    print(f"已搜索关键词：{keyword}")
    time.sleep(2)

    # 等待搜索结果正文出现
    results = []
    for sel in ["h3 a", ".result h3 a", ".t a", ".c-title a"]:
        els = driver.find_elements(By.CSS_SELECTOR, sel)
        if any(e.text.strip() for e in els):
            results = [e for e in els if e.text.strip()]
            break

    print("前5条搜索结果标题如下：")
    for i, result in enumerate(results[:5], 1):
        print(f"{i}. {result.text}")

finally:
    time.sleep(3)
    driver.quit()