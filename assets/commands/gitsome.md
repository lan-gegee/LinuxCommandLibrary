# TAGLINE

带自动补全的增强版 Git/GitHub Shell

# TLDR

**启动 gitsome shell**

```gitsome```

**查看 GitHub 动态**

```gh feed```

查看热门仓库

```gh trending [python]```

**搜索仓库**

```gh search-repos [query]```

**查看用户**

```gh user [username]```

# SYNOPSIS

**gitsome**

# DESCRIPTION

**gitsome** 是一个功能增强的 Git/GitHub 命令行界面。它提供集成 GitHub 的增强 shell，具备自动补全和语法高亮。

该工具将 Git 命令与 GitHub 功能相结合，例如查看动态、热门仓库和通知。它为 Git 命令和 GitHub 交互提供丰富的自动补全，全部封装在一个定制的 shell 环境中。

# CAVEATS

Python 工具（通过 `pip3 install gitsome` 安装，需要 Python 3.4-3.7）。GitHub 功能需要通过 `gh configure` 完成身份验证。它提供的 `gh` 命令与 GitHub 官方 `gh` CLI 无关，若两者都安装会产生冲突。该项目自上次发布（0.8.0，2019 年）以来几乎没有维护。

# HISTORY

gitsome 由 **Donne Martin** 创建，构建于 xonsh shell 之上，旨在通过自动补全和集成的 GitHub 动态为 Git 和 GitHub 用户带来增强的命令行体验。

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [hub](/man/hub)(1)

# RESOURCES

```[Source code](https://github.com/donnemartin/gitsome)```

<!-- verified: 2026-07-17 -->
