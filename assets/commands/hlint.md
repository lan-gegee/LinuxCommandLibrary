# TAGLINE

针对 Haskell 源代码提出改进建议的工具

# TLDR

显示 Haskell 文件的**建议**

```hlint [path/to/file.hs]```

检查所有 Haskell 文件并生成**报告**

```hlint [path/to/directory] -r```

**自动应用**大部分建议

```hlint [path/to/file.hs] --refactor```

显示额外的**重构选项**

```hlint [path/to/file.hs] --refactor-options```

生成一个忽略所有当前提示的**设置文件**

```hlint [path/to/file.hs] --default > .hlint.yaml```

使用**所有可用处理器**运行

```hlint [path/to/directory] -j```

**忽略特定提示**

```hlint [path/to/file.hs] --ignore="Use camelCase"```

以 **JSON** 格式输出建议

```hlint [path/to/file.hs] --json```

# SYNOPSIS

**hlint** [_options_] [_files_]

# PARAMETERS

**-r**, **--report**[**=**_FILE_]
> 生成建议的 HTML 报告（默认：report.html）

**--refactor**
> 自动应用建议，使用 apply-refact 的 `refactor` 工具

**--refactor-options** _OPTIONS_
> 向 `refactor` 可执行文件传递额外选项

**-d**, **--default**
> 将忽略当前所有已触发提示的默认 .hlint.yaml 打印到 stdout

**-h**, **--hint** _FILE_
> 使用指定文件中的提示规则

**-i**, **--ignore** _HINT_
> 忽略特定提示

**-s**, **--show**
> 显示所有提示，包括通常跳过的提示

**-j**[_N_], **--threads**[**=**_N_]
> 在 N 个处理器上运行（默认：1；单独的 -j 使用所有物理核心）

**-c**, **--colour**, **--color**[**=**_always|never|auto_]
> 控制彩色输出

**--json**
> 以 JSON 输出提示数据

**--sarif**
> 以 SARIF 输出提示数据

**-f**, **--find** _FILE_
> 在 Haskell 文件中搜索可转化为新提示规则的模式

**-X** _EXTENSION_, **--language** _EXTENSION_
> 启用或禁用 GHC 语言扩展（例如 -XNoCPP）

**--cpp-define** _NAME_[**=**_VALUE_], **--cpp-include** _DIR_
> 配置对输入文件运行的 cpphs C 预处理器

# DESCRIPTION

**hlint** 是一个为 Haskell 源代码提出改进建议的工具。它分析代码并基于常见的 Haskell 惯用法给出简化、消除冗余和改进风格的建议。

建议内容包括简化表达式、移除不必要的扩展、应用标准库函数以及遵循最佳实践。该工具可以通过重构模式自动应用其中的许多建议。

配置文件（.hlint.yaml）允许按项目自定义要应用或忽略哪些提示。

# CAVEATS

并非所有建议都适用于每个代码库。某些提示可能与特定的编码规范或性能要求相冲突。提交前务必审查自动化重构所做的改动。

# HISTORY

hlint 由 Neil Mitchell 创建，约在 **2006 年**首次发布。它已成为 Haskell 生态系统中维护代码质量的标准工具，通常集成到 CI 流水线和编辑器插件中。

# INSTALL

```apt: sudo apt install hlint```

```dnf: sudo dnf install hlint```

```pacman: sudo pacman -S hlint```

```apk: sudo apk add hlint```

```zypper: sudo zypper install hlint```

```brew: brew install hlint```

```nix: nix profile install nixpkgs#hlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1)

# RESOURCES

```[Source code](https://github.com/ndmitchell/hlint)```

```[Documentation](https://hackage.haskell.org/package/hlint)```

<!-- verified: 2026-07-19 -->
