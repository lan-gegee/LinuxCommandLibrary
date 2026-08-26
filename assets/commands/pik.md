# TAGLINE

查找并杀死进程的交互式 TUI 工具

# TLDR

**启动交互式进程选择器**

```pik```

**按名称过滤进程**

```pik [process_name]```

# SYNOPSIS

**pik** [_options_] [_pattern_]

# DESCRIPTION

**pik** (Process Interactive Kill) 是一个交互式查找并杀死进程的终端工具。它的作用类似 **pkill**，但提供一个实时交互式搜索界面：输入字符过滤进程，再选择要杀死的对象。它支持针对参数和端口的前缀搜索、可配置的 readline 风格按键映射，并可跨平台运行。

# HISTORY

**pik** 由 **Jacek Kurlit**（jacek-kurlit）创建，用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S pik```

```zypper: sudo zypper install pik```

```nix: nix profile install nixpkgs#pik```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkill](/man/pkill)(1), [kill](/man/kill)(1), [htop](/man/htop)(1), [procs](/man/procs)(1)
