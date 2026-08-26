# TAGLINE

面向 WebAssembly 组件的 JavaScript 工具集

# TLDR

**转译 WASM 组件**

```jco transpile [component.wasm] -o [output/]```

**从模块创建组件**

```jco componentize [module.wasm] -o [component.wasm]```

**检查组件**

```jco print [component.wasm]```

**运行组件**

```jco run [component.wasm]```

**生成类型定义**

```jco types [component.wasm] -o [types/]```

# SYNOPSIS

**jco** _command_ [_options_] _file_

# PARAMETERS

**transpile** _FILE_
> 转换为 JavaScript。

**componentize** _FILE_
> 从核心模块创建组件。

**print** _FILE_
> 打印组件信息。

**run** _FILE_
> 执行组件。

**types** _FILE_
> 生成 TypeScript 类型。

**-o** _DIR_
> 输出目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jco** 是面向 WebAssembly 组件的 JavaScript 工具集。它将 WASM 组件转译为 JavaScript，供浏览器/Node.js 使用。

该工具遵循组件模型标准。它生成 JavaScript 绑定和 TypeScript 类型定义。

# CAVEATS

WASM 标准仍处于实验阶段。Bytecode Alliance 项目。Node.js 工具。

# HISTORY

jco 由 **Bytecode Alliance** 创建，是为 WebAssembly Component Model 标准提供的 JavaScript 工具集。

# SEE ALSO

[wasmtime](/man/wasmtime)(1)
