# TAGLINE

WebAssembly 软件包管理器

# TLDR

**安装软件包**

```wapm install [package]```

**运行软件包**

```wapm run [package]```

**搜索软件包**

```wapm search [query]```

**发布软件包**

```wapm publish```

**登录**

```wapm login```

**列出已安装的软件包**

```wapm list```

# SYNOPSIS

**wapm** _command_ [_options_] [_args_]

# PARAMETERS

**install**
> 安装软件包。

**run**
> 运行软件包。

**search**
> 查找软件包。

**publish**
> 上传软件包。

**login**
> 进行身份验证。

**list**
> 显示已安装的软件包。

# DESCRIPTION

**wapm** 是面向 WebAssembly 模块的软件包管理器，提供从 wapm.io 仓库安装、运行、搜索和发布软件包的命令。它与 Wasmer 运行时配合，在任何平台上执行 WebAssembly 软件包。

通过 wapm 安装的软件包包含预编译的 WebAssembly 模块，运行在沙箱环境中，因此可以跨操作系统和架构移植。该仓库托管着由 Rust、C 和 AssemblyScript 等语言编译成 WebAssembly 的各类工具和库。

发布软件包需要 wapm.io 账号以及一个描述软件包元数据、入口点和依赖关系的 wapm.toml 清单文件。

# CAVEATS

推荐搭配 Wasmer 使用。属于 WASM 生态。发布需要 wapm.io 账号。

# HISTORY

**wapm** 是 **Wasmer** 的软件包管理器，提供 WebAssembly 软件包管理功能。

# INSTALL

```nix: nix profile install nixpkgs#wapm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasmer](/man/wasmer)(1), [wasm-pack](/man/wasm-pack)(1)
