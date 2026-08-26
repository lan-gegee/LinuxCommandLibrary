# TAGLINE

ls 的配色方案配置工具

# TLDR

**输出用于设置** LS_COLORS 的 Shell 命令

```dircolors```

**使用指定的数据库文件**

```dircolors [/path/to/dircolors.db]```

**输出 Bourne shell 命令**

```dircolors -b```

**输出 C shell 命令**

```dircolors -c```

**打印默认数据库**

```dircolors -p```

# SYNOPSIS

**dircolors** [_options_] [_file_]

# PARAMETERS

**-b**, **--sh**, **--bourne-shell**
> 输出 Bourne shell 命令。

**-c**, **--csh**, **--c-shell**
> 输出 C shell 命令。

**-p**, **--print-database**
> 打印默认数据库。

# CONFIGURATION

**~/.dircolors** 或 **~/.dir_colors**
> 用户专属的颜色配置数据库，将文件类型和扩展名映射到颜色。

**/etc/DIR_COLORS**
> 系统级默认颜色配置。

# DESCRIPTION

**dircolors** 输出用于设置 LS_COLORS 环境变量的 Shell 命令，该变量控制 **ls** 等工具使用的颜色。它会读取一个将文件类型和扩展名映射到颜色的配置文件。

通常在 Shell 配置文件中这样调用：**eval "$(dircolors)"**。

# CAVEATS

输出必须由 Shell 求值（如 `eval "$(dircolors)"`）才能生效。默认数据库覆盖常见文件类型；可通过 `dircolors -p > ~/.dircolors` 生成副本并编辑来自定义。只影响读取 LS_COLORS 的工具（主要是 GNU ls 及兼容工具）。

# HISTORY

**dircolors** 是 GNU coreutils 的一部分，自终端彩色输出的早期便已包含在 Linux 发行版中。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [dir](/man/dir)(1)
