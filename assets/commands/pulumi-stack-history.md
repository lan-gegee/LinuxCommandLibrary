# TAGLINE

查看堆栈部署历史

# TLDR

**显示堆栈部署历史**

```pulumi stack history```

**以 JSON 格式显示**

```pulumi stack history --json```

**显示指定数量的条目**

```pulumi stack history --page-size [n]```

**显示指定堆栈的历史**

```pulumi stack history -s [stack]```

# SYNOPSIS

**pulumi** **stack** **history** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈。

**--json**
> 以 JSON 格式输出。

**--page-size** _n_
> 要显示的条目数量。

**--page** _n_
> 页码。

# DESCRIPTION

**pulumi stack history** 显示堆栈的部署历史。展示更新、预览和操作，包含时间戳、结果和资源变更。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-stack](/man/pulumi-stack)(1)
