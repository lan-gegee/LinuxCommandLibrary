# TAGLINE

系统级 locale 与语言配置

# TLDR

**列出**可用的 locale

```eselect locale list```

**按名称设置** LANG 环境变量

```eselect locale set [en_US.utf8]```

**按编号设置** LANG 环境变量

```eselect locale set [4]```

**显示**当前的 LANG 值

```eselect locale show```

# SYNOPSIS

**eselect locale** _action_ [_options_]

# DESCRIPTION

**eselect locale** 管理 Gentoo 系统上的 LANG 环境变量。它通过修改 /etc/env.d/02locale 来设置系统级的语言和 locale。更改之后，需运行 `env-update && source /etc/profile` 使其生效。

它是用于系统配置的 eselect 框架的一部分。

# PARAMETERS

**list**
> 列出可用的 locale。

**set** _target_
> 将 LANG 设置为指定的 locale（按名称或编号）。

**show**
> 显示当前的 LANG 设置。

# CAVEATS

仅适用于 Gentoo Linux。locale 必须先用 locale-gen 生成。更改需要运行 env-update 并重新加载 profile 或重新登录后才能生效。

# SEE ALSO

[eselect](/man/eselect)(1), [locale](/man/locale)(1), [locale-gen](/man/locale-gen)(8)
