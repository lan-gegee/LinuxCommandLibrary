# TAGLINE

管理 OpenCode 智能体

# TLDR

**列出**所有可用智能体

```opencode agent list```

**创建**带自定义系统提示词的新智能体

```opencode agent create [name]```

# SYNOPSIS

**opencode agent** _subcommand_ [_options_]

# DESCRIPTION

**opencode agent** 管理 OpenCode（一个基于终端的 AI 编程助手）中的智能体。智能体是带有自定义系统提示词和工具设置的配置，可为特定任务定制 AI 的行为。你可以创建新智能体、列出现有智能体，并配置它们的工具访问权限。

# CAVEATS

智能体是项目特定的，存储在本地 OpenCode 配置中。自定义智能体继承基础模型配置，但会覆盖系统提示词和可用工具。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-session](/man/opencode-session)(1), [opencode-models](/man/opencode-models)(1)
