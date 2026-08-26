# TAGLINE

向 Koji hub 执行任意 XML-RPC 调用

# TLDR

向 Koji hub 执行**任意 XML-RPC 调用**

```koji call build '"git+https://src.fedoraproject.org/rpms/pkg.git#commit"' target```

以 **scratch** 选项调用 build

```koji call build '"git+https://url#commit"' target --kwargs '{"opts":{"scratch": True}}'```

以 **arch override** 调用 build

```koji call build '"git+https://url#commit"' target --kwargs '{"opts":{"arch_override":"x86_64"}}'```

在**指定通道**上调用 build

```koji call build '"git+https://url#commit"' target --kwargs '{"channel":"default"}'```

显示**帮助**

```koji call --help```

# SYNOPSIS

**koji call** [_options_] _function_ [_arguments_]

# DESCRIPTION

**koji call** 向 Koji hub 执行任意 XML-RPC 调用。这允许直接访问 Koji API，执行标准子命令未覆盖的高级操作。

函数签名遵循 Koji API，例如 `build(src, target, opts=None, priority=None, channel=None)`。参数按位置传递，复杂选项通过 `--kwargs` 提供。

# PARAMETERS

**function**
> 要调用的 XML-RPC 函数名

**--kwargs JSON**
> 以 JSON 对象形式传递关键字参数

**--json-output**
> 以 JSON 格式输出结果

**-h, --help**
> 显示帮助信息

# CAVEATS

需要对 Koji API 有深入了解。不当的调用可能产生意外效果。JSON 语法必须正确加引号以便 shell 转义。

# SEE ALSO

[koji](/man/koji)(1), [koji-build](/man/koji-build)(1)
