# TAGLINE

漂亮时尚的现代终端文件管理器

# TLDR

**启动文件管理器**

```spf```

**在指定目录中打开**

```spf [/path/to/dir]```

**在给定路径打开多个面板**

```spf [/path/one] [/path/two]```

**打印配置和数据文件路径**

```spf path-list```

**使用自定义配置文件**

```spf --config-file [/path/to/config.toml]```

**使用自定义快捷键文件**

```spf --hotkey-file [/path/to/hotkeys.toml]```

**打印版本号**

```spf --version```

# SYNOPSIS

**spf** [_options_] [_PATH_...]

**spf** **path-list** [**--lastdir-file**]

# PARAMETERS

**--config-file**, **-c** _PATH_
> 使用其他配置文件。

**--hotkey-file**, **-hf** _PATH_
> 使用其他快捷键配置文件。

**--chooser-file**, **-cf** _PATH_
> 将已打开文件的路径写入此文件并退出。

**--print-last-dir**, **-pld**
> 退出时将最后一个目录打印到标准输出（用于退出时切换目录的集成）。

**--fix-hotkeys**, **-fh**
> 将缺失的快捷键补充到快捷键配置文件。

**--fix-config-file**, **-fch**
> 将缺失的字段补充到配置文件。

**--debug-info**, **-di**
> 打印调试信息。

**--version**, **-v**
> 打印版本号。

**path-list**, **pl**
> 打印配置、快捷键、日志和数据目录的路径。

# DESCRIPTION

**superfile** 是一款基于终端的文件管理器，支持多面板同时查看目录、自定义主题、Vim 键位、剪贴板查看器和进程列表。可用于 Linux、macOS 和 Windows。

面板可以用 Tab 分割和导航。按 **>** 可打开内置命令提示符，执行 SPF 模式命令，如 `split` 和 `open <PATH>`。

# HISTORY

**superfile** 由 **yorukot** 创建，使用 **Go** 语言和 Bubble Tea 框架编写。

# INSTALL

```pacman: sudo pacman -S superfile```

```brew: brew install superfile```

```nix: nix profile install nixpkgs#superfile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1), [yazi](/man/yazi)(1), [vifm](/man/vifm)(1)
