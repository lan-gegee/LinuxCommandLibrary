# TAGLINE

安全的 JavaScript 和 TypeScript 运行时

# TLDR

**运行一个 TypeScript/JavaScript** 文件

```deno run [script.ts]```

**带网络权限**运行

```deno run --allow-net [script.ts]```

**以全部权限**运行

```deno run -A [script.ts]```

**启动 REPL**

```deno repl```

**运行远程脚本**

```deno run [https://example.com/script.ts]```

**编译为可执行文件**

```deno compile [script.ts]```

**格式化源码文件**

```deno fmt```

**运行测试**

```deno test```

**启动 HTTP 服务器**（使用默认导出）

```deno serve [script.ts]```

**添加依赖**

```deno add [npm:package-name]```

**初始化新项目**

```deno init [project-name]```

# SYNOPSIS

**deno** _subcommand_ [_options_] [_script_] [_args_]

# PARAMETERS

_SUBCOMMAND_
> 子命令：run、repl、serve、compile、test、fmt、lint、add、remove、install、init、doc、info、task、publish、upgrade 等。

_SCRIPT_
> 要执行的 TypeScript/JavaScript 文件或 URL。

**--allow-net** [_HOSTS_]
> 允许访问网络。

**--allow-read** [_PATHS_]
> 允许读取文件系统。

**--allow-write** [_PATHS_]
> 允许写入文件系统。

**--allow-env** [_VARS_]
> 允许访问环境变量。

**-A**, **--allow-all**
> 允许所有权限。

**--unstable-**_FEATURE_
> 启用特定的不稳定 API 特性（如 `--unstable-kv`、`--unstable-ffi`）。通用的 `--unstable` 标志已在 Deno 2 中移除。

**--watch**
> 监视文件变化并自动重启。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Deno** 是一个安全的 JavaScript 和 TypeScript 运行时。它在沙箱环境中执行代码，对文件、网络和环境变量的访问权限必须被显式授予。

Deno 无需任何配置即可原生支持 TypeScript，内置格式化工具、linter、测试运行器和标准库。它只使用 ES 模块，可以直接从 URL 导入模块，因此不再需要包管理器。

该运行时构建于 V8 和 Rust 之上，强调安全性和现代 JavaScript 特性。它提供 Web API 兼容性，让代码在 Deno 与浏览器环境之间更容易移植。

Deno 2 新增了内置包管理器（`deno add`、`deno remove`），支持 npm 和 JSR 软件包，并提供了用于运行 HTTP 服务器的 `deno serve` 子命令。通用的 `--unstable` 标志已被按特性的细粒度标志取代。

# CONFIGURATION

**deno.json** 或 **deno.jsonc**
> 项目配置文件，用于 import 映射、任务、编译选项和格式化规则。

# CAVEATS

与 Node.js 模块不完全兼容。部分 npm 软件包需要兼容层。必须为每种资源类型分别指定权限标志。URL 导入依赖远程地址的可用性。

# HISTORY

Deno 由 Node.js 的原作者 **Ryan Dahl** 创建，于 **2018 年**公布。它的设计目的是解决 Node.js 中被认为存在的不足，特别是在安全性、TypeScript 支持和模块系统方面。1.0 版本于 **2020 年**发布。

# INSTALL

```pacman: sudo pacman -S deno```

```apk: sudo apk add deno```

```zypper: sudo zypper install deno```

```brew: brew install deno```

```nix: nix profile install nixpkgs#deno```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [bun](/man/bun)(1), [tsc](/man/tsc)(1)
