# TAGLINE

通过录制交互会话生成 Expect 脚本

# TLDR

启动 shell 并根据会话**生成脚本**

```autoexpect```

运行一条命令并据此**生成脚本**

```autoexpect [command]```

生成脚本并**保存到指定文件**

```autoexpect -f [path/to/file] [command]```

**使用提示符模式**，只匹配输出的最后一行

```autoexpect -p [command]```

**使用保守模式**，字符之间加入轻微延迟

```autoexpect -c [command]```

# SYNOPSIS

**autoexpect** [_options_] [_command_...]

# DESCRIPTION

**autoexpect** 会监视一次交互会话，并生成可自动重放该会话的 Expect 脚本。它记录用户输入和程序响应，创建适合自动化重复性交互任务的脚本。

生成的脚本默认保存为 **script.exp**。可以修改并复用该脚本，以自动化录制的交互过程。

# PARAMETERS

**-f** _file_
> 将生成的脚本保存到指定文件，而非 script.exp。

**-p**
> 启用提示符模式。autoexpect 只匹配程序输出的最后一行（通常是提示符），使脚本对输出变化不那么敏感。

**-P** _key_
> 定义一个按键，用于在会话过程中开关提示符模式。

**-c**
> 启用保守模式。autoexpect 在发送每个字符前短暂暂停（十分之一秒），提高在慢速系统上的可靠性。

**-C** _key_
> 定义一个按键，用于在会话过程中开关保守模式。

**-Q** _key_
> 定义一个引号字符，用于输入那些会被 autoexpect 当作切换键消费的字符。

**-quiet**
> 关闭 autoexpect 产生的信息性消息。

# CAVEATS

生成的脚本可能需要手动编辑才能足够健壮。录制期间输入的密码和敏感数据会被写入脚本。为保证可靠回放，可能需要调整交互的时序。

# HISTORY

**autoexpect** 属于 Expect 软件包，由 NIST 的 Don Libes 创建。Expect 于 **1990 年**首次发布，被广泛用于自动化交互式应用。

# INSTALL

```apt: sudo apt install expect```

```dnf: sudo dnf install expect```

```pacman: sudo pacman -S expect```

```apk: sudo apk add expect```

```zypper: sudo zypper install expect```

```brew: brew install expect```

```nix: nix profile install nixpkgs#expect```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[expect](/man/expect)(1), [ssh](/man/ssh)(1)
