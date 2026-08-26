# TAGLINE

终端代码片段管理器

# TLDR

**启动片段 TUI**

```nap```

**创建新片段**

```nap "[snippet_name]"```

**列出所有片段**

```nap list```

**模糊查找并复制片段**

```nap [query]```

# SYNOPSIS

**nap** [_options_] [_query_]

# DESCRIPTION

**nap** 是一个同时提供 CLI 和 TUI 界面的代码片段管理器。TUI 让你直接在终端中浏览、管理和整理代码片段，而 CLI 则通过模糊搜索提供快速访问。

片段可以从文件或标准输入创建，按文件夹组织，并复制到剪贴板。该工具通过 **$XDG_CONFIG_HOME/nap/config.yaml** 进行配置。

# CONFIGURATION

**$XDG_CONFIG_HOME/nap/config.yaml**
> 用于配置片段存储位置和行为的配置文件。

# CAVEATS

片段存储在本地。没有内置的跨设备同步功能。

# HISTORY

**nap** 由 **maaslalani** 创建，使用 **Go** 语言和 Charm 框架编写。

# INSTALL

```brew: brew install nap```

```nix: nix profile install nixpkgs#nap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pet](/man/pet)(1)
