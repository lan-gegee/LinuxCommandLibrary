# TAGLINE

检查命令行工具是否存在及其版本

# TLDR

**检查特定工具是否可用**

```has [git] [node] [python3]```

**检查一组工具**并报告缺失项

```has [docker] [kubectl] [helm] [terraform]```

**在脚本中使用**以验证依赖

```has [make] [gcc] && echo "Ready to build"```

# SYNOPSIS

**has** _command_ [_command_...]

# DESCRIPTION

**has** 是一个简单的 shell 脚本，用于检查 PATH 上是否存在各种命令行工具，并报告它们已安装的版本。在运行构建、部署或初始化脚本之前，可以用它快速验证所有必需的依赖是否就绪。

对于作为参数传入的每个命令，**has** 会检查它是否存在于 PATH 上，并尝试确定其版本。找到的工具会连同版本号一起以绿色对勾显示，缺失的工具则以红色叉号显示。退出状态码等于未找到的命令数量。

# CAVEATS

**has** 是单个 bash 脚本，除 bash 本身之外没有任何依赖。版本检测依赖 **--version** 和 **-v** 等常见标志，未必对所有工具有效。有些工具可能以非标准格式报告版本信息。

# HISTORY

**has** 由 **Kunal Dabir**（kdabir）创建，是一个用于验证开发环境前置条件的轻量级工具。它实现为单个 **bash** 脚本，在任何类 Unix 系统上都能轻松安装。

# INSTALL

```brew: brew install has```

```nix: nix profile install nixpkgs#has```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[which](/man/which)(1), [command](/man/command)(1), [type](/man/type)(1)
