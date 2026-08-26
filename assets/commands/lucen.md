# TAGLINE

面向普通 Python 的注释 pragma 并行化工具

# TLDR

**运行 Python 脚本**并启用 Lucen（重写标记的循环）

```lucen run [script.py]```

**解释**哪些标记块可被并行化（静态报告）

```lucen explain [script.py]```

**分析**脚本的性能，并报告每个块的实际执行情况

```lucen profile [script.py]```

用于 CI 基线的 **JSON explain** 报告

```lucen explain --format=json [script.py]```

**严格基线检查**（分类退化时失败）

```lucen explain --strict --baseline=[baseline.json] [script.py]```

**带脚本参数运行**

```lucen run [script.py] -- [arg1] [arg2]```

分析期间**实时输出分块统计信息**

```lucen profile --live [script.py]```

# SYNOPSIS

**lucen** [**--version**] *command* [*args*]

**lucen run** *script* [*args*...]

**lucen explain** [*options*] *file*

**lucen profile** [*options*] *script* [*args*...]

# PARAMETERS

**--version**
> 打印 Lucen 版本并退出

## run

**script**
> Python 文件路径；标记为 **# LUCEN START** / **# LUCEN END** 的循环会被重写并在 Lucen 激活的状态下执行

**args**
> 作为 **sys.argv** 传递给脚本的参数

## explain

**file**
> 要进行静态分析的源文件（不执行）

**--block** *N*
> 只报告索引为 *N* 的块

**--format** *text*|*json*
> 输出格式（**json** 是基线格式）

**--assume-gil** / **--assume-free-threaded**
> 按假定的解释器模式报告后端选择

**--strict**
> 若分类与 **--baseline** 不同则返回非零退出码

**--baseline** _FILE_
> 此前 **--format=json** 运行生成的基线 JSON（使用 **--strict** 时必需）

## profile

**script** / **args**
> 要在 Lucen 下执行的脚本及其参数

**--live**
> 在运行过程中实时输出分块完成统计

**--per-block**
> 按标记的块细分报告

**--export** _FILE_
> 将报告以 JSON 而非文本形式写出

# DESCRIPTION

**lucen** 是一个由注释 pragma 驱动的源到源编译器和自动循环并行化工具，面向普通 Python。你可以用 **# LUCEN START** 和 **# LUCEN END** 标记一个循环；Lucen 只并行化它能够证明安全且有益的循环，并保证结果与顺序执行逐位一致（包括浮点位模式和字典插入顺序）。

该 CLI 有三个主要子命令：

- **lucen run** 重写入口脚本并在激活 Lucen 的情况下运行。直接用 **python script.py** 无法并行化入口模块中 **lucen.activate()** 之后标记的循环，因为该模块已被编译；**run** 为单文件脚本解决了这个问题。
- **lucen explain** 打印静态的逐块报告：可并行与需顺序执行的判定、预测的后端，以及原因或建议（例如 **depend=none** 或 **calibrate=false**）。
- **lucen profile** 执行脚本并报告观测到的调度情况和耗时。

对于更大的应用程序，你也可以 **import lucen** 并在导入包含标记循环的模块之前调用 **lucen.activate()**。pragma 就是普通注释：在未安装或未激活 Lucen 时，程序的行为如同这些 pragma 从未存在过（注释不变性）。

可通过 **pip install lucen** 从 PyPI 安装（Python 3.9+）。可选的原生加速通过 GIL 构建上的 Rust 核心提供；自由线程版 CPython 使用纯 Python 回退实现。

# CAVEATS

只有在源代码可读时才能完全证明辅助函数的纯度；C 扩展和动态可调用对象是被信任的，有状态的辅助函数可能在各 worker 间产生分歧。进程 worker 会重新导入入口模块——请使用 **if __name__ == "__main__":** 保护。除非块发生回退，否则被并行化的块内部副作用顺序并非顺序执行。每对 pragma 一个块，每个块一个循环，不支持 **async** 函数体。收益与可 pickle 性的判断可能只能在运行时确定；请使用 **lucen profile** 观测实际行为。

# HISTORY

**Lucen** 以 Apache-2.0 许可证开源发布，是一个注重正确性的注释 pragma 并行化工具：私有写入 slab、有序提交，以及在冲突或无收益时回退到顺序执行。该项目提供诊断 CLI（**explain**、**profile**、**run**）、正式与技术规格文档，以及可选的 Rust 编排热路径。

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1), [pytest](/man/pytest)(1), [ruff](/man/ruff)(1)

# RESOURCES

```[Source code](https://github.com/fcmv/lucen)```

```[Homepage](https://pypi.org/project/lucen/)```

<!-- verified: 2026-07-25 -->
