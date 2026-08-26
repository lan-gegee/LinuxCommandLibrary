# TAGLINE

逐行比较文件的工具

# TLDR

**比较**文件

```diff [file1.txt] [file2.txt]```

**统一（unified）**格式

```diff -u [file1.txt] [file2.txt]```

**比较**目录

```diff -r [dir1] [dir2]```

**并排**比较

```diff -y [file1.txt] [file2.txt]```

**忽略**空白字符

```diff -w [file1.txt] [file2.txt]```

# SYNOPSIS

**diff** [_options_] _file1_ _file2_

# DESCRIPTION

**diff** 逐行比较文件并输出差异。它是版本控制、代码审查以及理解文件版本间变化的重要工具。

该工具是补丁文件的基础，也被各版本控制系统所使用。

# PARAMETERS

**-u**, **--unified**
> 统一（unified）diff 格式（推荐）

**-c**, **--context**
> 上下文（context）diff 格式

**-y**, **--side-by-side**
> 并排比较

**-r**, **--recursive**
> 递归比较目录

**-q**, **--brief**
> 仅在文件不同时报告

**-s**, **--report-identical-files**
> 文件相同时也报告

**-w**, **--ignore-all-space**
> 忽略所有空白差异

**-b**, **--ignore-space-change**
> 忽略空白字符数量的变化

**-B**, **--ignore-blank-lines**
> 忽略空行的变化

**-i**, **--ignore-case**
> 不区分大小写地比较

**-N**, **--new-file**
> 将缺失的文件视为空文件

# OUTPUT FORMATS

**普通格式：**
```
3c3
< old line
---
> new line
```

**统一格式（-u）：**
```
--- file1.txt
+++ file2.txt
@@ -1,3 +1,3 @@
 context
-old line
+new line
 context
```

**上下文格式（-c）：**
```
*** file1.txt
--- file2.txt
***************
*** 1,3 ****
  context
! old line
  context
--- 1,3 ----
  context
! new line
  context
```

# WORKFLOW

```bash
# Basic comparison
diff file1.txt file2.txt

# Unified diff (best for patches)
diff -u original.txt modified.txt

# Save as patch
diff -u original.txt modified.txt > changes.patch

# Compare directories
diff -r old_version/ new_version/

# Ignore whitespace
diff -w file1.txt file2.txt

# Brief output
diff -q file1.txt file2.txt

# Side by side
diff -y file1.txt file2.txt | less
```

# CREATING PATCHES

```bash
# Create patch
diff -u old.c new.c > fix.patch

# Apply patch
patch old.c < fix.patch

# Reverse patch
patch -R new.c < fix.patch
```

# DIRECTORY COMPARISON

```bash
# Compare directories
diff -r dir1/ dir2/

# Exclude files
diff -r --exclude="*.log" dir1/ dir2/

# Brief directory diff
diff -rq dir1/ dir2/
```

# EXIT STATUS

- **0** - 文件相同
- **1** - 文件不同
- **2** - 发生错误

# CAVEATS

大文件可能较慢。二进制文件只显示 "differ" 而无细节。空白字符的处理方式因选项而异。行尾符（CRLF 与 LF）可能引发问题。不适合二进制比较（请用 cmp）。

# HISTORY

**diff** 由贝尔实验室的 **James W. Hunt** 和 **Doug McIlroy** 于 **1974** 年前后编写，其算法发表于两人 **1976** 年的合作论文中。

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

[patch](/man/patch)(1), [git-diff](/man/git-diff)(1), [cmp](/man/cmp)(1), [vimdiff](/man/vimdiff)(1)
