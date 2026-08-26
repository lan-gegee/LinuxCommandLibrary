# TAGLINE

Gentoo 系统 profile 管理

# TLDR

**列出**可用的 profile 符号链接目标

```eselect profile list```

**设置** /etc/portage/make.profile 符号链接

```eselect profile set [name|number]```

**显示**当前系统 profile

```eselect profile show```

# SYNOPSIS

**eselect profile** _action_ [_options_]

# DESCRIPTION

**eselect profile** 管理 Gentoo 系统上的 /etc/portage/make.profile 符号链接。该符号链接决定系统 profile，进而影响默认 USE 标志、被屏蔽的软件包以及其他 Portage 设置。

它是用于系统配置的 eselect 框架的一部分。

# PARAMETERS

**list**
> 列出可用的 profile

**set** _target_
> 将 profile 符号链接设置为指定目标

**show**
> 显示当前 profile

**--force**
> 允许设置一个目标当前不存在的 profile

# CAVEATS

仅适用于 Gentoo Linux。切换 profile 会影响默认 USE 标志、屏蔽规则和编译器设置，因此之后应运行 `emerge --update --deep --newuse @world` 重新构建受影响的内容。profile 模块属于基础 eselect 软件包，与单独打包的 repository 模块不同。

# SEE ALSO

[eselect](/man/eselect)(1), [eselect-repository](/man/eselect-repository)(1), [emerge](/man/emerge)(1)

# RESOURCES

```[Source code](https://gitweb.gentoo.org/proj/eselect.git/)```

```[Documentation](https://wiki.gentoo.org/wiki/Profile_(Portage))```

<!-- verified: 2026-07-14 -->
