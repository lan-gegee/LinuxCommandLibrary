# TAGLINE

命令行的自然语言界面

# TLDR

**向 Betty 提问**

```betty [whats my username]```

**统计目录中的字数**

```betty [how many words are in this directory]```

**查找包含文本的文件**

```betty [find me all files that contain california]```

**查看当前时间**

```betty [what time is it]```

**统计文件行数**

```betty [count lines in myfile.txt]```

**压缩文件**

```betty [compress this directory]```

**下载文件**

```betty [download https://example.com/file.zip]```

# SYNOPSIS

**betty** _natural language query_

# DESCRIPTION

**betty** 是一个友好的类英语命令行接口，使用 Ruby 编写。它将自然语言短语翻译成可执行的命令，让你不必离开终端去查询晦涩的语法。当你忘记某个命令时，直接用平实的英语问 Betty 即可。

Betty 会在运行前显示它推断出的命令。如果存在多种解释，它会给出带编号的选项并请你选择合适的一项，在此过程中也提供了学习机会。

# CAPABILITIES

**文件操作**
> 查找、计数、压缩、解压文件

**系统查询**
> 用户名、真实姓名、IP 地址、日期/时间、磁盘用量

**进程管理**
> 列出、查找、杀死进程

**文本处理**
> 统计单词数、行数、字符数

**网络**
> 下载文件、网页查询、天气

**权限**
> 更改文件所有者和权限

**媒体控制**
> 控制 iTunes 和 Spotify（播放、暂停、下一曲）

# INSTALLATION

需要 Ruby。克隆仓库并运行安装器（或手动添加别名）。

```
git clone https://github.com/pickhardt/betty
ruby betty/install.rb
# or, manually:
echo 'alias betty="~/betty/main.rb"' >> ~/.bashrc
source ~/.bashrc
```

# CAVEATS

需要 Ruby 运行时。仅限于预定义的命令模式。不适合复杂或非常规的命令。

# INSTALL

```brew: brew install betty```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [cheat](/man/cheat)(1)

# RESOURCES

```[Source code](https://github.com/pickhardt/betty)```

<!-- verified: 2026-06-19 -->
