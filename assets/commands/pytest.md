# TAGLINE

带 fixtures 和插件的 Python 测试框架

# TLDR

**运行所有测试**

```pytest```

**运行指定测试文件**

```pytest [test_file.py]```

**运行指定测试函数**

```pytest [test_file.py]::[test_function]```

**运行匹配关键字的测试**

```pytest -k "[keyword]"```

**以详细输出运行**

```pytest -v```

**首次失败即停止**

```pytest -x```

**显示 print 语句**

```pytest -s```

**并行运行测试**（需要 pytest-xdist）

```pytest -n [4]```

**运行匹配标记的测试**

```pytest -m "[slow]"```

# SYNOPSIS

**pytest** [_-v_] [_-x_] [_-k expression_] [_-m marker_] [_--cov package_] [_options_] [_paths_]

# PARAMETERS

**-v**, **--verbose**
> 提高详细程度。

**-q**, **--quiet**
> 降低详细程度。

**-x**, **--exitfirst**
> 首次失败即停止。

**-s**, **--capture=no**
> 禁用输出捕获（显示 print）。

**-k** _EXPRESSION_
> 运行匹配关键字表达式的测试。

**-m** _MARKER_
> 运行带有特定标记的测试。

**--collect-only**
> 只列出测试而不运行。

**--lf**, **--last-failed**
> 只运行上次失败的测试。

**--ff**, **--failed-first**
> 优先运行上次失败的测试。

**-n** _NUM_
> 并行工作进程数（pytest-xdist）。

**--cov** _PACKAGE_
> 度量覆盖率（pytest-cov）。

**--cov-report** _TYPE_
> 覆盖率报告格式。

**--pdb**
> 失败时进入调试器。

**--tb** _STYLE_
> 回溯风格：short、long、line、native、no。

**--maxfail** _NUM_
> N 次失败后停止。

**--ignore** _PATH_
> 收集阶段忽略指定路径。

**--durations** _NUM_
> 显示最慢的 N 个测试。

# DESCRIPTION

**pytest** 是 Python 最流行的测试框架。它自动发现并运行测试，拥有强大的 fixture、参数化和丰富的插件生态。

测试发现会查找匹配 test_*.py 或 *_test.py 的文件，以及以 test_ 开头的函数/方法；以 Test 开头的类也会被收集。这种基于约定的方式将配置降到最低。

fixture 提供可复用的测试依赖。用 @pytest.fixture 定义后，它们可以搭建数据库、创建对象或配置环境。fixture 可以限定作用域（function、class、module、session）以高效管理资源。

参数化通过 @pytest.mark.parametrize 用多组输入运行同一测试。标记（@pytest.mark.X）为测试打标签，便于选择性运行或自定义行为。

插件生态扩展功能：pytest-cov 用于覆盖率，pytest-xdist 用于并行执行，pytest-mock 用于 mock，还有数百个其他插件。插件经 pip 安装后自动启用。

断言内省无需特殊的断言方法即可给出详细的失败信息。标准 Python assert 语句配合丰富的差异对比展示即可工作。

# CONFIGURATION

**pytest.ini**
> 主要配置文件，用于设置测试发现路径、标记、命令行默认值和插件选项。

**pyproject.toml**
> 项目配置文件，包含 `[tool.pytest.ini_options]` 段，支持与 pytest.ini 相同的选项。

**setup.cfg**
> 另一种配置文件，包含 `[tool:pytest]` 段用于测试设置。

**conftest.py**
> pytest 自动加载的目录级 fixture 与插件文件，用于定义共享 fixture、钩子和测试配置。

# CAVEATS

大型测试套件需要 pytest-xdist 才能有合理的运行时间。过度复杂的 fixture 会掩盖测试逻辑。插件之间偶尔会冲突。覆盖率可能遗漏部分代码模式。参数化测试的输出可能很冗长。

# HISTORY

**pytest** 由 **Holger Krekel** 于 **2004 年前后**以 py.test 之名创建，从 py 库演化而来。它作为 unittest 的替代方案成长，强调简洁和最少样板代码。该项目在 **2016 年前后**随 3.0 版本更名为 pytest。它现在是 Python 测试领域事实上的标准。

# INSTALL

```apk: sudo apk add py3-pytest```

```brew: brew install pytest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [coverage](/man/coverage)(1), [tox](/man/tox)(1), [mypy](/man/mypy)(1)
