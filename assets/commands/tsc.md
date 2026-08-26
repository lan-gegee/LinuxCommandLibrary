# TAGLINE

TypeScript 到 JavaScript 的编译器

# TLDR

**编译 TypeScript 文件**为 JavaScript

```tsc [file.ts]```

**使用 tsconfig.json** 配置编译

```tsc -p [tsconfig.json]```

**以监视模式编译**（文件变化时重新编译）

```tsc -w```

**启用 strict 模式**编译

```tsc --strict [file.ts]```

**编译为指定的 ECMAScript** 目标版本

```tsc --target [ES2020] [file.ts]```

**输出到指定目录**

```tsc --outDir [dist] [file.ts]```

**生成 source map**

```tsc --sourceMap [file.ts]```

**初始化新的 tsconfig.json**

```tsc --init```

# SYNOPSIS

**tsc** [_options_] [_file_...]

# PARAMETERS

**-p**, **--project** _path_
> 根据指定路径的 tsconfig.json 编译项目

**-w**, **--watch**
> 监视输入文件并在变化时重新编译

**-t**, **--target** _version_
> ECMAScript 目标版本（ES5、ES2015、ES2020、ES2022、ESNext）

**--outDir** _directory_
> 将输出重定向到指定目录

**--outFile** _file_
> 合并所有输出并写入单个文件

**--strict**
> 启用所有严格类型检查选项

**--noEmit**
> 不输出结果，仅进行类型检查

**--sourceMap**
> 生成对应的 .map source map 文件

**--declaration**
> 生成 .d.ts 声明文件

**--module** _system_
> 模块系统：commonjs、es2015、es2020、esnext、node16、nodenext

**--moduleResolution** _strategy_
> 模块解析策略：node、nodenext、bundler

**--incremental**
> 启用增量编译以加快重新构建速度

**--skipLibCheck**
> 跳过对声明文件的类型检查

**--esModuleInterop**
> 启用 CommonJS 与 ES Module 之间的互操作性

**--resolveJsonModule**
> 允许导入 .json 文件

**--jsx** _mode_
> JSX 处理方式：react、react-jsx、react-jsxdev、preserve

**--lib** _libs_
> 指定要包含的库文件（例如 ES2020、DOM、ES2020.Promise）

**--noEmitOnError**
> 存在任何报错时不输出结果

**--init**
> 初始化一个 tsconfig.json 文件

**--listFiles**
> 打印参与编译的文件名

**--showConfig**
> 打印最终解析后的配置而不是执行编译

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**tsc** 是 TypeScript 编译器，将 TypeScript（.ts、.tsx）文件转换为 JavaScript（.js）。TypeScript 由 Microsoft 开发，是 JavaScript 的超集，增加了可选的静态类型和现代语言特性。

在包含 **tsconfig.json** 的目录中不带参数运行时，tsc 会按照该配置编译整个项目。当在命令行上指定了文件时，除非使用 **-p**，否则 tsconfig.json 会被忽略。

编译器通过类型检查在开发阶段发现错误，然后输出合法的 JavaScript。**--strict** 选项启用全面的类型检查，包括严格的 null 检查和禁止隐式 any。

监视模式（**-w**）会监控源文件并在检测到变化时自动重新编译，实现快速的开发工作流。

# CAVEATS

tsc 依赖 Node.js，通常通过 npm 安装（**npm install -g typescript**）。命令行上的编译选项会覆盖 tsconfig.json 的设置。当在命令行上指定文件时，**tsconfig.json** 会被忽略（请用 **-p** 来使用配置文件）。大型项目的编译可能较慢；对于仅需类型检查的工作流，可以考虑使用 **--incremental** 或 **--noEmit**。

# HISTORY

**TypeScript** 由 **Microsoft** 在 **Anders Hejlsberg**（C# 和 Turbo Pascal 之父）的主导下开发，于 **2012 年 10 月**首次公开发布。该语言旨在通过添加可选静态类型来应对大规模 JavaScript 开发的挑战，同时与现有 JavaScript 保持完全兼容。

# INSTALL

```dnf: sudo dnf install typescript```

```pacman: sudo pacman -S typescript```

```apk: sudo apk add typescript```

```zypper: sudo zypper install typescript```

```brew: brew install typescript```

```nix: nix profile install nixpkgs#typescript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [ts-node](/man/ts-node)(1), [esbuild](/man/esbuild)(1), [swc](/man/swc)(1), [webpack](/man/webpack)(1), [babel](/man/babel)(1)
