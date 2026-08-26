# TAGLINE

为 shell 脚本提供终端对话框

# TLDR

显示一个简单的**消息**框

```whiptail --title "[title]" --msgbox "[message]" [height] [width]```

显示**是/否**选择框

```whiptail --title "[title]" --yesno "[message]" [height] [width]```

**自定义**是/否按钮文本

```whiptail --title "[title]" --yes-button "[text]" --no-button "[text]" --yesno "[message]" [height] [width]```

显示**文本输入**框

```result=$(whiptail --title "[title]" --inputbox "[message]" [height] [width] [default] 3>&1 1>&2 2>&3)```

显示**密码**输入框

```result=$(whiptail --title "[title]" --passwordbox "[message]" [height] [width] 3>&1 1>&2 2>&3)```

显示带选项的**菜单**

```result=$(whiptail --title "[title]" --menu "[message]" [height] [width] [menu_height] "val1" "text1" "val2" "text2" 3>&1 1>&2 2>&3)```

显示支持多选的**复选列表**

```result=$(whiptail --title "[title]" --checklist "[message]" [height] [width] [list_height] "opt1" "text1" ON "opt2" "text2" OFF 3>&1 1>&2 2>&3)```

显示**进度条**（gauge）

```echo [50] | whiptail --title "[title]" --gauge "[message]" [height] [width] [0]```

# SYNOPSIS

**whiptail** [**--title** _title_] [**--backtitle** _backtitle_] _box-type_ [_box-options_] _height_ _width_

# PARAMETERS

**--title** _title_
> 对话框标题

**--backtitle** _text_
> 背景标题

**--msgbox** _text_ _height_ _width_
> 显示消息和 OK 按钮

**--yesno** _text_ _height_ _width_
> 显示是/否对话框

**--inputbox** _text_ _height_ _width_ [_init_]
> 文本输入对话框

**--passwordbox** _text_ _height_ _width_
> 密码输入（隐藏文本）

**--menu** _text_ _height_ _width_ _menu-height_ [_tag_ _item_]...
> 选择菜单

**--checklist** _text_ _height_ _width_ _list-height_ [_tag_ _item_ _status_]...
> 多选复选列表

**--radiolist** _text_ _height_ _width_ _list-height_ [_tag_ _item_ _status_]...
> 单选按钮列表

**--gauge** _text_ _height_ _width_ _percent_
> 进度条

**--yes-button** _text_
> 自定义 yes 按钮标签

**--no-button** _text_
> 自定义 no 按钮标签

**--ok-button** _text_
> 自定义 OK 按钮标签

**--cancel-button** _text_
> 自定义取消按钮标签

**--defaultno**
> 在是/否对话框中默认选择 No

**--nocancel**
> 不显示 Cancel 按钮

**--separate-output**
> 复选列表结果每行输出一项

**--scrolltext**
> 强制显示垂直滚动条

**--topleft**
> 将对话框放在左上角

**--clear**
> 退出时清屏

**--fullbuttons**
> 使用全宽按钮而不是紧凑按钮

**--output-fd** _FD_
> 将输出发送到给定的文件描述符而不是 stderr

**--textbox** _file_ _height_ _width_
> 在可滚动的框中显示文件内容

**--infobox** _text_ _height_ _width_
> 显示消息但不等待输入

# DESCRIPTION

**whiptail** 可从 shell 脚本中显示基于文本的对话框，为输入和选择提供友好的界面。它创建基于 ncurses 的对话框，可在终端环境中工作，支持多种对话框类型，包括消息框、输入框、菜单和进度条。

输入对话框的输出走 stderr，需要重定向文件描述符（3>&1 1>&2 2>&3）才能捕获到 shell 变量中。退出码表示用户的选择（0 表示 OK/Yes，1 表示 Cancel/No）。

# CAVEATS

对话框尺寸必须以字符为单位指定，且应适应终端大小。结果输出到 stderr，需要重定向文件描述符才能捕获。它是 **dialog** 的轻量替代品，功能较少但依赖更小。

# HISTORY

作为 **dialog** 工具的轻量级重新实现而创建，基于 newt 库构建，属于 Red Hat 开发的 **newt** 库的一部分。由于占用资源少，常用于 Debian 安装器和系统配置脚本中。

# INSTALL

```apt: sudo apt install whiptail```

```dnf: sudo dnf install newt```

```apk: sudo apk add newt```

```zypper: sudo zypper install newt```

```brew: brew install newt```

```nix: nix profile install nixpkgs#newt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dialog](/man/dialog)(1), [zenity](/man/zenity)(1), [gum](/man/gum)(1)
