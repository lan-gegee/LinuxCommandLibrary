# TAGLINE

按 PEP 8 规范检查 Python 代码风格

# TLDR

**检查 Python 文件**

```pycodestyle [script.py]```

**检查目录**

```pycodestyle [src/]```

**显示源代码**

```pycodestyle --show-source [script.py]```

**显示 PEP8 说明**

```pycodestyle --show-pep8 [script.py]```

**忽略特定错误**

```pycodestyle --ignore=[E501,W503] [script.py]```

**仅选择特定错误**

```pycodestyle --select=[E1,W1] [script.py]```

**设置最大行宽**

```pycodestyle --max-line-length=[120] [script.py]```

**显示统计信息**

```pycodestyle --statistics [src/]```

# SYNOPSIS

**pycodestyle** [_--ignore codes_] [_--select codes_] [_--max-line-length n_] [_options_] _files_

# PARAMETERS

**--ignore** _CODES_
> 跳过指定的错误码。

**--select** _CODES_
> 仅显示指定的错误码。

**--max-line-length** _N_
> 行宽限制（默认 79）。

**--show-source**
> 显示源代码。

**--show-pep8**
> 显示 PEP8 相关说明文档。

**--statistics**
> 显示错误统计。

**--count**
> 输出错误总数。

**--config** _FILE_
> 配置文件。

**--first**
> 仅显示第一个错误。

**-q**, **--quiet**
> 安静模式。

**--benchmark**
> 为运行计时。

# ERROR CODES

**E1xx**
> 缩进错误。

**E2xx**
> 空格错误。

**E3xx**
> 空行错误。

**E4xx**
> 导入错误。

**E5xx**
> 行宽错误。

**E7xx**
> 语句错误。

**W xxx**
> 警告。

# DESCRIPTION

**pycodestyle**（前身为 pep8）依据 PEP 8 风格指南检查 Python 代码，只识别格式问题而不修改代码。

PEP 8 定义了 Python 官方风格：缩进、空格、命名和行宽约定。统一的风格有助于提升可读性。

错误码按类别分组。E5 系列与行宽有关。W503/W504 处理表达式中的换行。可以忽略特定的错误码。

配置文件（setup.cfg、tox.ini、.pycodestyle）可定义项目级设置，其优先级高于命令行默认值。

该工具不会自动修复问题。如需自动格式化，请使用 autopep8 或 black。

与编辑器集成可实时显示问题；CI 流水线可在合并前捕获风格违规。

# CONFIGURATION

**setup.cfg**
> 项目配置文件，包含 `[pycodestyle]` 段，可设置 max-line-length、ignore 和 select 选项。

**tox.ini**
> 另一种项目配置文件，支持相同的 `[pycodestyle]` 段选项。

**~/.config/pycodestyle**
> 用户级配置文件，在未找到项目配置时应用其中的默认设置。

# CAVEATS

仅做风格检查，不检测逻辑错误。部分规则存在争议（W503 与 W504）。严格的行宽限制不一定适合所有项目。

# HISTORY

**pycodestyle** 原名 **pep8**，由 **Johann C. Rocholl** 于 **2006 年前后**创建。**2016 年**更名为 pycodestyle，因为 PEP 8 自己也说明 Guido 的命名约定是指导方针而非硬性规则。

# INSTALL

```apk: sudo apk add py3-pycodestyle```

```brew: brew install pycodestyle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flake8](/man/flake8)(1), [pylint](/man/pylint)(1), [black](/man/black)(1), [autopep8](/man/autopep8)(1)
