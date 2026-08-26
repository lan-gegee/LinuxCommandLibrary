# TAGLINE

感知 Git 的 Python AST 静态审查 CLI

# TLDR

**审查**相对 Git HEAD 有改动的 Python 文件（外加未跟踪的 `.py` 文件）

```avouch```

以 **JSON** 格式打印检查结果

```avouch --json```

审查**每一个符合条件的** Python 文件（适用于 CI 的模式）

```avouch --all-files```

仅审查已**暂存**的文件

```avouch --staged```

在**没有 Git 仓库**的情况下审查 `.py` 文件

```avouch --not-git```

打印已更改文件的**精简 diff**，而不是检查结果报告

```avouch --changed```

只做分析并返回**退出码**（不输出报告）

```avouch --quiet```

# SYNOPSIS

**avouch** [**--json**] [**--quiet**] [**--verbose**] [**--ignore-path** _PATH_] [**--changed** | **--staged** | **--all-files**] [**--not-git**]

**avouch** **--docs**

**avouch** **--version**

# PARAMETERS

**--json**
> 在 stdout 上输出一份带版本号的 JSON 文档（schema `version` 为 1）。省略人类可读报告。可与任何审查范围标志组合使用。

**--quiet**
> 执行同样的分析但不打印报告。错误仍然输出到 stderr。退出码不变。

**--verbose**
> 将分步诊断信息打印到 stderr（配置来源、忽略路径、审查集合）。

**--ignore-path** _PATH_
> 排除一个相对于仓库根目录的文件或目录。可重复使用。与 `avouch.toml` 中的 `ignore_paths` 合并生效。

**--changed**
> 显示相对 HEAD 有改动文件的新增和删除行，而不是检查结果报告。与 **--staged** 和 **--all-files** 互斥。

**--staged**
> 仅审查有 Git 暂存变更的文件（`git diff --cached --name-only`）。与 **--changed** 和 **--all-files** 互斥。

**--all-files**
> 审查仓库中每一个符合条件的 Python 文件（`git ls-files`）。在 CI 中请使用此选项：干净的检出相对 HEAD 没有任何改动。

**--not-git**
> 遍历当前目录查找 `.py` 文件并跳过对 Git 的要求。不能与 **--changed** 或 **--staged** 组合。

**--docs**
> 打印内置文档并以退出码 0 结束，不做审查。在 TTY 上使用交互式分页器；通过管道时输出纯文本。

**--version**
> 打印 Avouch 软件包版本并退出。

**--help**
> 显示 argparse 帮助并退出。

# DESCRIPTION

**avouch** 是一个本地的、感知 Git 的 Python 静态分析 CLI。它会询问 Git 下一次提交将涉及哪些文件，用标准库的 `ast` 模块解析每个改动的 `.py` 文件，并根据你在 `avouch.toml` 中配置的上限报告结构性问题。

默认的审查集合是相对 `HEAD` 有修改的被跟踪文件加上未跟踪的 `.py` 文件。被删除的路径、非 Python 文件以及看起来是生成产物的名字（`generated.py`、`*_generated.py`、`codegen.py`、`autogen.py` 等）会被跳过。已提交且未改动的文件永远不会出现在输出中。

检查结果是**警告**，由 17 个规则标识符（SCR001–SCR017）以及针对函数和类的圈复杂度检查产生。参数数量、嵌套深度、行跨度等指标均来自 AST。无法读取或语法错误的文件会成为一条 `ERROR` 记录；单个损坏的文件不会取消其余文件的审查。

Avouch 只做审查；它不会重写文件。强制执行由调用它的工具负责。退出码为 **0**（干净）、**1**（报告了问题）、**2**（Avouch 无法运行）。仅在 stdout 是 TTY 时才输出颜色。

需要 **Python 3.10+**（`ast.Match`、`tomllib`）；除非使用 **--not-git**，否则需要 `PATH` 上有 **Git**。用 `pip install avouch` 安装，会注册 `avouch` 控制台脚本。

# CONFIGURATION

**avouch.toml**
> 可选的 TOML 文件，只查找**当前工作目录**（不向上级搜索）。缺失或为空时使用内置默认值，且不会警告。

**[limits]**
> 数值阈值。未设置的键保持默认值。示例：`max_parameters`（5）、`max_nesting`（5）、`max_function_lines`（300）、`max_class_lines`（200）、`max_file_lines`（1000）、`max_complexity`（40）、`max_boolean_conditions`（5）、`max_if_chain`（5）、`max_local_variables`（30）、`max_return_statements`（6）、`max_lambda_nodes`（10）、`max_large_comprehensions`（40）。

**[rules]**
> 按规则的开/关切换（`true`/`false`）。键名对应规则模块（`bare_except`、`nested_function`、`max_parameters` 等）。将某个开关设为 `false` 即禁用该规则。

**ignore_paths**
> 顶层的 TOML 列表，列出要跳过的仓库相对路径（必须是列表）。匹配按路径组件进行：`tests` 会跳过 `tests/` 和 `tests/x.py`，但不会跳过 `tests.py`。可与可重复使用的 **--ignore-path** 合并生效。

没有用于配置的环境变量。`AVOUCH_FONT` 只是通过 OSC 50 在支持的终端上选择可选的终端字体。未知的 TOML 键会被静默忽略。格式错误的 TOML 或非列表的 `ignore_paths` 会以退出码 **2** 结束。

# CAVEATS

在干净的 Git 检出上运行默认模式会打印 `error: nothing to review` 并以退出码 **2** 结束——CI 中请使用 **--all-files**。配置只识别当前工作目录，因此在子目录中运行看不到仓库根目录下的 `avouch.toml`。未知的配置键不会警告。上限值在加载时不做类型检查。只审查 Python。方法上的 `self` 也计入 `max_parameters`。嵌套的 `async def` 不会被 SCR015 标记。声明依赖的 `rich` 并未被报告器使用。

# HISTORY

Avouch 是 **Mukund**（`mukundzha`）开发的 Python CLI，首次以软件包 **avouch** 的名义发布在 PyPI 上。它面向推送前的、按 diff 划定范围的审查，而非整个仓库的 lint。控制台脚本入口点是 `avouch.cli:main`。

# SEE ALSO

[ruff](/man/ruff)(1), [flake8](/man/flake8)(1), [pylint](/man/pylint)(1), [mypy](/man/mypy)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/mukundzha/avouch)```

<!-- verified: 2026-08-18 -->
