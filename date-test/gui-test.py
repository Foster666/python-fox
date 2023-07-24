import pyautogui  # 导入pyautogui库


class My_gui():
    def __init__(self):
        self.funct = f"pyautogui.size()获取屏幕分辨率"
        """
        'Press Ctrl+C to quit' # 提示按Ctrl+C可以退出
        pyautogui.size()  # 获取屏幕尺寸
        
        pyautogui.position() # 获取鼠标当前位置
        pyautogui.onScreen(x, y) # 返回布尔值True和False
        pyautogui.PAUSE = 2.5 # 更改操作延迟时间为2.5秒
        pyautogui.FAILSAFE = True # 鼠标光标在屏幕左上角，会导致程序异常，用于终止程序运行。
        pyautogui.moveTo(100, 200, duration=1.2) # 用1.2秒的时间把光标移动到(100, 200)绝对坐标位置
        
        pyautogui.click(x=100, y=200, duration=2) # 先用2秒钟时间移动到(100, 200)再单击鼠标左键（默认）
        pyautogui.click(50, 100, clicks=3, interval=0.25, button='right') # 先移动到绝对坐标（50,100）,单击3次，间隔0.25秒，默认左键,left（左键），middle（中键）和right（右键）
        
        pyautogui.scroll(-10) # 向下滚动10格
        pyautogui.scroll(10, x=100, y=100) # 移动到(100, 100)位置，然后滚轮向上滚动10格
        
        pyautogui.mouseDown(x=100, y=200, button='left') # 移动到(100, 200)位置，然后松开鼠标右键
        pyautogui.mouseUp(x=100, y=200, button='left') # 移动到(100, 200)位置，然后松开鼠标右键
        pyautogui.mouseUp(button='right', x=100, y=200) # 移动到(100, 200)位置，然后松开鼠标右键
        
        pyautogui.dragTo(100, 200, button='left') # 鼠标左键拖拽到屏幕“100，200”的位置
        pyautogui.dragTo(300, 400, 2, button='left') # 鼠标左键用“2秒”拖拽到屏幕“300，400”的位置
        pyautogui.dragRel(30, 0, 2, button='left') # 鼠标左键用“2秒”拖拽到相对当前位置右边30像素的位置
        pyautogui.dragRel(30, 0, duration=2, button='left') # 上面也可以写成这样
        
        pyautogui.typewrite('Hello world!') # 输入Hello world!
        pyautogui.typewrite('Hello world!', interval=0.25) # 每次输入间隔0.25秒，输入Hello world!
        pyautogui.typewrite('Hello world!\n', interval=0.1) # 模拟按键依次键入Hello world!字符并换行（\n），按键的时间间隔0.1秒。
        pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.1) # 依然按列表中的按键，间隔0.1秒
        
        pyautogui.press('esc') # 按一下键盘Esc键
        pyautogui.press(['left','left','left']) # 键盘上三次点击左方向键左箭头
        pyautogui.hotkey('ctrl', 'a') # 全选
        
        pyautogui.press('a') # 按一次a =====>pyautogui.keyDown('a') # 按下a不释放 ++++++ pyautogui.keyUp('a') # 释放a
        
        
        下面是press()，keyDown()，keyUp()和hotkey()函数可以输入的按键名称：
        print(pyautogui.KEYBOARD_KEYS)
        [’\t’, ‘\n’, ‘\r’, ’ ‘, ‘!’, ‘"’, ‘#’, ‘$’, ‘%’, ‘&’, "’", ‘(’, ‘)’, ‘*’, ‘+’, ‘,’, ‘-’, ‘.’, ‘/’, ‘0’, ‘1’, ‘2’, ‘3’,
        ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’, ‘:’, ‘;’, ‘<’, ‘=’, ‘>’, ‘?’, ‘@’, ‘[’, ‘\’, ‘]’, ‘^’, ‘_’, ‘`’, ‘a’, ‘b’, ‘c’, ‘d’, ‘e’,
        ‘f’, ‘g’, ‘h’, ‘i’, ‘j’, ‘k’, ‘l’, ‘m’, ‘n’, ‘o’, ‘p’, ‘q’, ‘r’, ‘s’, ‘t’, ‘u’, ‘v’, ‘w’, ‘x’, ‘y’, ‘z’, ‘{’, ‘|’, ‘}’,
        ‘~’, ‘accept’, ‘add’, ‘alt’, ‘altleft’, ‘altright’, ‘apps’, ‘backspace’, ‘browserback’, ‘browserfavorites’, ‘browserforward’,
        ‘browserhome’, ‘browserrefresh’, ‘browsersearch’, ‘browserstop’, ‘capslock’, ‘clear’, ‘convert’, ‘ctrl’, ‘ctrlleft’, 
        ‘ctrlright’, ‘decimal’, ‘del’, ‘delete’, ‘divide’, ‘down’, ‘end’, ‘enter’, ‘esc’, ‘escape’, ‘execute’, ‘f1’, ‘f10’, 
        ‘f11’, ‘f12’, ‘f13’, ‘f14’, ‘f15’, ‘f16’, ‘f17’, ‘f18’, ‘f19’, ‘f2’, ‘f20’, ‘f21’, ‘f22’, ‘f23’, ‘f24’, ‘f3’, ‘f4’, 
        ‘f5’, ‘f6’, ‘f7’, ‘f8’, ‘f9’, ‘final’, ‘fn’, ‘hanguel’, ‘hangul’, ‘hanja’, ‘help’, ‘home’, ‘insert’, ‘junja’, ‘kana’,
        ‘kanji’, ‘launchapp1’, ‘launchapp2’, ‘launchmail’, ‘launchmediaselect’, ‘left’, ‘modechange’, ‘multiply’, ‘nexttrack’,
        ‘nonconvert’, ‘num0’, ‘num1’, ‘num2’, ‘num3’, ‘num4’, ‘num5’, ‘num6’, ‘num7’, ‘num8’, ‘num9’, ‘numlock’, ‘pagedown’,
        ‘pageup’, ‘pause’, ‘pgdn’, ‘pgup’, ‘playpause’, ‘prevtrack’, ‘print’, ‘printscreen’, ‘prntscrn’, ‘prtsc’, ‘prtscr’,
        ‘return’, ‘right’, ‘scrolllock’, ‘select’, ‘separator’, ‘shift’, ‘shiftleft’, ‘shiftright’, ‘sleep’, ‘stop’, 
        ‘subtract’, ‘tab’, ‘up’, ‘volumedown’, ‘volumemute’, ‘volumeup’, ‘win’, ‘winleft’, ‘winright’, ‘yen’, ‘command’, 
        ‘option’, ‘optionleft’, ‘optionright’]
        
        
        im1 = pyautogui.screenshot()
        im2 = pyautogui.screenshot('my_screenshot.png')
        im = pyautogui.screenshot(region=(0, 0, 300 ,400)) # 如果不需要截取整个屏幕，还有一个可选的region参数。可以控制截取区域的左上角X、Y坐标值和宽度、高度的参数，用来截取。
        
        1. pyautogui.locateOnScreen('looks.png') #  找到会返回(最上角坐标x，y，宽度，高度)4个数值。如果有一个像素不匹配，它就会返回None。
        2. x, y = pyautogui.center((643, 745, 70, 29)) # 获得中心点x,y的坐标
        1+2====> x, y = pyautogui.locateCenterOnScreen('calc7key.png', confidence=0.9)
        """

    def test(self):
        screen_width, screen_height = pyautogui.size()  # 获取屏幕尺寸
        pyautogui.moveTo(screen_width / 2, screen_height / 2)  # 鼠标移动到屏幕中心
        current_mouse_x, current_mouse_y = pyautogui.position()  # 获取鼠标当前位置
        print(current_mouse_x, current_mouse_y)  # 打印鼠标位置，输出屏幕中心值

    def debug(self):
        # self.test()
        im = pyautogui.screenshot(region=(0, 0, 300, 400))
        x, y = pyautogui.locateCenterOnScreen(im, confidence=0.9, region=(0, 0, 300, 400))
        # pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click(x, y, clicks=1, interval=0.25, button='left') # 默认左键,left（左键），middle（中键）和right（右键）
        print(x, y)


gui = My_gui()
gui.debug()

