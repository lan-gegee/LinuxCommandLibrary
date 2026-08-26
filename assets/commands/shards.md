# TAGLINE

Crystal 语言依赖管理器

# TLDR

**安装依赖**

```shards install```

**更新所有依赖**

```shards update```

**构建项目目标**

```shards build```

**检查过时的依赖**

```shards outdated```

**初始化新的 shard.yml**

```shards init```

**列出已安装的 shard**

```shards list```

**安装时不包含开发依赖**

```shards install --production```

**校验依赖是否已安装并满足要求**

```shards check```

# SYNOPSIS

**shards** _command_ [_options_] [_args_]

# SUBCOMMANDS

**install**
> 解析并将依赖安装到 lib 文件夹。

**update**
> 重新解析并更新所有依赖，重新生成 shard.lock。

**build** [_targets_]
> 将指定目标构建到 bin/ 目录。未指定时构建全部。

**check**
> 校验所有依赖已安装且版本要求得到满足。

**init**
> 在当前目录创建默认的 shard.yml。

**list**
> 显示已安装的 shard 及其版本。

**outdated**
> 列出有更新版本的依赖。

**version**
> 打印 shard.yml 中当前的 shard 版本。

# PARAMETERS

**--production**
> 跳过开发依赖，只使用锁定的版本。

**--without-development**
> 安装时跳过开发依赖。

**--skip-postinstall**
> 跳过 postinstall 脚本的执行。

**--skip-executables**
> 跳过可执行文件的安装。

**-q**, **--quiet**
> 降低日志详细程度，只打印警告和错误。

**-v**, **--verbose**
> 提高日志详细程度。

**--jobs** _N_
> 并行下载任务数。

**--frozen**
> 要求 shard.lock 为最新状态，并拒绝更新它。

**--ignore-crystal-version**
> 不检查 shard.yml 中的 Crystal 版本限制。

# DESCRIPTION

**shards** 是 Crystal 编程语言的官方依赖管理器，类似于 Ruby 的 Bundler 或 JavaScript 的 npm。它从 **shard.yml** 文件读取项目依赖，该文件定义了包元数据、版本约束和开发依赖。

依赖从 Git 仓库解析获得，GitHub 是最常见的来源。**shard.lock** 文件锁定确切的版本，确保跨环境的可重现构建。**build** 命令编译 Crystal 项目并将可执行文件放入 **bin/** 目录，而 **install** 和 **update** 则管理依赖的生命周期。

# CONFIGURATION

**shard.yml**
> 项目级配置文件，定义名称、版本、依赖和开发依赖。

**shard.lock**
> 锁定确切依赖版本的锁文件，用于可重现构建。

# CAVEATS

Crystal 生态比 Ruby 或 JavaScript 小。部分依赖可能无人维护。Crystal 版本之间可能出现二进制兼容性破坏。CI 构建建议使用 **--frozen** 标志，以确保锁文件不会被意外修改。

# HISTORY

**shards** 是类 Ruby 编译型语言 **Crystal** 的官方依赖管理器。它沿用了 Ruby 开发者熟悉的惯例。

# INSTALL

```apt: sudo apt install shards```

```pacman: sudo pacman -S shards```

```apk: sudo apk add shards```

```nix: nix profile install nixpkgs#shards```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crystal](/man/crystal)(1), [bundler](/man/bundler)(1), [cargo](/man/cargo)(1), [npm](/man/npm)(1)
