# TAGLINE

WebAssembly 运行时与软件包管理器

# TLDR

**运行 WebAssembly 文件**

```wasmer run [program.wasm]```

**调用特定函数运行**

```wasmer run [program.wasm] -i [function_name]```

**从仓库运行软件包**

```wasmer run [python/python]```

**全局安装软件包**

```wasmer install -g [package]```

**编译为原生代码**

```wasmer compile [program.wasm] -o [program.wasmu]```

**启用 HTTP 客户端运行**

```wasmer run --http-client [program.wasm]```

**校验 WebAssembly 文件**

```wasmer validate [program.wasm]```

**显示 Wasmer 版本**

```wasmer --version```

# SYNOPSIS

**wasmer** [_command_] [_options_] [_input_] [_args_...]

# COMMANDS

**run**: 执行 WebAssembly 文件或软件包。

**compile**: 编译为原生代码。

**validate**: 校验 WebAssembly 文件。

**install**: 安装软件包。

**publish**: 将软件包发布到仓库。

**config**: 管理配置。

**self-update**: 更新 Wasmer。

# PARAMETERS

**-i**, **--invoke** _function_
> 要调用的函数。

**-e**, **--entrypoint** _module_
> 软件包的入口模块。

**--stack-size** _size_
> 栈大小（默认：1048576）。

**--http-client**
> 允许发起 HTTP 请求。

**--wasmer-dir** _dir_
> Wasmer 主目录。

**--cache-dir** _dir_
> 缓存目录。

**--backend** _backend_
> 编译器后端：cranelift、llvm、singlepass。

**-v**, **--verbose**
> 详细输出。

**-h**, **--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**wasmer** 是一个用于在浏览器之外运行 Wasm 模块的 WebAssembly 运行时。它支持 WASI 以访问系统，并提供快速、安全的多后端执行能力。

该运行时默认是安全的，除非显式启用，否则无法访问文件、网络或环境变量。Wasmer 既可以运行其仓库中的软件包，也可以运行本地 .wasm 文件。

各编译器后端各有取舍：Singlepass 编译最快，Cranelift 在编译与执行速度之间取得平衡（默认），LLVM 则生成优化程度最高的代码。

通过以下方式安装：`curl https://get.wasmer.io -sSfL | sh`

# CAVEATS

WASI 支持程度因模块而异。某些系统接口需要显式指定标志才能启用。向软件包仓库发布需要账号。预先编译的模块与平台相关。

# HISTORY

**Wasmer** 由 Syrus Akbary 创建，于 2018 年发布。此后它成为领先的独立 WebAssembly 运行时之一，支持多种语言和平台。该项目还包含用于分发 Wasm 应用的软件包仓库。

# INSTALL

```pacman: sudo pacman -S wasmer```

```brew: brew install wasmer```

```nix: nix profile install nixpkgs#wasmer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasmtime](/man/wasmtime)(1), [wasm-pack](/man/wasm-pack)(1), [node](/man/node)(1)
