# TAGLINE

三方文件比较与合并

# TLDR

**比较**三个文件

```diff3 [path/to/file1] [path/to/file2] [path/to/file3]```

显示所有变更并**标出冲突**

```diff3 -A [path/to/file1] [path/to/file2] [path/to/file3]```

# SYNOPSIS

**diff3** [_options_] _myfile_ _oldfile_ _yourfile_

# DESCRIPTION

**diff3** 逐行比较三个文件，显示差异和冲突。它通常用于三方合并场景：一个文件是共同祖先，另外两个文件是基于它的修改版本。

其输出格式适合用于解决合并冲突。

# PARAMETERS

**-A, --show-all**
> 显示所有变更，并用括号标出冲突部分

**-e, --ed**
> 输出 ed 脚本

**-E, --show-overlap**
> 类似 -e，但会用括号标出冲突

**-m, --merge**
> 直接输出合并后的文件（除非给定 -e、-E 或 -x，否则隐含 -A）

**-x, --overlap-only**
> 仅输出重叠（冲突）的变更

**-3, --easy-only**
> 仅输出第三个文件中不重叠的变更

**-T, --initial-tab**
> 通过在行首添加制表符使各列对齐

# CAVEATS

文件顺序很重要：我的、旧的、你的。常被版本控制系统内部使用。属于 GNU diffutils 的一部分。

# INSTALL

```apt: sudo apt install diffutils```

```dnf: sudo dnf install diffutils```

```pacman: sudo pacman -S diffutils```

```apk: sudo apk add diffutils```

```zypper: sudo zypper install diffutils```

```brew: brew install diffutils```

```nix: nix profile install nixpkgs#diffutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [merge](/man/merge)(1), [patch](/man/patch)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/diffutils/)```

```[Documentation](https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff3.html)```

<!-- verified: 2026-07-11 -->
