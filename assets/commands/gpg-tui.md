# TAGLINE

用于 GnuPG 密钥管理的终端用户界面

# TLDR

**启动 gpg-tui**

```gpg-tui```

**指定要使用的密钥环**

```gpg-tui --homedir [~/.gnupg]```

**使用指定的样式**

```gpg-tui --style [colored]```

**导出输出格式**

```gpg-tui --output-format [minimal]```

# SYNOPSIS

**gpg-tui** [_options_]

# PARAMETERS

**--homedir** _DIR_
> 将 _DIR_ 用作 GnuPG 主目录（覆盖 **GNUPGHOME**）。

**-c**, **--color** _COLOR_
> 设置强调色（例如 _gray_、_red_、_green_、_blue_ 或十六进制值）。

**-s**, **--style** _STYLE_
> 设置表格边框样式：_plain_、_bold_、_double_ 或 _light_。

**-d**, **--detail-level** _LEVEL_
> 密钥的初始详细级别：_minimum_、_standard_ 或 _full_。

**-r**, **--no-tty**
> 在无 TTY 交互的情况下运行（管道场景下很有用）。

**-x**, **--select** _SELECTION_
> 启动时预选中某些行（密钥 ID 或指纹）。

**--splash**
> 启动时显示启动画面。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**gpg-tui** 是一个用于管理 GnuPG 密钥的终端用户界面。它用 Rust 编写，提供交互式界面来列出、查看、导入、导出、签名、编辑和删除密钥，无需记忆复杂的 gpg 命令行选项。

该工具从标准 GnuPG 密钥环读取数据，并支持多种视觉样式以自定义显示效果。

# INSTALL

```pacman: sudo pacman -S gpg-tui```

```apk: sudo apk add gpg-tui```

```zypper: sudo zypper install gpg-tui```

```brew: brew install gpg-tui```

```nix: nix profile install nixpkgs#gpg-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [gpg2](/man/gpg2)(1)
