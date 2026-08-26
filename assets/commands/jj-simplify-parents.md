# TAGLINE

从合并提交中移除冗余的父边

# TLDR

简化父级关系

```jj simplify-parents```

简化特定修订

```jj simplify-parents -r [revision]```

# SYNOPSIS

**jj** **simplify-parents** [_options_]

# PARAMETERS

**-r**, **--revision** _rev_
> 要简化的修订。

# DESCRIPTION

**jj simplify-parents** 从合并提交中移除冗余的父边。当一个提交有多个父修订，而其中一个父修订是另一个的祖先时，冗余的父修订会被移除。它可清理不必要的合并复杂度。

# SEE ALSO

[jj](/man/jj)(1), [jj-rebase](/man/jj-rebase)(1)
