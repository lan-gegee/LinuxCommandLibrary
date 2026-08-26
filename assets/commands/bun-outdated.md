# TAGLINE

检查过时的依赖

# TLDR

**检查过时的软件包**

```bun outdated```

**以 JSON 格式输出**

```bun outdated --json```

# SYNOPSIS

**bun** **outdated** [_options_]

# PARAMETERS

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**bun outdated** 检查项目中是否有可用更新版本的软件包。它会将已安装的版本与软件仓库中最新的可用版本进行比较。

输出内容显示每个过时软件包的当前版本、所需版本（匹配 semver 范围）以及最新版本。

# SEE ALSO

[bun](/man/bun)(1), [bun-update](/man/bun-update)(1), [bun-list](/man/bun-list)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
