import time as t
import random as r


def FenYiCi(Num: int):
    Num -= 1  # 拿出天、人、地
    a = r.randint(1, Num)
    u1 = a % 4
    if u1 == 0:
        u1 += 4
    u2 = (Num - a) % 4
    if u2 == 0:
        u2 += 4
    Num -= u1 + u2
    return Num


def SuanYiYao():
    r.seed(t.perf_counter())

    YarrowNum = 50
    YarrowNum -= 1  # 分出太极

    for c in range(3):  # 进行三次分
        YarrowNum = FenYiCi(YarrowNum)

    f = int(YarrowNum / 4)
    if f == 9:
        i = "--- O    - -"
        id = 1
    elif f == 8:
        i = "- -      - -"
        id = 2
    elif f == 7:
        i = "---      ---"
        id = 3
    elif f == 6:
        i = "- - X    ---"
        id = 4

    return [i, id]


def SuanYiGua():
    div = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]
    for i in range(6):
        div[i] = SuanYiYao()
    for i in div[::-1]:
        print(i)


if __name__ == "__main__":
    import webbrowser
    import os

    print('====== 蓍 草 占 筮 ======')
    print('>> 输入“1”   -算卦')
    print('>> 输入“2”   -六十四卦象')
    print('>> 输入“3”   -朱熹解卦方法')
    print('>> 输入“4”   -退出 ')
    print('=========================')

    flag = 1
    while flag:

        key = input(">>")

        if key == "1":

            print()
            print("===================")
            print("[ 本卦     之卦   ]")
            SuanYiGua()
            print("===================")
            print()

        elif key == "2":

            html_path = os.path.join(os.getcwd(), "解卦.html")  # 使用os.getcwd()获取当前工作目录的路径
            webbrowser.open_new_tab(html_path)

        elif key == "3":

         print('''①有一爻变，用本卦变爻爻辞占断；
②有两爻变，用本卦两变爻爻辞判断，而以上爻爻辞为主；
③有三爻变，以本卦和之卦的《彖辞》判断。以本卦为贞（体），变卦为悔（用）。前十卦主贞，后十卦主悔；
④有四爻变，以之卦的两个不变爻为准进行判断，而以下爻为主；
⑤有五爻变，看之卦不变的一爻；
⑥六爻皆变，乾变坤看乾卦用九；坤变乾看坤卦用六。其余各卦看之卦《彖辞》；
⑦六爻皆不变，看本卦《彖辞》，以内卦为贞，外卦为悔。

        ''')

        elif key == "4":

            flag = 0

        else:
            print("输入错误")



    # ①有一爻变，用本卦变爻爻辞占断；
    # ②有两爻变，用本卦两变爻爻辞判断，而以上爻爻辞为主；
    # ③有三爻变，以本卦和之卦的《彖辞》判断。以本卦为贞（体），变卦为悔（用）。前十卦主贞，后十卦主悔；
    # ④有四爻变，以之卦的两个不变爻为准进行判断，而以下爻为主；
    # ⑤有五爻变，看之卦不变的一爻；
    # ⑥六爻皆变，乾变坤看乾卦用九；坤变乾看坤卦用六。其余各卦看之卦《彖辞》；
    # ⑦六爻皆不变，看本卦《彖辞》，以内卦为贞，外卦为悔。

    # 上卦称为外卦，下卦称为内卦。在卦象中，内卦代表着卦象的本质和基础，而外卦则代表着卦象的变化和发展。
    # 在卜筮中，如果问卦者所卜之事与天文、气象、自然界的变化相关，则主贞；
    # 如果所卜之事与人类社会、人际关系、政治、经济等方面的变化相关，则主悔。

    # 乾满 坤断 离中空 坎中满 震下连 巽下断 艮上连 兑上断

    # 上九：上六
    # 九五：六五
    # 九四：六四
    # 九三：六三
    # 九二：六二
    # 初九：初六
