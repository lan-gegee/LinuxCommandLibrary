# TAGLINE

国际化消息目录查找工具

# TLDR

**显示翻译后的字符串**

```gettext [domain] "[message]"```

**从目录翻译**

```TEXTDOMAIN=[domain] gettext "[message]"```

**带上下文**

```gettext -c "[context]" "[message]"```

**复数形式**

```ngettext "[singular]" "[plural]" [count]```

# SYNOPSIS

**gettext** [_options_] [_domain_] _msgid_

# PARAMETERS

_DOMAIN_
> 消息目录域。

_MSGID_
> 待翻译的消息。

**-d** _DOMAIN_
> 文本域。

**-e**
> 启用转义序列解释。

**-E**
> 保留反斜杠但不解释。

**-c** _CONTEXT_
> 消息上下文。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gettext** 从消息目录中检索翻译后的字符串。它是 GNU 国际化系统的运行时组件，根据当前区域设置（locale）查找翻译。

该工具在 .mo 文件中搜索翻译，找不到时返回原文。它让 shell 脚本和程序能够产生本地化的输出。

gettext 为命令行应用程序提供国际化能力。

# CONFIGURATION

**/usr/share/locale/[LANG]/LC_MESSAGES/[domain].mo**
> 已编译的消息目录，包含特定域和区域设置的翻译。

# CAVEATS

需要已编译的 .mo 目录文件。必须设置 LANG/LC_MESSAGES。缺失的翻译会返回原文。

# HISTORY

gettext 由 **GNU** 为国际化而开发。它成为 Unix 上标准的本地化系统，使软件能够支持多种语言。

# INSTALL

```apt: sudo apt install gettext-base```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xgettext](/man/xgettext)(1), [msgfmt](/man/msgfmt)(1), [envsubst](/man/envsubst)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gettext/)```

```[Documentation](https://www.gnu.org/software/gettext/manual/gettext.html)```

<!-- verified: 2026-07-15 -->
