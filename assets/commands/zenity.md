# TAGLINE

在 Shell 脚本中显示 GTK 对话框

# TLDR

**显示**默认的提问对话框

```zenity --question```

**显示**带消息的信息对话框

```zenity --info --text "[message]"```

**显示**带自定义分隔符的名称/密码表单

```zenity --forms --add-entry "[name_label]" --add-password "[password_label]" --separator ";"```

**显示**仅限目录的文件选择对话框

```zenity --file-selection --directory```

**显示**可更新的进度条

```(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100") | zenity --progress```

# SYNOPSIS

**zenity** [_options_]

# PARAMETERS

**--question**
> 显示带"是/否"按钮的提问对话框

**--info**
> 显示信息对话框

**--warning**
> 显示警告对话框

**--error**
> 显示错误对话框

**--file-selection**
> 显示文件选择对话框

**--forms**
> 显示表单对话框

**--progress**
> 显示进度对话框

**--text _text_**
> 设置对话框文本

**--add-entry _label_**
> 添加文本输入框（表单）

**--add-password _label_**
> 添加密码输入框（表单）

**--directory**
> 仅允许选择目录

**--separator _char_**
> 设置输出分隔符

# DESCRIPTION

**zenity** 在命令行脚本中显示 GTK+ 对话框。它提供多种对话框类型，包括提问、信息、文件选择、进度条和表单。

返回值表示用户的操作：0 表示确定/是，1 表示取消/否，5 表示超时，-1 表示出错。表单数据通过标准输出返回。

# CAVEATS

需要图形环境（X11 或带 XWayland 的 Wayland）。对话框外观取决于 GTK 主题。对于 KDE 环境，可考虑使用 **kdialog** 作为替代。

# INSTALL

```apt: sudo apt install zenity```

```dnf: sudo dnf install zenity```

```pacman: sudo pacman -S zenity```

```apk: sudo apk add zenity```

```zypper: sudo zypper install zenity```

```brew: brew install zenity```

```nix: nix profile install nixpkgs#zenity```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kdialog](/man/kdialog)(1), [dialog](/man/dialog)(1), [whiptail](/man/whiptail)(1)
