# TAGLINE

具备高级特性的扩展 Bourne Shell

# TLDR

**启动交互式 zsh shell**

```zsh```

**执行脚本**

```zsh [script.zsh]```

**执行命令**

```zsh -c "[command]"```

**不加载配置文件启动**

```zsh -f```

**启动登录 shell**

```zsh -l```

**检查脚本语法**而不执行

```zsh -n [script.zsh]```

# SYNOPSIS

**zsh** [**-cefinslvx**] [_script_ [_args_...]]

# PARAMETERS

**-c** _string_
> 执行字符串中的命令

**-f**
> 不读取启动文件

**-i**
> 强制进入交互模式

**-l**
> 登录 shell

**-n**
> 不执行；仅检查语法

**-s**
> 从 stdin 读取命令

**-v**
> 详细输出；按读取内容原样打印

**-x**
> Xtrace；打印实际执行的命令

# DESCRIPTION

**zsh**（Z Shell）是扩展版 Bourne shell，结合了 bash、ksh 和 tcsh 的特性，并有众多改进。它提供强大的补全、主题和脚本功能。

Zsh 高度可定制：交互式设置放在 **~/.zshrc**，对所有 shell 生效的设置放在 **~/.zshenv**。Oh My Zsh 和 Prezto 等框架项目提供了预配置的主题与插件。

关键特性包括先进的 Tab 补全（可编程且能感知上下文）、拼写纠正、跨会话共享历史、强大的 globbing（递归模式、限定符），以及丰富的自定义选项。

Zsh 在需要时可兼容 POSIX，同时凭借关联数组、浮点运算和高级参数展开等能力远超 POSIX 的范畴。

# KEY FEATURES

**补全**：上下文感知、可编程、支持菜单选择
**Glob 模式匹配**：**\*\*/** 递归匹配、用于过滤的 **(.)** 限定符
**历史**：跨会话共享、可搜索、子串匹配
**提示符**：可通过主题深度自定义
**别名**：全局别名、后缀别名
**数组**：索引数组与关联数组

# CAVEATS

Zsh 语法在某些方面与 bash 不同（数组下标默认从 1 开始、参数展开语法不一样）。脚本可能需要调整。

过度定制会拖慢 shell 启动。可用 **zprof** 分析性能并延迟加载插件，让交互使用更快。

默认补全系统需要用 **compinit** 初始化。多数框架会自动完成这一步。

# HISTORY

Zsh 由 **Paul Falstad** 于 **1990 年**在普林斯顿大学创建，得名于耶鲁大学教授 Zhong Shao（zsh = Zhong SHell）。它已发展为功能最丰富的 shell 之一，并从 macOS Catalina（2019 年）起成为 macOS 的默认 shell。

# INSTALL

```apt: sudo apt install zsh```

```dnf: sudo dnf install zsh```

```pacman: sudo pacman -S zsh```

```apk: sudo apk add zsh```

```zypper: sudo zypper install zsh```

```brew: brew install zsh```

```nix: nix profile install nixpkgs#zsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [fish](/man/fish)(1), [ksh](/man/ksh)(1)
