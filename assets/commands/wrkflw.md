# TAGLINE

在本地验证并运行 GitHub Actions 工作流

# TLDR

**启动**交互式 TUI

```wrkflw```

**验证**仓库中的工作流

```wrkflw validate```

在本地**运行**工作流

```wrkflw run [workflow.yml]```

# SYNOPSIS

**wrkflw** [*command*] [*options*]

# DESCRIPTION

**wrkflw** 使用 Docker、Podman 或安全模拟在你的机器上验证并执行 GitHub Actions 工作流。它提供 TUI 用于浏览工作流、执行日志、DAG、触发器和密钥——在推送 CI 改动之前非常有用。

# PARAMETERS

**validate**

> 对工作流文件进行结构/语法检查。

**run** *workflow*

> 使用容器或模拟后端在本地执行。

默认 TUI 模式会列出工作流和历史运行记录。监视模式与后端标志参见 **wrkflw --help**。

# CAVEATS

并非所有 GitHub 托管的能力都能离线复现（actions 市场、OIDC、服务网络）。访问 Docker socket 存在安全隐患。密钥的处理必须保持在本地。

# INSTALL

```brew: brew install wrkflw```

```nix: nix profile install nixpkgs#wrkflw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[act](/man/act)(1), [docker](/man/docker)(1), [gh](/man/gh)(1)

# RESOURCES

```[Source code](https://github.com/bahdotsh/wrkflw)```

<!-- verified: 2026-07-19 -->
