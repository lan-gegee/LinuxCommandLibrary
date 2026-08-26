# TAGLINE

显示当前仓库的 GitHub/GitLab 上下文信息

# TLDR

**显示**本仓库的 issue、PR 和 CI 信息

```gitty```

在指定目录中**打开**

```gitty -p [path/to/repo]```

# SYNOPSIS

**gitty** [*options*]

# DESCRIPTION

**gitty** 根据当前仓库的 git 远程地址，输出一份简洁的远程项目信息面板——开放的 issue、pull request 以及流水线/CI 提示。由 Christian Muehlhaeuser（muesli）开发；与 **gh** 搭配使用可执行更深入的操作。

# PARAMETERS

**-p**, **--path** *dir*

> 仓库路径（默认：当前目录）。

其他标志控制服务提供方令牌和输出——参见 **gitty --help**。API 访问需要时使用 **GITHUB_TOKEN** / 主机配置。

# CAVEATS

私有仓库需要网络访问和 API 凭据。输出取决于远程托管平台（对 GitHub/GitLab 的支持程度随版本而异）。

# INSTALL

```nix: nix profile install nixpkgs#gitty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [glab](/man/glab)(1)

# RESOURCES

```[Source code](https://github.com/muesli/gitty)```

<!-- verified: 2026-07-19 -->
