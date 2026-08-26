# TAGLINE

查找源文件与测试文件的对应关系，便于相互切换

# TLDR

为一个源文件**查找**对应文件

```alt [path/to/file.rb]```

**查找**对应文件且只显示排名最**靠前**的结果

```alt --truncate [1] [path/to/file.rb]```

**查找**对应文件，包含**隐藏**文件

```alt -a [path/to/file.rb]```

从**标准输入**读取文件列表来**查找**对应文件

```find . -type f -print | alt -f - [path/to/file.rb]```

# SYNOPSIS

**alt** [_options_] _path_

# DESCRIPTION

**alt** 为给定的源文件查找"对应文件"，通常用于在实现文件和测试文件之间切换。它会按与给定路径的相似度对项目中的所有文件排序，并按排名顺序输出。

例如，给定 **app/models/user.rb**，它会找到 **test/models/user_test.rb** 或 **spec/models/user_spec.rb**。这使得在 Vim、NeoVim 和 VS Code 等编辑器集成中于代码与测试之间跳转变得十分方便。

默认情况下，**alt** 会忽略隐藏目录项、**.ignore** 文件中定义的 glob 模式，以及项目的 **.gitignore** 和全局 **.gitignore** 中定义的模式。

# PARAMETERS

**-a**
> 在搜索中包含隐藏文件和目录。

**-f** _-_
> 从标准输入读取文件路径，而不是扫描目录。

**-t** _N_, **--truncate** _N_
> 将输出截断为 N 个对应文件（默认 0，表示显示全部）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

对应文件匹配依赖于基于常见命名约定的路径相似度排名；不寻常的项目结构可能产生意外结果。默认按排名顺序显示所有可能的对应文件；使用 **--truncate 1** 可只获取最佳匹配。

# HISTORY

**alt** 由 **Drew De Ponte**（uptech）创建，是一款快速、不依赖特定编辑器的查找对应文件的命令行工具。它使用 Rust 编写，最初为 Vim 集成而设计，但也可配合任何编辑器或 Shell 工作流使用。

# SEE ALSO

[find](/man/find)(1), [fd](/man/fd)(1), [fzf](/man/fzf)(1)
