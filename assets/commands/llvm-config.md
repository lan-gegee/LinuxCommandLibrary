# TAGLINE

提供针对 LLVM 进行构建所需的配置信息

# TLDR

**显示 LLVM 版本**

```llvm-config --version```

**显示编译器标志**

```llvm-config --cxxflags```

**显示链接器标志**

```llvm-config --ldflags```

**显示库名称**

```llvm-config --libs```

**显示特定组件的标志**

```llvm-config --cxxflags --ldflags --libs core```

**显示安装前缀**

```llvm-config --prefix```

# SYNOPSIS

**llvm-config** [_options_] [_components_...]

# PARAMETERS

**--version**
> 打印 LLVM 版本。

**--prefix**
> 打印安装前缀。

**--cxxflags**
> 打印 C++ 编译器标志。

**--ldflags**
> 打印链接器标志。

**--libs**
> 打印库名称。

**--system-libs**
> 打印系统库名称。

**--components**
> 打印可用组件。

**--targets-built**
> 打印可用的目标架构。

# DESCRIPTION

**llvm-config** 提供针对 LLVM 进行构建所需的配置信息。输出编译和链接基于 LLVM 库的程序所需的编译器标志、链接器标志和库名称。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm-dev```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [llc](/man/llc)(1)
