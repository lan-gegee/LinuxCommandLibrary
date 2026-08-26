# TAGLINE

支持类 vim 导航的命令行 JSON 查看器

# TLDR

**查看 JSON 文件**

```jless [file.json]```

**从 stdin 查看 JSON**

```cat [file.json] | jless```

**查看 YAML 文件**

```jless --yaml [file.yaml]```

**以数据模式启动**（默认）

```jless -m data [file.json]```

**以行模式启动**

```jless -m line [file.json]```

**截断长字符串**

```jless --truncate [file.json]```

**以 scrolloff 模式打开**

```jless --scrolloff [5] [file.json]```

# SYNOPSIS

**jless** [_options_] [_file_]

# PARAMETERS

**-m**, **--mode** _mode_
> 初始查看模式：data 或 line。

**--yaml**
> 将输入解析为 YAML 而非 JSON。

**--json**
> 将输入解析为 JSON（默认）。

**--truncate**
> 在显示中截断长字符串。

**--scrolloff** _lines_
> 光标上方/下方的最少保留行数。

**-n**, **--line-numbers**
> 显示行号。

**-N**, **--no-line-numbers**
> 隐藏行号。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# KEYBOARD COMMANDS

**j**/**k** 或 **Down**/**Up**
> 向下/向上移动光标。

**h**/**l** 或 **Left**/**Right**
> 折叠/展开对象，或向外/向内移动。

**H**/**L**
> 聚焦父节点/第一个子节点。

**g**/**G**
> 跳转到第一个/最后一个元素。

**Space**
> 切换当前节点的折叠状态。

**c**
> 折叠所有节点。

**e**
> 展开所有节点。

**/**
> 向前搜索。

**?**
> 向后搜索。

**n**/**N**
> 下一个/上一个搜索结果。

**y**
> 复制（yank）当前值。

**.**
> 重复上一条命令。

**:q** 或 **q**
> 退出。

# DESCRIPTION

**jless** 是一个支持类 vim 导航的命令行 JSON 查看器。它提供语法高亮、可折叠节点和搜索功能，便于浏览 JSON 和 YAML 数据。

它有两种查看模式：**数据模式**以树状视图呈现可折叠的对象和数组，而**行模式**则显示原始格式化输出。可以使用 **-m** 在两种模式间切换或指定启动模式。

导航遵循 vim 约定。使用 **h**/**j**/**k**/**l** 移动光标，用 **Space** 切换节点展开状态，用 **c**/**e** 批量折叠/展开。使用 **/** 搜索，并用 **n**/**N** 在搜索结果间跳转。

**yank** 命令会将当前位置的值复制到剪贴板，适合从大型结构中提取特定数据。

jless 通过惰性解析和渲染高效处理大文件，因此也适用于数十 MB 的 JSON 文件。

# CAVEATS

需要终端支持 256 色才能获得最佳显示效果。部分终端可能不支持 yank 的剪贴板集成。嵌套极深的结构可能影响导航性能。YAML 支持需要显式指定 --yaml 标志。

# HISTORY

jless 由 **Paul Julius Martinez** 创建，于 **2022 年**首次发布。它使用 Rust 编写，旨在填补类 vim 导航的专用 JSON 浏览工具这一空白。该项目作为 jq 的补充，在交互式 JSON 探索场景中广受欢迎，目前仍在持续开发中，不断加入 YAML 支持等改进。

# INSTALL

```pacman: sudo pacman -S jless```

```apk: sudo apk add jless```

```zypper: sudo zypper install jless```

```brew: brew install jless```

```nix: nix profile install nixpkgs#jless```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [gojq](/man/gojq)(1), [fx](/man/fx)(1), [less](/man/less)(1)
