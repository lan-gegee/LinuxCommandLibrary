# TAGLINE

基于 Rust 的现代进程查看器

# TLDR

**列出所有进程**

```procs```

**按名称搜索进程**

```procs [nginx]```

**监视进程**（自动刷新）

```procs --watch```

**显示树状视图**

```procs --tree```

**按 CPU 使用率排序**

```procs --sortd cpu```

**按内存使用率排序**

```procs --sortd mem```

**显示特定列**

```procs --insert [read,write]```

**显示指定用户的进程**

```procs --or "user eq [username]"```

# SYNOPSIS

**procs** [_--tree_] [_--watch_] [_--sortd column_] [_--insert columns_] [_keyword_]

# PARAMETERS

**--tree**, **-t**
> 显示父子关系的树状视图。

**--watch**, **-w**
> 自动刷新的监视模式。

**--watch-interval** _SEC_
> 刷新间隔（秒）。

**--sortd** _COLUMN_
> 按列降序排序。

**--sorta** _COLUMN_
> 按列升序排序。

**--insert** _COLUMNS_
> 添加要显示的列。

**--only** _COLUMNS_
> 只显示指定的列。

**--or** _FILTER_
> 使用 OR 逻辑过滤。

**--and** _FILTER_
> 使用 AND 逻辑过滤。

**--color** _MODE_
> 颜色模式：auto、always、disable。

**--pager** _MODE_
> 分页器：auto、always、disable。

**--config** _FILE_
> 使用指定的配置文件。

**--theme** _THEME_
> 颜色主题。

**--no-header**
> 隐藏列标题。

# DESCRIPTION

**procs** 是 ps 的现代替代品，用 Rust 编写，输出格式经过增强。它以语法高亮的方式显示进程信息，使输出更易读。

默认视图比 ps 显示更多有用的信息：命令名、PID、用户、CPU 占用、内存以及截断的命令行。颜色用于区分进程类型并突出关键词。

树状视图（-t）通过可视化缩进展示进程层次结构，无需通过 pstree 管道即可轻松查看父子关系。

监视模式（-w）提供类似 top 的实时更新。结合排序功能，有助于识别占用资源较多的进程。刷新间隔可配置。

搜索通过关键字匹配多个字段：进程名、命令行、用户。过滤器使用诸如 "cpu gt 10" 或 "user eq root" 的表达式，提供更精确的控制。

配置文件（~/.config/procs/config.toml）允许自定义列、颜色和默认选项。

# CONFIGURATION

**~/.config/procs/config.toml**
> 用户配置文件，定义默认列、颜色主题、排序方式和显示选项。

# CAVEATS

某些 ps 选项没有直接对应项。过滤器语法与 ps 不同。配置文件格式可能随版本变化。大量进程列表渲染可能较慢。终端需要支持颜色才能获得最佳体验。

# HISTORY

**procs** 由 **dalance** 于 **2019 年**前后创建，是用 Rust 重写 Unix 工具浪潮的一部分。它旨在改进 ps 过时的输出格式，同时保持熟悉的使用体验。该工具强调视觉清晰度和现代终端特性。

# INSTALL

```apt: sudo apt install procs```

```pacman: sudo pacman -S procs```

```apk: sudo apk add procs```

```zypper: sudo zypper install procs```

```brew: brew install procs```

```nix: nix profile install nixpkgs#procs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [top](/man/top)(1), [htop](/man/htop)(1), [pgrep](/man/pgrep)(1)
