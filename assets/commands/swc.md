# TAGLINE

基于 Rust 的高速 JavaScript 和 TypeScript 编译器

# TLDR

**编译文件**

```swc [input.js] -o [output.js]```

**编译目录**

```swc [src/] -d [dist/]```

**监视模式**

```swc [src/] -d [dist/] -w```

**生成 source map**

```swc [input.js] -o [output.js] --source-maps```

**使用配置文件**

```swc [input.js] -o [output.js] --config-file [.swcrc]```

# SYNOPSIS

**swc** [_-o output_] [_-d dir_] [_-w_] [_options_] _input_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-d** _DIR_
> 输出目录。

**-w**
> 监视模式。

**--source-maps**
> 生成 source map。

**--config-file** _FILE_
> 配置文件。

**--sync**
> 同步模式。

# DESCRIPTION

**swc**（Speedy Web Compiler）是一个用 Rust 编写的 JavaScript 和 TypeScript 编译器，定位为比 Babel 快得多的替代方案。它在单一工具中完成转译、JSX 转换、TypeScript 类型剥离和压缩。

该编译器支持现代 JavaScript 特性、向下编译到较旧的目标版本，以及 React JSX 转换。TypeScript 文件通过剥离类型来编译，不执行类型检查，因此在类型检查单独处理的构建流程中，它比 tsc 快得多。

SWC 可以处理单个文件或整个目录（支持开发用的监视模式），并生成用于调试的 source map。它被 Next.js 和 Parcel 等工具用作编译引擎。

# CONFIGURATION

**.swcrc**
> 项目配置文件，JSON 格式，定义编译目标、模块类型、JSX 设置和压缩选项。

# CAVEATS

插件比 Babel 少。生态基于 Rust。配置方式与 Babel 不同。

# HISTORY

**SWC**（Speedy Web Compiler）由 **Donny** 创建，是一个用 Rust 编写的高速 JavaScript/TypeScript 编译器。

# INSTALL

```apk: sudo apk add swc```

```brew: brew install swc```

```nix: nix profile install nixpkgs#swc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[babel](/man/babel)(1), [tsc](/man/tsc)(1), [esbuild](/man/esbuild)(1)
