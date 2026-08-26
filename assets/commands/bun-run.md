# TAGLINE

执行文件和软件包脚本

# TLDR

**运行 JavaScript/TypeScript 文件**

```bun run [script.ts]```

**运行 package.json 脚本**

```bun run [start]```

**以监视模式运行文件**

```bun --watch run [script.ts]```

**列出可用脚本**

```bun run```

**求值代码字符串**

```bun run --eval "[console.log('hello')]"```

**求值并打印结果**

```bun run --print "[1 + 2]"```

**使用环境文件运行**

```bun run --env-file [.env] [script.ts]```

# SYNOPSIS

**bun run** [_options_] _file|script_ [_arguments_]

**bun** _file|script_ [_arguments_]

# DESCRIPTION

**bun run** 使用 Bun 快速的原生转译器执行 JavaScript、TypeScript 和 JSX 文件。它还可以在支持生命周期钩子的情况下运行 package.json 脚本。

该命令可以简写为 **bun** 后跟文件或脚本名称，但内置命令具有更高的优先级。

# PARAMETERS

**--watch**
> 文件变化时重新运行。必须放在命令中 `run` 之前。

**--hot**
> 启用热重载，而不是在文件变化时完全重启。

**--eval, -e** _code_
> 将参数作为脚本求值

**--print, -p** _code_
> 求值并打印结果

**--env-file** _file_
> 从文件加载环境变量

**--cwd** _directory_
> 设置工作目录

**--silent**
> 抑制脚本输出

**--smol**
> 通过更频繁地运行垃圾回收器来降低内存使用，代价是性能下降。

**--if-present**
> 如果入口点或脚本不存在，则无错误退出。

**--filter** _pattern_
> 按名称模式在匹配的工作区软件包中运行脚本。

**--bun**
> 强制脚本通过 Bun 的运行时运行，覆盖 shebang 行。

# BEHAVIOR

**源文件**
> 以 ./ 开头或绝对路径的路径作为源文件运行

**软件包脚本**
> package.json 中定义的脚本会连同生命周期钩子（pre/post）一起执行

**解析规则**
> 使用 bun run 时，package.json 脚本优先于同名文件

# LIFECYCLE HOOKS

Bun 支持 pre 和 post 生命周期钩子。运行 **bun run build** 会依次执行 **prebuild**、**build** 和 **postbuild**。如果 pre 脚本失败，主脚本将不会执行。

# CAVEATS

TypeScript 和 JSX 无需配置即可即时转译。启动时间明显快于 npm run。某些 Node.js 特有的 API 可能不可用。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-test](/man/bun-test)(1), [bun-build](/man/bun-build)(1), [node](/man/node)(1), [npm-run](/man/npm-run)(1)
