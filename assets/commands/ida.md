# TAGLINE

用于分析二进制可执行文件的反汇编器和调试器

# TLDR

**在 IDA 中打开二进制文件**

```ida [binary]```

**以文本模式运行 IDA**

```ida -T [binary]```

**批处理模式分析**

```ida -B [binary]```

**运行脚本**

```ida -S[script.py] [binary]```

**打开 64 位二进制文件**

```ida64 [binary]```

# SYNOPSIS

**ida** [_options_] [_file_]

**ida64** [_options_] [_file_]

# PARAMETERS

_file_
> 要分析的二进制文件。

**-T**
> 文本模式（无 GUI）。

**-B**
> 批处理模式（分析后退出）。

**-A**
> 自主模式（自动应答对话框）。

**-S**_script_
> 启动时运行脚本。

**-L**_logfile_
> 日志文件。

**-c**
> 创建新数据库。

**-o**_database_
> 输出数据库文件。

# DESCRIPTION

**IDA**（Interactive DisAssembler，交互式反汇编器）是用于分析二进制可执行文件的反汇编器和调试器。它是逆向工程、恶意软件分析和漏洞研究领域的行业标准。

IDA 支持众多处理器架构和文件格式。它提供交叉引用、函数识别以及 IDAPython 脚本接口等功能。

# EDITIONS

- **IDA Free**：功能受限的免费版本
- **IDA Home**：个人使用版本
- **IDA Pro**：完整专业版本

# SCRIPTING

```python
# IDAPython example
import idautils
for func in idautils.Functions():
    print(hex(func), idc.get_func_name(func))
```

# CAVEATS

商业软件（免费版有功能限制）。大型二进制文件需要大量内存。数据库文件可能很大。要熟练使用需要一定的学习成本。

# HISTORY

IDA 由 **Ilfak Guilfanov** 开发，首次发布于 **1991 年**。它由 Hex-Rays 维护开发，已成为安全研究领域二进制分析的事实标准。

# INSTALL

```dnf: sudo dnf install fbida-ida```

```apk: sudo apk add fbida-ida```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[radare2](/man/radare2)(1), [objdump](/man/objdump)(1)
