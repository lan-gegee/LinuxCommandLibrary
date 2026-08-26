# TAGLINE

通过 gh-environments 扩展管理部署环境

# TLDR

**安装 gh-environments 扩展**

```gh extension install katiem0/gh-environments```

**列出某仓库的环境**

```gh environments list [owner] --repo [repo]```

**列出某所有者全部仓库的环境**

```gh environments list [owner]```

**从 CSV 文件创建环境**

```gh environments create [owner] --from-file [envs.csv]```

**将环境 secret 列表导出为 CSV**

```gh environments secrets list [owner] --repo [repo] -o [secrets.csv]```

**将环境变量列表导出为 CSV**

```gh environments variables list [owner] --repo [repo] -o [vars.csv]```

**从 CSV 文件创建环境 secret**

```gh environments secrets create --from-file [secrets.csv]```

# SYNOPSIS

**gh** **environments** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 为仓库或所有者生成包含环境及元数据的 CSV 报告。

**create**
> 从 CSV 文件创建环境及其元数据。

**secrets list**
> 生成环境 secret 的 CSV 报告。

**secrets create**
> 从 CSV 文件创建环境 secret。

**variables list**
> 生成环境变量的 CSV 报告。

**variables create**
> 从 CSV 文件创建环境变量。

# PARAMETERS

**-t**, **--token** _token_
> GitHub 个人访问令牌（覆盖 `gh auth`）。

**--hostname** _host_
> GitHub Enterprise Server 主机名。

**-o**, **--output-file** _file_
> list 命令输出 CSV 的文件名。

**-f**, **--from-file** _file_
> create 命令所用 CSV 文件的路径。

**-d**, **--debug**
> 启用调试日志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh-environments** 是一个用于批量管理仓库部署环境的 GitHub CLI 扩展。它不是内置的 `gh` 命令；请通过 `gh extension install katiem0/gh-environments` 安装。

环境表示部署目标（生产、预发布等），可附带保护规则以及特定于环境的 secret 和变量。该扩展读写 CSV 文件，适合跨多个仓库审计或复制环境配置。

若要查看控制 `gh` CLI 本身的**环境变量**，请运行 `gh help environment`。

# CAVEATS

这是第三方扩展，不是核心 `gh` 子命令。保护规则（必需审查者、等待计时器、分支限制）无法完全通过此扩展管理——高级配置请使用网页 UI 或 REST API。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-secret](/man/gh-secret)(1)
