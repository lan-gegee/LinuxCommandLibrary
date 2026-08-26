# TAGLINE

带 Vim 按键绑定的极简文件列表工具

# TLDR

在当前目录启动 jjj

```jjj```

在特定目录中启动 jjj

```jjj [path/to/directory]```

导航并选中一个文件，通过管道传给其他命令

```jjj | xargs [command]```

切换到选中的目录

```cd $(jjj .)```

# SYNOPSIS

**jjj** [_path_]

# DESCRIPTION

**jjj** 是一款极简、快速的终端文件导航工具，使用 **Vim** 按键绑定浏览和列出文件。你可以用 **j/k** 键快速浏览目录，并将选中的文件通过管道传给其他命令行工具做进一步处理。

该工具专为从命令行直接、以最小开销快速导航文件系统而设计。

# KEY BINDINGS

**j/k** 或 **方向键** — 向下/向上移动
**h** — 进入上级目录
**l** — 进入目录
**Enter** 或 **空格键** — 退出并返回所选路径
**r** — 刷新当前文件夹视图
**q** 或 **Esc** — 退出

# CAVEATS

功能集刻意保持精简。不支持复制、移动或删除等文件操作。

# HISTORY

**jjj** 由 **Simone Poggiali**（gibbok）创建，用 **C** 基于 ncurses 库编写。

# INSTALL

```aur: yay -S jjj```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [lf](/man/lf)(1), [ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [vifm](/man/vifm)(1)
