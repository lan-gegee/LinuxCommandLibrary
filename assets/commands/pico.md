# TAGLINE

简单易用的文本编辑器，最初作为 Pine 邮件客户端的撰写器开发

# TLDR

**打开文件**进行编辑

```pico [path/to/file]```

**打开文件**并定位到指定行号

```pico +[10] [path/to/file]```

以只读模式**打开文件**

```pico -v [path/to/file]```

在 xterm 中**启用鼠标支持**

```pico -m [path/to/file]```

**禁用自动换行**

```pico -w [path/to/file]```

**使用替代拼写检查器**

```pico -s [aspell] [path/to/file]```

# SYNOPSIS

**pico** [_options_] [_file_]

**pico** +_line_ [_options_] [_file_]

# PARAMETERS

**+**_n_
> 启动时光标位于第 n 行

**-a**
> 在文件浏览器中显示隐藏文件（以 . 开头）

**-d**
> 将删除键重绑定为删除光标下的字符

**-e**
> 启用文件名补全

**-f**
> 使用功能键执行命令

**-g**
> 在文件浏览器中显示光标位置

**-h**
> 显示帮助并退出

**-j**
> 在文件浏览器中启用 Goto 命令

**-k**
> 剪切从光标到行尾的内容，而不是整行

**-m**
> 启用鼠标支持（在 xterm 中）

**-n** _SECS_
> 启用新邮件通知（默认：180 秒）

**-o** _DIR_
> 将操作限制在指定目录内

**-s** _PROG_
> 使用替代拼写检查程序

**-t**
> 工具模式，供其他程序调用

**-v**
> 查看模式（只读）

**-w**
> 禁用自动换行；长行会延伸出屏幕

**-x**
> 禁用底部命令菜单

**-z**
> 启用 Ctrl+Z 挂起

# KEYBOARD COMMANDS

**Ctrl+G**
> 显示帮助

**Ctrl+X**
> 退出（提示保存）

**Ctrl+O**
> 写出（保存文件）

**Ctrl+R**
> 读取/插入文件

**Ctrl+W**
> 搜索（Where Is）

**Ctrl+K**
> 剪切整行

**Ctrl+U**
> 粘贴（Uncut）

**Ctrl+J**
> 排版段落

**Ctrl+T**
> 拼写检查

**Ctrl+C**
> 显示光标位置

**Ctrl+Y**
> 上一页

**Ctrl+V**
> 下一页

# DESCRIPTION

**pico** 是一个简单易用的文本编辑器，最初作为 Pine 邮件客户端的撰写器开发。命令显示在屏幕底部，对新手非常友好。按 **Ctrl+G** 可获取上下文相关的帮助。

该编辑器提供搜索、剪切/粘贴、拼写检查和段落排版等基本功能。它采用无模式界面，按键直接输入文本，命令则通过 Control 组合键触发。

在大多数现代 Linux 发行版上，**pico** 是指向 **nano** 的符号链接，后者是一个功能更多的自由软件再实现。两个编辑器共享相同的界面风格和键盘命令。

# CAVEATS

Pico 最初属于受许可证限制的 Pine 邮件套件。**nano** 编辑器就是作为自由替代品而创建的，如今更为常见。文件以 Unix 换行符保存。连接断开时（SIGHUP），pico 会将工作保存到 filename.save 或 pico.save。

# HISTORY

Pico 由**华盛顿大学**开发，是 **Pine** 邮件客户端的一部分，于 **1992 年**首次发布。其名称代表 "**P**ine **I**nternal **CO**mposer" 或 "**P**rogram for **I**nternet **CO**mmunications"。由于 Pine 的限制性许可，GNU 项目于 **1999 年**创建了 **nano** 作为自由替代品。nano 最终在大多数发行版中取代了 pico，不过 pico 命令通常仍作为别名保留。

# INSTALL

```dnf: sudo dnf install alpine```

```apk: sudo apk add alpine```

```zypper: sudo zypper install alpine```

```brew: brew install alpine```

```nix: nix profile install nixpkgs#alpine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [vi](/man/vi)(1), [emacs](/man/emacs)(1), [pine](/man/pine)(1)
