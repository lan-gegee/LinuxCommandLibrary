# TAGLINE

管理 Poetry 安装与插件

# TLDR

**更新 Poetry**

```poetry self update```

**添加 Poetry 插件**

```poetry self add [plugin]```

**移除 Poetry 插件**

```poetry self remove [plugin]```

**显示 Poetry 信息**

```poetry self show```

# SYNOPSIS

**poetry self** _command_ [_options_]

# PARAMETERS

**update**
> 更新 Poetry 自身。

**add** _PKG_
> 添加 Poetry 插件。

**remove** _PKG_
> 移除插件。

**show**
> 显示已安装的插件。

# DESCRIPTION

**poetry self** 用于管理 Poetry 自身的安装，与项目依赖相互独立。**update** 子命令将 Poetry 升级到最新版本，而 **add** 和 **remove** 则用于管理 Poetry 插件。

**show** 子命令列出已安装的插件及其版本。插件可以通过额外的命令或行为扩展 Poetry 的功能。该命令作用于 Poetry 自身的环境，而不是项目的虚拟环境。

# CAVEATS

修改的是 Poetry 本身的安装，而非项目依赖。

# HISTORY

poetry self 为 Poetry 提供**自我管理**能力。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1)
