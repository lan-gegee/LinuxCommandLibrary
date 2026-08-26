# TAGLINE

交互式 JSON 查看器和 jq 过滤器编辑器

# TLDR

**打开 JSON 文件**进行交互式过滤

```jnv [path/to/data.json]```

**过滤来自 stdin 的 JSON**

```cat [path/to/data.json] | jnv```

**以默认过滤器打开**

```jnv --default-filter '.[0]' [path/to/data.json]```

**使用自定义配置文件**

```jnv -c [path/to/config.toml] [path/to/data.json]```

**退出时将过滤结果写入 stdout**

```jnv --write-to-stdout [path/to/data.json]```

# SYNOPSIS

**jnv** [_OPTIONS_] [_INPUT_]

# PARAMETERS

_INPUT_
> JSON 文件路径。省略或为 "-" 时从 stdin 读取。

**-c**, **--config** _file_
> TOML 配置文件路径。

**--default-filter** _filter_
> 应用于输入数据的默认 jq 过滤器。

**--write-to-stdout**
> 退出时将当前 JSON 结果写入 stdout。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本号。

# DESCRIPTION

**jnv** 是一个交互式 JSON 查看器和 **jq** 过滤器编辑器。它采用分栏界面：顶部是过滤器编辑区，下方是语法高亮的 JSON 视图，会随着你输入 jq 过滤器实时更新。jnv 受 **jid** 和 **jiq** 启发，内部使用 **jaq** 应用过滤器，因此无需单独安装 jq。

该工具支持 JSON 文件和 JSON Lines 输入、通过 TOML 配置自定义界面、提示消息开关，以及包括防抖时间在内的响应灵敏度调节。

# CAVEATS

内部使用 jaq（而非 jq），某些高级 jq 特性或边缘情况的行为可能有所不同。大型 JSON 文件可能影响实时预览的响应速度。支持 JSON 和 JSON Lines 输入。

# HISTORY

**jnv** 由 **ynqa** 开发，使用 **Rust** 编写。相比 jid 和 jiq 等早期工具，它的目标是提供更完善、更开箱即用的交互式 JSON 探索体验。

# INSTALL

```pacman: sudo pacman -S jnv```

```brew: brew install jnv```

```nix: nix profile install nixpkgs#jnv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jaq](/man/jaq)(1), [fx](/man/fx)(1), [jiq](/man/jiq)(1)
