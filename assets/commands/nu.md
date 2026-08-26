# TAGLINE

nushell，一个处理结构化数据的现代化 shell

# TLDR

**启动 Nushell**

```nu```

**执行命令**

```nu -c "[command]"```

**运行脚本**

```nu [script.nu]```

**以表格列出文件**

```ls | where size > 1mb```

**解析 JSON**

```open [file.json] | get [field]```

# SYNOPSIS

**nu** [_options_] [_script_]

# PARAMETERS

_SCRIPT_
> 要执行的 Nushell 脚本（以 **.nu** 结尾的文件）。其余位置参数可通过 `$argv` 访问。

**-c**, **--commands** _COMMAND_
> 运行给定的 Nushell 命令字符串然后退出。

**--config** _FILE_
> 加载 _FILE_ 而不是默认的 `config.nu`。

**--env-config** _FILE_
> 加载 _FILE_ 作为环境变量设置配置（`env.nu`）。

**--login**, **-l**
> 作为登录 shell 启动（加载 `login.nu`）。

**--interactive**, **-i**
> 即使 stdin 不是 TTY 也强制进入交互模式。

**--no-config-file**, **-n**
> 跳过加载任何配置文件。

**--no-std-lib**
> 跳过加载内置的标准库。

**--stdin**
> 从 stdin 读取脚本。

**--table-mode**, **-m** _MODE_
> 设置表格渲染模式（如 **rounded**、**heavy**、**light**、**compact**、**none**）。

**--log-level** _LEVEL_
> 设置日志级别（**trace**、**debug**、**info**、**warn**、**error**）。

**--ide-check** _N_
> 对输入进行适合 IDE 的语法检查。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# CONFIGURATION

**$nu.default-config-dir/config.nu**
> 用户级配置（通常是 **~/.config/nushell/config.nu**）。

**$nu.default-config-dir/env.nu**
> 用户级环境变量设置，先于 `config.nu` 加载。

# DESCRIPTION

**nu** 即 **Nushell**，是一个跨平台 shell，把每条命令的输出视为流经管道的**结构化数据**（表格、记录、列表）。内置命令可将常见格式（JSON、YAML、TOML、CSV、SQLite、ODS、XLSX、XML、NDJSON）解析为同一类表格类型，因此 `where`、`sort-by`、`select`、`group-by` 和 `histogram` 等命令可以统一作用于各种数据源。

管道传递的是带类型的值而非字节流，这让数据处理更具表达力，但也意味着混合任意字节流的传统 Unix 管道行为会有所不同——用 `^cmd` 包装外部命令可获得原始 stdout，或用 `into binary` / `into string` 做显式转换。

# CAVEATS

不兼容 POSIX——为 **bash**/**zsh** 编写的脚本无法不加修改地运行。配置文件使用 Nushell 自己的语言。插件协议和内置命令名称在小版本之间仍可能变化（Nushell 尚未到 1.0）；编写脚本时应固定版本。

# HISTORY

**Nushell** 由 **Jonathan Turner**、**Yehuda Katz** 和 **Andrés Robalino** 于 **2019 年**创建，旨在把 PowerShell 风格的结构化管道带到一个对 Unix 友好、由 Rust 实现的 shell 中。目前由 **Nushell Project** 以 **MIT 许可证**维护。

# INSTALL

```dnf: sudo dnf install nushell```

```pacman: sudo pacman -S nushell```

```apk: sudo apk add nushell```

```zypper: sudo zypper install nushell```

```brew: brew install nushell```

```nix: nix profile install nixpkgs#nushell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [pwsh](/man/pwsh)(1)
