# TAGLINE

基于 Chrome V8 引擎构建的 Node.js JavaScript 运行时

# TLDR

**运行** JavaScript 文件

```node [script.js]```

**启动 REPL**（交互式 Shell）

```node```

**求值**表达式并打印结果

```node -e "[console.log('hello')]"```

向脚本**传递参数**（可通过 `process.argv` 访问）

```node [script.js] [arg1] [arg2]```

**运行**脚本并启用检查器、在第一行中断

```node --inspect-brk [script.js]```

**语法检查**而不执行

```node --check [script.js]```

在文件变化时**监视并重启**（Node.js 18+）

```node --watch [script.js]```

使用自定义 loader **运行 TypeScript**

```node --import [tsx] [script.ts]```

**打印版本号**

```node --version```

# SYNOPSIS

**node** [_options_] [_v8-options_] [_script_ | _-_ | -e _string_] [_arguments_]

# PARAMETERS

**-e**, **--eval** _CODE_
> 将 _code_ 作为 JavaScript 求值，不加载文件。

**-p**, **--print** _CODE_
> 与 **-e** 类似，但将结果打印到 stdout。

**-r**, **--require** _MODULE_
> 在运行主脚本前预加载 _module_（仅限 CommonJS）。

**--import** _MODULE_
> 在运行主脚本前预加载一个 ES 模块。

**-c**, **--check**
> 解析脚本并检查语法错误，但不执行。

**-i**, **--interactive**
> 即使 stdin 不是 TTY 也强制进入 REPL。

**--inspect**[=_host:port_]
> 在给定的主机/端口上启用 V8 检查器（默认 127.0.0.1:9229）。

**--inspect-brk**[=_host:port_]
> 与 **--inspect** 类似，但在用户代码开始前中断。

**--watch**
> 当被监视的文件变化时重启进程。（Node.js 18+）

**--watch-path** _PATH_
> 启用 **--watch** 时额外要监视的路径。

**--enable-source-maps**
> 在堆栈追踪中使用 source map。

**--no-warnings**
> 静默所有进程警告（包括弃用警告）。

**--max-old-space-size** _MB_
> 以兆字节为单位设置 V8 老年代堆大小。

**--experimental-vm-modules**
> 在 `vm` 模块中启用实验性的 ES 模块 API。

**-v**, **--version**
> 打印 Node.js 版本。

**-h**, **--help**
> 打印 Node.js 命令行帮助。

# CONFIGURATION

**NODE_OPTIONS**
> 以空格分隔的 CLI 选项列表，会在任何显式选项之前应用（例如 `NODE_OPTIONS="--enable-source-maps"`）。

**NODE_PATH**
> 以冒号分隔的附加目录列表，用于查找 CommonJS 模块。

**NODE_ENV**
> 许多框架使用的约定；Node 本身不解释它。

**package.json**
> `"type": "module"` 的存在会将 `.js` 文件切换为 ES 模块；`"main"` 和 `"exports"` 定义入口点。

# DESCRIPTION

**node** 是基于 V8 引擎构建的 Node.js JavaScript 运行时（通过 `--experimental-wasi` 也可运行 WebAssembly）。它在服务端执行脚本，提供事件驱动、非阻塞 I/O 模型和庞大的标准库（`fs`、`http`、`crypto`、`stream`、`child_process` 等）。

Node 同时支持 CommonJS（`require`）和 ECMAScript 模块（`import`）。模块类型由文件扩展名（`.cjs`/`.mjs`）或最近的 `package.json` 的 `"type"` 字段决定。内置模块可以使用 `node:` 前缀导入（例如 `import fs from 'node:fs/promises'`）。

解释器自带用于包管理的 **npm** 和 **npx**、内置测试运行器（`node --test`）、面向 CPU 密集型并行的 worker 线程，以及可通过 `--inspect` 访问的内置调试器和分析器。

# CAVEATS

默认事件循环是单线程的——CPU 密集型工作会阻塞所有 I/O，除非将其卸载到 **worker_threads** 或子进程。长期支持（LTS）版本线与当前版本线的功能集不同；在依赖 **--watch** 或 **--import** 等标志前，请先检查 `node --version` 和相关文档。一些历史悠久的标志（如 `--loader`）已被 `--import`/`--experimental-loader` 取代。

# HISTORY

Node.js 由 **Ryan Dahl** 于 **2009 年**创建。现由 **OpenJS Foundation** 管理，遵循偶数号 LTS 版本线（如 18、20、22）支持约 30 个月、奇数号为引入较新 V8 特性的当前版本的发布节奏。

# INSTALL

```apt: sudo apt install nodejs```

```pacman: sudo pacman -S nodejs```

```apk: sudo apk add nodejs```

```brew: brew install nodejs```

```nix: nix profile install nixpkgs#nodejs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npx](/man/npx)(1), [deno](/man/deno)(1), [bun](/man/bun)(1)
