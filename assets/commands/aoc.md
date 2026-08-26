# TAGLINE

Advent of Code 谜题助手（下载、阅读、提交）

# TLDR

**下载**今天的谜题输入

```aoc download```

**下载**指定日期的谜题

```aoc download --day [1]```

**提交**答案

```aoc submit [1] [answer]```

**查看**日历 / 星星进度

```aoc calendar```

**阅读**谜题描述

```aoc read```

# SYNOPSIS

**aoc** *command* [*options*]

# DESCRIPTION

**aoc**（来自 **aoc-cli** crate）使用你的会话 cookie 与 [Advent of Code](https://adventofcode.com) 交互：在终端中下载谜题描述和输入、提交答案并查看星星进度。可通过 **cargo install aoc-cli**、Homebrew tap 或发布版二进制文件安装。

按照上游文档，将会话 cookie 放入环境变量或配置文件即可完成认证（**AOC_SESSION** 等）。

# PARAMETERS

**download** | **d**

> 保存谜题描述和/或输入文件。

**submit** | **s**

> 提交第 1/2 部分的答案。

**read** | **r**

> 显示谜题描述。

**calendar** | **c**

> 显示日历和已收集的星星。

**--day** *n* / **--year** *y*

> 选择谜题的日期/年份（12 月活动期间默认为当天）。

# CAVEATS

需要有效的 AoC 会话 cookie；切勿提交到代码库。请遵守活动的自动化规则和速率限制。谜题内容版权归 Eric Wastl 所有。

# SEE ALSO

[curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/scarvalhojr/aoc-cli)```

<!-- verified: 2026-07-19 -->
