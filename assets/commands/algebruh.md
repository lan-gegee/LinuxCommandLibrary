# TAGLINE

用独立的证明检查器判定算术等式命题

# TLDR

**检查**等式是否成立

```algebruh "[2 = 3]"```

从假设出发**证明**一个命题

```algebruh --assume "[a = c]" --assume "[c = b]" "[a = b]"```

**比较**多种解释（整数、实数、位向量、模运算）

```algebruh --interpret [int,real,bv8,mod:1] "[2 = 3]"```

**声明**函数为单射并检查参数相等性

```algebruh --injective [f] --assume "[f(a) = f(b)]" "[a = b]"```

**运行所有检查器**并输出 JSON 报告

```algebruh --all --json "[a = b]"```

**生成** SMT-LIB 和 Z3 证明工件

```algebruh --emit [result] "[x + 0 = x]"```

**检查**哪些可选的外部求解器可用

```algebruh doctor```

# SYNOPSIS

**algebruh** [**--all**] [**--json**] [**--interpret** _LIST_] [**--assume** _EXPR_]... [**--injective** _NAME_]... [**--ai-command** _CMD_] [**--emit** _PREFIX_] _CLAIM_

**algebruh** **doctor** [**--json**]

# PARAMETERS

**--all**
> 运行附加的检查器（cvc5、Carcara、Lean/Mathlib、Vampire、E，如果可用）、额外的求解器种子以及充分前提搜索。打印每次尝试。

**--json**
> 以 JSON 格式而不是人类可读文本输出完整报告。

**--interpret** _LIST_
> 逗号分隔的解释列表。默认是整数（**int**）。取值包括 **int**、**real**、**bv**_N_ / **sbv**_N_（有符号 N 位，N=1..256）、**ubv**_N_（无符号）、**mod:**_N_、**quot:**_N_、**equiv:**_N_、**f32**、**f64** 和 **singleton**。整数解释总是作为基线参与求值。

**--assume** _EXPR_
> 添加一条相等或不等前提。可重复使用。每条假设必须恰好包含一个 **=**、**==** 或 **!=**。

**--injective** _NAME_
> 声明某个一元函数名为单射。可重复使用。其他函数应用保持未解释状态。

**--ai-command** _CMD_
> 将问题以 JSON 形式发送给 _CMD_。该命令的 stdout 必须是一条 Lean 策略（tactic），并且只有通过 Lean 内核验证后才会被接受。

**--emit** _PREFIX_
> 当存在选定的 Z3 证明时，写出 SMT-LIB（**_PREFIX_.smt2**）和 Z3 证明（**_PREFIX_.proof**）。不会覆盖已有文件。

_CLAIM_
> 待判定的算术等式或不等式（例如 **"2 = 3"** 或 **"a + 0 = a"**）。

**doctor**
> 报告 **PATH** 上可选外部工具的可用性。若有列出的工具缺失则退出码为 1。接受 **--json**。

# DESCRIPTION

**algebruh** 对算术等式和不等式命题进行判定。给定一个命题和可选假设，它会报告该命题是被证明、被反驳、取决于条件、空洞成立还是未知，并能揭示独立检查器之间的分歧。

默认路径链接 Z3 库，并在适用时通过精确求值、等价饱和、有界模型搜索和 LRAT 回放独立验证候选结果。使用 **--all** 时，它还会尝试在 **PATH** 上找到的外部工具（cvc5、Carcara、带 Mathlib 的 Lean、Vampire、E）。在可用时，外部工具在 Bubblewrap 和 **prlimit** 下运行。

表达式支持整数、变量名、一元函数应用（如 **f(x)**）、括号、一元负号、**+**、**-**、**\***、**/**、**%**、**=**、**==** 和 **!=**。乘法、除法和取模的优先级高于加法和减法。每个命题或假设必须包含一个等式或不等式；不支持 **<**、**>=** 等比较运算。

结果标签包括 **PROVED**、**REFUTED**（退出码 0）、**CONTINGENT**、**CONDITIONAL**、**VACUOUS**、**UNKNOWN**、**UNSAFE_AXIOM**、**CHECKER_BUG_CANDIDATE**（退出码 1），以及在非整数解释下证明了整数解释无法证明的命题时的 **REINTERPRETED**（退出码 0）。输入、沙箱和求解器错误使用退出码 2。

构建需要 Rust 1.85+、Cargo、pkg-config 和 Z3 开发库（或使用项目提供的 **nix-shell**）。安装方法是构建 **target/release/algebruh** 并将其放入 **PATH**。

# CAVEATS

非线性算术可能返回 **UNKNOWN**。除以零和零取模遵循 Z3 语义。用户自定义相等仅限于模运算 **equiv:**_N_。可选检查器需单独安装；**algebruh doctor** 会报告当前可用的工具。**--emit** 从不覆盖已有的工件文件。

# HISTORY

Algebruh 是 Sebastian Korotkiewicz 开发的 Rust 命令行工具，用于借助 Z3 和可选的独立求解器（cvc5、Lean 等）交叉验证算术命题。以源代码形式通过 GitHub 分发。

# SEE ALSO

[z3](/man/z3)(1), [cargo](/man/cargo)(1)

# RESOURCES

```[Source code](https://github.com/skorotkiewicz/algebruh)```

<!-- verified: 2026-08-09 -->
