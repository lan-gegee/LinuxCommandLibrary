# TAGLINE

终端交互式速查表管理器

# TLDR

**启动交互式模糊搜索菜单**

```cheatshh```

**创建新的命令分组**

```cheatshh -g```

**显示帮助**

```cheatshh -h```

# SYNOPSIS

**cheatshh** [_options_]

# DESCRIPTION

**cheatshh** 是一个交互式命令行工具，用于存储、组织和快速访问你自己的命令速查表。无需死记硬背命令，你可以将它们保存到带自定义描述的命名分组中，并通过模糊搜索器（fzf）和 whiptail 菜单调取。

除了存储的命令之外，cheatshh 还能显示 **tldr** 和 **man** 页面，并从 **cheat.sh** 等外部来源拉取示例，这些均可通过其设置进行配置。它支持添加、编辑和删除命令，收藏常用条目，以及自定义颜色和自动显示 man page。它用 shell 编写并包含 Python 组件，可运行于 Linux 和 macOS。

# PARAMETERS

**-g**
> 创建新的命令分组

**-h**, **--help**
> 显示帮助信息

# INSTALL

```aur: yay -S cheatshh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [man](/man/man)(1), [cheat](/man/cheat)(1), [fzf](/man/fzf)(1)

# RESOURCES

```[Source code](https://github.com/AnirudhG07/cheatshh)```

<!-- verified: 2026-06-22 -->
