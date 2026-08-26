# TAGLINE

watch 命令的现代替代品，支持 diff 历史

# TLDR

每 2 秒**监视一个命令**

```hwatch [command]```

以自定义间隔进行**监视**

```hwatch -n [5] [command]```

以彩色输出进行**监视**

```hwatch -c [command]```

**监视并高亮差异**

```hwatch -d [command]```

在输出变化时**执行动作**

```hwatch -A "[action_command]" [command]```

将 diff **输出到 stdout** 而非 TUI

```hwatch -b [command]```

# SYNOPSIS

**hwatch** [**-n** _interval_] [**-c**] [**-d**] [**-A** _command_] [**-b**] _command_

# DESCRIPTION

**hwatch** 是 **watch** 命令的现代替代品，它会记录执行结果的差异，并允许你事后回顾这段历史。它提供一个 TUI，可以滚动查看之前的输出、搜索和过滤历史，并高亮各次运行之间的差异。

主要特性包括彩色模式支持、使用 **/** 和 **\*** 键对历史进行正则过滤、通过 **-A** 选项进行变化检测（该选项会将变化信息以 JSON 形式存储在 **HWATCH_DATA** 环境变量中），以及通过 **-b** 将 diff 直接输出到 stdout 而不使用 TUI。

# CAVEATS

历史记录保存在内存中，重启后不会保留。非常频繁的间隔加上大量输出可能消耗大量内存。

# HISTORY

**hwatch** 由 **blacknon** 创建，用 **Rust** 编写。它的设计目的是解决传统 watch 命令的局限性，尤其是无法回顾或比较之前输出的问题。

# INSTALL

```brew: brew install hwatch```

```nix: nix profile install nixpkgs#hwatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1)
