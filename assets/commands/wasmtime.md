# TAGLINE

独立的 WebAssembly 运行时

# TLDR

**运行 WebAssembly 文件**

```wasmtime [program.wasm]```

**带目录访问权限运行**

```wasmtime --dir [/path/to/dir] [program.wasm]```

**调用特定的导出函数**

```wasmtime run --invoke [function_name] [program.wasm] [args]```

**运行 WASI HTTP 服务器**

```wasmtime serve [component.wasm]```

**预先编译为原生代码**

```wasmtime compile [program.wasm] -o [program.cwasm]```

**运行已编译的模块**

```wasmtime run [program.cwasm]```

**启用 WASI 特性**

```wasmtime -S inherit-env [program.wasm]```

# SYNOPSIS

**wasmtime** [_options_] [_command_] [_wasm-file_] [_args_...]

# COMMANDS

**run**: 执行 WebAssembly 模块（默认）。

**serve**: 将组件作为 WASI HTTP 服务器运行。

**compile**: AOT 编译为原生代码。

**config**: 管理 Wasmtime 配置。

**wast**: 执行 WebAssembly 规范测试。

# PARAMETERS

**--dir** _path_
> 授予对主机目录的访问权限。

**--env** _key=value_
> 设置环境变量。

**--invoke** _expr_
> 调用特定的导出函数。

**-O**, **--optimize** _options_
> 优化设置。

**-C**, **--codegen** _options_
> 代码生成设置。

**-D**, **--debug** _options_
> 调试设置。

**-W**, **--wasm** _options_
> WebAssembly 语义设置。

**-S**, **--wasi** _options_
> WASI 配置（inherit-env、inherit-network）。

**--config** _file_
> 从 TOML 文件加载设置。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**wasmtime** 是 Bytecode Alliance 开发的独立 WebAssembly 运行时。它在浏览器之外执行 WebAssembly 模块和组件，支持 WASI（WebAssembly System Interface）以访问系统。

该运行时既可以执行二进制（.wasm）文件，也可以执行文本（.wat）格式的 WebAssembly 文件。对于性能关键的应用，可以使用 compile 子命令将模块预先编译为原生代码。

默认情况下，Wasmtime 将模块沙箱化，不允许访问任何系统资源。文件、环境和网络的访问必须通过命令行选项显式授予。

serve 子命令将实现了 wasi:http/proxy 接口的 WebAssembly 组件作为 HTTP 服务器运行。

# CAVEATS

WASI 并未完全兼容 POSIX。某些系统调用可能不可用。预先编译的模块与平台相关。Component Model 支持仍在演进中。

# HISTORY

**Wasmtime** 由 Bytecode Alliance 开发，该非营利组织包括 Mozilla、Fastly、Intel 和 Red Hat 等。它是浏览器之外 WebAssembly 的参考实现，并推动着 WASI 与 Component Model 标准的发展。

# INSTALL

```pacman: sudo pacman -S wasmtime```

```apk: sudo apk add wasmtime```

```brew: brew install wasmtime```

```nix: nix profile install nixpkgs#wasmtime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasmer](/man/wasmer)(1), [wasm-pack](/man/wasm-pack)(1), [wasm-opt](/man/wasm-opt)(1), [wasm-validate](/man/wasm-validate)(1)
