# TAGLINE

高性能 monorepo 构建系统

# TLDR

**运行任务**

```turbo run [build]```

**运行多个任务**

```turbo run [build] [test]```

**使用过滤器运行**

```turbo run [build] --filter=[package-name]```

**并行运行**

```turbo run [build] --parallel```

**出错时继续**

```turbo run [build] --continue```

**显示依赖图**

```turbo run [build] --graph```

**为部署裁剪**

```turbo prune [app]```

以 Docker 优化输出进行**裁剪**

```turbo prune [app] --docker```

**绕过缓存并重新执行**

```turbo run [build] --force```

# SYNOPSIS

**turbo** _command_ [_--filter pattern_] [_options_]

# PARAMETERS

**run** _TASKS_
> 跨软件包运行指定任务。

**prune** _package_
> 为目标软件包创建 monorepo 的裁剪子集。

**-F**, **--filter** _PATTERN_
> 按名称、目录或 git 变更过滤软件包。

**--affected**
> 只在自基线分支以来有变更的软件包中运行。

**--continue**
> 出错时的继续策略（never、dependencies-successful、always）。

**--graph** _file_
> 输出依赖图（svg、html、mermaid、dot）。

**--force**
> 绕过缓存并重新执行所有任务。

**--dry**
> 仅显示任务而不执行。

**--cache-dir** _DIR_
> 设置文件系统缓存目录。

**--concurrency** _num_
> 限制并行任务数量（数字或百分比）。

# DESCRIPTION

**Turborepo** 是面向 JavaScript 和 TypeScript monorepo 的高性能构建系统。它跨多个软件包执行 build、test 和 lint 等任务，同时遵循包间依赖关系并自动维护拓扑顺序。

该工具使用基于内容的哈希来缓存任务输出，在输入未变化时跳过工作。缓存既可以在本地使用，也可以通过远程缓存在团队间共享，开发者无需重复构建他人已经构建过的内容。**--filter** 选项可针对特定软件包进行聚焦开发。

配置在仓库根目录的 **turbo.json** 中定义，用于指定任务依赖关系和缓存行为。**--graph** 选项可视化依赖结构，**prune** 则为高效部署创建 monorepo 的最小子集。

# CAVEATS

需要 turbo.json 配置。需要 monorepo 项目结构。**--parallel** 和 **--scope** 选项已弃用，请改用 **--filter** 和任务配置。

# HISTORY

**Turborepo** 由 **Jared Palmer** 创建，并于 2021 年被 **Vercel** 收购。它专注于让 monorepo 开发变得更快。

# INSTALL

```pacman: sudo pacman -S turbo```

```zypper: sudo zypper install turbo```

```nix: nix profile install nixpkgs#turbo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1), [nx](/man/nx)(1)
