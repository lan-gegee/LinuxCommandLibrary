# TAGLINE

英文散文风格 linter

# TLDR

**检查文本文件**

```proselint [document.txt]```

**检查多个文件**

```proselint [*.md]```

**以 JSON 输出**

```proselint --json [document.txt]```

**显示版本**

```proselint --version```

**从 stdin 检查**

```cat [document.txt] | proselint```

**清除缓存**

```proselint --clean```

# SYNOPSIS

**proselint** [_options_] _files_...

# DESCRIPTION

**proselint** 是一个英文散文 linter。它检查陈词滥调、行话、冗余和常见错误等写作问题，帮助提升表达的清晰度和风格。

该工具汲取各类写作风格指南和编辑最佳实践的建议，为改进写作提供可操作的意见。

# PARAMETERS

**-j**, **--json**
> 以 JSON 格式输出。

**--config** _file_
> 配置文件路径。

**--compact**
> 紧凑的输出格式。

**-d**, **--debug**
> 输出详细信息。

**-c**, **--clean**
> 清除缓存。

**--demo**
> 对内置演示文件运行检查。

**--dump-config**
> 打印当前配置。

**--dump-default-config**
> 打印默认配置。

**-v**, **--version**
> 显示版本。

**--help**
> 显示帮助。

# CHECKS

Clichés, jargon, weasel words, redundancy, sexism, consistency, typography, hedging, archaisms, mixed metaphors, and more.

# CONFIGURATION

**~/.config/proselint/config.json**
> JSON 配置文件，通过层级式的检查选择系统启用或禁用特定检查项，类别包括 cliches、jargon、redundancy 和 typography 等。

# CAVEATS

风格建议带有主观性。可能标记有意的用法。仅支持英语。某些检查不一定适用于所有语境。

# HISTORY

**proselint** 由 **Amperser Labs** 创建，旨在将代码 lint 的理念引入散文写作。它汇集各编辑风格指南的经验，形成自动化的检查工具，适用于写作者、文档编写和内容审校。

# INSTALL

```dnf: sudo dnf install proselint```

```brew: brew install proselint```

```nix: nix profile install nixpkgs#proselint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vale](/man/vale)(1), [write-good](/man/write-good)(1), [aspell](/man/aspell)(1), [textlint](/man/textlint)(1), [hunspell](/man/hunspell)(1)
