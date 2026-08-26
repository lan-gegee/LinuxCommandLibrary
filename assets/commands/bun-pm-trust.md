# TAGLINE

管理 Bun 项目中受信任的依赖

# TLDR

**运行被阻止的生命周期脚本**（针对指定软件包）并将其添加到受信任的依赖中

```bun pm trust [package1] [package2]```

**一次性信任所有**当前不受信任的依赖

```bun pm trust --all```

**列出**所有生命周期脚本被阻止的依赖

```bun pm untrusted```

**安装**软件包并在一步中信任它

```bun add --trust [package]```

# SYNOPSIS

**bun pm trust** [**--all**] [_names..._]

# PARAMETERS

**--all**
> 一次性信任所有当前不受信任的依赖，运行它们所有被阻止的生命周期脚本，并将它们添加到 **package.json** 的 **trustedDependencies** 中

# DESCRIPTION

**bun pm trust** 为指定的不受信任的依赖运行被阻止的生命周期脚本（如 **postinstall**、**preinstall** 和 **node-gyp** 构建），并将这些软件包添加到 **package.json** 的 **trustedDependencies** 数组中。

与 npm 不同，作为安全措施，Bun 默认会阻止已安装依赖执行任意生命周期脚本。当 Bun 阻止一个脚本时，它仍会安装该软件包，但会静默跳过其生命周期脚本。**bun pm trust** 命令就是你经过审查并信任某些软件包后，显式选择运行这些脚本的机制。

Bun 维护着一个已知 postinstall 脚本安全的流行软件包的默认允许列表。此默认列表仅适用于来自 npm 的软件包；来自 **file:**、**link:**、**git:** 或 **github:** 来源的软件包需要显式的 **trustedDependencies** 条目。

# CAVEATS

信任一个软件包只允许该特定软件包的生命周期脚本，不包括其依赖的依赖。每个需要运行生命周期脚本的软件包都必须单独列出。没有 **bun pm untrust** 命令；要撤销信任，你必须手动编辑 **package.json** 中的 **trustedDependencies**。由于 Bun 会静默阻止生命周期脚本，依赖 postinstall 步骤的软件包（如 **esbuild**、**sharp**、**@biomejs/biome**）可能看似安装成功，但在运行时失败。

# HISTORY

受信任依赖的工作流在 **Bun v1.0.31**（2024 年 3 月）中随 **bun add --trust** 标志和 **bun pm trust** 命令引入。早期版本在 Windows 上存在 **bun pm trust** 可能崩溃的错误，已在 **v1.1.18**（2024 年 7 月）修复。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm-cache](/man/bun-pm-cache)(1), [npm](/man/npm)(1)
