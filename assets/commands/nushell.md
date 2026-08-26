# TAGLINE

把数据当作结构化信息处理的现代化 shell

# TLDR

**启动 shell**

```nu```

**运行命令字符串并退出**

```nu -c "[command]"```

**运行脚本文件**

```nu [path/to/script.nu]```

**作为登录 shell 启动**

```nu --login```

**启动时不加载配置文件**

```nu -n```

**以结构化数据列出文件**（在 nu 内）

```ls | where size > 1mb | sort-by modified```

**将 JSON 转换为表格**（在 nu 内）

```open [data.json] | select name age | sort-by age```

# SYNOPSIS

**nu** [_options_] [_script_]

# PARAMETERS

**-c**, **--commands** _COMMAND_
> 执行命令字符串并退出。

**--config** _FILE_
> 指定配置文件（config.nu）。

**--env-config** _FILE_
> 指定环境配置文件（env.nu）。

**-n**, **--no-config-file**
> 启动时不加载配置文件。

**--login**, **-l**
> 作为登录 shell 启动。

**--stdin**
> 为脚本重定向 stdin。

**--table-mode** _MODE_
> 表格显示模式（rounded、basic、compact 等）。

# DESCRIPTION

**nushell**（命令名：**nu**）是一个现代 shell，它把数据视为结构化信息而不是纯文本。它将类似电子表格的数据操作带入命令行，内置支持 JSON、CSV、YAML、SQLite、Excel 等格式。

Nu 管道使用结构化数据，因此你可以每次都以相同的方式安全地进行选择、过滤和排序。它的灵感来自 PowerShell、函数式编程语言和现代 CLI 工具。它是跨平台的，对 Windows、macOS 和 Linux 提供一流支持。

# CONFIGURATION

**$nu.config-path**
> 配置文件位置（用 `$nu.config-path` 查找）。

**$nu.env-path**
> 环境配置位置（用 `$nu.env-path` 查找）。

**login.nu**
> 仅当 Nushell 作为登录 shell 启动时运行。

# CAVEATS

并非完全兼容 POSIX。部分 Bash 脚本和惯用法无法直接在 Nushell 中运行。插件生态仍在发展之中。

# HISTORY

**nushell** 由 **Yehuda Katz** 和 **Jonathan Turner** 创建，使用 **Rust** 编写。开发始于 **2019 年**。

# INSTALL

```dnf: sudo dnf install nushell```

```pacman: sudo pacman -S nushell```

```zypper: sudo zypper install nushell```

```brew: brew install nushell```

```nix: nix profile install nixpkgs#nushell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [pwsh](/man/pwsh)(1)
