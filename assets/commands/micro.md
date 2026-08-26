# TAGLINE

现代终端文本编辑器

# TLDR

**打开文件**

```micro [file.txt]```

**跳转到指定行打开**

```micro [file.txt]:[line]```

**打开多个文件**

```micro [file1.txt] [file2.txt]```

**对比文件差异**

```micro -diff [file1] [file2]```

**只读模式**

```micro -readonly [file.txt]```

**显示版本**

```micro -version```

# SYNOPSIS

**micro** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要编辑的文件。可在文件名后附加 `:LINE` 或 `:LINE:COL` 以跳转到相应位置；`+LINE` 参数同样有效。

**-clean**
> 移除所有配置文件（谨慎使用）。

**-config-dir** _PATH_
> 覆盖默认配置目录（`~/.config/micro`）。

**-options**
> 将所有可用的全局选项打印到标准输出后退出。

**-debug**
> 打开编辑器时显示日志缓冲区（`Ctrl-E logbuffer`）。

**-readonly**
> 只读模式。

**-plugin** _CMD_ [_PLUGIN..._]
> 管理插件：`install`、`remove`、`update`、`list`、`available`、`search`。

**-multiopen** _GLOB_
> 打开匹配 glob 模式的所有文件。

**-version**
> 显示版本信息并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**micro** 是一个用 Go 编写的现代终端文本编辑器，目标是兼具 nano 的易用性与更丰富编辑器的强大功能。它支持常见快捷键（`Ctrl-S`、`Ctrl-C`、`Ctrl-V`、`Ctrl-Z`）、鼠标选择、多光标、分屏窗格、130 多种文件类型的语法高亮以及基于 Lua 的插件系统。

设置存储在 `~/.config/micro/settings.json`，按键绑定存储在同目录下的 `bindings.json` 中。大多数编辑器命令也可通过 `Ctrl-E` 打开命令栏来调用。

# CAVEATS

单个静态二进制文件；无外部依赖。插件系统基于 Lua，对需要 vim 式模态编辑的用户可能不适用。

# HISTORY

Micro 由 **Zachary Yedidia** 创建，是 nano 和 vim 的现代化直观替代品。

# INSTALL

```apt: sudo apt install micro```

```dnf: sudo dnf install micro```

```pacman: sudo pacman -S micro```

```apk: sudo apk add micro```

```brew: brew install micro```

```nix: nix profile install nixpkgs#micro```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [vim](/man/vim)(1), [emacs](/man/emacs)(1)
