# TAGLINE

用于管理变更请求的 Git 与 Gerrit 审查界面

# TLDR

**列出所有待处理审查**（跨已配置的服务器）

```gri```

**列出**特定服务器的审查

```gri [server_name]```

**显示分配给你的审查**

```gri --mine```

**显示具有特定状态的审查**

```gri --status [open|merged|abandoned]```

# SYNOPSIS

**gri** [_options_] [_server_]

# DESCRIPTION

**gri**（Git Review Interface）是一款命令行工具，它以更易于识别哪些审查需要你关注的方式列出多个服务器上的 git 审查。它支持 **Gerrit** 和 **GitHub** 作为后端，让开发者能够通过单一终端界面管理跨多个仓库和服务器的拉取请求与代码审查。

gri 聚合变更请求并以统一视图呈现，帮助开发者跟踪未完成的审查、发现过时的变更，并安排代码审查工作的优先级。

# CAVEATS

需要 Python 3 以及为每个服务器配置好的身份验证凭据。配置通过一个指定服务器 URL 和身份验证令牌的配置文件管理。性能取决于所跟踪的服务器和变更请求数量。

# HISTORY

**gri** 作为 **pycontribs** 项目的一部分开发，旨在简化跨多个 Gerrit 和 GitHub 实例审查代码的开发者的工作流。它以 **Python** 编写，作为开源软件发布。

# INSTALL

```apt: sudo apt install gri```

```zypper: sudo zypper install gri```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1)
