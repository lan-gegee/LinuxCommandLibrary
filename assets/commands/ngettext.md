# TAGLINE

处理翻译中的复数形式

# TLDR

**按复数形式翻译**

```ngettext "[singular]" "[plural]" [count]```

**指定域进行翻译**

```ngettext -d [domain] "[singular]" "[plural]" [count]```

**使用指定的语言环境**

```LANG=[de_DE] ngettext "[1 file]" "[%d files]" [5]```

**启用转义并指定域**

```ngettext -d [domain] -e "[singular]" "[plural]" [count]```

# SYNOPSIS

**ngettext** [_options_] _singular_ _plural_ _count_

# PARAMETERS

_SINGULAR_
> 单数形式的消息。

_PLURAL_
> 复数形式的消息。

_COUNT_
> 用于选择复数形式的数字。

**-d** _DOMAIN_
> 消息域。

**-e**
> 启用转义序列。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ngettext** 处理翻译中的复数形式，是 GNU gettext 的一部分。

该工具根据数量选择正确的复数形式，遵循特定语言的复数规则。

# CAVEATS

属于 gettext 的一部分。是一个 Shell 工具。输出依赖语言环境（locale）。

# HISTORY

ngettext 是 **GNU gettext** 的一部分，为国际化程序提供复数形式支持。

# INSTALL

```apt: sudo apt install gettext-base```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gettext](/man/gettext)(1), [envsubst](/man/envsubst)(1), [msgfmt](/man/msgfmt)(1)
