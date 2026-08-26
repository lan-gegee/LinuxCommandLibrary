# TAGLINE

从源码构建 Python 软件包

# TLDR

**构建软件包**

```uv build```

**仅构建 wheel**

```uv build --wheel```

**仅构建 sdist**

```uv build --sdist```

**构建到指定目录**

```uv build --out-dir [dist]```

**同时构建 sdist 和 wheel**

```uv build --sdist --wheel```

在工作区中**构建指定的软件包**

```uv build --package [mypackage]```

**从指定的源码目录构建**

```uv build [src/]```

# SYNOPSIS

**uv** **build** [_options_] [_src_]

# PARAMETERS

**--wheel**
> 仅构建 wheel（二进制发行版）。

**--sdist**
> 仅构建源代码发行版。

**--out-dir** _dir_
> 输出目录。默认：dist/。

**--no-build-isolation**
> 禁用构建隔离（使用现有环境）。

**--package** _name_
> 在当前工作区内构建指定的软件包。

**--build-constraint** _requirement_
> 限制构建需求的版本。

**--require-hashes**
> 要求构建依赖提供哈希值以保证可复现性。

**--python** _version_
> 用于构建的 Python 解释器。

**--config-setting** _KEY=VALUE_
> 向 PEP 517 构建后端传递设置。

**--all-packages**
> 构建工作区中的所有软件包。

# DESCRIPTION

**uv build** 从源码构建 Python 软件包，生成可分发的 wheel 和/或源代码发行版软件包。它支持 PEP 517/518 构建系统。

默认情况下，uv build 构建当前目录中的项目，并将产物放在 dist/ 子目录中。默认会同时生成 wheel 和 sdist；可使用 **--wheel** 或 **--sdist** 只构建其中一种。

构建隔离默认启用，会在隔离的环境中安装构建依赖。可使用 **--no-build-isolation** 改为在现有环境中构建。

# INSTALL

```apk: sudo apk add py3-uv-build```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-publish](/man/uv-publish)(1), [pip](/man/pip)(1), [build](/man/build)(1)
