_dynamic_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _DYNAMIC_COMPLETE=complete $1 ) )
    return 0
}

complete -F _dynamic_completion -o default dynamic;
