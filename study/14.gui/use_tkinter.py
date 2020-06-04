from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='hello, world!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Alert', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


# 从Frame派生一个Application类，这是所有Widget的父容器
# GUI 中，每个Button、Lable、输入框等，都是一个Widget，Frame 是可以容纳其他Widget 的容器
# pack() 方法将Widget 加入父容器内，并实现布局。grid() 可以实现更复杂的布局
# 创建Label 和Button，当Button 点击时，触发self.quit 退出程序

app = Application()
# 设置窗口标题
app.master.title('Hello Tkinter')
# 主消息循环
# 主线程负责监听来自操作系统的消息，并依次处理每一条消息
app.mainloop()