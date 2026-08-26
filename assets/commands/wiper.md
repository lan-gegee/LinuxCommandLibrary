# TAGLINE

TUI 磁盘空间分析与清理工具

# TLDR

**分析当前目录**

```wiper```

**分析指定目录**

```wiper [/home]```

**键盘导航：j/k 或方向键移动，l/Enter 进入文件夹，h/Backspace 返回上级**

```wiper```

**按两次 d 删除选中项，按 t 切换回收站模式**

```wiper```

# SYNOPSIS

**wiper** [_path_]

# PARAMETERS

**j, k, Down, Up**
> 在目录中上下移动

**l, Right, Enter**
> 进入选中的文件夹

**h, Left, Backspace**
> 返回父目录

**d**
> 删除模式（按一次选中，再按确认）

**s**
> 在按名称和按大小之间切换排序方式

**c**
> 切换渐变着色以直观展示空间占用

**t**
> 切换回收站模式（永久删除与可恢复删除）

**q**
> 退出应用

# DESCRIPTION

**wiper** 是一个基于终端的磁盘分析器，它会扫描目录并以可视化方式展示哪些文件夹占用空间最多。它提供彩色输出、文件大小指标以及用于浏览和清理磁盘占用的快捷键。支持 Linux、macOS 和 Windows。

# HISTORY

**wiper** 由 **Alexandr Kobrin**（ikebastuz）创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#wiper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dust](/man/dust)(1), [dua](/man/dua)(1), [ncdu](/man/ncdu)(1), [du](/man/du)(1)
