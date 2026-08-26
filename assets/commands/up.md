# TAGLINE

以交互方式编写 Linux 管道并实时预览

# TLDR

**以交互方式从命令输出构建管道**

```lshw |& up```

**以交互方式处理 CSV 数据**

```cat [data.csv] | up```

# SYNOPSIS

_command_ | **up**

# DESCRIPTION

**up**（Ultimate Plumber）让你能以交互方式构建复杂的 shell 管道：在你输入的同时即时实时预览命令结果。管道会被交给 bash 执行，因此 bash 的所有特性均可用。按 **Ctrl-X** 可将最终确定的管道保存为脚本文件。输入缓冲区上限为 40 MB。

# HISTORY

**up** 由 **Mateusz Czaplinski**（akavel）创建，使用 **Go** 语言编写。

# INSTALL

```pacman: sudo pacman -S up```

```brew: brew install up```

```nix: nix profile install nixpkgs#up```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1), [fzf](/man/fzf)(1), [pv](/man/pv)(1)
