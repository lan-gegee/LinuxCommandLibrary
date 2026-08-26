# TAGLINE

在 shell 中轻松运行 Python 进行数据管道处理

# TLDR

**将每行翻倍**（按整数）

```seq 3 | pyp 'int(x)*2'```

**对 stdin 中的数字求和**

```seq 10 | pyp 'sum(map(int, lines))'```

**美化输出 JSON** 行

```cat [data.jsonl] | pyp 'json.loads(x)'```

**运行并解释自动导入**

```pyp -b '...'```

# SYNOPSIS

**pyp** [*options*] *expression*

# DESCRIPTION

**pyp** 让你用简短的 Python 表达式充当 shell 过滤器。stdin 的每一行都可用 **x**（及相关辅助对象）表示，**lines** 则暴露全部输入以便做归约。它会在引用到常用模块时自动导入，旨在 Python 更合适的场景中替代许多 **awk**/**sed** 单行命令。

通过 **pip install pypyp** 安装（PyPI 包名为 **pypyp**；命令为 **pyp**）。

# PARAMETERS

*expression*

> 应用于输入的 Python 表达式或小型脚本。

**-b**, **--explain** / 与自动导入相关的标志

> 解释自动导入行为或控制其行为（见 **pyp --help**）。

**-h**, **--help**

> 所安装版本的完整选项列表。

# CAVEATS

Python 的启动开销使其在处理海量数据流时比 **awk** 慢。自动导入可能带来意外，生产脚本建议显式导入。不能替代复杂的多文件程序。

# INSTALL

```brew: brew install pyp```

```nix: nix profile install nixpkgs#pyp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [awk](/man/awk)(1), [jq](/man/jq)(1), [perl](/man/perl)(1)

# RESOURCES

```[Source code](https://github.com/hauntsaninja/pyp)```

<!-- verified: 2026-07-19 -->
