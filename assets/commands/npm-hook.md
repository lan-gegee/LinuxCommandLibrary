# TAGLINE

管理 npm registry 的 webhook

# TLDR

**列出 hook**

```npm hook ls```

**添加 hook**

```npm hook add [package] [url] [secret]```

**移除 hook**

```npm hook rm [id]```

**更新 hook**

```npm hook update [id] [url] [secret]```

# SYNOPSIS

**npm** **hook** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> hook 子命令。

**ls**
> 列出 hook。

**add** _PKG_ _URL_
> 添加 webhook。

**rm** _ID_
> 移除 hook。

**update** _ID_
> 更新 hook。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm hook** 管理 npm registry 的 webhook，在软件包事件发生时触发。

该命令用于配置通知，适合与 CI/CD 集成。

# CAVEATS

需要身份验证。属于 registry webhook，是企业版功能。

# HISTORY

npm hook 提供 **webhook 管理**能力，用于对 npm registry 事件做出自动响应。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1)
