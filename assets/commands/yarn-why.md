# TAGLINE

解释软件包为何被安装

# TLDR

**解释**软件包为何被安装

```yarn why [package]```

**追踪**软件包的特定版本（Yarn Berry）

```yarn why [package@version]```

**显示完整的递归依赖原因**（Yarn Berry）

```yarn why [package] -R```

供脚本使用的 **JSON 输出**（Yarn Berry）

```yarn why [package] --json```

# SYNOPSIS

**yarn why** _package_ [_options_]

# DESCRIPTION

**yarn why** 解释给定软件包为何被安装在当前项目中。它会遍历依赖树并打印出最终需要目标软件包的依赖链，同时给出哈希/校验和以及磁盘占用估算。

它可以用来诊断为什么存在不需要的传递依赖，发现版本冲突（同一软件包经由不同路径被固定在不同版本），以及在发布前审计 **node_modules**。

# PARAMETERS

_package_
> 要调查的软件包名称（Yarn Berry 中也可用 **name@version**）。

**--json**
> 仅限 Yarn Berry：输出机器可读的 JSON。

**-R**, **--recursive**
> 仅限 Yarn Berry：打印完整的传递依赖树，而不只是第一个原因。

# CAVEATS

**Yarn Classic（1.x）** 与 **Yarn Berry（2+）** 的输出格式和接受的标志有所不同。递归和 JSON 选项是 Berry 的扩展功能，1.x 中不存在。该命令需要一个已安装的项目（它会读取 **node_modules** / **.pnp.cjs**），仅有 **package.json** 是不够的。

# INSTALL

```pacman: sudo pacman -S yarn```

```apk: sudo apk add yarn```

```zypper: sudo zypper install yarn```

```brew: brew install yarn```

```nix: nix profile install nixpkgs#yarn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yarn](/man/yarn)(1), [npm-explain](/man/npm-explain)(1)
