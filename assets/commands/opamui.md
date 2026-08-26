# TAGLINE

用于浏览和搜索 OCaml opam 软件包的 TUI

# TLDR

**交互式浏览 opam 软件包**

```opamui```

# SYNOPSIS

**opamui**

# DESCRIPTION

**opamui** 是一个终端用户界面，用于浏览和搜索 OCaml 的 opam 软件包。它会启动一个全屏 TUI，列出来自当前所配置 opam switch 的软件包，你可以按名称过滤、查看哪些软件包已安装，并检查软件包的元数据，例如版本、简介、依赖和主页。

它**不会**安装或修改软件包——纯粹是一个只读浏览器，封装了 **opam** 的软件包列出和检查命令。

# KEY BINDINGS

**↑** / **↓**
> 在软件包列表中移动选择。

**/**
> 按子字符串过滤软件包。

**Enter**
> 打开所选软件包的元数据视图。

**q**
> 退出。

# CAVEATS

需要已安装 **opam** 并初始化了 opam switch（**opam init**）。显示的软件包集合反映当前激活的 switch；运行 **opam switch** 可查看另一组。

# HISTORY

**opamui** 由 **Nicolas Lamirault**（nlamirault）创建，使用 OCaml 编写，面向希望在不离开终端的情况下探索 opam 生态的开发者。

# SEE ALSO

[opam](/man/opam)(1)
