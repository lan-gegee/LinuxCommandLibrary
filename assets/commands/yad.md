# TAGLINE

用于 shell 脚本的 GTK 对话框工具

# TLDR

**显示信息对话框**

```yad --info --text="[Message text]"```

**显示文件选择对话框**

```yad --file --title="[Select a file]"```

**显示文本输入对话框**

```yad --entry --text="[Enter your name:]"```

**创建包含多个字段的表单**

```yad --form --field="[Name]" --field="[Email]" --field="[Age]:NUM"```

**显示列表选择对话框**

```yad --list --column="[ID]" --column="[Name]" [1] "[Alice]" [2] "[Bob]"```

从标准输入**显示进度条**

```[command] | yad --progress --text="[Processing...]" --auto-close```

**创建日历对话框**

```yad --calendar --title="[Select date]"```

在系统托盘中**显示通知图标**

```yad --notification --image="[icon-name]" --text="[Tooltip text]"```

# SYNOPSIS

**yad** [_--info_|_--warning_|_--error_|_--question_] [_--entry_] [_--file_] [_--form_] [_--list_] [_--progress_] [_--calendar_] [_--notification_] [_options_]

# PARAMETERS

**--info**
> 显示信息对话框。

**--warning**
> 显示警告对话框。

**--error**
> 显示错误对话框。

**--question**
> 显示带 Yes/No 按钮的提问对话框。

**--entry**
> 显示文本输入对话框。

**--file**
> 显示文件选择对话框。

**--directory**
> 显示目录选择对话框。

**--form**
> 显示含多个输入字段的表单。

**--list**
> 显示列表/表格选择对话框。

**--progress**
> 显示进度条对话框。

**--calendar**
> 显示日历日期选择对话框。

**--color**
> 显示颜色选择对话框。

**--font**
> 显示字体选择对话框。

**--notification**
> 显示系统托盘通知图标。

**--text** _string_
> 设置对话框文本。

**--title** _string_
> 设置对话框窗口标题。

**--width** _n_
> 设置对话框宽度。

**--height** _n_
> 设置对话框高度。

**--field** _label[:type]_
> 向表单添加字段（类型：TEXT、NUM、CHK、CB 等）。

**--column** _name_
> 为列表对话框添加列。

**--auto-close**
> 进度达到 100% 时关闭对话框。

**--button** _label:action_
> 添加自定义按钮。

**--separator** _char_
> 设置输出字段分隔符。

# DESCRIPTION

**YAD**（Yet Another Dialog）是一个功能强大的 GTK+ 对话框工具，用于在 shell 脚本中创建图形化对话框。它是 Zenity 的一个分叉增强版，拥有显著更多的特性和自定义选项。

YAD 支持多种对话框类型：消息框、文件/目录选择、表单、列表、进度条、日历、颜色选择器、字体选择器以及系统托盘通知。表单可以包含各种字段类型，包括文本、数字、复选框、组合框、文件选择器等。

对话框的输出会写入标准输出，因此很容易在 shell 脚本中捕获用户输入。退出码表示按下的是哪个按钮。自定义按钮可以定义特定的返回码或动作。

对于复杂界面，YAD 支持带有标签页和多页容器的多窗格布局。**--plug** 和 **--tabnum** 选项允许将多个对话框嵌入同一个窗口。在支持 WebKit 的情况下，可以使用 **--html** 选项显示 HTML 内容。

# CAVEATS

需要 GTK+ 3 库。HTML 渲染等部分功能需要 WebKit。对话框外观随 GTK 主题而变化。复杂表单可能需要仔细转义特殊字符。系统托盘支持取决于桌面环境的兼容性。

# HISTORY

**YAD** 由 Victor Ananjevsky 创建，是 Zenity 的增强分叉版。开发始于 **2008 年**前后，目的是解决 Zenity 的局限并添加更复杂的 shell 脚本 GUI 所需的功能。该项目一直得到积极维护，定期发布新版本，不断添加新的对话框类型和选项。

# INSTALL

```apt: sudo apt install yad```

```dnf: sudo dnf install yad```

```pacman: sudo pacman -S yad```

```apk: sudo apk add yad```

```nix: nix profile install nixpkgs#yad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zenity](/man/zenity)(1), [dialog](/man/dialog)(1), [kdialog](/man/kdialog)(1), [whiptail](/man/whiptail)(1)
