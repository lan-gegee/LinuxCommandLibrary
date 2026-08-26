# TAGLINE

Shell 脚本静态分析工具

# TLDR

**检查 shell 脚本**

```shellcheck [script.sh]```

**检查多个脚本**

```shellcheck [script1.sh] [script2.sh]```

**以特定 Shell 方言检查**

```shellcheck --shell=[bash|sh|dash|ksh] [script.sh]```

**以不同格式输出**（JSON、GCC 等）

```shellcheck --format=[json|gcc|checkstyle] [script.sh]```

**排除特定警告**

```shellcheck --exclude=[SC2034,SC2086] [script.sh]```

**从 stdin 检查脚本**

```cat [script.sh] | shellcheck -```

**启用可选检查项**

```shellcheck --enable=all [script.sh]```

# SYNOPSIS

**shellcheck** [_options_] [_script_...]

# PARAMETERS

**-s**, **--shell** _dialect_
> 指定 Shell 方言（sh、bash、dash、ksh）

**-f**, **--format** _format_
> 输出格式（tty、gcc、json、checkstyle、diff、quiet）

**-e**, **--exclude** _codes_
> 排除特定错误代码（逗号分隔）

**-i**, **--include** _codes_
> 只包含特定错误代码

**--enable** _checks_
> 启用可选检查项（all、require-variable-braces 等）

**-x**, **--external-sources**
> 跟进并检查 source 引入的文件

**-a**, **--check-sourced**
> 检查被 source 引入的文件中的问题

**-S**, **--severity** _level_
> 最低严重级别（error、warning、info、style）

**-V**, **--version**
> 显示版本

**-C**, **--color** _when_
> 输出着色（auto、always、never）。

**--wiki-link-count** _n_
> 为前 n 条警告附上 wiki 链接。

# DESCRIPTION

**shellcheck** 是一款面向 shell 脚本的静态分析工具。它能检测 bash/sh/ksh/dash 脚本中的缺陷、语法问题和常见陷阱，并提供解释和修复建议。

每条警告都有一个代码（如 SC2086），链接到详细的 wiki 文档，说明问题所在、为何重要以及如何修复。这使 shellcheck 成为学习 shell 脚本最佳实践的绝佳工具。

该工具能捕获未加引号的变量、过时语法、命令替换陷阱和潜在的安全漏洞等常见问题。它还能区分不同 Shell 方言及其特有功能。

大多数编辑器（VS Code、Vim、Emacs、Sublime）和 CI 系统都提供集成，可实现自动化的脚本检查。

# COMMON WARNINGS

**SC2086**: 加双引号以防止通配符展开和单词拆分
**SC2034**: 变量似乎未被使用
**SC2046**: 加引号以防止单词拆分
**SC2006**: 用 $(...) 代替反引号
**SC2035**: 使用 ./\* 以免模式被展开为选项
**SC2164**: 使用 cd ... || exit，以防 cd 失败

# CONFIGURATION

**.shellcheckrc**
> 项目级配置文件，用于设置默认选项、禁用的警告和 Shell 方言。也会读取 ~/.shellcheckrc。

# CAVEATS

当变量被间接使用或来自外部文件时，ShellCheck 可能产生误报。可以使用 **# shellcheck disable=SC####** 注释来抑制特定警告。

某些合法的 shell 写法会触发警告。禁用前请先审查每条警告；建议的修复方式往往确实更好。

**--external-sources** 选项需要谨慎使用，因为检查会 source 其他文件的脚本时可能执行任意代码。

# HISTORY

**ShellCheck** 由 **Vidar Holen** 创建，最初发布于约 **2012 年**。它以 **Haskell** 编写，已成为事实上的 shell 脚本 linter 标准，广泛集成于 CI 流水线和编辑器插件中。

# INSTALL

```apt: sudo apt install shellcheck```

```pacman: sudo pacman -S shellcheck```

```apk: sudo apk add shellcheck```

```brew: brew install shellcheck```

```nix: nix profile install nixpkgs#shellcheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [lint](/man/lint)(1), [ksh](/man/ksh)(1)
