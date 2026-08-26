# 文件与文件夹

## 目录导航
**pwd** 显示你当前所在的目录。
```[pwd](/man/pwd)```

**cd** 让你前往另一个目录：给它一个路径，或者使用快捷写法。
```[cd](/man/cd) [path]```

向上一层，前往父目录。
```[cd](/man/cd) ..```

前往主目录（只用 **cd** 也是同样效果）。
```[cd](/man/cd) ~```

跳回之前所在的目录。
```[cd](/man/cd) -```

## 列出内容
**ls** 列出目录内容。**-l** 显示详情，**-a** 连隐藏文件一起列出（名称以点开头），**-h** 以易读的单位显示大小。
```[ls](/man/ls)```
```[ls](/man/ls) -lah```

按修改时间排序，最新的在前。加 **-r** 可反转任何排序顺序。
```[ls](/man/ls) -lt```

以树形结构展示嵌套目录。
```[tree](/man/tree)```

现代替代工具增加了颜色、图标和 git 状态。
```[eza](/man/eza) -la```
```[lsd](/man/lsd) -la```

## 查看文件
**cat** 输出整个文件；**less** 让你上下滚动并在其中搜索（按 **q** 退出，按 **/** 搜索）。**bat** 是带语法高亮的 cat 克隆版。
```[cat](/man/cat) [fileName]```
```[less](/man/less) [fileName]```
```[bat](/man/bat) [fileName]```

只显示文件的开头或结尾部分。
```[head](/man/head) -n 20 [fileName]```
```[tail](/man/tail) -n 20 [fileName]```

**-f** 会随着文件增长持续跟踪，非常适合日志场景。
```[tail](/man/tail) -f [logFile]```

辨别某个文件属于什么类型。
```[file](/man/file) [fileName]```

统计行数、单词数和字节数。只要行数就用 **-l**。
```[wc](/man/wc) [fileName]```

## 创建
**touch** 创建空文件（或更新现有文件的时间戳）。**mkdir -p** 一步创建多层嵌套目录，即使目录已存在也不报错。
```[touch](/man/touch) [fileName]```
```[mkdir](/man/mkdir) [folderName]```
```[mkdir](/man/mkdir) -p path/to/nested/folder```
```> [fileName]```

## 复制、移动、重命名
**cp** 复制文件。复制目录及其中的一切需要加 **-r**。
```[cp](/man/cp) [fileName] [newFileName]```
```[cp](/man/cp) -r [folder] [folderCopy]```

**mv** 既能移动又能重命名；并不存在单独的重命名命令。
```[mv](/man/mv) [oldName] [newName]```
```[mv](/man/mv) [fileName] [targetFolder]/```

**当心：** **cp** 和 **mv** 都会在不打招呼的情况下覆盖已有目标。加 **-i** 覆盖前先询问，加 **-n** 则绝不覆盖。

## 删除
**rm** 删除文件。**-r** 删除目录及其中的一切。**删除不可撤销**——操作永久生效、立即执行，所以务必先核对清楚。没把握时用 **rm -ri**，每次删除都会要求确认。
```[rm](/man/rm) [fileName]```
```[rm](/man/rm) -r [folderName]```

**rmdir** 只删除已经是空的目录。
```[rmdir](/man/rmdir) [emptyFolderName]```

比 **rm** 更安全的做法：把文件移入桌面回收站，日后仍可还原。
```[gio](/man/gio) trash [file]```
```[trash-put](/man/trash-put) [file]```

列出回收站内容或清空回收站。
```[trash-list](/man/trash-list)```
```[trash-empty](/man/trash-empty)```
```[gio](/man/gio) trash --empty```

## 链接
**符号链接**指向一个路径。目标一旦移动它就会失效，但在几乎所有场景下你要的正是它。
```[ln](/man/ln) -s [target] [linkName]```

**硬链接**是同一份文件内容的第二个名字，直到所有名字都被删除为止它一直有效。硬链接不能跨文件系统，也不能指向目录。
```[ln](/man/ln) [target] [linkName]```

解析链接最终指向的真实路径。
```[readlink](/man/readlink) -f [linkName]```

## 权限与所有权
每个文件都有所有者、组，以及针对所有者/组/其他人的权限位。**ls -l** 显示这些信息，**stat** 显示全部信息。
```[ls](/man/ls) -l [file]```
```[stat](/man/stat) [file]```

**chmod** 修改权限，既可以用符号法，也可以用八进制数字（读=4，写=2，执行=1）。
```[chmod](/man/chmod) +x [script]```
```[chmod](/man/chmod) 644 [file]```
```[chmod](/man/chmod) 755 [folder]```
```[chmod](/man/chmod) -R u+rwX [folder]```

| 模式 | 说明 |
|-----|-------------|
| **644** | 所有者读写，其他人只读（常见于普通文件） |
| **755** | 所有者拥有全部权限，其他人可读、可进入（常见于目录或脚本） |
| **600** | 只有所有者能读写（私钥、机密文件） |
| **700** | 只有所有者有任何访问权限（私密目录） |

**chown** 同时更改所有者和组，**chgrp** 只更改组。更改所有者需要 root 权限。
```[chown](/man/chown) [user]:[group] [file]```
```[chown](/man/chown) -R [user]:[group] [folder]```
```[chgrp](/man/chgrp) [group] [file]```

## 搜索文件内容
**grep** 在文件内容中搜索；**rg**（ripgrep）默认递归地做同样的事，而且快得多。
```[grep](/man/grep) "phrase" [fileName]```
```[grep](/man/grep) -rn "phrase" [folder]```
```[rg](/man/rg) "phrase"```

如果要改为按名称、大小或时间查找文件本身，请参阅 **搜索与查找** 入门页面。

## 比较文件
**diff -u** 以熟悉的补丁格式显示差异。
```[diff](/man/diff) -u [file1] [file2]```
```[diff](/man/diff) -r [folder1] [folder2]```

## 磁盘占用
**du** 统计各目录占了多少空间，**df** 显示各文件系统的剩余空间。
```[du](/man/du) -h --max-depth=1```
```[df](/man/df) -h```

交互式且更美观的替代工具，让你轻松找出是谁吃掉了磁盘空间。
```[ncdu](/man/ncdu)```
```[dust](/man/dust)```
```[leaves](/man/leaves)```
```[duf](/man/duf)```

## 挂载文件系统
先列出块设备，弄清分区上的文件系统，然后把它挂载到某个目录。
```[lsblk](/man/lsblk) -f```
```[mount](/man/mount) /dev/[device] [path]```
```[umount](/man/umount) [path]```

## 编辑文本文件
这些编辑器都能在终端中使用。**nano** 上手最容易；vim 和 emacs 有各自的入门页面。
```[nano](/man/nano) [fileName]```
```[vi](/man/vi) [fileName]```
```[emacs](/man/emacs) [fileName]```
```[micro](/man/micro) [fileName]```
