# TAGLINE

为 Shell 脚本提供文本模式的对话框

# TLDR

显示一条**消息**

```dialog --msgbox "[Message]" [height] [width]```

提示**文本输入**

```dialog --inputbox "[Enter text:]" 8 40 2>[output.txt]```

提示**是/否**问题

```dialog --yesno "[Continue?]" 7 40```

显示一个**菜单**供选择

```dialog --menu "[Choose one:]" 15 40 4 1 "[Option A]" 2 "[Option B]" 3 "[Option C]" 2>[output.txt]```

显示可多选的**复选列表**

```dialog --checklist "[Select items:]" 15 40 4 1 "[Item A]" on 2 "[Item B]" off 3 "[Item C]" on 2>[output.txt]```

显示一个**进度条**

```dialog --gauge "[Installing...]" 7 40 0```

显示**密码**输入框

```dialog --passwordbox "[Enter password:]" 8 40 2>[output.txt]```

# SYNOPSIS

**dialog** [_options_] _box-type_ [_box-options_]

# DESCRIPTION

**dialog** 用于在 Shell 脚本中显示对话框，为交互式脚本提供友好的基于文本的用户界面。它支持多种控件类型，包括消息框、输入框、菜单、复选列表、单选列表、进度条以及文件选择对话框。

该程序使用 ncurses 库在文本终端中创建伪图形界面，使 Shell 脚本无需图形环境也能呈现外观专业的用户界面。

输出写入 stderr（或指定文件），退出状态码表示用户按下了哪个按钮（0 表示 OK/Yes，1 表示 Cancel/No，255 表示 ESC）。这种设计使脚本既能捕获用户的选择，又能继续将 stdout 用于其他用途。dialog 广泛用于系统管理脚本、安装程序和配置工具中。

# PARAMETERS

**--msgbox** _text_ _height_ _width_
> 显示带有 OK 按钮的消息框

**--yesno** _text_ _height_ _width_
> 是/否问题对话框

**--inputbox** _text_ _height_ _width_ [_init_]
> 文本输入对话框

**--menu** _text_ _height_ _width_ _menu-height_ _tag_ _item_...
> 菜单选择

**--checklist** _text_ _height_ _width_ _list-height_ _tag_ _item_ _status_...
> 复选框选择

**--radiolist** _text_ _height_ _width_ _list-height_ _tag_ _item_ _status_...
> 单选按钮选择（单选）

**--gauge** _text_ _height_ _width_ _percent_
> 进度条显示

**--passwordbox** _text_ _height_ _width_
> 密码输入（字符隐藏）

**--fselect** _filepath_ _height_ _width_
> 文件选择对话框

**--calendar** _text_ _height_ _width_ _day_ _month_ _year_
> 日历日期选择

**--title** _title_
> 设置对话框标题

**--backtitle** _title_
> 设置屏幕顶部的背景标题

**--clear**
> 退出时清屏

**--colors**
> 启用对话框文本中的内嵌颜色代码

**--output-fd** _fd_
> 输出到指定文件描述符而非 stderr

# CAVEATS

输出默认写到 stderr，需用 2>file 重定向。退出状态码：0=OK/Yes，1=Cancel/No，255=ESC。如需图形化对话框，参见 zenity 或 kdialog。

# HISTORY

**dialog** 最初由 **Savio Lam** 于 **1994** 年编写，自 **1999** 年起由 **Thomas E. Dickey** 维护。它基于 ncurses 库，已成为在 Shell 脚本中创建文本模式用户界面的标准工具，广泛用于各 Linux 发行版的安装程序和配置工具。

# INSTALL

```apt: sudo apt install dialog```

```dnf: sudo dnf install dialog```

```pacman: sudo pacman -S dialog```

```apk: sudo apk add dialog```

```zypper: sudo zypper install dialog```

```brew: brew install dialog```

```nix: nix profile install nixpkgs#dialog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whiptail](/man/whiptail)(1), [zenity](/man/zenity)(1), [kdialog](/man/kdialog)(1), [gum](/man/gum)(1)
