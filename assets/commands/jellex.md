# TAGLINE

使用 Python 语法过滤 JSON 和 JSON Lines 的 TUI

# TLDR

在交互式编辑器中**打开 JSON 文件**

```jellex [path/to/file.json]```

从 stdin 管道传入 JSON

```cat [path/to/file.json] | jellex```

**打开 JSON Lines 数据**

```jellex [path/to/file.jsonl]```

# SYNOPSIS

**jellex** [_file_]

# DESCRIPTION

**jellex**（Jello Explorer）是一款 TUI 程序，用于以 **Python 语法**交互式处理 JSON 和 JSON Lines 数据。它提供分栏界面：左侧的 **Editor**（编辑器）窗口用于编写 Python 查询，右侧的 **Viewer**（查看器）窗口随查询修改而实时更新。还有一个可切换的 **Schema** 视图用于显示数据结构。

在查询中，**_** 表示已加载的 JSON 数据（Python dict 或 list）。点号表示法和方括号表示法均可用于访问键名。Editor 使用标准的 **Emacs** 按键绑定。jellex 在后端使用 **jello** 执行查询。

# KEY BINDINGS

**CTRL-\\** — 在 Editor、Viewer 和 Schema 之间切换焦点
**CTRL-S** — 切换 Schema 窗口的可见性
**CTRL-Q** 或 **CTRL-C** — 退出并显示构造好的 jello 过滤器
**Tab** — 为当前上下文自动补全列表索引和键名

# CAVEATS

需要 Python 和 jello 库。使用 Python 语法而非 jq 语法，jq 用户可能不熟悉，但对 Python 开发者很友好。Python 保留关键字必须使用方括号表示法（如 `_["get"]`）。

# HISTORY

**jellex** 由 **Kelly Brazil**（kellyjonbrazil）创建，采用 **Python** 编写。它基于作者的 **jello** CLI 工具构建，增加了一层用于探索数据的交互式 TUI。

# INSTALL

```aur: yay -S jellex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jello](/man/jello)(1), [fx](/man/fx)(1), [jaq](/man/jaq)(1)
