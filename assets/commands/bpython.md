# TAGLINE

增强型交互式 Python 解释器

# TLDR

**启动交互式 Python 会话**

```bpython```

**先执行脚本再进入交互模式**

```bpython -i [script.py]```

**执行一条命令**

```bpython -c "[print('hello')]"```

**不显示横幅启动**

```bpython -q```

# SYNOPSIS

**bpython** [_options_] [_file_]

# DESCRIPTION

**bpython** 是一款增强版 Python REPL（读取-求值-输出循环），具有语法高亮、自动补全、自动缩进和内联文档等特性。它为交互式 Python 开发提供了友好的界面。

该工具以类似现代 IDE 的特性改善了标准 Python 交互解释器的体验。

# PARAMETERS

**-i**
> 运行文件后进入交互模式。

**-q**
> 安静模式（不显示横幅）。

**-c** _command_
> 执行命令。

**--config** _file_
> 指定配置文件。

# FEATURES

- 语法高亮
- 输入时实时自动补全
- 预期的参数列表
- 内联文档（F1）
- 回退/重放执行（Ctrl+R）
- 将会话保存到文件（F2）
- 撤销（Ctrl+C）
- Pastebin 集成（F8）
- vi/emacs 键绑定

# KEYBINDINGS

- **F1** - 显示文档
- **F2** - 保存到文件
- **F8** - 发送到 pastebin
- **Ctrl+R** - 回退/重放
- **Ctrl+C** - 撤销上一次输入
- **Tab** - 自动补全
- **Ctrl+D** - 退出

# CONFIGURATION

**~/.config/bpython/config**
> 主配置文件，控制语法高亮、颜色、键绑定和行为设置。

# CAVEATS

不能完全替代复杂脚本的运行环境。某些扩展可能无法工作。启动速度比标准 Python 慢。重放功能有局限。不适合生产使用。

# HISTORY

**bpython** 由 Bob Farrell 等人于 **2008 年**前后创建，旨在提供更友好的 Python REPL 体验。

# INSTALL

```pacman: sudo pacman -S bpython```

```brew: brew install bpython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [ipython](/man/ipython)(1), [ptpython](/man/ptpython)(1)
