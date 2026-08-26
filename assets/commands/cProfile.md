# TAGLINE

Python 确定性性能分析器

# TLDR

**分析** Python 脚本的性能

```python -m cProfile [script.py]```

**分析并按累计时间排序**

```python -m cProfile -s cumtime [script.py]```

**分析并保存到文件**

```python -m cProfile -o [profile.prof] [script.py]```

**按函数自身耗时排序**

```python -m cProfile -s tottime [script.py]```

**分析代码中的特定函数**

```import cProfile; cProfile.run('[function_call()]')```

**用 pstats 查看已保存的分析结果**

```python -c "import pstats; p = pstats.Stats('[profile.prof]'); p.sort_stats('cumtime').print_stats(20)"```

**用 snakeviz 可视化**

```snakeviz [profile.prof]```

# SYNOPSIS

**python -m cProfile** [**-o** _output_] [**-s** _sort_] _script.py_ [_args_]

# PARAMETERS

**-o** _file_
> 将分析统计数据保存到文件，供以后分析。

**-s** _sort_
> 按指定列排序输出。

**-m** _module_
> 分析以脚本方式运行的模块（传递给 python -m）。

# SORT OPTIONS

**calls** / **ncalls**：调用次数
**cumulative** / **cumtime**：累计时间（含子调用）
**tottime** / **time**：函数自身总耗时（不含子调用）
**filename**：文件名
**module**：模块名
**name** / **nfl**：函数名（name/file/line）
**pcalls**：原生调用次数
**stdname**：标准名
**line**：行号

# DESCRIPTION

**cProfile** 是 Python 内置的确定性性能分析器，用于测量每个函数耗费了多少时间。它以 C 实现，开销很低，因此适合对生产代码进行性能分析。

该分析器跟踪每一次函数调用和返回，记录调用次数与耗时。输出会显示每个函数的调用次数、总时间、单次调用时间、累计时间以及单次累计时间。

分析数据可以保存下来，之后用 **pstats** 模块分析，或用 **snakeviz**、**pyprof2calltree**、**gprof2dot** 等工具可视化，便于深入排查性能瓶颈。

# PROGRAMMATIC USAGE

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# Code to profile
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumtime')
stats.print_stats(10)
```

# CAVEATS

性能分析本身会增加开销，可能影响测量结果，尤其是对执行很快的函数。该分析器是确定性的而非统计性的，会捕获每次调用，但可能影响性能。如需逐行分析可使用 **line_profiler**，如需开销更低的采样式分析可使用 **py-spy**。

# HISTORY

cProfile 在 Python **2.5** 版（2006 年）中加入，作为纯 Python 实现的 **profile** 模块的更快替代品。它基于 **Armin Rigo** 贡献的 **lsprof**。其 C 实现的开销比原来的 profiler 低约 10 倍，同时保持相同的接口。

# SEE ALSO

[py-spy](/man/py-spy)(1), [python](/man/python)(1)
