import argparse
from multiprocessing import Pool
from selenium import webdriver


def watch_article(num, username, password):
    """
    :param num: articles number (start from 1)
    :param username: your github username
    :param password: your github password
    :return: a list contains [article.text, des.text, lang.text, star.text, branch.text]
    """
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    with webdriver.Chrome(executable_path="./chromedriver", options=option) as driver:
        # Login
        driver.get("https://github.com/login")
        driver.find_element_by_name("login").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("commit").click()

        # Go to trending
        driver.get("https://github.com/trending")

        # Article info
        article = driver.find_element_by_xpath("//article[%d]/h1/a" % num)
        des = driver.find_element_by_xpath("//article[%d]/p" % num)
        lang = driver.find_element_by_xpath("//article[%d]/div[2]/span[1]/span[2]" % num)
        star = driver.find_element_by_xpath("//article[%d]/div[2]/a[1]" % num)
        branch = driver.find_element_by_xpath("//article[%d]/div[2]/a[2]" % num)

        # Store result
        res = [article.text, des.text, lang.text, star.text, branch.text]

        # Find all articles
        article.click()

        # Find watch button
        watch_button = driver.find_element_by_xpath("//form[@action='/notifications/subscribe']")
        watch_button.click()

        # Find watching in drop-down menu
        menu_button = driver.find_element_by_xpath(
            "//form[@action='/notifications/subscribe']//button[@value='subscribed']")
        menu_button.click()

        return res


result_list = []


def log_result(x):
    result_list.append(x)


def main_func(num, username, password):
    p = Pool(4)
    for i in range(1, num+1):
        p.apply_async(watch_article, args=(i, username, password), callback=log_result)
    print("Waiting for all processes...")
    p.close()
    p.join()
    print("Done!")
    print("----------------------------Result--------------------------------")

    for result in result_list:
        print("Article: ", result[0])
        print("Description: ", result[1])
        print("Programming Language: ", result[2])
        print("Stars: ", result[3])
        print("Branches: %s\n" % result[4])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trending-get Tool")
    parser.add_argument("username", action="store")
    parser.add_argument("password", action="store")
    arg = parser.parse_args()

    main_func(num=10, username=arg.username, password=arg.password)
