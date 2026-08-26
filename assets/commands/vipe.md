# TAGLINE

在管道中插入文本编辑器

# TLDR

**编辑管道内容**

```echo "text" | vipe```

**编辑命令输出**

```cat [file.txt] | vipe | [next_command]```

**使用指定编辑器编辑**

```EDITOR=[vim] cat [file.txt] | vipe```

**交互式转换数据**

```echo '{"key": "value"}' | vipe | jq .```

# SYNOPSIS

**vipe** < _stdin_ > _stdout_

# ENVIRONMENT

**EDITOR** - 所使用的编辑器
**VISUAL** - 可视化编辑器

# DESCRIPTION

**vipe** 将文本编辑器插入 Unix 管道中。它把标准输入读入一个临时文件，在 EDITOR 或 VISUAL 环境变量指定的编辑器中打开，并在编辑器退出时将编辑后的内容写入标准输出。

这样可以交互式地修改流经管道的数据，适用于在数据传给下一条命令前手动修正输入、调试管道中的数据，或执行那些用编辑器处理比 sed 或 awk 更方便的一次性转换。

# EXAMPLE

```
$ seq 5 | vipe | sort -r
# Editor opens with:
# 1
# 2
# 3
# 4
# 5
# Make edits, save, quit
# Output continues through sort
```

# CAVEATS

属于 moreutils 软件包的一部分。会中断非交互式管道。编辑器必须是终端程序。

# HISTORY

**vipe** 是 **Joey Hess** 所写 **moreutils** 的一部分。它让 Unix 管道中可以进行交互式编辑。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vidir](/man/vidir)(1), [sponge](/man/sponge)(1), [tee](/man/tee)(1)
