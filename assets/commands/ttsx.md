# TAGLINE

先对整个项目进行类型检查，再执行 TypeScript

# TLDR

**运行** TypeScript 入口文件

```ttsx src/index.ts```

**运行**并向脚本传递参数

```ttsx src/cli.ts -- --flag value```

通过 **npx****先类型检查再执行**

```npx ttsx src/main.ts```

# SYNOPSIS

**ttsx** _file_ [_script_args_...]

# DESCRIPTION

**ttsx** 是 **ttsc** 的执行伴侣。与 **tsx** 或 **ts-node** 类似，它无需单独的编译步骤即可运行 TypeScript 文件，但会先对**整个项目**进行类型检查。如果类型检查失败，进程会在任何用户代码运行之前退出。

它使用与 **ttsc** 相同的 **typescript-go** 工具链和插件管道，因此编译器插件（转换、**typia**、lint 诊断等）在每次运行时都会生效。安装方式为 **npm install -D ttsc typescript**（**ttsx** 二进制随 **ttsc** 软件包一起提供），然后通过 **npx ttsx** 或包脚本调用。

# PARAMETERS

_file_
> 要进行类型检查并执行的 TypeScript 入口文件

_script_args_
> 转发给运行中程序的参数（使用 **npx** 时通常放在 **--** 之后）

# CAVEATS

与仅转译的运行器相比，全项目类型检查会增加启动延迟。项目配置必须有效（能找到 **tsconfig.json**）。具体行为取决于已安装的 **ttsc** 版本以及启用的插件。若只需构建/检查而不执行，请改用 **ttsc**。

# HISTORY

属于 Jeongho Nam（**samchon**）的 **ttsc** 工具链的一部分，定位为基于 **typescript-go** 的类型安全版 **tsx** 和 **ts-node** 替代方案。

# SEE ALSO

[ttsc](/man/ttsc)(1), [tsx](/man/tsx)(1), [ts-node](/man/ts-node)(1), [tsc](/man/tsc)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/samchon/ttsc)```

```[Homepage](https://ttsc.dev)```

```[Documentation](https://ttsc.dev/docs/ttsc/execute/)```

<!-- verified: 2026-07-17 -->
