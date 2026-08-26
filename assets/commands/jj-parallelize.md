# TAGLINE

将一系列顺序提交重构为并行的兄弟提交

# TLDR

使修订并行

```jj parallelize [rev1]::[rev2]```

将一段区间的提交并行化

```jj parallelize [start]::[end]```

# SYNOPSIS

**jj** **parallelize** _revisions_

# DESCRIPTION

**jj parallelize** 将一系列顺序提交重构为并行的兄弟提交。它把原本互为父子关系的提交全部改为同一个共同父修订的子修订。当各改动相互独立时，适合用它重组历史。

# SEE ALSO

[jj](/man/jj)(1), [jj-rebase](/man/jj-rebase)(1)
