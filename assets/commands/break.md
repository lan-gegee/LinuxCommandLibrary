# TAGLINE

在 Shell 脚本中跳出循环

# TLDR

从循环中**跳出**

```break```

**跳出多层**循环

```break [2]```

# SYNOPSIS

**break** [_n_]

# DESCRIPTION

**break** 是 bash 的内置命令，用于退出 for、while 或 until 循环。它还可以通过指定层数一次跳出多个嵌套循环。

该命令是 shell 脚本中控制循环的关键工具。

# PARAMETERS

_n_
> 要跳出的循环层数（默认：1）。

# WORKFLOW

```bash
# Break from single loop
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    break
  fi
  echo $i
done

# Break from nested loops
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2  # Break both loops
    fi
    echo "$i $j"
  done
done

# Break from while loop
while read line; do
  if [ "$line" = "END" ]; then
    break
  fi
  process "$line"
done < file.txt
```

# CAVEATS

只能在循环（for、while、until）内使用。指定的层数超过实际嵌套层数时会退出所有循环。与 exit 不同（exit 会退出整个脚本）。continue 则是跳过当前迭代继续下一轮，而不是退出。

# HISTORY

**break** 自 **1970** 年代末的 Bourne shell 起就是标准的 shell 内置命令。

# SEE ALSO

[continue](/man/continue)(1), [exit](/man/exit)(1)
