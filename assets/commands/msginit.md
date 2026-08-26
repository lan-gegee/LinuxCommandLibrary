# TAGLINE

从 POT 文件创建新的 PO 文件

# TLDR

**从 POT 创建 PO 文件**

```msginit -i [messages.pot] -o [de.po] -l [de_DE]```

**以特定语言环境创建**

```msginit --input=[template.pot] --locale=[fr_FR.UTF-8]```

**不填写译者信息创建**

```msginit -i [messages.pot] -o [es.po] -l [es] --no-translator```

**指定输出目录**

```msginit -i [messages.pot] -l [ja] -o [locale/ja/messages.po]```

# SYNOPSIS

**msginit** [_options_]

# PARAMETERS

**-i**, **--input** _file_
> 输入的 POT 文件。

**-o**, **--output-file** _file_
> 输出的 PO 文件。

**-l**, **--locale** _locale_
> 目标语言环境。

**--no-translator**
> 不提示输入译者信息。

**--no-wrap**
> 不对长行折行。

**-w** _NUMBER_
> 设置输出页面宽度（默认：79）。

**--properties-output**
> 以 .properties 格式写出 Java ResourceBundle。

# DESCRIPTION

**msginit** 从 POT（PO Template）文件创建新的 PO（Portable Object）文件。它会为指定的语言环境初始化带有正确文件头的 PO 文件。

这通常是开始一个新翻译时的第一步。

# WORKFLOW

```
1. xgettext → messages.pot
2. msginit  → de.po (new translation)
3. (translate strings)
4. msgfmt   → messages.mo
```

# EXAMPLE

```bash
# Create German translation
msginit -i messages.pot -o de.po -l de_DE.UTF-8

# Headers set automatically:
# Language: de
# Content-Type: text/plain; charset=UTF-8
```

# CAVEATS

必须先有 POT 文件（通常由 xgettext 生成）。语言环境必须是系统中的有效 locale。默认情况下，msginit 会提示输入译者的电子邮件地址；在自动化脚本中使用 **--no-translator** 跳过。输出的 PO 文件包含所有标记为未翻译的字符串（msgstr 为空）。

# HISTORY

msginit 是 **GNU gettext** 的一部分，后者是大多数开源软件用于翻译管理的国际化框架。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xgettext](/man/xgettext)(1), [msgfmt](/man/msgfmt)(1), [msgmerge](/man/msgmerge)(1), [gettext](/man/gettext)(3)
