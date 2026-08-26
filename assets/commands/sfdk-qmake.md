# TAGLINE

在 Sailfish 构建环境中运行 qmake

# TLDR

**在构建环境中运行 qmake**

```sfdk qmake```

**以 debug 选项进行配置**

```sfdk qmake CONFIG+=debug```

**显示 qmake 帮助**

```sfdk qmake --help```

# SYNOPSIS

**sfdk qmake** [_qmake_options_]

# DESCRIPTION

**sfdk qmake** 使用正确的 Qt 配置在 Sailfish OS 构建环境内运行 qmake。与 **sfdk make** 配合使用时，可以只执行 SPEC 文件 %build 区段中对应的部分来运行 rpmbuild。属于 Sailfish SDK 的一部分。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-cmake](/man/sfdk-cmake)(1), [sfdk-make](/man/sfdk-make)(1), [qmake](/man/qmake)(1)
