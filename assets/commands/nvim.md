# TAGLINE

neovim，一个现代的 Vim 分支

# TLDR

**打开文件**

```nvim [file]```

**打开多个文件**

```nvim [file1] [file2]```

**在指定行号打开**

```nvim +[line] [file]```

**以 diff 模式打开**

```nvim -d [file1] [file2]```

**以只读方式打开**

```nvim -R [file]```

**启动时执行命令**

```nvim -c "[command]" [file]```

# SYNOPSIS

**nvim** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要编辑的文件。

**+**_LINE_
> 从指定行号开始。

**-c** _COMMAND_
> 加载后执行命令。

**-d**
> Diff 模式。

**-R**
> 只读模式。

**-u** _FILE_
> 使用替代配置文件。

**--headless**
> 无界面运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nvim** 即 Neovim，一个现代的 Vim 分支。支持 Lua 的可扩展文本编辑器。

该编辑器在架构上比 Vim 有所改进，拥有更好的插件系统和异步支持。

# CAVEATS

与 Vim 的差异会带来学习成本。推荐使用 Lua 配置。插件生态有所不同。

# HISTORY

Neovim 于 **2014 年**从 **Vim** 分叉而来，旨在通过更好的架构使代码库现代化。

# INSTALL

```apt: sudo apt install neovim```

```dnf: sudo dnf install neovim```

```pacman: sudo pacman -S neovim```

```apk: sudo apk add neovim```

```zypper: sudo zypper install neovim```

```brew: brew install neovim```

```nix: nix profile install nixpkgs#neovim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [vi](/man/vi)(1), [emacs](/man/emacs)(1)
