# TAGLINE

显示单元依赖树

# TLDR

显示 **default.target** 的依赖

```systemctl list-dependencies```

显示**特定单元**的依赖

```systemctl list-dependencies [unit]```

显示**所有**依赖类型

```systemctl list-dependencies [unit] -a```

按**单元类型**过滤

```systemctl list-dependencies [unit] -t [service|socket|target|mount]```

显示**反向**依赖

```systemctl list-dependencies [unit] --reverse```

输出时不带**表头**

```systemctl list-dependencies [unit] --no-legend```

# SYNOPSIS

**systemctl list-dependencies** [_OPTIONS_] [_UNIT_...]

# PARAMETERS

**-a, --all**
> 包括所有依赖类型（不只是 Requires 和 Wants）

**-t, --type=** _TYPE_
> 按单元类型过滤

**--reverse**
> 改为显示依赖于该单元的其他单元

**--no-legend**
> 不显示表头和页脚（用于脚本）

**--no-pager**
> 禁用分页器

# DESCRIPTION

**systemctl list-dependencies** 以层级结构显示单元的依赖树。默认只显示 Requires 和 Wants 依赖。使用 `--all` 时会包含所有依赖类型（After、Before、Conflicts 等）。

`--reverse` 选项会反转视图，显示哪些单元依赖于指定单元，而不是它依赖哪些单元。

# CAVEATS

对于 default.target 这类 target，依赖树可能非常庞大。活动单元与未激活单元的标记不同。该输出反映的是配置关系，而非运行时状态。

# HISTORY

**list-dependencies** 子命令帮助理解 systemd 中复杂的依赖关系，对排查启动问题以及理解服务启动顺序至关重要。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-list-units](/man/systemctl-list-units)(1)
