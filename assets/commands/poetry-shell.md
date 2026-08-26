# TAGLINE

激活项目虚拟环境的 shell

# TLDR

**激活项目的虚拟环境**（Poetry 1.x）

```poetry shell```

**退出**已激活的 shell

```exit```

在 Poetry 2.x 上**安装插件**（该命令不再是内置命令）

```poetry self add poetry-plugin-shell```

Poetry 2.x 上的**现代替代方案**——输出适用于你 shell 的激活命令

```eval $(poetry env activate)```

# SYNOPSIS

**poetry shell** [_options_]

# DESCRIPTION

**poetry shell** 会启动一个新的 shell 会话，并激活项目的虚拟环境。在该 shell 中运行的所有命令都将使用项目的 Python 解释器和已安装的软件包。

输入 **exit** 或按 Ctrl+D 即可离开虚拟环境 shell，返回原来的会话。如果虚拟环境不存在，会自动创建。

# CAVEATS

**已在 Poetry 2.0（2025 年 1 月）中从 Poetry 核心移除。** 在 Poetry 2.x 中，只有安装 **poetry-plugin-shell** 插件后才能使用该命令（**poetry self add poetry-plugin-shell**）。官方推荐的替代方案是 **poetry env activate**，它会输出特定于 shell 的激活命令，而不是启动子 shell——可通过 **eval**（POSIX shell）或 **Invoke-Expression**（PowerShell）执行它。

会以子进程方式创建新的子 shell；嵌套调用 **poetry shell** 会层层叠加。取决于你的 shell 配置，进入时 rc 文件可能会被重新加载。

# HISTORY

poetry shell 在 Poetry 虚拟环境中提供**交互式 shell**。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-run](/man/poetry-run)(1)
