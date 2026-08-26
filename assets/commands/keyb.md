# TAGLINE

在终端中创建并查看自定义快捷键速查表

# TLDR

**查看你的快捷键速查表**

```keyb```

**添加快捷键文件**

```keyb add [path/to/keybindings.yml]```

# SYNOPSIS

**keyb** [_command_] [_options_]

# DESCRIPTION

**keyb** 是一款用于创建和查看个性化快捷键速查表的终端工具。它让你可以直接在终端中列出和管理自定义快捷键，并提供模糊过滤和自定义布局等功能。这对于在不同工具和窗口管理器之间记录各应用专属的快捷键十分有用。

快捷键定义保存在 YAML 文件中，便于在各系统间维护和共享速查表。

# CAVEATS

快捷键定义需要手动维护。不会从正在运行的应用中自动检测快捷键。

# INSTALL

```aur: yay -S keyb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cheat](/man/cheat)(1), [tldr](/man/tldr)(1)
