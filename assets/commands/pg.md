# TAGLINE

逐页显示文本文件，类似 more 和 less

# TLDR

**逐页查看**文件

```pg [path/to/file]```

显示**帮助**

```pg -h```

# SYNOPSIS

**pg** [**-**_number_] [**-p** _prompt_] [**-cefnrs**] [_file_...]

# PARAMETERS

**-_number_**
> 每页的行数

**-c**
> 显示每一页前先清屏

**-e**
> 到达文件末尾时不暂停

**-f**
> 不拆分长行

**-n**
> 接受不带换行符的命令

**-p _string_**
> 将 string 用作提示符

**-r**
> 允许受限的 Shell 逃逸

**-s**
> 以突出模式显示消息

# DESCRIPTION

**pg** 逐页显示文本文件，类似 more 和 less。它允许在文件中前后翻阅，并支持在已显示的内容中搜索。

这个分页器在提示符处接受多种命令：按回车前进一行，按空格前进一页，还可以用斜杠记法输入搜索模式。

# CAVEATS

功能不如 less 等现代分页器丰富。许多系统默认不安装它。主要用于兼容较旧的脚本和工作流程。

# HISTORY

**pg** 是一个较老的 Unix 分页器，比 **more** 和 **less** 出现得更早。它最初为 System V Unix 开发。虽然在很大程度上已被更强大的分页器取代，但它仍保留在 util-linux 中以供兼容。

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1), [cat](/man/cat)(1)
