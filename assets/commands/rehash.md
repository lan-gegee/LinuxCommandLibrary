# TAGLINE

重建命令哈希表

# TLDR

**重建命令哈希表**

```rehash```

**安装新软件后重建哈希表**

```sudo apt install [package] && rehash```

# SYNOPSIS

**rehash**

# DESCRIPTION

**rehash** 是一个 shell 内建命令，用于重建可执行命令的内部哈希表。shell 维护一张将命令名映射到其完整路径的哈希表，以避免重复搜索 **$PATH**。当安装或卸载新程序时，这张表可能过时，导致 shell 对新安装的程序报告 "command not found"，或执行过时的路径。

运行 **rehash** 会强制 shell 丢弃缓存的哈希表，并重新发现 **$PATH** 所列目录中的所有可执行文件。

在 **zsh** 中，rehash 还会重新生成补全列表，使 Tab 补全能够反映新安装的命令。

# CAVEATS

在 **bash** 中，等价命令是 **hash -r**。大多数现代 shell 在 **$PATH** 被修改时会自动处理，但对于出现在已有 **$PATH** 目录中的新装程序，可能仍需手动 rehash。该命令只影响当前 shell 会话。

# HISTORY

命令哈希机制由 **Bourne Shell** 引入，通过缓存命令位置来提升性能。**rehash** 内建命令出现于 **csh**（1978 年），随后被 **tcsh**、**zsh** 等 shell 采纳。Bash 使用 **hash** 内建命令代替，但支持相同的概念。

# SEE ALSO

[hash](/man/hash)(1), [which](/man/which)(1), [type](/man/type)(1), [zsh](/man/zsh)(1), [csh](/man/csh)(1), [tcsh](/man/tcsh)(1)
