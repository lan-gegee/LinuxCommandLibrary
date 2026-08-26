# 搜索与查找

## 入门
三种不同的任务，对应三套工具：**find** 实时遍历文件系统，可以按任意属性过滤；**locate** 从预先构建的索引中即时给出结果；**grep** 在文件内容中搜索。**fd**、**plocate** 和 **rg** 是它们更现代、更快速的替代品。

## 按名称查找文件
**find** 需要一个起始目录；**-iname** 匹配时不区分大小写。**fd** 默认搜索当前目录，忽略隐藏文件和被 git 忽略的文件，并使用正则表达式模式。
```[find](/man/find) . -iname "*report*"```
```[find](/man/find) / -name "[fileName]" 2>/dev/null```
```[fd](/man/fd) [query]```
```[fd](/man/fd) -e pdf [query]```

从 **/** 开始搜索会对无法读取的目录输出权限错误；**2>/dev/null** 可以隐藏这些错误。

## 按类型、大小和时间查找
测试条件可以自由组合：形如 **-7** 的数字表示“小于”，**+7** 表示“大于”，不带符号的 **7** 表示“恰好”。
```[find](/man/find) . -type f -size +10M -size -100M```
```[find](/man/find) . -type f -empty```
```[find](/man/find) . -type d -empty```
```[find](/man/find) . -mmin -60```
```[find](/man/find) . -mtime -7```
```[find](/man/find) . -mtime +30```

| 测试条件 | 说明 |
|-----|-------------|
| **-type f / -type d** | 文件 / 目录 |
| **-size +10M** | 大于 10 MB |
| **-mmin -60** | 内容在不到 60 分钟前修改过 |
| **-mtime -7** | 内容在过去 7 天内修改过 |
| **-cmin / -ctime** | 状态（权限、所有者）发生变化的时间 |
| **-atime** | 最后访问时间 |
| **-empty** | 空文件或空目录 |
| **-user name** | 属于指定用户的文件 |

## 对找到的结果执行操作
**-exec** 会对每个匹配结果执行一条命令；**{}** 会被替换为文件名。以 **+** 结尾时每次调用可传入多个文件，而不是一次一个。**-delete** 直接删除匹配结果。
```[find](/man/find) . -name "*.tmp" -delete```
```[find](/man/find) . -name "*.sh" -exec [chmod](/man/chmod) +x {} +```
```[find](/man/find) . -type f -exec [grep](/man/grep) -l "TODO" {} +```

**先测试有破坏性的命令：**把 **-delete** 或 **-exec rm** 换成 **-print**，核对列表无误后再真正执行。

## 索引搜索
**locate** 从索引中即时查找路径名，而不是扫描磁盘。索引由 **updatedb** 定期更新，因此刚创建的文件可能尚未收录。**plocate** 是速度更快的现代实现。
```[locate](/man/locate) [query]```
```[plocate](/man/plocate) [query]```
```sudo [updatedb](/man/updatedb)```

## 搜索文件内容
**grep -r** 递归搜索目录；**-n** 显示行号，**-i** 不区分大小写，**-l** 只列出文件名。**rg**（ripgrep）默认递归搜索，跳过被 git 忽略的文件，在大型目录树上快得多。
```[grep](/man/grep) "[query]" [file]```
```[grep](/man/grep) -rni "[query]" [path]```
```[grep](/man/grep) -rl "[query]" [path]```
```[rg](/man/rg) "[query]"```
```[rg](/man/rg) -t py "[query]"```
```[ag](/man/ag) "[query]"```

把任意命令的输出通过管道交给 grep，即可搜索其输出。
```[history](/man/history) | [grep](/man/grep) "[phrase]"```
```[ps](/man/ps) aux | [grep](/man/grep) "[processName]"```

## 模糊查找
**fzf** 在你输入的同时交互式地过滤任何列表。单独使用时它可以模糊查找文件；与其他命令结合则成为通用的选择器。
```[fzf](/man/fzf)```
```[vim](/man/vim) $([fzf](/man/fzf))```
```[history](/man/history) | [fzf](/man/fzf)```

fzf 的 Shell 集成绑定了 **Ctrl+R**（历史记录）、**Ctrl+T**（文件）和 **Alt+C**（cd 进入目录）。

## 查找命令
某个命令位于何处？它究竟是什么？
```[which](/man/which) [command]```
```[whereis](/man/whereis) [command]```
```type [command]```
```command -v [command]```

**whereis** 还能找到 man 手册页和源代码。**type** 是 Shell 自带的视角，能正确报告别名、函数和内建命令。
