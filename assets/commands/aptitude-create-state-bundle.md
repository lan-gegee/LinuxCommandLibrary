# TAGLINE

打包 aptitude 状态用于错误报告

# TLDR

**创建**用于错误报告的状态包

```aptitude-create-state-bundle [bundle.tar.bz2]```

以**详细输出**模式创建

```aptitude-create-state-bundle --verbose [bundle.tar.bz2]```

# SYNOPSIS

**aptitude-create-state-bundle** [_options_] _output-file_

# DESCRIPTION

**aptitude-create-state-bundle** 创建包含 aptitude 状态信息的压缩归档。该状态包对提交错误报告很有用，因为它捕获了重现问题所需的准确状态。

状态包包含软件包列表、aptitude 设置和依赖解析器状态。

# PARAMETERS

**--force-bzip2**
> 无论文件扩展名如何都强制使用 bzip2 压缩。

**--force-gzip**
> 即使 bzip2 可用也强制使用 gzip 压缩。

**--print-inputs**
> 显示将要包含的文件和目录列表，但不创建状态包。

**-v**, **--verbose**
> 详细输出

# CAVEATS

状态包可能包含系统特定信息。主要用于调试 aptitude 问题。在装有大量软件包的系统上可能产生较大的状态包。

# HISTORY

**aptitude-create-state-bundle** 的加入是为了帮助开发者重现和调试 aptitude 的依赖解析问题。

# INSTALL

```apt: sudo apt install aptitude```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aptitude](/man/aptitude)(8), [aptitude-run-state-bundle](/man/aptitude-run-state-bundle)(1)
