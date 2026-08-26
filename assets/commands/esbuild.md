# TAGLINE

极快的 JavaScript 与 TypeScript 打包器

# TLDR

**打包 JavaScript 文件**

```esbuild [app.js] --bundle --outfile=[out.js]```

**压缩打包**

```esbuild [app.js] --bundle --minify --outfile=[out.js]```

**打包 TypeScript**

```esbuild [app.ts] --bundle --outfile=[out.js]```

**监视模式**

```esbuild [app.js] --bundle --watch --outfile=[out.js]```

**启动开发服务器**

```esbuild [app.js] --bundle --serve=[8000]```

**面向浏览器打包**

```esbuild [app.js] --bundle --platform=browser --outfile=[out.js]```

**生成 source map**

```esbuild [app.js] --bundle --sourcemap --outfile=[out.js]```

# SYNOPSIS

**esbuild** [_options_] [_entry_points_...]

# PARAMETERS

_ENTRY_POINTS_
> 要处理的输入文件。

**--bundle**
> 打包依赖。

**--outfile** _FILE_
> 输出文件路径。

**--minify**
> 压缩输出。

**--watch**
> 文件变化时重新构建。

**--serve** [_PORT_]
> 启动开发服务器。

**--platform** _PLATFORM_
> 目标平台：browser、node、neutral。

**--sourcemap**
> 生成 source map。

**--target** _VERSION_
> JavaScript 目标版本，例如 es2020 或 chrome100。

**--outdir** _DIR_
> 输出目录（存在多个输出时用其代替 --outfile）。

**--format** _FORMAT_
> 输出模块格式：iife、cjs 或 esm。

**--loader:**_.ext=loader_
> 指定如何加载给定扩展名的文件（js、ts、jsx、json、text、base64、dataurl、file 等）。

**--define:**_K=V_
> 构建时将全局标识符替换为常量表达式。

**--external:**_pkg_
> 将某个包排除在 bundle 之外，保留原样的 import 语句。

**--splitting**
> 启用代码分割（仅限 esm 格式）。

**--metafile** _FILE_
> 写出一个描述构建结果的 JSON 文件，用于 bundle 分析。

**--help**
> 显示帮助信息。

# DESCRIPTION

**esbuild** 是一个极快的 JavaScript 与 TypeScript 打包和压缩工具。它以 Go 编写，速度比 webpack 或 Parcel 等传统打包器快 10 到 100 倍。

该工具处理打包、压缩、代码分割、tree shaking 和转译。无需配置即可支持 JSX、TypeScript 和现代 JavaScript 特性。

esbuild 的速度使其非常适合开发构建，也可作为构建流水线中的底层工具。

# CAVEATS

插件生态小于 webpack。部分转换不受支持。配置方式与其他打包器不同。复杂场景可能需要借助插件。

# HISTORY

esbuild 由 **Evan Wallace**（Figma 联合创始人）创建，于 **2020 年**发布。它相比现有工具的巨大速度提升源于 Go 编写与并行化设计。

# INSTALL

```apt: sudo apt install esbuild```

```pacman: sudo pacman -S esbuild```

```apk: sudo apk add esbuild```

```zypper: sudo zypper install esbuild```

```brew: brew install esbuild```

```nix: nix profile install nixpkgs#esbuild```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[webpack](/man/webpack)(1), [rollup](/man/rollup)(1), [vite](/man/vite)(1), [swc](/man/swc)(1)

# RESOURCES

```[Source code](https://github.com/evanw/esbuild)```

```[Homepage](https://esbuild.github.io/)```

```[Documentation](https://esbuild.github.io/api/)```

<!-- verified: 2026-07-14 -->
