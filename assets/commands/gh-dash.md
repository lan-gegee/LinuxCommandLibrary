# TAGLINE

面向 GitHub 拉取请求和 issue 的终端 UI 仪表板

# TLDR

**打开**仪表板（需要已认证的 **gh**）

```gh dash```

**或运行**独立二进制文件

```gh-dash```

**作为 GitHub CLI 扩展安装**

```gh extension install dlvhdr/gh-dash```

# SYNOPSIS

**gh-dash** [*options*]

**gh dash** [*options*]

# DESCRIPTION

**gh-dash**（常作为 **gh** 扩展 **dash** 安装）是一个基于 Bubble Tea 的 GitHub 终端 UI。它显示可配置的拉取请求和 issue 分区，支持 vim 风格按键、PR checkout/diff/comment 工作流，以及由 YAML 配置驱动的自定义操作。

它依赖官方 **gh** CLI 进行身份验证并访问 GitHub API。查看 diff 时通常与 **delta** 集成。完整的配置和按键绑定文档见 https://gh-dash.dev。

# PARAMETERS

大多数操作都在 TUI 内交互完成。常见入口：

**gh dash**

> 通过 **gh** 扩展启动仪表板。

**gh-dash**

> 若按独立二进制方式安装，则直接启动该二进制文件。

配置通常位于用户的配置目录下（**config.yml** 的路径见文档）：分区查询、按键绑定、主题和自定义命令。

对已安装的二进制文件使用 **--help**，可查看当前版本支持的命令行选项。

# CAVEATS

需要有效的 **gh auth login** 会话以及可访问 GitHub 的网络。受 API 速率限制约束。功能范围取决于已认证用户/令牌所拥有的 GitHub 权限。

# INSTALL

```nix: nix profile install nixpkgs#gh-dash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [delta](/man/delta)(1), [lazygit](/man/lazygit)(1)

# RESOURCES

```[Source code](https://github.com/dlvhdr/gh-dash)```

```[Homepage](https://gh-dash.dev)```

```[Documentation](https://gh-dash.dev/getting-started)```

<!-- verified: 2026-07-19 -->
