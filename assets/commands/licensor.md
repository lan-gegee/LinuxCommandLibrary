# TAGLINE

为开源项目生成许可证文本

# TLDR

**生成 MIT 许可证**并指定版权持有人姓名

```licensor MIT "[Your Name]"```

**生成 Apache 许可证**并保存到文件

```licensor Apache-2.0 > LICENSE```

**生成 GPL 许可证**

```licensor GPL-3.0```

**带例外表达式生成许可证**

```licensor "Apache-2.0 WITH LLVM-exception" --skip-optional```

**列出可用许可证**

```licensor --licenses```

# SYNOPSIS

**licensor** _license_ [_name_] [_options_]

# PARAMETERS

_LICENSE_
> SPDX 许可证标识符（MIT、Apache-2.0、GPL-3.0 等）。支持例外表达式。

_NAME_
> 版权持有人姓名（可选，用于包含该信息的许可证）。

**--licenses**
> 列出所有可用的 SPDX 许可证标识符。

**--skip-optional**
> 省略许可证文本中的可选章节。

**--help**
> 显示帮助信息。

# DESCRIPTION

**licensor** 根据给定的 SPDX 许可证标识符将许可证文本写入 stdout。所有许可证都编译进了二进制文件。如果提供的 ID 未找到，会建议相似的 ID。

该工具输出的许可证文本格式规范，版权持有人和年份均已填入。

# CAVEATS

使用 SPDX 标识符。基于 Rust 的工具。可能需要通过 cargo 安装。

# HISTORY

licensor 由 **Raphael Theriault**（raftario）创建，是一个使用 SPDX 许可证标识符的 **Rust** 许可证文本生成器。

# INSTALL

```brew: brew install licensor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[license](/man/license)(1), [cargo](/man/cargo)(1)
