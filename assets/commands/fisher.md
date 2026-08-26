# TAGLINE

fish shell 的插件管理器

# TLDR

**安装插件**

```fisher install [jorgebucaran/nvm.fish]```

**列出已安装的插件**

```fisher list```

**更新所有插件**

```fisher update```

**移除插件**

```fisher remove [jorgebucaran/nvm.fish]```

**更新指定插件**

```fisher update [jorgebucaran/nvm.fish]```

# SYNOPSIS

**fisher** _command_ [_plugins_...]

# PARAMETERS

_COMMAND_
> 操作：install、remove、update、list。

_PLUGINS_
> 插件名（github/repo 格式）。

**install** _PLUGIN_
> 安装一个或多个插件。

**remove** _PLUGIN_
> 卸载插件。

**update**
> 更新已安装的插件。

**list**
> 列出已安装的插件。

# CONFIGURATION

**~/.config/fish/fish_plugins**
> 已安装插件的清单，方便纳入版本控制以及批量安装。

# DESCRIPTION

**fisher** 是 fish shell 的插件管理器。它能从 GitHub 仓库、本地目录或 URL 安装插件，为 fish 增添主题、函数和补全。

这款管理器非常精简，无需任何配置文件。它把插件引用记录在 fish_plugins 文件中以利于版本控制，并且能根据该文件批量安装。

fisher 会处理插件之间的依赖，并通过并行下载实现快速安装。

# CAVEATS

只能用于 fish shell。某些插件之间可能存在冲突。不会自动解析依赖。

# HISTORY

fisher 由 **Jorge Bucaran** 创建，是一个极简而快速的 fish 插件管理器。它用更简单直接的安装方式取代了旧的 Oh My Fish 框架思路。

# INSTALL

```pacman: sudo pacman -S fisher```

```apk: sudo apk add fisher```

```brew: brew install fisher```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fish](/man/fish)(1), [omf](/man/omf)(1)

# RESOURCES

```[Source code](https://github.com/jorgebucaran/fisher)```

<!-- verified: 2026-07-15 -->
