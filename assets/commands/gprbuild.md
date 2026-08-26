# TAGLINE

支持 GNAT 项目感知的 Ada 构建工具

# TLDR

**构建项目**

```gprbuild -P [project.gpr]```

**使用配置构建**

```gprbuild -P [project.gpr] -XBUILD_MODE=release```

**清理并构建**

```gprbuild -P [project.gpr] --clean```

**并行构建**

```gprbuild -P [project.gpr] -j[4]```

# SYNOPSIS

**gprbuild** [_options_] [_project_]

# PARAMETERS

_PROJECT_
> 项目文件（.gpr）。

**-P** _FILE_
> 项目文件。

**-X** _NAME=VALUE_
> 外部变量。

**-j** _N_
> 并行任务数。

**--clean**
> 构建前先清理。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gprbuild** 是 GNAT 面向 Ada 的项目感知构建工具。它编译以 GPR（GNAT Project）文件定义的 Ada 项目，自动处理依赖关系和构建配置。

该工具通过增量构建管理 Ada 源码的编译，并支持通过外部变量和多种构建模式进行配置。

# CAVEATS

仅适用于 Ada/GNAT。需要 GPR 项目文件。属于 GNAT 工具链的一部分。

# HISTORY

gprbuild 是 **GNAT** Ada 工具链的一部分，由 AdaCore 开发，用于构建 Ada 项目。

# INSTALL

```apt: sudo apt install gprbuild```

```dnf: sudo dnf install gprbuild```

```nix: nix profile install nixpkgs#gprbuild```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnat](/man/gnat)(1), [gnatmake](/man/gnatmake)(1)

# RESOURCES

```[Source code](https://github.com/AdaCore/gprbuild)```

<!-- verified: 2026-07-17 -->
