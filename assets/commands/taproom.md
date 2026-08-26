# TAGLINE

管理 Homebrew 软件包的交互式 TUI

# TLDR

**启动 Homebrew TUI 浏览器**

```taproom```

**启动时只显示已安装的软件包**

```taproom --filters installed```

按名称排序并隐藏帮助栏

```taproom --sort-column name --hide-help```

# SYNOPSIS

**taproom** [_options_]

# DESCRIPTION

**taproom** 是 Homebrew 的终端用户界面，可用于浏览、搜索、安装、移除 formulae 和 casks，并查看其依赖关系。它以可搜索的表格展示软件包，支持实时过滤、状态指示和递归的依赖可视化。

# CAVEATS

需要已安装 Homebrew。

# HISTORY

**taproom** 由 **Johnny Huang**（hzqtc）创建，采用 **Go** 编写。

# INSTALL

```brew: brew install taproom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[brew](/man/brew)(1), [stew](/man/stew)(1), [nix](/man/nix)(1)
