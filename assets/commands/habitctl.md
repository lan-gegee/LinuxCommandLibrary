# TAGLINE

极简的命令行习惯打卡工具

# TLDR

**打开每日打卡界面**（常用别名 **h**）

```habitctl```

**在 $EDITOR 中编辑习惯列表**

```habitctl edith```

**首次运行**会在 ~/.habitctl 下创建配置

```habitctl```

# SYNOPSIS

**habitctl** [*command*]

# DESCRIPTION

**habitctl** 是一款极简的终端习惯追踪器。习惯和记录以纯文件形式存放在 **~/.habitctl/** 下。首次运行时会创建 **habits** 和 **log** 文件。使用 **edith** 定义习惯，每行包含一个周期数字（1 = 每天，7 = 每周，0 = 仅记录）和一个名称。以交互方式运行 **habitctl** 时，它会针对每个习惯提示 **y/n/s**（是 / 否 / 跳过），并绘制一张紧凑的历史图表。

使用 Rust 从源码构建：**cargo build --release**（二进制文件为 **target/release/habitctl**）。许多用户会将其别名为 **h**。

# PARAMETERS

*(no args)*

> 交互式每日记录与历史查看。

**edith**

> 在 **$EDITOR** 中打开习惯列表。

如果构建中包含其他子命令，可通过 **habitctl --help** 查看。

# CONFIGURATION

**~/.habitctl/habits**

> 习惯定义：形如 **1 Meditated** 或 **7 Cleaned the apartment** 的行。

**~/.habitctl/log**

> 只追加的回答日志。

# CAVEATS

专为个人本地使用设计；不支持同步或多设备。图表密度取决于终端宽度。跳过（**s**）适用于习惯当天不适用的日子。

# SEE ALSO

[klog](/man/klog)(1), [task](/man/task)(1), [todo.sh](/man/todo.sh)(1)

# RESOURCES

```[Source code](https://github.com/blinry/habitctl)```

<!-- verified: 2026-07-19 -->
