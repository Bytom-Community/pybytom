#!/usr/bin/env python3

from pybytom.script import (
    script_hash, p2sh_program, p2wsh_program, p2wsh_address
)

# Bytom network & Bytom contract program(bytecode)
NETWORK, BYTECODE = "mainnet", "01642091ff7f525ff40874c4f47f0cab42e46e3bf53adad59adef9558ad1b6448" \
                               "f22e220ac13c0bb1445423a641754182d53f0677cd4351a0e743e6f10b35122c3" \
                               "d7ea01203a26da82ead15a80533a02696656b14b5dbfd84eb14790f2e1be5e9e4" \
                               "5820eeb741f547a6416000000557aa888537a7cae7cac631f000000537acd9f69" \
                               "72ae7cac00c0"

# Get script hash
script_hash = script_hash(bytecode=BYTECODE)
print("Script Hash:", script_hash)
# Get Pay to Script Hash(P2SH) program
p2sh_program = p2sh_program(script_hash=script_hash)
print("P2SH Program:", p2sh_program)
# Get Pay to Witness Script Hash(P2SH) program
p2wsh_program = p2wsh_program(script_hash=script_hash)
print("P2WSH Program:", p2wsh_program)
# Get Pay to Witness Script Hash(P2SH) address
p2wsh_address = p2wsh_address(script_hash=script_hash, network=NETWORK)
print("P2WSH Address:", p2wsh_address)
