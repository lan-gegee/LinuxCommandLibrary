# TAGLINE

将消息目录文件从人类可读的 PO 格式编译为二进制 MO 格式

# TLDR

**将 PO 文件编译为 MO**

```msgfmt -o [messages.mo] [messages.po]```

**检查 PO 文件中的错误**

```msgfmt --check [messages.po]```

**详细输出**

```msgfmt -v -o [messages.mo] [messages.po]```

**生成统计信息**

```msgfmt --statistics [messages.po]```

**编译所有 PO 文件**

```for f in *.po; do msgfmt -o "${f%.po}.mo" "$f"; done```

# SYNOPSIS

**msgfmt** [_options_] _file_.po ...

# PARAMETERS

**-o** _file_
> 输出文件。

**-c**, **--check**
> 检查错误。

**-v**, **--verbose**
> 详细输出。

**--statistics**
> 显示翻译统计信息。

**-f**, **--use-fuzzy**
> 包含 fuzzy 翻译。

**--strict**
> 严格模式。

# DESCRIPTION

**msgfmt** 将消息目录文件从人类可读的 PO（Portable Object）格式编译为 gettext 在运行时使用的二进制 MO（Machine Object）格式。

这是使用 GNU gettext 本地化应用程序过程中的关键一步。

# WORKFLOW

```
xgettext → POT file (template)
msginit  → PO file (translations)
msgfmt   → MO file (binary)
```

# EXAMPLE

```bash
# Compile with checking
msgfmt --check --statistics -o locale/de/LC_MESSAGES/app.mo de.po

# Result: 150 translated, 3 fuzzy, 2 untranslated
```

# CAVEATS

PO 中的语法错误会阻止编译。默认排除 fuzzy 翻译。输出编码必须与系统匹配。

# HISTORY

msgfmt 是 **GNU gettext** 的一部分，后者是 Unix 上标准的国际化系统，作为 GNU 计划的一部分而开发。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xgettext](/man/xgettext)(1), [msginit](/man/msginit)(1), [msgmerge](/man/msgmerge)(1), [gettext](/man/gettext)(1)
