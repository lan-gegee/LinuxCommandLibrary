# TAGLINE

将 JavaScript 和 TypeScript 打包用于生产环境

# TLDR

**打包 JavaScript/TypeScript 文件**

```bun build [./src/index.ts] --outdir [./dist]```

**创建独立可执行文件**

```bun build [./server.ts] --compile --outfile [server]```

**以压缩方式打包**

```bun build [./src/index.ts] --outdir [./dist] --minify```

**生成 source map**

```bun build [./src/index.ts] --outdir [./dist] --sourcemap```

**面向 Node.js 目标打包**

```bun build [./src/index.ts] --outdir [./dist] --target [node]```

**将包标记为外部依赖**

```bun build [./src/index.ts] --outdir [./dist] --external [react]```

**打包多个入口文件**

```bun build [./src/index.ts] [./src/worker.ts] --outdir [./dist]```

# SYNOPSIS

**bun build** _entrypoints_ [_options_]

# DESCRIPTION

**bun build** 是 Bun 的快速原生打包器，支持 JavaScript 和 TypeScript。它可以为生产环境打包代码、生成独立可执行文件，并用一条命令同时处理服务端和客户端代码。

该打包器自动执行 tree-shaking 以剔除未使用的代码。它可以面向多种运行时，包括浏览器、Node.js 和 Bun 自身。**--compile** 标志会创建内嵌 Bun 运行时的自包含可执行文件，用户无需安装 Bun 即可分发运行。通过命令行标志或等效的 JavaScript API（**Bun.build()**）还可以使用代码分割、source map 和压缩等特性。

# PARAMETERS

**--outdir** _directory_
> 打包文件的输出目录

**--outfile** _file_
> 输出文件路径（单一输出时）

**--compile**
> 创建内嵌 Bun 运行时的独立可执行文件

**--minify**
> 启用压缩

**--sourcemap**
> 生成 source map（external、inline 或 none）

**--target** _runtime_
> 目标运行时：browser、bun 或 node

**--external** _package_
> 将包排除在打包之外

**--splitting**
> 启用代码分割

**--format** _type_
> 输出格式：esm 或 cjs

**--define** _key=value_
> 定义全局常量

**--loader** _ext:loader_
> 配置各文件类型的加载器

# JAVASCRIPT API

```javascript
await Bun.build({
  entrypoints: ['./src/index.js'],
  outdir: './build',
  minify: true,
})
```

# CAVEATS

独立可执行文件包含一份 Bun 运行时副本，文件体积会增大。Tree-shaking 始终启用。由于动态导入的原因，某些 npm 包可能无法正确打包。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-run](/man/bun-run)(1), [esbuild](/man/esbuild)(1), [webpack](/man/webpack)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
