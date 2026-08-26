# TAGLINE

合并 RCS 文件的修订

# TLDR

**将修订合并到工作文件**

```rcsmerge -r[1.1] -r[1.2] [file]```

**合并特定修订**

```rcsmerge -r[1.3] [file]```

**打印到 stdout**

```rcsmerge -p -r[1.1] -r[1.2] [file]```

**安静模式**

```rcsmerge -q -r[1.1] -r[1.2] [file]```

# SYNOPSIS

**rcsmerge** [_-p_] [_-r rev1_] [_-r rev2_] [_options_] _file_

# PARAMETERS

**-r** _REV_
> 要合并的修订。空修订表示默认分支上的最新修订。

**-p**
> 将结果发送到 stdout，而不是覆盖工作文件。

**-q**
> 安静模式；不打印诊断信息。

**-A**
> 使用 diff3(1) 的 -A 风格输出冲突。

**-E**
> 使用 diff3(1) 的 -E 风格输出冲突（默认）。

**-e**
> 使用 diff3(1) 的 -e 风格输出冲突。不警告冲突。

**-k** _SUBST_
> 关键字替换模式（如 -kk 会忽略关键字值的差异）。

**-V** _N_
> 模拟指定版本的 RCS 行为。

# DESCRIPTION

**rcsmerge** 对 RCS 文件修订执行三方合并，把两个指定修订之间的更改融入当前工作文件。它会确定一个共同祖先修订并应用差异以产生合并结果，类似于现代版本控制系统处理分支合并的方式。

默认情况下，合并会直接修改工作文件，而 **-p** 标志会将合并结果打印到 stdout。检测到冲突的更改时，冲突标记会被插入到输出中，必须手动解决后才能重新检入文件。

# CAVEATS

RCS 是遗留版本控制系统。冲突以内联方式标记，必须手动解决。退出码：0 表示无重叠，1 表示有重叠，2 表示错误。新项目建议使用 Git。

# HISTORY

**rcsmerge** 属于 **RCS**（Revision Control System），由 **Walter Tichy** 于 1982 年在普渡大学创建。

# INSTALL

```apt: sudo apt install rcs```

```dnf: sudo dnf install rcs```

```pacman: sudo pacman -S rcs```

```apk: sudo apk add rcs```

```zypper: sudo zypper install rcs```

```brew: brew install rcs```

```nix: nix profile install nixpkgs#rcs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rcs](/man/rcs)(1), [rcsdiff](/man/rcsdiff)(1), [merge](/man/merge)(1), [ci](/man/ci)(1), [co](/man/co)(1), [rlog](/man/rlog)(1)
