# TAGLINE

用于本地 lint 和运行流程的 Concord 工作流 CLI

# TLDR

**显示已安装的 CLI 版本**

```concord --version```

**对当前目录中的 Concord YAML 文件进行 lint**

```concord lint```

**以详细输出对指定目录中的文件进行 lint**

```concord lint -v [path/to/project]```

**在本地运行 concord.yml 中定义的默认流程**

```concord run```

**使用自定义的本地密钥目录运行**

```concord run --secret-dir=[$HOME/.my_secrets]```

# SYNOPSIS

**concord** **lint** [_options_] [_target_dir_]

**concord** **run** [_options_]

**concord** **--version**

# COMMANDS

**lint** [_dir_]
> 解析并校验 _dir_ 中的 Concord YAML 文件（默认：当前目录）。在不执行任何内容的情况下检查 DSL 语法和表达式的正确性。无法验证任务调用、参数类型或动态导入的资源。

**run**
> 在本地执行 Concord v2 流程，无需连接 Concord 服务器。当前目录中的文件会被复制到 **$PWD/target**，随后解析依赖并运行默认流程。

# PARAMETERS

**-h**, **--help**
> 显示帮助文本。

**-v**, **--verbose**
> 详细输出（lint 命令）。

**--secret-dir** _DIR_
> 本地 secret 解析器使用的目录（默认 **$HOME/.concord/secrets**）。

**--version**
> 打印 CLI 版本。

# DESCRIPTION

**concord** 是由 Walmart Labs 开发的 **Concord** 工作流编排服务器的命令行伴侣工具。该 CLI 专注于本地开发循环：

- **Lint** 会解析 **concord.yml** 及其导入的所有 YAML，验证 DSL 语法和表达式语法。它不需要正在运行的 Concord 服务器。
- **本地运行流程**会在开发者机器上执行流程，将 Maven 依赖解析到 **$HOME/.concord/depsCache**，将 Git 导入解析到 **$HOME/.concord/repoCache**。基于文件的本地 secret 从 **$HOME/.concord/secrets**（或传给 **--secret-dir** 的目录）解析。

本地执行支持标准流程元素、任务、外部依赖、Git 导入以及字符串/密钥对/凭据/文件类型的 secret。**表单**、**profile** 和**受密码保护的 secret** 目前不受支持。本地执行会将运行时强制为 **concord-v2**。

# CONFIGURATION

**concord.yml**
> 由 **lint** 和 **run** 共同消费的流程定义文件。

**$HOME/.concord/secrets/_org_/_name_**
> 本地 secret 的默认存放位置，按 org 和 secret 名称组织。可识别字符串、密钥对（**name** + **name.pub**）、凭据（JSON）和文件型 secret。

**$HOME/.concord/depsCache/**
> **concord run** 期间拉取的 Maven 依赖缓存。

**$HOME/.concord/repoCache/**
> 导入所使用的 Git 仓库缓存。

# CAVEATS

需要 **PATH** 中存在 **Java 17** 或更高版本。本地 **run** 并非完整的 Concord 服务器：表单、profile 和受密码保护的 secret 均不可用。lint 尽力而为，可能遗漏仅在运行时才暴露的错误，例如缺少任务、参数类型错误或未解析的动态导入。

# HISTORY

**Concord** 由 **Walmart Labs** 于 **2017** 年开源，是一个围绕 YAML 定义的流程和服务器运行时构建的工作流编排与持续部署平台。独立的 **concord** CLI 后来才加入，目的是让开发者无需往返 Concord 服务器即可获得快速的本地 lint 与执行循环。

# INSTALL

```brew: brew install concord```

```nix: nix profile install nixpkgs#concord```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [git](/man/git)(1), [mvn](/man/mvn)(1), [yq](/man/yq)(1)
