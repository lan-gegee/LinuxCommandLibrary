# TAGLINE

显示修订历史

# TLDR

显示日志

```jj log```

显示时附带 diff

```jj log -p```

限制条目数量

```jj log -n [10]```

过滤修订

```jj log -r "[revset]"```

显示所有提交

```jj log -r "all()"```

紧凑格式

```jj log --template builtin_log_oneline```

# SYNOPSIS

**jj log** [_options_]

# PARAMETERS

**-r** _REVSET_
> 要显示的修订集。

**-p**, **--patch**
> 显示 diff。

**-n** _LIMIT_
> 最大条目数。

**--template** _TEMPLATE_
> 输出模板。

**--no-graph**
> 禁用图形显示。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj log** 显示修订历史。它以图形方式展示变更及其描述和元数据。

该命令支持用 revset 过滤。它在历史图形中可视化分支与合并。

# CAVEATS

jj 的子命令。revset 语法与 Git 不同。默认显示工作副本。

# HISTORY

jj log 是 **Jujutsu** 的一部分，基于其独特的变更模型提供修订历史查看功能。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-show](/man/jj-show)(1), [jj-evolog](/man/jj-evolog)(1)
