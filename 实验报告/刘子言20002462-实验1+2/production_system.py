import tkinter as tk


# 动物识别系统
# 自定义函数，判断有无重复元素
def judge_repeat(value, list=[]):
    for i in range(0, len(list)):
        if list[i] == value:
            return 1
        else:
            if i != len(list) - 1:
                continue
            else:
                return 0


# 自定义函数，对已经整理好的综合数据库rea
# l_list进行最终的结果判断
reasoning_result = []
def judge_last(list):
    for i in list:
        if i == '23':  # 食肉类
            for i in list:
                if i == '12':  # 黄褐色
                    for i in list:
                        if i == '21':  # 哺乳类
                            for i in list:
                                if i == '13':  # 有斑点
                                    reasoning_result.append("黄褐色，有斑点,哺乳类，食肉类->金钱豹\n")
                                    reasoning_result.append("所识别的动物为金钱豹")
                                    return 0
                                elif i == '14':  # 有黑色条纹
                                    reasoning_result.append("黄褐色，有黑色条纹，哺乳类，食肉类->虎\n")
                                    reasoning_result.append("所识别的动物为虎")
                                    return 0
        elif i == '14':  # 有黑色条纹
            for i in list:
                if i == '24':  # 蹄类
                    reasoning_result.append("有黑色条纹，蹄类->斑马\n")
                    reasoning_result.append("所识别的动物为斑马")
                    return 0
        elif i == '24':  # 蹄类
            for i in list:
                if i == '13':  # 有斑点
                    for i in list:
                        if i == '15':  # 长脖
                            for i in list:
                                if i == '16':  # 长腿
                                    reasoning_result.append("有斑点，有黑色条纹，长脖，蹄类->长颈鹿\n")
                                    reasoning_result.append("所识别的动物为长颈鹿")
                                    return 0
        elif i == '20':  # 善飞
            for i in list:
                if i == '22':  # 鸟类
                    reasoning_result.append("善飞，鸟类->信天翁\n")
                    reasoning_result.append("所识别的动物为信天翁")
                    return 0
        elif i == '22':  # 鸟类
            for i in list:
                if i == '4':  # 不会飞
                    for i in list:
                        if i == '15':  # 长脖
                            for i in list:
                                if i == '16':  # 长腿
                                    reasoning_result.append("不会飞，长脖，长腿，鸟类->鸵鸟\n")
                                    reasoning_result.append("所识别的动物为鸵鸟")
                                    return 0

        elif i == '4':  # 不会飞
            for i in list:
                if i == '22':  # 鸟类
                    for i in list:
                        if i == '18':  # 会游泳
                            for i in list:
                                if i == '19':  # 黑白二色
                                    reasoning_result.append("不会飞，会游泳，黑白二色，鸟类->企鹅\n")
                                    reasoning_result.append("所识别的动物企鹅")
                                    return 0
        else:
            if list.index(i) < len(list) - 2:
                continue
            else:
                reasoning_result.append("根据所给条件无法判断为何种动物")
                break


dict_before = {'1': '有毛发', '2': '产奶', '3': '有羽毛', '4': '不会飞', '5': '会下蛋', '6': '吃肉', '7': '有犬齿',
               '8': '有爪', '9': '眼盯前方', '10': '有蹄', '11': '反刍', '12': '黄褐色', '13': '有斑点', '14': '有黑色条纹',
               '15': '长脖', '16': '长腿', '17': '不会飞', '18': '会游泳', '19': '黑白二色', '20': '善飞', '21': '哺乳类',
               '22': '鸟类', '23': '食肉类', '24': '蹄类', '25': '金钱豹', '26': '虎', '27': '长颈鹿', '28': '斑马',
               '29': '鸵鸟', '30': '企鹅', '31': '信天翁', '32': '吃草', '33': '食草类', '34': '杂食类'}
rule = """    
          *************************************************
            1:有毛发
            2:产奶
            3:有羽毛
            4:不会飞
            5:会下蛋
            6:吃肉
            7:有犬齿
            8:有爪
            9:眼盯前方
            10:有蹄
            11:反刍
            12:黄褐色
            13:有斑点
            14:有黑色条纹
            15:长脖
            16:长腿
            17:不会飞
            18:会游泳
            19:黑白二色
            20:善飞
            21：哺乳类
            22:鸟类
            23:食肉类
            24:蹄类
            32:吃草
            33:食草类
            34:杂食类
          ~~~~~~~~~~~~~~~~~~~~~~~~~~
          ****当输入数字0时!表示输入结束****
          ***点击开始按钮，系统开始推理***"""

# 保存、显示、遍历前提条件的函数
list_real = []
def conditionIN():
    # 保存你输入的条件数字
    num_real_all = the_condition_you_choose.get(1.0, tk.END)
    m = 0
    while 1:
        # 循环输入前提条件所对应的字典中的键
        num_real = num_real_all[m]
        num_real_next = num_real_all[m + 1]
        if num_real == '0':
            break
        if num_real != '\n' and num_real_next == '\n':
            list_real.append(num_real)
            m = m + 1
        elif num_real != '\n' and num_real_next != '\n':
            num_real = num_real + num_real_next
            list_real.append(num_real)
            m = m + 2
        else:
            m = m + 1
    print(list_real)

    # 转换并输出前提条件的文字
    condition_real = []
    for i in range(0, len(list_real)):
        condition_real.append(dict_before[list_real[i]])
    the_condition_show.delete(0, tk.END)
    the_condition_show.insert(0, condition_real)

    # 遍历综合数据库list_real中的前提条件
    reasoning_process = []
    for i in list_real:
        if i == '1':
            if judge_repeat('21', list_real) == 0:
                list_real.append('21')
                reasoning_process.append("有毛发->哺乳类\n")
        elif i == '2':
            if judge_repeat('21', list_real) == 0:
                list_real.append('21')
                reasoning_process.append("产奶->哺乳类\n")
        elif i == '3':
            if judge_repeat('22', list_real) == 0:
                list_real.append('22')
                reasoning_process.append("有羽毛->鸟类\n")
        else:
            if list_real.index(i) != len(list_real) - 1:
                continue
            else:
                break
    for i in list_real:
        if i == '4':
            for i in list_real:
                if i == '5':
                    if judge_repeat('22', list_real) == 0:
                        list_real.append('22')
                        reasoning_process.append("不会飞，会下蛋->鸟类\n")
        elif i == '6':
            for i in list_real:
                if i == '21':
                    if judge_repeat('21', list_real) == 0:
                        list_real.append('21')
                        reasoning_process.append("食肉->哺乳类\n")
        elif i == '32':  # 以下为新增的部分
            for i in list_real:
                flag = 1
                for j in list_real:
                    if j == '6':
                        flag = 0
                        break
                if judge_repeat('33', list_real) == 0 and flag:
                    list_real.append('33')
                    reasoning_process.append("食草->食草类\n")
                elif judge_repeat('34', list_real) == 0 and flag == 0:
                    list_real.append('34')
                    reasoning_process.append("食肉，食草->杂食类\n")
        elif i == '7':
            for i in list_real:
                if i == '8':
                    for i in list_real:
                        if i == '9':
                            if judge_repeat('23', list_real) == 0:
                                list_real.append('23')
                                reasoning_process.append("有犬齿,有爪,眼盯前方->食肉类\n")
        elif i == '10':
            for i in list_real:
                if i == '21':
                    if judge_repeat('24', list_real) == 0:
                        list_real.append('24')
                        reasoning_process.append("有蹄，哺乳类->蹄类\n")
        elif i == '11':
            for i in list_real:
                if i == '21':
                    if judge_repeat('24', list_real) == 0:
                        list_real.append('24')
                        reasoning_process.append("反刍，哺乳类->哺乳类\n")

        else:
            if i != len(list_real) - 1:
                continue
            else:
                break
    show_reasoning_process.delete(1.0, tk.END)
    for i in reasoning_process:
        show_reasoning_process.insert(tk.END, i)

    # 结果判断
    judge_last(list_real)
    show_reasoning_result.delete(1.0, tk.END)
    for i in reasoning_result:
        show_reasoning_result.insert(tk.END, i)

# 取消函数
def conditionOUT():
    the_condition_you_choose.delete(1.0, tk.END)
    list_real.clear()
    reasoning_result.clear()


# --------------------------- GUI界面设计如下 --------------------------------
root = tk.Tk()
root.wm_title("产生式系统_20002462")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 800
wh = 700
x = (sw - ww) / 2
y = (sh - wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

# GUI标题
label1 = tk.Label(root, text="动物识别系统", fg="#DAA520", bg="#FFEBCD")
label1.place(width=200, height=30, x=280, y=20)  # 注：用label.pack()会使该布局无效

# 系统给出的条件
label2 = tk.Label(root, text="以下为本系统给出的可供选择的条件：" + '\n' + rule, fg="#DAA520")
label2.place(x=20, y=50, width=300, height=600)

# 输入你的前提条件
label3 = tk.Label(root, text="请输入选择的条件：", fg="#DAA520")
label3.place(x=350, y=100, width=150, height=30)
the_condition_you_choose = tk.Text(root, width=20, height=30)
the_condition_you_choose.pack(padx=5, pady=10)
the_condition_you_choose.place(x=500, y=100, width=170, height=60)

# “开始”按钮
button1 = tk.Button(root, text="开始", command=conditionIN, activebackground="#2082AA", fg="#DAA520", bg="#FFEBCD")
button1.place(x=450, y=180, width=100, height=30)

# “取消”按钮
button2 = tk.Button(root, text="取消", command=conditionOUT, activebackground="#2082AA", fg="#DAA520", bg="#FFEBCD")
button2.place(x=600, y=180, width=100, height=30)

# 显示前提条件
Label4 = tk.Label(root, text="前提条件为：", fg="#DAA520")
Label4.place(x=350, y=240, width=150, height=30)
the_condition_show = tk.Entry(root, width=20, font=('宋体', '10'))
the_condition_show.place(x=470, y=250, width=200, height=50)

# 显示推理过程
Label5 = tk.Label(root, text="推理过程如下：", fg="#DAA520")
Label5.place(x=350, y=340, width=150, height=30)
show_reasoning_process = tk.Text(root, width=20, font=('宋体', '10'))
show_reasoning_process.place(x=470, y=350, width=200, height=80)

# 显示推理结果
Label6 = tk.Label(root, text="推理结果如下：", fg="#DAA520")
Label6.place(x=350, y=440, width=150, height=30)
show_reasoning_result = tk.Text(root, width=20, font=('宋体', '10'))
show_reasoning_result.place(x=470, y=450, width=200, height=50)

root.mainloop()
