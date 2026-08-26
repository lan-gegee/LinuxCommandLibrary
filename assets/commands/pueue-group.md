# TAGLINE

管理 pueue 任务执行分组

# TLDR

**列出分组**

```pueue group```

**创建分组**

```pueue group add [name]```

**删除分组**

```pueue group remove [name]```

**设置并行任务数**

```pueue parallel [N] --group [name]```

# SYNOPSIS

**pueue group** [_subcommand_] [_options_]

# PARAMETERS

**add** _NAME_
> 创建分组。

**remove** _NAME_
> 删除分组。

# DESCRIPTION

**pueue group** 管理任务执行分组。分组可将任务组织成多个独立队列，各自拥有独立的并行度设置。分组可用 **add** 创建、用 **remove** 删除。每个分组的任务独立运行，因此可以将 CPU 密集型分组限制为单任务执行，而让 I/O 密集型分组大量并行。

# CAVEATS

存在默认分组。pueue 的一部分。

# HISTORY

**pueue group** 是 **pueue** 任务管理器的一部分，提供任务分组以实现独立的队列管理。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-parallel](/man/pueue-parallel)(1)
