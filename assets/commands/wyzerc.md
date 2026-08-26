# TAGLINE

Wyzer 编程语言的编译器与运行器

# TLDR

从源码检出**构建**编译器（OCaml / Dune）

```dune build```

**运行** Wyzer 程序（解释器路径）

```wyzerc run [file.wyz]```

通过 LLVM + clang 将程序**编译**为原生二进制文件

```wyzerc build [file.wyz]```

**投影**编排（choreography）到指定角色后运行

```wyzerc run [file.wyz] --role [RoleName]```

**为特定角色构建**（输出 _base_Role.ll_ 及链接好的二进制文件）

```wyzerc build [file.wyz] --role [RoleName]```

# SYNOPSIS

**wyzerc** **run**|**build** _file.wyz_ [**--role** _RoleName_]

# DESCRIPTION

**wyzerc** 是 **Wyzer** 的编译器前端。Wyzer 是一种静态类型、面向资源的编程语言，采用 Perceus 风格的内存管理，并通过编排式编程（choreographic programming）保障分布式安全。源文件使用 **.wyz** 扩展名。

以 **wyzerc run** _file.wyz_ 调用时，该工具会解析并做类型检查，应用 Perceus 变换，然后在内置的 OCaml 解释器中求值。**wyzerc build** 走相同的前端流程，随后生成 LLVM IR（**_base_Role.ll_**），并调用 **clang** 配合 Wyzer 运行时（**lib/wyzer_runtime.c**）生成名为 **_base_Role_** 的原生二进制文件（省略 **--role** 时默认角色为 **Poly**）。

可选的 **--role** 用于选择编排投影，使多方程序可以按参与者分别特化。该项目尚处早期研究阶段；部分语言特性和分布式特性仍未完成。

# PARAMETERS

**run** _file.wyz_
> 对 _file.wyz_ 进行类型检查、变换并用解释器执行。

**build** _file.wyz_
> 进行类型检查、变换、生成 LLVM IR，再用 **clang -O3** 加 Wyzer C 运行时编译。

**--role** _RoleName_
> 在求值或代码生成前将程序投影到 _RoleName_。build 的默认角色为 **Poly**。

# CAVEATS

构建 **wyzerc** 本身需要 OCaml 工具链（Dune、Menhir、LLVM 绑定及相关 opam 包）；**build** 模式还需要 **clang** 和仓库内的 **lib/wyzer_runtime.c**。目前还没有完善的包管理器安装途径——典型工作流是克隆仓库、安装 **opam** 依赖，然后执行 **dune build** / **dune exec wyzerc**。较旧的文档有时会展示不带 **run**/**build** 子命令的 **dune exec wyzerc -- file.wyz** 用法；当前用法要求将 **run** 或 **build** 作为第一个参数。项目状态为实验性研究，尚未达到生产可用。

# HISTORY

**Wyzer** 是一门研究性语言，探索用同一条所有权规则统一内存、并发和网络协议的处理，它将 Perceus 引用计数与编排式编程相结合。**wyzerc** 是上游仓库中编译器的公开 Dune 可执行文件名。

# SEE ALSO

[clang](/man/clang)(1), [dune](/man/dune)(1), [opam](/man/opam)(1)

# RESOURCES

```[Source code](https://github.com/Wyzer-Lang/wyzer)```

```[Documentation](https://github.com/Wyzer-Lang/wyzer/tree/master/docs)```

<!-- verified: 2026-08-07 -->
