# TAGLINE

性能剖析调用栈的可视化工具

# TLDR

**从 perf 数据生成火焰图**

```perf script | stackcollapse-perf.pl | flamegraph.pl > [flame.svg]```

**从 dtrace 输出生成**

```stackcollapse.pl [out.dtrace] | flamegraph.pl > [flame.svg]```

**自定义标题**

```flamegraph.pl --title "[My App Profile]" [stacks.txt] > [flame.svg]```

**倒置（冰柱）图**

```flamegraph.pl --inverted [stacks.txt] > [flame.svg]```

**设置宽度**

```flamegraph.pl --width [1200] [stacks.txt] > [flame.svg]```

# SYNOPSIS

**flamegraph.pl** [_options_] [_input_]

# PARAMETERS

**--title** _text_
> 图表标题。

**--subtitle** _text_
> 二级标题（可选）。

**--width** _pixels_
> SVG 宽度（默认 1200）。

**--height** _pixels_
> 帧的高度（默认 16）。

**--minwidth** _pixels_
> 省略比这更窄的函数（默认 0.1 像素）。

**--fontsize** _num_
> 字号（默认 12）。

**--fonttype** _font_
> 字体类型（默认 "Verdana"）。

**--countname** _text_
> 计数类型的标签（默认 "samples"）。

**--nametype** _text_
> 名称类型的标签（默认 "Function:"）。

**--inverted**
> 生成冰柱图（自顶向下）。

**--reverse**
> 反转调用栈顺序。

**--colors** _palette_
> 调色板：hot（默认）、mem、io、wakeup、chain、java、js、perl、red、green、blue、aqua、yellow、purple、orange。

**--bgcolors** _color_
> 背景渐变：yellow（默认）、blue、green、grey，或纯色 "#rrggbb"。

**--hash**
> 按函数名的哈希值分配颜色。

**--cp**
> 使用一致性调色板（palette.map）。

**--flamechart**
> 按时间排序的火焰图（按时间先后排列，不合并调用栈）。

**--negate**
> 对调差分色调（蓝/红）。

# DESCRIPTION

**FlameGraph** 是一款性能剖析调用栈可视化工具，由 Brendan Gregg 开发。它生成可交互的 SVG 图形，其中 x 轴表示调用栈的数量占比，y 轴表示栈的深度。

火焰图可以快速揭示哪些代码路径消耗的资源最多。任何能转换成折叠栈（collapsed stacks）格式的剖析器输出都可以配合它使用。

# WORKFLOW

```bash
# 1. Collect profile (Linux perf)
perf record -g ./myapp

# 2. Convert to text stacks
perf script > out.perf

# 3. Collapse stacks
stackcollapse-perf.pl out.perf > stacks.txt

# 4. Generate flame graph
flamegraph.pl stacks.txt > flame.svg
```

# CAVEATS

需要 Perl 环境。输入必须为折叠栈格式（可用 stackcollapse-*.pl 脚本转换）。规模很大的剖析数据可能产生非常复杂的图形。除非指定 --hash 或 --cp，否则配色是随机的。交互功能（缩放、搜索）需要支持 SVG 的浏览器。

# HISTORY

火焰图由 **Brendan Gregg** 在 **2011 年**任职 Joyent 期间发明，用于分析性能问题。这种可视化技术如今已是跨语言、跨平台性能剖析的标准做法。

# INSTALL

```dnf: sudo dnf install flamegraph```

```pacman: sudo pacman -S cargo-flamegraph```

```apk: sudo apk add cargo-flamegraph```

```brew: brew install cargo-flamegraph```

```nix: nix profile install nixpkgs#cargo-flamegraph```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perf](/man/perf)(1), [bpftrace](/man/bpftrace)(8), [strace](/man/strace)(1), [gprof](/man/gprof)(1), [valgrind](/man/valgrind)(1)
