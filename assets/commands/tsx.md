# TAGLINE

基于 esbuild 的快速 TypeScript 执行器

# TLDR

**运行 TypeScript 文件**

```tsx [script.ts]```

**以监视模式运行**

```tsx watch [script.ts]```

**启动 TypeScript REPL**

```tsx```

**作为 Node.js 加载器运行**

```node --import tsx [script.ts]```

**使用环境变量运行**

```tsx [script.ts] --env-file [.env]```

**向脚本传递参数**

```tsx [script.ts] -- [arg1] [arg2]```

# SYNOPSIS

**tsx** [_options_] [_file_] [_args_...]

**tsx** **watch** [_options_] [_file_]

# PARAMETERS

**watch**
> 监视模式：文件变化时重启。

**--tsconfig** _file_
> tsconfig.json 文件路径。

**--env-file** _file_
> 从文件加载环境变量。

**--no-cache**
> 禁用转换缓存。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**tsx**（TypeScript Execute）是一个增强版 Node.js 运行时，可以无缝运行 TypeScript 和 ESM 文件。它使用 esbuild 进行快速转译，非常适合开发和脚本场景。

该工具零配置即可使用，没有 tsconfig.json 文件也能工作。它同时支持 CommonJS 和 ES 模块，能处理 tsconfig.json 中的路径别名，并带有面向开发的监视模式。

tsx 是 node 的直接替代品，支持所有 Node.js 命令行选项。它即时转译 TypeScript，不会把 JavaScript 文件写入磁盘。

注意 tsx 专注于执行速度，不做类型检查。类型检查请使用 tsc 或你的编辑器。

全局安装：`npm install -g tsx`

# CAVEATS

不执行类型检查。转译会带来轻微的启动开销。生产环境请用 tsc 预编译 TypeScript。与动态链接的 Node.js 特性配合效果最佳。

# HISTORY

**tsx** 由 Hiroki Osame（privatenumber）创建，作为 ts-node 的现代化替代方案。它优先考虑速度和简洁性，借助 esbuild 实现近乎即时的转译。该项目已成为开发阶段运行 TypeScript 的流行选择。

# INSTALL

```nix: nix profile install nixpkgs#tsx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ts-node](/man/ts-node)(1), [node](/man/node)(1), [tsc](/man/tsc)(1), [esbuild](/man/esbuild)(1)
