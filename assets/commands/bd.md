# TAGLINE

按名称跳转到父目录

# TLDR

**按名称**（或名称前几个字母）**跳回**父目录

```bd [name]```

**区分大小写**匹配

```bd -s [name]```

在父目录中**执行命令**而不切换过去

```ls `bd [name]` ```

# SYNOPSIS

**bd** [_-si_] _name_

# DESCRIPTION

**bd**（back directory）是一个 bash 工具，用于按名称快速跳转到父目录，免去输入多个 `cd ../../../` 的麻烦。它会沿着当前路径向上查找名称匹配的目录（匹配前几个字母即可）。

如果多个祖先目录同名，bd 会跳到最近的一个（直接父目录不算匹配）。它以 shell 别名的方式安装，这样目录切换才能在你的 shell 中生效：

```alias bd=". bd -si"```

# PARAMETERS

**-s**
> 区分大小写匹配（默认别名使用 **-si** 表示不区分大小写）。

**-i**
> 不区分大小写匹配（若本就是默认则无效果）。

# WORKFLOW

```bash
# Current path: /home/user/projects/myapp/src/components
# Jump up to 'myapp'
bd myapp
# Now in: /home/user/projects/myapp

# Or just the first letters
bd my

# Use a parent path inline without leaving the current directory
cp file.txt `bd projects`
```

# FEATURES

- 对父目录名进行前缀匹配
- 支持 Bash 补全（通过附带的补全文件）
- 路径中出现重名时选择最近的匹配

# CAVEATS

需要安装并在 shell 配置中设置别名（别名通过 source 加载脚本，使 `cd` 生效）。只沿当前路径向上遍历，不会进入兄弟目录树。为 bash 设计；zsh 和 fish 有各自的移植版本。大多数系统默认不带此工具。

# HISTORY

**bd** 由 Vigneshwaran Raveendran（vigneshwaranr）创建，目的是简化按名称向上遍历目录树的操作。

# INSTALL

```aur: yay -S bd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cd](/man/cd)(1), [pushd](/man/pushd)(1), [z](/man/z)(1)
