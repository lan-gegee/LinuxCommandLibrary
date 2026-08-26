# TAGLINE

更改文件的所有者和组

# TLDR

**更改**所有者

```chown [user] [file]```

**更改**所有者和组

```chown [user]:[group] [file]```

**递归**更改

```chown -R [user]:[group] [directory/]```

仅**更改**组

```chown :[group] [file]```

# SYNOPSIS

**chown** [_options_] _owner_[:_group_] _file_...

# DESCRIPTION

**chown**（change owner）修改文件所有权。它可以更改用户所有者、组所有者或两者。文件所有权决定谁对文件权限拥有最终控制权。

将所有权更改为其他用户通常需要 root 权限。

# PARAMETERS

**-R**, **--recursive**
> 递归地更改文件和目录

**-v**, **--verbose**
> 详细输出

**-c**, **--changes**
> 仅报告更改

**--reference=**_file_
> 使用参考文件的所有权

**-h**, **--no-dereference**
> 影响符号链接本身而非目标文件

**-f**, **--silent**, **--quiet**
> 屏蔽大多数错误信息

**--from=**_current_owner_[:_current_group_]
> 仅当当前所有者和/或组匹配时才更改

**--dereference**
> 影响每个符号链接所指向的文件（这是默认行为）

**-H**
> 若命令行参数是指向目录的符号链接，则遍历之（配合 -R 使用）

**-L**
> 遍历遇到的每一个指向目录的符号链接（配合 -R 使用）

**-P**
> 不遍历任何符号链接（默认，配合 -R 使用）

**--preserve-root**
> 拒绝在 / 上递归操作

**--no-preserve-root**
> 不特殊对待 /（默认）

# OWNERSHIP FORMAT

**user**
> 仅更改用户所有者

**user:group**
> 更改用户和组

**user:**
> 更改用户，并将组设为该用户的登录组

**:group**
> 仅更改组（等同于 chgrp）

# WORKFLOW

```bash
# Change owner
sudo chown alice file.txt

# Change owner and group
sudo chown alice:developers file.txt

# Change owner, group to user's login group
sudo chown alice: file.txt

# Change group only
sudo chown :www-data file.txt

# Recursive change
sudo chown -R alice:developers project/

# Use reference file
sudo chown --reference=template.txt newfile.txt

# Change only if owned by specific user
sudo chown --from=bob alice file.txt
```

# COMMON USES

**Web 服务器文件：**
```bash
sudo chown -R www-data:www-data /var/www/html
```

**用户主目录：**
```bash
sudo chown -R alice:alice /home/alice
```

**恢复所有权：**
```bash
sudo chown -R $(whoami):$(whoami) ~/myproject
```

# CAVEATS

通常需要 root/sudo。更改所有权会移除某些安全特性（如 setuid）。递归更改可能破坏系统文件。不能将所有权更改为不存在的用户。符号链接的处理方式因选项而异。

# HISTORY

**chown** 自 **20 世纪 70 年代初**起就是 Unix 文件所有权安全模型的一部分。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chmod](/man/chmod)(1), [chgrp](/man/chgrp)(1), [ls](/man/ls)(1), [stat](/man/stat)(1)
