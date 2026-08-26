# TAGLINE

基于 eBPF 的函数级测试覆盖率分析器，无需对二进制文件插桩

# TLDR

**以守护进程模式为某个二进制启动**分析器

```xcover run --detach --path /path/to/bin```

**等待**就绪后运行测试

```xcover wait
/path/to/bin test1
/path/to/bin test2
xcover stop```

**生成** JSON 覆盖率报告

```xcover run --path myapp --report```

**查看**状态或停止

```xcover status
xcover stop```

# SYNOPSIS

**xcover** <command> [options]

# DESCRIPTION

xcover 使用内核 eBPF uprobe 在测试执行期间追踪任意已编译 ELF 二进制文件（Go、C、Rust 等）中的函数调用。无需修改源码，也无需用覆盖率标志重新编译。

它支持守护进程模式：先开始追踪，然后执行任意测试套件或手动运行，最后停止并获得关于哪些函数被执行的报告。已剥离符号的 Go 二进制仍可通过 `.gopclntab` 进行符号化；其他被剥离的二进制可使用 `--debug-path` 指定单独的调试文件。

# COMMANDS

**run**
> 开始分析。关键标志：`--detach`/`-d`、`--path`/`-p`、`--pid`、`--include`/`--exclude` 正则表达式、`--scope`（Go 模块可用 `binary` 或 `project`）、`--report`、`--debug-path`、`--no-build-id-check`、`--verbose`。

**wait**
> 阻塞直到分析器完全初始化并开始追踪。

**status**
> 显示分析器守护进程是否正在运行。

**stop**
> 停止守护进程并生成最终结果/报告（启用报告时输出 `xcover-report.json`）。

# PARAMETERS

**--path** _EXE_PATH_
> 要分析的 ELF 可执行文件。

**--pid** _PID_
> 按进程 ID 过滤。

**--include** / **--exclude** _regex_
> 包含或排除函数符号名。

**--scope** binary|project
> 全部函数（默认），或仅限生成该二进制的 Go 模块的符号。

**--report**
> 写出 JSON 覆盖率报告（run 时默认开启）。

**--debug-path** _path_
> 为已剥离符号的非 Go 二进制指定单独的调试/符号文件。

**--detach**
> 作为后台守护进程运行。

# CAVEATS

- 需要具备 eBPF 支持及相应权限的 Linux 内核（通常需要 root 或 CAP_BPF）。
- 已剥离符号的二进制需要语言特定的回退方案（Go 用 `.gopclntab`）或单独的调试信息。
- 测量的是二进制层面的函数覆盖率，而非函数内部的行/分支覆盖率。
- 通过 `go build main.go` 生成的单文件二进制缺少模块元数据；项目范围会回退为二进制范围。

# SEE ALSO

[bpftrace](/man/bpftrace)(8), [perf](/man/perf)(1)

# RESOURCES

```[Source code](https://github.com/maxgio92/xcover)```

```[Documentation](https://github.com/maxgio92/xcover#readme)```

<!-- verified: 2026-07-11 -->
