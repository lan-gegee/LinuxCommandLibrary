# TAGLINE

打字教学程序

# TLDR

以默认课程**启动 GNU Typist**

```gtypist```

**启动指定课程文件**

```gtypist [path/to/lesson.typ]```

**从指定的课程标签开始**

```gtypist -l [S1]```

**设置允许的最大错误率**（默认：3.0）

```gtypist -e [5.0]```

**以静音模式启动**（错误时不发出提示音）

```gtypist -s```

**记录个人最佳打字速度**

```gtypist -b```

# SYNOPSIS

**gtypist** [_options_] [_script_]

# PARAMETERS

_script_
> 要使用的课程文件（.typ 格式）。

**-l** _label_
> 从脚本中特定的课程标签开始。

**-e** _percent_
> 允许的最大错误百分比（默认：3.0，范围：0.0-100.0）。

**-s**
> 静音模式（出错时不发出提示音）。

**-b**, **--personal-best**
> 记录个人最佳打字速度。

**-n**, **--notimer**
> 在练习中关闭 WPM 计时器。

**-t**, **--term-cursor**
> 使用终端的硬件光标。

**-w**
> 文字处理器模式。

**-V**, **--version**
> 打印版本并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**GNU Typist**（gtypist）是一款打字教学程序。它提供结构化的盲打课程，练习从主键盘行逐步推进到全键盘熟练水平。

程序会跟踪准确率和速度，要求用户达到准确率阈值（可通过 **-e** 配置）后才能进入下一练习。课程脚本可以使用 gtypist 课程文件格式自定义或从头编写。

# INCLUDED LESSONS

- QWERTY 键盘布局（美式、英式）
- Dvorak 布局
- Colemak 布局
- 数字小键盘训练
- 多种语言（德语、法语、西班牙语等）

# LESSON FILE FORMAT

```
# Comment
*:LABEL
T:Tutorial text to display
D:Drill text to type
S:Speed test paragraph
```

# CAVEATS

基于终端的界面（需要 ncurses）。课程默认以英语为主。除非使用 --personal-best 记录速度，否则进度不会在会话之间保存。

# HISTORY

GNU Typist 由 **Simon Baldwin** 编写，作为 **GNU** 工程的一部分维护。它延续了早期计算机教育时代打字教学软件的传统。

# INSTALL

```apt: sudo apt install gtypist```

```dnf: sudo dnf install gtypist```

```zypper: sudo zypper install gtypist```

```brew: brew install gtypist```

```nix: nix profile install nixpkgs#gtypist```

<!-- packages: 2026-07-22 -->
