# TAGLINE

编译 Node

# TLDR

**编译 Node.js 项目**

```ncc build [src/index.js]```

**编译并指定输出目录**

```ncc build [src/index.js] -o [dist/]```

**编译并压缩**

```ncc build [src/index.js] -m```

**编译并生成 source map**

```ncc build [src/index.js] -s```

**编译并监视变更**

```ncc build [src/index.js] -w```

**直接运行**（编译后执行）

```ncc run [src/index.js]```

**编译 TypeScript**

```ncc build [src/index.ts]```

# SYNOPSIS

**ncc** [_build_] [_run_] [_-o dir_] [_-m_] [_-s_] [_-w_] [_options_] _file_

# PARAMETERS

**build** _FILE_
> 编译为单个文件。

**run** _FILE_
> 编译并运行。

**-o** _DIR_
> 输出目录。

**-m**, **--minify**
> 压缩输出。

**-s**, **--source-map**
> 生成 source map。

**-w**, **--watch**
> 监视文件变更。

**-e**, **--external** _PKG_
> 将软件包保持为外部依赖。

**-a**, **--asset-builds**
> 单独输出资源文件。

**--license** _FILE_
> 输出许可证文件。

**-q**, **--quiet**
> 静默模式。

**-v**, **--version**
> 显示版本号。

# DESCRIPTION

**ncc**（Node.js Compiler Collection）将 Node.js 项目编译为单个文件。它把代码和依赖打包在一起，生成无需 node_modules 即可运行的便携产物。

该编译器支持 CommonJS 和 ES 模块，自动解析导入。原生模块和资源文件会随包一起提取出来。

TypeScript 和现代 JavaScript 特性会被自动转译。输出目标为 Node.js，与 Node 的模块系统保持兼容。

外部依赖（externals）可将特定软件包排除在打包之外。这对于无法打包的原生模块，或运行时已能获取依赖、希望减小体积的场景很有用。

压缩可以减小输出体积。Source map 通过映射回原始源码，使打包后的代码仍可调试。

监视模式会在文件变更时重新编译，开发阶段很实用。

# CAVEATS

原生模块需要特殊处理。动态 require 可能无法解析。某些软件包存在打包问题。大型打包产物的构建可能较慢。

# HISTORY

**ncc** 由 **Vercel**（前身为 ZEIT）于 **2018 年**前后创建，用于简化 Node.js 部署。它让 Node.js 应用能像 Go 二进制一样以单文件形式分发，解决了 node_modules 的复杂性。

# INSTALL

```brew: brew install ncc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[webpack](/man/webpack)(1), [esbuild](/man/esbuild)(1), [rollup](/man/rollup)(1), [pkg](/man/pkg)(1)
