import time
import csv
from langdetect import detect
from DrissionPage import ChromiumPage

content = input('searching keywords：')
start_day = input('time_from(ep:2024-09-07)：')
end_day = input('time_to(ep:2024-09-07)：')

delay = 3

def wait_for_load(tab):
    while True:
        cnt = 0
        height = tab.rect.size[1]
        tab.scroll.to_bottom()
        print('collecting comments...')
        while tab.rect.size[1] == height:
            cnt += 1
            time.sleep(0.1)
            if cnt > delay / 0.1:
                return

def get_comments():
    # 获取评论信息
    comment_set = []
    offset_1 = 0
    while True:
        detail_tab.wait.doc_loaded()
        comment_list = detail_tab.s_eles('xpath=//div[@class="css-175oi2r"]/div/div/article/div/div/div[2]/div[2]')
        if comment_list:
            for comment in comment_list:
                try:
                    comment_text = comment.s_ele('xpath=/div[2]//span').text
                    if comment_text in comment_set:
                        continue
                    comment_time = comment.s_ele('xpath=/div[1]//time').attr('datetime')
                    # 判断评论是否为英语
                    if detect(comment_text) == 'en':
                        writer.writerow(('', '', '', '', comment_time, comment_text))
                        comment_set.append(comment_text)
                        print('comment：', comment_time, comment_text)
                except:
                    pass
        if offset_1 > detail_tab.rect.size[1] - 400:
            print('comment_end')
            return

        detail_tab.scroll.up(400)
        offset_1 += 400


page = ChromiumPage()
page.get('https://x.com/home')
first_tab = page.get_tab(1)

first_tab.wait.ele_displayed('xpath=//input[@autocapitalize="sentences"]')

first_tab.ele('xpath=//input[@autocapitalize="sentences"]').input(f'{content} until:{end_day} since:{start_day}\n')

name_list = []
offset = 0
with open('TwitterBlog_LLM_2023-Q4-p3.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('user', 'time', 'location', 'tweets', 'comment_time', 'comment_texts'))
    while True:
        first_tab.wait.doc_loaded()
        div_list = first_tab.s_eles('xpath=//div[@class="css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu"]')
        if div_list:
            for div in div_list:
                name = div.s_ele(
                    'xpath=//div[@class="css-175oi2r r-1awozwy r-18u37iz r-1wbh5a2 r-dnmrzs"]/div[@dir="ltr"][1]/span/span').text
                if name in name_list:
                    continue
                name_list.append(name)
                time_stamp = div.s_ele('xpath=//div[@class="css-175oi2r r-18u37iz r-1q142lx"]/a/time').attr('datetime')
                span = div.s_eles(
                    'xpath=//div[@class="css-175oi2r"]/div[@dir="auto"]/span[@class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"]')
                text = ''.join(span.get.texts())

                if detect(text) == 'en':
                    user_url = div.s_ele('xpath=/div/div/div/div/div/div/div/a').attr('href')
                    user_tab = page.new_tab(user_url)
                    try:
                        loc = user_tab.s_ele(
                            'xpath=//div[@class="css-175oi2r r-3pj75a r-ttdzmv r-1ifxtd0"]//span[@data-testid="UserLocation"]/span/span').text
                    except:
                        loc = None
                    user_tab.close()
                    item = (name, time_stamp, loc, text, '', '')
                    writer.writerow(item)
                    print(item)

                    detail_url = div.s_ele('xpath=/div/div/div/div/div/div[2]/div/div[3]/a').attr('href')
                    detail_tab = page.new_tab(detail_url)

                    wait_for_load(detail_tab)
                    get_comments()
                    detail_tab.close()

            if offset > first_tab.rect.size[1]:
                break

            first_tab.scroll.down(400)
            offset += 400

page.quit()
