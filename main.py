import customtkinter as ctk

#——————————函数定义—————————————
# 登录函数
def submit():
    uid = enter_uid.get()
    password = enter_pass.get()
    result = f"uid:{uid}\npassword:{password}\n"
    if uid != "" and password != "":
        print(result)

# 主题切换函数
def appearance():
    if str(ctk.get_appearance_mode()) == "Light":
        ctk.set_appearance_mode("dark")
        block.configure(fg_color="dark gray", border_color="gray")
    else:
        ctk.set_appearance_mode("light")
        block.configure(fg_color="white", border_color="light gray")

# 密码可见函数
def whether_can_see():
    if check_var.get() == 1:
        enter_pass.configure(show="")
    elif check_var.get() == 0:
        enter_pass.configure(show="*")


def show_see_box():
        # 显示
        block.place(relx=1, x=-10, y=40, anchor="ne")
        uid.place(x=70, y=100)
        enter_uid.place(x=65, y=125)
        pw.place(x=70, y=220)
        enter_pass.place(x=65, y=245)
        checkbox.place(x=65, y=280)
        log_on.place(x=65, y=400)
        theme.place(x=35, y=5)
        see_box.place_forget()
        hide_box.place(x=5, y=5) 
   
def hide_see_box():
        # 隐藏
        block.place_forget()
        uid.place_forget()
        enter_uid.place_forget()
        pw.place_forget()
        enter_pass.place_forget()
        checkbox.place_forget()
        log_on.place_forget()
        theme.place_forget()
        see_box.place(x=860, y=40)
        hide_box.place_forget()

#——————————————主程序——————————————

width = 900
height = 630

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("light")  # 浅色模式

tk = ctk.CTk()
tk.title("LogOn-system")
tk.geometry(f"{width}x{height}")
tk.resizable(False, False)

# 右侧白色方块（完美固定大小）
block = ctk.CTkFrame(
    tk,
    width=430,
    height=540,
    fg_color="white",
    border_width=3,
    border_color="light gray"
)
block.pack_propagate(False)  # 关键：不让内容压扁它

# uid 文字 + 输入框
x = 10
uid = ctk.CTkLabel(block, text="uid:", font=("微软雅黑", x))
enter_uid = ctk.CTkEntry(block, width=300, font=("微软雅黑", x), fg_color="white", text_color="black")

# 密码文字 + 输入框
pw = ctk.CTkLabel(block, text="password:", font=("微软雅黑", x))
enter_pass = ctk.CTkEntry(block, width=300, font=("微软雅黑", x), show="*", fg_color="white", text_color="black")

check_var = ctk.IntVar()
checkbox = ctk.CTkCheckBox(block, text="whether can see or not",variable=check_var,command=whether_can_see)

# 登录按钮
log_on = ctk.CTkButton(block, text="登录", width=300, font=("微软雅黑", 15), command=submit)

#主题切换按钮
theme = ctk.CTkButton(block, text="主题", width=20,height=20, font=("微软雅黑", 15), command=appearance)

# 显示 按键
see_box = ctk.CTkButton(tk, text="<", width=20, height=20, font=("微软雅黑", 15), command=show_see_box)
see_box.pack_propagate(False)
see_box.place(x=860, y=40)

#隐藏 按钮
hide_box = ctk.CTkButton(block, text=">", width=20, height=20, font=("微软雅黑", 15), command=hide_see_box)
hide_box.pack_propagate(False)
hide_box.place(x=5, y=5)

tk.mainloop()