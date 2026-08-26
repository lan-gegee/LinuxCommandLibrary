# TAGLINE

遗留的 Python 2.7 解释器

# TLDR

**运行 Python 2.7 脚本**

```python2.7 [script.py]```

**交互模式**

```python2.7```

**执行命令**

```python2.7 -c "[print 'hello']"```

**运行模块**

```python2.7 -m [module]```

# SYNOPSIS

**python2.7** [_options_] [_script_] [_args_]

# PARAMETERS

**-c** _command_
> 执行命令。

**-m** _module_
> 以脚本方式运行库模块。

**-i**
> 脚本执行后进入交互模式。

**-u**
> I/O 不使用缓冲。

**-O**
> 优化字节码。

**-v**
> 导入过程详细输出。

**-V**
> 打印版本。

# DESCRIPTION

**python2.7** 是 Python 2.7 解释器。Python 2 已于 2020 年 1 月 1 日终止支持，只应用于维护遗留代码。

所有新开发都请使用 Python 3。

# EXAMPLES

```bash
# Run script
python2.7 legacy_script.py

# Check version
python2.7 --version

# One-liner (note print statement)
python2.7 -c "print 'Hello, Python 2'"

# Install pip for Python 2
python2.7 -m ensurepip
```

# KEY DIFFERENCES FROM PYTHON 3

```python
# Python 2 syntax
print "hello"              # Statement
raw_input("Name: ")        # User input
unicode_string = u"text"   # Unicode prefix
5 / 2 == 2                 # Integer division
```

# CAVEATS

Python 2 已停止支持且不再接收更新。安全漏洞不会修复。请迁移到 Python 3。

# HISTORY

Python 2.0 发布于 2000 年。Python 2.7 是最后一个 2.x 版本（2010 年），支持已于 2020 年 1 月 1 日结束。

# SEE ALSO

[python3](/man/python3)(1), [2to3](/man/2to3)(1), [pip](/man/pip)(1)
