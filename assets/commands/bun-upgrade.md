# TAGLINE

升级运行时本身

# TLDR

将 **Bun** **升级**到最新版本

```bun upgrade```

**升级到指定版本**

```bun upgrade --version [1.0.0]```

**升级到 canary 通道**

```bun upgrade --canary```

# SYNOPSIS

**bun** **upgrade** [_options_]

# PARAMETERS

**--version** _version_
> 升级到指定版本。

**--canary**
> 升级到最新的 canary（开发）构建。

# DESCRIPTION

**bun upgrade** 将 **Bun** JavaScript 运行时二进制文件原地更新到新版本。默认从官方 GitHub release 源获取最新稳定版并替换当前二进制文件。**--canary** 切换到跟踪开发分支的滚动 canary 通道，适合体验未发布功能或复现 bug 报告。**--version** 将升级（或降级）固定到某个已发布的特定版本。

该命令不会影响安装在 **node_modules** 下的项目级依赖包——那些由 **bun install** 管理。升级后，**bun --version** 应显示新版本。若 Bun 是通过包管理器（Homebrew、npm、Scoop 等）安装的，请改用对应管理器升级，以保持其记录同步。

# CAVEATS

canary 构建可能包含 bug 或破坏性变更；生产环境应固定使用稳定版。Bun 二进制文件必须对当前用户可写；系统级安装通常需要 **sudo** 或使用原始安装器。若某个版本引入了新的磁盘格式，**bun upgrade** 不会迁移 **bun.lockb** 锁文件格式。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-info](/man/bun-info)(1), [npm](/man/npm)(1), [node](/man/node)(1)
