# TAGLINE

从 Python 代码中移除未使用的导入和变量

# TLDR

以 diff 形式**预览**更改而不修改文件

```autoflake [file.py]```

原地**删除**所有未使用的导入

```autoflake --in-place --remove-all-unused-imports [file.py]```

递归删除**所有 Python 文件**中未使用的导入

```autoflake --in-place --remove-all-unused-imports -r [.]```

**检查**而不修改文件，如有需要更改则以非零状态退出

```autoflake --check [file.py]```

原地删除未使用的导入和**变量**

```autoflake --in-place --remove-unused-variables --remove-all-unused-imports [file.py]```

# SYNOPSIS

**autoflake** [_--in-place_] [_--remove-unused-variables_] [_options_] _files_

# DESCRIPTION

**autoflake** 从 Python 代码中移除未使用的导入和变量。它通过自动清除死代码来保持代码整洁。

该工具使用静态分析识别未使用的元素，可以直接修改文件或报告问题。

# PARAMETERS

**-i**, **--in-place**
> 直接修改文件而不是打印 diff

**-s**, **--stdout**
> 将结果写到标准输出

**--remove-unused-variables**
> 删除未使用的变量

**--remove-all-unused-imports**
> 删除所有未使用的导入，而不仅是标准库导入

**--ignore-init-module-imports**
> 不改动 __init__.py 文件中的导入

**--expand-star-imports**
> 在名称可解析的情况下展开通配符导入（from x import *）

**--remove-duplicate-keys**
> 删除字典字面量中的重复键

**--check**
> 如需更改则以非零状态退出，但不修改文件（CI 模式）

**--check-diff**
> 类似 --check，但同时打印建议更改的 diff

**-r**, **--recursive**
> 递归处理目录

**-j** _n_, **--jobs** _n_
> 并行任务数（0 表示使用全部 CPU 核心）

**--exclude** _globs_
> 排除匹配逗号分隔 glob 的文件和目录

**--imports** _modules_
> 额外要移除未使用导入的模块列表，逗号分隔

# CAVEATS

可能错误地识别仅在类型注解中使用的导入。无法处理所有边界情况。提交前请检查更改。与 black 等其他格式化工具配合良好。

# HISTORY

**autoflake** 的创建是为了自动化清理 Python 中未使用的导入，作为代码格式化工具和 linter 的补充。

# INSTALL

```nix: nix profile install nixpkgs#autoflake```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[black](/man/black)(1), [isort](/man/isort)(1), [flake8](/man/flake8)(1)

# RESOURCES

```[Source code](https://github.com/PyCQA/autoflake)```

<!-- verified: 2026-06-17 -->
