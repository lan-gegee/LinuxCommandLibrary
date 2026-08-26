# TAGLINE

OCaml 库的软件包管理器

# TLDR

**带软件包编译**

```ocamlfind ocamlc -package [str] -linkpkg [program.ml] -o [program]```

**带软件包进行原生编译**

```ocamlfind ocamlopt -package [core,yojson] -linkpkg [program.ml] -o [program]```

**列出已安装的软件包**

```ocamlfind list```

**显示软件包信息**

```ocamlfind query [package]```

**显示软件包目录**

```ocamlfind query -d [package]```

**显示软件包依赖**

```ocamlfind query -r [package]```

**安装软件包**

```ocamlfind install [package] META [*.cmi] [*.cmo] [*.cma]```

**移除软件包**

```ocamlfind remove [package]```

# SYNOPSIS

**ocamlfind** [_ocamlc_] [_ocamlopt_] [_query_] [_list_] [_install_] [_-package pkgs_] [_options_] [_files_]

# PARAMETERS

**ocamlc** _ARGS_
> 运行字节码编译器。

**ocamlopt** _ARGS_
> 运行原生编译器。

**query** _PKG_
> 查询软件包信息。

**list**
> 列出已安装的软件包。

**install** _PKG_ _FILES_
> 安装软件包。

**remove** _PKG_
> 移除软件包。

**-package** _PKGS_
> 要使用的软件包（逗号分隔）。

**-linkpkg**
> 将软件包链接进可执行文件。

**-predicates** _PREDS_
> 设置谓词。

**-syntax** _SYNTAX_
> 设置语法扩展。

**-d**
> 显示软件包目录。

**-r**
> 递归解析依赖。

# DESCRIPTION

**ocamlfind** 是 OCaml 库的软件包管理器。它可以定位已安装的软件包并自动配置编译器调用。

该工具封装了 OCaml 编译器，根据软件包规范自动添加包含路径和库引用，通过处理库依赖来简化构建过程。

每个软件包都有一个 META 文件，描述其组件、依赖和位置。查询命令可提取这些信息供构建系统和脚本使用。

软件包安装会将库放入带有 META 文件的中央仓库。这种标准化布局使可靠的发现和链接成为可能。

依赖会以传递方式解析。指定一个高层软件包时会自动包含其前置依赖。

与 Dune 等构建系统的集成很常见。许多项目直接使用 ocamlfind 或通过包装工具使用它。

# CAVEATS

在现代项目中，软件包安装已被 opam 取代。手动创建 META 文件容易出错。并非所有软件包都带有 META 文件。

# HISTORY

**ocamlfind**（findlib）由 **Gerd Stolpmann** 自 **2000 年代初期**创建，旨在标准化 OCaml 库管理。它成为 OCaml 软件包生态的基础，后来由 opam 补充了下载和安装软件包的功能。

# INSTALL

```apt: sudo apt install ocaml-findlib```

```dnf: sudo dnf install ocaml-findlib```

```pacman: sudo pacman -S ocaml-findlib```

```apk: sudo apk add ocamlfind```

```zypper: sudo zypper install ocaml-findlib```

```brew: brew install ocaml-findlib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocaml](/man/ocaml)(1), [ocamlc](/man/ocamlc)(1), [ocamlopt](/man/ocamlopt)(1), [opam](/man/opam)(1), [dune](/man/dune)(1)
