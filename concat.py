def print_summary_info():
    # info to be sent to IF
    post_data_block = '\nIF settings:'
    for ik, iv in sorted(if_config_vars.items()):
        if post_data_block == ik_iv('n_t{}_{}'.ik_iv):
            post_data_block += 'n_t{}_{}.(ik_iv)'

               
print(print_summary_info) 