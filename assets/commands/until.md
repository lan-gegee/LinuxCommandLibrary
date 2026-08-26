# TAGLINE

条件变为真之前反复执行的 Shell 循环

# TLDR

**循环直到条件满足**

```until [condition]; do [commands]; done```

**等待文件出现**

```until [ -f [file] ]; do sleep 1; done```

**等待进程出现**

```until pgrep [process]; do sleep 1; done```

**计数循环**

```until [ $i -gt 10 ]; do echo $i; i=$((i+1)); done```

# SYNOPSIS

**until** _condition_; **do** _commands_; **done**

# DESCRIPTION

**until** 是一种 Shell 循环结构，只要条件的求值结果为假（非零退出状态），就会重复执行一段命令。它与 **while** 在逻辑上正好相反——后者在条件为真时循环。条件在每次迭代之前都会测试，因此如果循环开始时条件已经为真，循环体将永远不会执行。

until 最常见的用途是轮询某个条件何时成立，例如等待一台网络主机上线、等待某个文件出现或等待某个进程启动。结合 **sleep** 使用，它提供了一种在 Shell 脚本中实现重试逻辑的简单方法。

until 循环的退出状态是循环体中最后执行的命令的退出状态。如果因条件已为真而从未执行循环体，退出状态则为零。

# CAVEATS

Shell 内建命令。与 while 相反。每次迭代都会重新评估条件。

# EXAMPLES

```
until ping -c1 host &>/dev/null; do
  echo "Waiting..."
  sleep 5
done
echo "Host is up"
```

# HISTORY

**until** 是 POSIX Shell 中提供的标准控制结构，与 while 循环相反。

# SEE ALSO

[while](/man/while)(1), [for](/man/for)(1), [if](/man/if)(1), [sleep](/man/sleep)(1), [test](/man/test)(1)
