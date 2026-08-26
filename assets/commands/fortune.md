# TAGLINE

随机格言与签语显示

# TLDR

**显示随机格言**

```fortune```

**显示短格言**

```fortune -s```

**显示冒犯性格言**

```fortune -o```

**使用指定数据库**

```fortune [literature]```

**显示格言来源**

```fortune -c```

# SYNOPSIS

**fortune** [_options_] [_databases_...]

# PARAMETERS

_DATABASES_
> 要使用的 fortune 文件。

**-s**
> 仅显示短格言（< 160 字符）。

**-l**
> 仅显示长格言。

**-c**
> 显示格言文件来源。

**-o**
> 包含冒犯性格言。

**-a**
> 包含所有 fortune 文件。

**-f**
> 列出可用的 fortune 文件。

**-m** _PATTERN_
> 匹配格言中的模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fortune** 从其数据库文件中随机显示引言、笑话或谚语。它是经典的 Unix 程序，为终端和登录会话增添趣味。

多个 fortune 数据库涵盖文学、谜语、定义和笑话等类别。可以使用 strfile 工具创建自定义数据库文件。

fortune 常被加入 Shell 启动文件中，用于每日激励或消遣。

# CAVEATS

冒犯性格言默认禁用。数据库的可用性因安装而异。部分内容可能已过时。

# HISTORY

fortune 起源于 **Unix Version 7**（1979 年），灵感来自幸运饼干。它成为 Unix 系统的标准组成部分，在命令行提供娱乐，偶尔也带来智慧。

# INSTALL

```apk: sudo apk add fortune```

```zypper: sudo zypper install fortune```

```brew: brew install fortune```

```nix: nix profile install nixpkgs#fortune```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cowsay](/man/cowsay)(1), [figlet](/man/figlet)(1)

# RESOURCES

```[Source code](https://github.com/shlomif/fortune-mod)```

<!-- verified: 2026-07-15 -->
