# TAGLINE

将 Go 的一个子集转译为 BPF C 代码

# TLDR

**转译** Go BPF 程序并生成 C 代码及类型化绑定

```gobee translate --bindings-dir [./bpf] [./bpf/src]```

**安装**最新发布版本

```go install github.com/boratanrikulu/gobee/cmd/gobee@latest```

借助生成的 sourcemap **诊断**验证器错误

```gobee diagnose [verifier.log]```

# SYNOPSIS

**gobee** _subcommand_ [_options_] [_paths_]

# DESCRIPTION

**gobee** 是一个纯 Go 编写的转译器，可将 Go 的一个严格子集转换为 BPF（Berkeley Packet Filter）C 源代码，并为生成的程序提供类型化的 Go 绑定。它面向希望编写 eBPF 程序而又不直接手写 C 的开发者，同时保证生成的目标文件与 **libbpf** 以及 **clang** 的 BPF 后端保持兼容。

主子命令 **translate** 读取描述 BPF 程序的 Go 源文件，并在目标目录中生成三个产物：一个 **.bpf.c** 文件、一个用于错误定位的 sourcemap（**.bpf.c.map**），以及暴露类型化加载器和程序句柄的 **\*_bindings.go** 文件。要把生成的 C 编译成目标文件，需要支持 BPF 目标的 **clang**；而 **gobee** 本身只依赖 Go。

该工具还为 **libbpf** v1.5.0 辅助函数集提供类型化存根（stub），通过 **bpfvet** 进行内核版本把关，并能将验证器错误映射回原始 Go 源码位置，便于离线调试。

# PARAMETERS

**translate**
> 将 Go BPF 源码转译为 C 并生成 Go 绑定。

**diagnose**
> 使用生成的 sourcemap 把验证器输出映射回源码位置。

**--bindings-dir  _dir_**
> 生成的 Go 绑定的输出目录。

# CAVEATS

只接受 Go 的严格子集；转译后的代码无法使用 goroutine、支持动态派发的接口等惯用 Go 特性，也无法使用完整的标准库。构建可加载的 BPF 对象仍需带 **bpf** 目标的 **clang**，而在运行时加载这些对象则需要提升权限。

# SEE ALSO

[clang](/man/clang)(1), [bpftool](/man/bpftool)(8), [bpftrace](/man/bpftrace)(8)
