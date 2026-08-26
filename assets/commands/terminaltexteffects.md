# TAGLINE

面向终端文本输出的视觉效果引擎

# TLDR

**对文本应用 decrypt 效果**

```cat [your_text] | tte decrypt```

**应用 beams 效果**

```echo "hello world" | tte beams```

**查看特定效果的帮助**

```tte [decrypt] -h```

# SYNOPSIS

_command_ | **tte** _effect_ [_options_]

# DESCRIPTION

**terminaltexteffects**（tte）是一个终端视觉效果引擎，既可以作为独立应用运行，也可以作为 Python 库使用。它内置 37 种以上的效果，包括 matrix、decrypt、rain、beams、burn 等，支持通过路径、航点、运动缓动和贝塞尔曲线实现复杂的字符移动。效果以行内方式运行，保留终端状态和工作流。

# HISTORY

**terminaltexteffects** 由 **ChrisBuilds** 创建，使用 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#terminaltexteffects```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lolcat](/man/lolcat)(1), [figlet](/man/figlet)(1), [toilet](/man/toilet)(1)
