# TAGLINE

在 Sailfish 构建环境中运行 CMake

# TLDR

**在构建环境中运行 CMake**

```sfdk cmake [cmake_args]```

**以 Release 构建类型进行配置**

```sfdk cmake -DCMAKE_BUILD_TYPE=Release```

**配置并使用 make 构建**

```sfdk cmake [cmake_args] && sfdk make```

**显示帮助**

```sfdk cmake --help```

# SYNOPSIS

**sfdk cmake** [_cmake_options_]

# DESCRIPTION

**sfdk cmake** 使用正确的工具链配置在 Sailfish OS 构建环境内运行 CMake。与 **sfdk make** 配合使用时，可以只执行 SPEC 文件 %build 区段中对应的部分来运行 rpmbuild。属于 Sailfish SDK 的一部分。

对于使用 qmake 或 CMake 的项目，还提供原生构建系统支持。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-qmake](/man/sfdk-qmake)(1), [cmake](/man/cmake)(1)
