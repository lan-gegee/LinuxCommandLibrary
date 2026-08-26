# TAGLINE

Bun 包管理器实用工具

# TLDR

**显示 bin 目录路径**

```bun pm bin```

**显示全局 bin 目录路径**

```bun pm bin -g```

**列出已安装的软件包**

```bun pm ls```

**列出所有已安装的软件包包括依赖**

```bun pm ls --all```

**输出包管理器版本**

```bun pm version```

**从 npm 或 yarn 迁移到 Bun**

```bun pm migrate```

**生成或更新 lockfile 而不安装**

```bun pm hash```

# SYNOPSIS

**bun** **pm** _subcommand_ [_options_]

# SUBCOMMANDS

**bin**
> 输出 bin 文件夹的路径。使用 **-g** 查看全局 bin 目录。

**ls**
> 列出已安装的软件包。使用 **--all** 包括传递依赖。

**version**
> 输出包管理器版本。

**migrate**
> 通过转换 lockfile 从 npm 或 yarn 迁移到 Bun。

**hash**
> 输出 lockfile 的哈希值。

**hash-print**
> 输出存储在 lockfile 中的哈希值。

**hash-string**
> 输出用于计算 lockfile 哈希的字符串。

**cache**
> 输出全局模块缓存的路径，或使用 **rm** 清空它。

# DESCRIPTION

**bun pm** 提供用于管理依赖和软件包配置的包管理器实用工具。它提供检查安装情况、从 npm/yarn 迁移项目以及处理 lockfile 和缓存的命令。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-install](/man/bun-install)(1), [bun-pm-ls](/man/bun-pm-ls)(1), [npm](/man/npm)(1)
