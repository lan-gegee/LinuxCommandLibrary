# TAGLINE

将 C/C++ 编译为 WebAssembly 或 JavaScript

# TLDR

**将 C 编译为 WebAssembly**

```emcc [input.c] -o [output.wasm]```

**编译为 JavaScript**

```emcc [input.c] -o [output.js]```

**附带 HTML 宿主页面编译**

```emcc [input.c] -o [output.html]```

**编译 C++**

```em++ [input.cpp] -o [output.js]```

**针对体积优化**

```emcc -Os [input.c] -o [output.wasm]```

**针对速度优化**

```emcc -O3 [input.c] -o [output.wasm]```

**导出指定函数**

```emcc -sEXPORTED_FUNCTIONS=['_main','_myFunc'] [input.c] -o [output.js]```

# SYNOPSIS

**emcc** [_options_] _files_

# PARAMETERS

**-o** _file_
> 输出文件（.js、.wasm、.html）。

**-O0** 到 **-O3**、**-Os**、**-Oz**
> 优化级别。

**-s** _SETTING=VALUE_
> Emscripten 特有设置。

**-I** _dir_
> 头文件目录。

**-L** _dir_
> 库目录。

**-l** _lib_
> 链接库。

**-g**
> 生成调试信息。

**--preload-file** _path_
> 将文件预加载到虚拟文件系统。

**--embed-file** _path_
> 将文件嵌入输出中。

**-sMODULARIZE**
> 以 ES6 模块形式输出。

# CONFIGURATION

**.emscripten**
> Emscripten 配置文件，包含 SDK 路径与编译器设置。

# DESCRIPTION

**emcc**（Emscripten Compiler Frontend）使用 LLVM 和 Emscripten 将 C 与 C++ 代码编译为 WebAssembly（Wasm）或 JavaScript。它使原生代码能够在 Web 浏览器及其他 Wasm 运行时中运行。

Emscripten 为 POSIX API、OpenGL（通过 WebGL）和 SDL 提供兼容层。它可以编译完整的代码库，包括游戏和应用程序，让它们在浏览器中运行。

# CAVEATS

并非所有 C/C++ 特性的行为都完全一致。文件系统访问依赖虚拟文件系统。线程需要 SharedArrayBuffer。性能与原生代码有差异。大型应用可能编译时间很长。还受浏览器安全限制的约束。

# HISTORY

Emscripten 由 **Alon Zakai** 于 **2011 年**在 Mozilla 创建，最初以 asm.js 为目标，当时 WebAssembly 尚未问世。**2017 年** WebAssembly 发布后，Emscripten 成为将 C/C++ 带入 Web 的主要编译器工具链。

# SEE ALSO

[clang](/man/clang)(1), [wasm2wat](/man/wasm2wat)(1)
