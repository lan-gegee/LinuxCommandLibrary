# TAGLINE

Node.js 的 TypeScript 执行环境

# TLDR

**运行 TypeScript 文件**

```ts-node [script.ts]```

**启动 REPL**

```ts-node```

**使用指定配置运行**

```ts-node -P [tsconfig.json] [script.ts]```

**仅转译**（跳过类型检查）

```ts-node --transpile-only [script.ts]```

**以 ESM 方式运行**

```ts-node --esm [script.ts]```

**执行代码**

```ts-node -e "console.log('Hello')"```

**使用 SWC 转译**（最快模式）

```ts-node --swc [script.ts]```

**输出表达式的求值结果**

```ts-node -p "1 + 1"```

# SYNOPSIS

**ts-node** [_-P config_] [_--transpile-only_] [_--swc_] [_--esm_] [_options_] [_file_] [_args_]

# PARAMETERS

**-P** _FILE_
> tsconfig.json 的路径。

**--transpile-only**, **-T**
> 跳过类型检查。

**--esm**
> 使用 ESM 加载器。

**-e** _CODE_
> 执行代码。

**-p** _CODE_
> 执行并打印结果。

**-r** _MODULE_
> 加载（require）模块。

**--pretty**
> 美化打印错误信息。

**--skip-project**
> 跳过加载 tsconfig.json。

**--swc**
> 使用 SWC 转译以加快启动速度。隐含 --transpileOnly。

**--files**
> 启动时从 tsconfig.json 加载 files、include 和 exclude 指定的文件。

**-C** _NAME_, **--compiler** _NAME_
> 要使用的 TypeScript 编译器（默认：typescript）。

**-D** _CODES_, **--ignoreDiagnostics** _CODES_
> 按代码忽略 TypeScript 诊断信息。

**--emit**
> 将编译输出的文件写入 .ts-node 目录。

**-i**, **--interactive**
> 即使 stdin 不是终端也强制进入 REPL。

**--skipIgnore**
> 跳过忽略检查，允许编译 node_modules 中的文件。

**-O** _JSON_, **--compilerOptions** _JSON_
> 将 JSON 编译器选项与 tsconfig 合并。

**--showConfig**
> 打印解析后的 tsconfig.json 并退出。

# DESCRIPTION

**ts-node** 是 Node.js 的 TypeScript 执行引擎，可以即时编译并运行 TypeScript 文件，无需单独的构建步骤。默认情况下它会在运行时执行完整的类型检查，在开始执行之前报告类型错误。

**--transpile-only** 模式跳过类型检查，可显著加快启动速度，在你的编辑器已经提供类型反馈的开发阶段非常有用。**--swc** 选项使用 SWC 转译器（用 Rust 编写），速度提升更明显，且隐含 --transpileOnly。ESM 模式（**--esm**）处理 ES 模块导入，原生使用 import/export 语法时需要该模式。内置 REPL 提供了一个交互式 TypeScript 环境，便于实验。

配置默认从 tsconfig.json 加载，也可以用 **-P** 指定自定义配置。配合 ts-node-dev 或 nodemon 在文件变化时自动重启，它能很好地融入开发工作流。

# CAVEATS

启动速度比预编译的 JavaScript 慢。类型检查会带来额外开销。部分高级 TypeScript 特性需要额外配置。不建议在生产环境使用。

# HISTORY

**ts-node** 创建于 **2015** 年前后，用于直接执行 TypeScript。它成为 TypeScript 开发的重要工具，支持脚本、REPL 和开发服务器的运行。

# INSTALL

```pacman: sudo pacman -S ts-node```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tsc](/man/tsc)(1), [node](/man/node)(1), [npx](/man/npx)(1), [tsx](/man/tsx)(1)
