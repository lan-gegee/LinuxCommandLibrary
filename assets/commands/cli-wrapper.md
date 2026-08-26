# TAGLINE

以普通命令方式启动 Mono CLI 程序集的 Debian 辅助工具

# TLDR

显示包装器的内置帮助（它刻意**不提供手册页**）

```cli-wrapper --help```

通过系统的 CLI 运行时运行 **CLI/.NET 程序集**

```cli [path/to/program.exe]```

显示 **/usr/bin/cli** 当前解析到哪个运行时

```update-alternatives --display cli```

检查包装器本身

```file $(command -v cli-wrapper)```

# SYNOPSIS

**cli-wrapper** [_options_]

# DESCRIPTION

**cli-wrapper** 是 Debian 及其衍生版上由 Mono 运行时软件包附带的一个小型辅助程序。包含 CLI（Common Language Infrastructure，即 .NET）程序集的 Debian 软件包不会把 `.exe` 文件直接放进 `/usr/bin`。它们会安装一个启动器，将该程序集交给系统当前选定的 CLI 运行时，从而让托管程序可以像其他原生命令一样被调用。

该运行时以通用名称 **cli** 通过 `update-alternatives` 注册。在典型系统上它解析为 **mono**，但任何符合规范的运行时都可以替换它，而无需改动依赖它的软件包。正是这种间接机制让 `apt` 能够独立于实际存在的运行时来安装 .NET 软件。

这个包装器非常精简，并不打算手动运行：它的存在是为了给打包工具和 alternatives 系统提供一个稳定的指向目标。

# CAVEATS

Debian 明确将此命令标记为 **UNDOCUMENTED**（未文档化）：`man cli-wrapper` 只会让你用帮助开关运行它，并引导你去查阅 Mono 文档。它的行为甚至其存在与否都因 Mono 版本而异，而且当前的 `mono-runtime` 软件包中已不再包含它，因此主要见于较旧的 Debian、Ubuntu 和 Raspbian 安装。不要在脚本中依赖它；请改用 **mono** 或通用的 **cli** alternative。

# HISTORY

该包装器可追溯到 2000 年代中期 Debian 的 CLI 政策工作，当时 `cli-common` 和 Mono 软件包引入了一种与运行时无关的方式来分发 .NET 程序集——那时 Mono、Portable.NET 和其他运行时还在相互竞争。当 Mono 成为 Debian 中唯一实用的 CLI 运行时后，这种间接机制失去了大部分意义，包装器也逐渐被弃用。

# SEE ALSO

[mono](/man/mono)(1), [update-alternatives](/man/update-alternatives)(1), [dotnet](/man/dotnet)(1)

# RESOURCES

```[Source code](https://github.com/mono/mono)```

```[Homepage](https://www.mono-project.com)```

```[Documentation](https://www.mono-project.com/docs/)```

<!-- verified: 2026-07-14 -->
