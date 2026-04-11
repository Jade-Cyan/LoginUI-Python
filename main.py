import customtkinter as ctk

def submit():
    uid = enter_uid.get()
    password = enter_pass.get()
    result = f"uid:{uid}\npassword:{password}\n"
    if uid != "" and password != "":
        print(result)

width = 900
height = 630

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("light")  # 浅色模式

#切换主题
def appearance():
    if str(ctk.get_appearance_mode()) == "Light":
        ctk.set_appearance_mode("dark")
        block.configure(fg_color="dark gray", border_color="gray")
    else:
        ctk.set_appearance_mode("light")
        block.configure(fg_color="white", border_color="light gray")

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
block.pack(side="right", padx=10, pady=10)

# uid 文字 + 输入框
ctk.CTkLabel(block, text="uid:", font=("微软雅黑", 14)).place(x=70, y=100)
enter_uid = ctk.CTkEntry(block, width=300, font=("微软雅黑", 14),fg_color="white",text_color="black")
enter_uid.place(x=65, y=125)

# 密码文字 + 输入框
ctk.CTkLabel(block, text="password:", font=("微软雅黑", 14)).place(x=70, y=220)
enter_pass = ctk.CTkEntry(block, width=300, font=("微软雅黑", 14),show="*",fg_color="white",text_color="black")
enter_pass.place(x=65, y=245)

check_var = ctk.IntVar()
def whether_can_see():
    if check_var.get() == 1:
        enter_pass.configure(show="")
    elif check_var.get() == 0:
        enter_pass.configure(show="*")
checkbox = ctk.CTkCheckBox(block, text="whether can see or not", variable=check_var,command=whether_can_see)
checkbox.place(x=65,y=280)

# 登录按钮
log_on = ctk.CTkButton(block, text="登录", width=300, font=("微软雅黑", 15), command=submit)
log_on.place(x=65, y=400)

#主题切换按钮
theme = ctk.CTkButton(block, text="主题", width=20,height=20, font=("微软雅黑", 15), command=appearance)
theme.place(x=5, y=5)

tk.mainloop()