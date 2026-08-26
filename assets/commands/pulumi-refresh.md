# TAGLINE

将堆栈状态与云资源同步

# TLDR

**从云端刷新状态**

```pulumi refresh```

**刷新指定堆栈**

```pulumi refresh -s [stack]```

**自动确认并刷新**

```pulumi refresh --yes```

**按 URN 刷新指定资源**

```pulumi refresh --target [urn]```

**检测到变更时刷新并失败**

```pulumi refresh --expect-no-changes```

**以 JSON 输出刷新**

```pulumi refresh --json```

# SYNOPSIS

**pulumi** **refresh** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

**--target** _urn_
> 刷新指定的资源。

**-m**, **--message** _string_
> 与更新操作关联的消息。

**-j**, **--json**
> 将刷新差异和输出序列化为 JSON。

**--expect-no-changes**
> 如果刷新期间发生任何变更则返回错误。

**--exclude** _urn_
> 在刷新中排除指定的资源（支持通配符）。

**--import-pending-creates**
> 导入在待处理操作期间创建的资源。

**--clear-pending-creates**
> 从状态中移除所有待处理的 CREATE。

**-p**, **--parallel** _n_
> 并行度（1 表示不并行）。

# DESCRIPTION

**pulumi refresh** 更新堆栈状态以匹配实际的云资源。它检测 Pulumi 状态与真实基础设施之间的漂移。当资源可能在 Pulumi 之外发生了变化时，在更新前运行此命令。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-preview](/man/pulumi-preview)(1), [pulumi-destroy](/man/pulumi-destroy)(1), [pulumi-stack](/man/pulumi-stack)(1)
