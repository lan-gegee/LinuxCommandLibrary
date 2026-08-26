# TAGLINE

从 shell 脚本显示 KDE 对话框，使命令行脚本具备图形用户交互能力

# TLDR

显示**消息框**

```kdialog --msgbox "message"```

显示**是/否**询问对话框

```kdialog --yesno "message"```

显示带是/否/取消的**警告**对话框

```kdialog --warningyesnocancel "message"```

显示**输入**对话框

```kdialog --inputbox "message" "default"```

显示**密码**输入对话框

```kdialog --password "message"```

显示**下拉组合框**

```kdialog --combobox "message" "item1" "item2" "item3"```

打开**文件选择**对话框

```kdialog --getopenfilename```

显示**进度条**对话框

```kdialog --progressbar "message"```

# SYNOPSIS

**kdialog** [_options_] [_arguments_]

# DESCRIPTION

**kdialog** 从 shell 脚本中显示 KDE 对话框，使命令行脚本能够进行图形用户交互。它提供多种对话框类型，包括消息框、输入对话框、文件选择器和进度条。

# PARAMETERS

**--msgbox TEXT**
> 显示带 OK 按钮的消息框

**--yesno TEXT**
> 显示是/否对话框；选是返回 0，选否返回 1

**--yesnocancel TEXT**
> 显示是/否/取消对话框；分别返回 0、1 或 2

**--warningyesno TEXT**
> 显示带是/否按钮的警告

**--warningyesnocancel TEXT**
> 显示带是/否/取消按钮的警告

**--inputbox TEXT [DEFAULT]**
> 显示输入对话框；将输入内容打印到 stdout

**--password TEXT**
> 显示密码输入对话框

**--combobox TEXT ITEM...**
> 显示下拉选择对话框

**--getopenfilename [DIR] [FILTER]**
> 显示文件打开对话框

**--getsavefilename [DIR] [FILTER]**
> 显示文件保存对话框

**--getexistingdirectory [DIR]**
> 显示目录选择对话框

**--progressbar TEXT [TOTAL]**
> 显示进度条；返回 D-Bus 引用

**--title TEXT**
> 设置对话框窗口标题

**--icon ICON**
> 设置对话框图标

# CAVEATS

kdialog 需要运行中的 KDE/Qt 环境。退出码因对话框类型而异；请检查返回值以获知用户的选择。进度条返回 D-Bus 引用，脚本可用它来更新进度。

# HISTORY

**kdialog** 是 KDE 基础应用的一部分，让脚本能访问 KDE 原生对话框系统。它相当于 GTK 环境中的 zenity。

# INSTALL

```apt: sudo apt install kdialog```

```dnf: sudo dnf install kdialog```

```pacman: sudo pacman -S kdialog```

```apk: sudo apk add kdialog```

```zypper: sudo zypper install kdialog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zenity](/man/zenity)(1), [dialog](/man/dialog)(1), [whiptail](/man/whiptail)(1)
