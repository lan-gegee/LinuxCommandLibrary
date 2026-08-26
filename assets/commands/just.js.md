# TAGLINE

面向 Linux 的小型可嵌入 V8 JavaScript 运行时

# TLDR

启动 **REPL**（交互式 shell）

```just```

**运行** JavaScript 文件

```just [path/to/file.js]```

**求值** JavaScript 代码

```just eval "[code]"```

**初始化**新项目

```just init [project_name]```

将 JavaScript 应用**构建**为可执行文件

```just build [path/to/file.js] --static```

# SYNOPSIS

**just** [_options_] [_file_]

# PARAMETERS

**eval** _CODE_
> 求值 JavaScript 代码字符串

**init** _NAME_
> 初始化新的项目目录

**build** _FILE_
> 将 JavaScript 构建为可执行文件

**--static**
> 创建静态链接的可执行文件

# DESCRIPTION

**just** 是一个面向 Linux 的小型可嵌入 V8 JavaScript 运行时。它提供一个最小化的运行时环境，用于执行 JavaScript 应用并直接访问 Linux 系统调用。

该运行时追求轻量和快速启动，适合 serverless 函数、命令行工具和嵌入式应用。它还能将 JavaScript 编译成独立的可执行文件。

# CAVEATS

仅支持 Linux。API 与 Node.js 不同，应用程序可能需要修改。生态规模小于 Node.js 或 Deno。

# HISTORY

just-js 的开发目标是一个面向 Linux 的极简 V8 运行时，注重低开销和直接的系统调用访问，而非像 Node.js 那样广泛的 API 兼容性。

# SEE ALSO

[node](/man/node)(1), [deno](/man/deno)(1), [bun](/man/bun)(1)
