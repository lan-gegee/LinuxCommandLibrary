# TAGLINE

移除 Python 3 编译字节码文件

# TLDR

**清理 Python 3 字节码**

```py3clean [directory]```

**清理整个系统**

```sudo py3clean -p [package]```

**试运行（dry run）**

```py3clean -n [directory]```

**详细输出**

```py3clean -v [directory]```

# SYNOPSIS

**py3clean** [_options_] _directory_|**-p** _package_

# PARAMETERS

**-p**, **--package** _package_
> 清理指定的 Debian 软件包。

**-v**, **--verbose**
> 详细输出。

**-n**, **--dry-run**
> 显示将被删除的内容。

**-q**, **--quiet**
> 静默模式。

# DESCRIPTION

**py3clean** 移除 Python 3 编译字节码文件（.pyc）和 __pycache__ 目录。它是 Debian 的 python3-minimal 软件包的一部分，用于系统清理。

# EXAMPLES

```bash
# Clean project directory
py3clean /path/to/project

# Clean installed package
sudo py3clean -p python3-requests

# Dry run first
py3clean -n /usr/lib/python3

# Verbose cleaning
py3clean -v ~/myproject

# Clean current directory
py3clean .
```

# WHAT IT REMOVES

```
*.pyc files
__pycache__/ directories
```

# CAVEATS

Debian/Ubuntu 专用工具。替代方案：find . -name '*.pyc' -delete。字节码会在下次导入时重新生成。

# HISTORY

py3clean 是 Debian 的 **dh-python** 软件包的一部分，用于 Python 3 打包与清理。

# INSTALL

```apt: sudo apt install python3-minimal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pyclean](/man/pyclean)(1), [python3](/man/python3)(1)
