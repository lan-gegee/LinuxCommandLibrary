# TAGLINE

JavaScript 静态类型检查器

# TLDR

对项目进行**类型检查**

```flow check```

**启动 Flow 服务器**

```flow server```

**检查单个文件**

```flow check-contents < [file.js]```

**初始化 Flow 配置**

```flow init```

**获取位置处的类型**

```flow type-at-pos [file.js] [10] [5]```

# SYNOPSIS

**flow** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 操作类型：check、server、status、init 等。

**check**
> 对所有文件进行类型检查。

**server**
> 启动后台服务器。

**status**
> 显示服务器状态和错误。

**init**
> 创建 .flowconfig 文件。

**stop**
> 停止后台服务器。

**type-at-pos** _FILE_ _LINE_ _COL_
> 获取指定位置的类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flow** 是 Facebook 出品的 JavaScript 静态类型检查器。它通过类型注解和类型推断实现渐进式类型化，在运行之前捕获错误。

该工具以后台服务器方式运行，可实现快速的增量检查。类型注解使用 JavaScript 语法的超集，会在构建阶段剥离。

Flow 与编辑器集成以进行实时类型检查，并提供包含修复建议的详细错误信息。

# CONFIGURATION

**.flowconfig**
> 配置文件，控制 Flow 检查哪些文件、库定义、lint 规则以及类型检查行为的相关选项。

# CAVEATS

需要 .flowconfig 文件。并非与所有 JavaScript 编写模式兼容。需要构建步骤来剥离类型注解。

# HISTORY

Flow 由 **Facebook**（现 Meta）于 2014 年创建，目的是为其 JavaScript 代码库增加类型安全。它与 TypeScript 竞争，提供了一种不同的渐进式类型化方案。

# INSTALL

```apt: sudo apt install libopm-simulators-bin```

```brew: brew install flow```

```nix: nix profile install nixpkgs#flow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tsc](/man/tsc)(1), [eslint](/man/eslint)(1), [node](/man/node)(1)

# RESOURCES

```[Homepage](https://flow.org/)```

```[Source code](https://github.com/facebook/flow)```

<!-- verified: 2026-07-15 -->
