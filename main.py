# 主程序
# 注释？我把代码喂给AI帮我写的注释（）
import tkinter as tk
from tkinter import messagebox, font, PhotoImage
import requests
from bs4 import BeautifulSoup
from echolog import *

class Browser:
    def __init__(self, root):
        self.root = root
        self.root.title("AlphaBeta浏览器 v0.1.0 By Ekuta Studio")
        self.root.geometry("800x600")

        self.about_button = tk.Button(root,text='关于AlphaBeta浏览器',command=self.about_button).pack()

        # URL输入框
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=(10, 2))

        # 访问按钮
        self.go_button = tk.Button(root, text="前往", command=self.load_url)
        self.go_button.pack(pady=(2, 10))

        # 创建Canvas，用于放置内容
        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=True)

        # 创建滚动条并与Canvas关联
        self.sbar1 = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.sbar1.pack(side="right", fill="y")

        # 配置Canvas的yview与滚动条关联
        self.canvas.config(yscrollcommand=self.sbar1.set)


        # 创建滚动条并与Canvas关联
        self.sbar1 = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.sbar1.pack(side="right", fill="y")

        # 配置Canvas的yview与滚动条关联
        self.canvas.config(yscrollcommand=self.sbar1.set)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # 绑定鼠标滚轮事件到canvas上
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        # 计算滚动量，正值向上滚动，负值向下滚动
        scroll_units = -event.delta // 120
        self.canvas.yview('scroll', scroll_units, 'units')
        return "break"

    def about_button(self):
        messagebox.showinfo("关于", "AlphaBeta浏览器\n一个与众不同的浏览器\nBy Ekuta Studio\nGithub:github.com/mibino/alphabeta")

    def load_url(self, url=None):
        if not url:
            url = self.url_entry.get()
        if not url:
            messagebox.showerror("错误", "请输入URL")
            echo_log_error('未输入URL')
            return

        try:
            response = requests.get(url)
            response.raise_for_status()
            echo_log_info(str(url))
        except requests.RequestException as e:
            messagebox.showerror("错误", f"无法加载界面: {e}")
            echo_log_error('无法加载界面:' + str(e))
            return

        # 清空当前Canvas内容
        self.canvas.delete("all")

        # 解析HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        current_y = 10  # 起始Y坐标

        # 设置字体格式
        h1_font = font.Font(family="Microsoft Yahei", size=16, weight="bold")
        normal_font = font.Font(family="Microsoft Yahei", size=12)
        bold_font = font.Font(family="Microsoft Yahei", size=12, weight='bold')

        # 显示内容
        for tag in soup.find_all(['h1', 'p', 'br', 'a', 'center', 'title', 'dd', 'b', 'img']):
            text = tag.get_text().strip()
            if not text:
                continue
            if tag.name == 'br':
                current_y += 10
            elif tag.name == 'h1':
                label = tk.Label(
                    self.root, 
                    text=text, 
                    font=h1_font,
                    bg="white")
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
                current_y += label.winfo_reqheight() + 5
            elif tag.name == 'p':
                label = tk.Label(
                    self.root, 
                    text=text,  
                    font=normal_font, 
                    bg="white",
                    fg='black')
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
                current_y += label.winfo_reqheight() + 5
            elif tag.name == 'b':
                label = tk.Label(
                    self.root, 
                    text=text,  
                    font=bold_font, 
                    bg="white",
                    fg='black')
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
                current_y += label.winfo_reqheight() + 5
            elif tag.name == 'a':
                label = tk.Label(
                    self.root, 
                    text=text, 
                    font=normal_font, 
                    bg="white",
                    fg='blue')
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
                current_y += label.winfo_reqheight() + 5
            elif tag.name == 'dd':
                label = tk.Label(
                    self.root, 
                    text='    ' + text,  
                    font=normal_font, 
                    bg="white",
                    fg='black')
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
                current_y += label.winfo_reqheight() + 5
            elif tag.name == 'center':
                self.canvas.create_text((self.canvas.winfo_width() // 2, current_y), text=text, font=normal_font, fill="black", anchor="center")
                current_y += 20
            elif tag.name == 'title':
                continue
            elif tag.name == 'img':
                label = tk.Label(
                    self.root, 
                    text='这里应该要显示图片，但是我没写出来', 
                    font=normal_font, 
                    bg="white",
                    fg='black')
                self.canvas.create_window((10, current_y), window=label, anchor="nw")
        # 更新滚动区域
        self.update_scrollregion()

    

def main():
    root = tk.Tk()
    app = Browser(root)
    root.mainloop()

if __name__ == "__main__":
    main()