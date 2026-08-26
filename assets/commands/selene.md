# TAGLINE

用 Rust 编写的快速 Lua 代码检查器

# TLDR

**检查当前目录中的 Lua 文件**

```selene .```

**检查指定文件**

```selene [path/to/file1.lua] [path/to/file2.lua]```

**使用自定义配置文件检查**

```selene --config [path/to/selene.toml] [path/to/files]```

**检查并抑制摘要**信息

```selene --no-summary [path/to/files]```

以安静输出**检查**，只显示必要信息

```selene --quiet [path/to/files]```

以 JSON 输出进行**检查**，便于工具集成

```selene --display-style json [path/to/files]```

**校验配置文件**是否有错误

```selene validate-config```

# SYNOPSIS

**selene** [_flags_] [_options_] _files_...

**selene** _subcommand_

# PARAMETERS

**--allow-warnings**
> 只出现警告（无错误）时正常退出。

**--color** _color_
> 控制彩色输出。可选值：**Always**、**Auto**、**Never**。默认：**Auto**。

**--config** _config_
> TOML 配置文件路径。默认为当前目录下的 **selene.toml**。

**--display-style** _style_
> 设置输出显示格式。可选值：**Json**、**Json2**、**Rich**、**Quiet**。

**--num-threads** _n_
> 使用的线程数量。默认为逻辑 CPU 核心数。

**--pattern** _pattern_
> 用于匹配待检查文件的 glob 模式。可多次指定。

**--no-exclude**
> 不遵循配置中的排除模式。

**-n**, **--no-summary**
> 抑制检查结束时的摘要信息。

**-q**, **--quiet**
> 仅显示必要信息。等同于 **--display-style=quiet**。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# SUBCOMMANDS

**validate-config**
> 报告 selene 配置文件中的任何错误。

**capabilities**
> 打印当前 selene 构建的能力特性。

**generate-roblox-std**
> 生成 Roblox 标准库定义。

**update-roblox-std**
> 更新 Roblox 标准库定义。

**upgrade-std**
> 将标准库格式升级到最新版本。

**help**
> 打印 selene 或特定子命令的帮助。

# DESCRIPTION

**selene** 是一款用 Rust 编写的快速、现代的 Lua 代码检查器。它分析 Lua 代码，在运行时之前检测 bug、风格问题和潜在问题。该工具通过可配置的标准库支持标准 Lua 以及 Luau（Roblox 的 Lua 方言）。

配置通过 **selene.toml** 文件完成，你可以在其中启用或禁用特定的 lint 规则、设置严重级别并配置标准库定义。借助其 JSON 输出模式，该检查器可以很好地与编辑器和 CI/CD 流水线集成。

selene 在 Roblox 开发社区中尤为流行，但也适用于任何 Lua 项目。它可以扩展自定义 lint 规则和标准库定义。

# CONFIGURATION

**selene.toml**
> 项目级配置文件，指定启用的 lint 规则、严重级别、标准库定义和文件排除模式。

**std**
> selene.toml 中的配置键，指定 Lua 标准库变体（例如 "lua51"、"lua52"、"luau" 或自定义定义文件）。

# CAVEATS

selene 需要一个 **selene.toml** 配置文件来自定义行为。没有配置文件时，它会使用可能与你的 Lua 变体或编码规范不匹配的默认设置。对于 Luau/Roblox 项目，需要生成或配置相应的标准库定义。

# HISTORY

**selene** 由 Kampfkarren（Lucas）创建，作为开源项目首次发布于 GitHub。它出于性能和安全性考虑采用 Rust 编写，在 Roblox 开发社区尤其受欢迎——在那里，快速可靠的 Lua 检查至关重要。该项目持续活跃开发，定期发布新版本，增加对新 Luau 特性和更多 lint 规则的支持。

# INSTALL

```pacman: sudo pacman -S selene```

```brew: brew install selene```

```nix: nix profile install nixpkgs#selene```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[luacheck](/man/luacheck)(1), [stylua](/man/stylua)(1), [lua](/man/lua)(1)
