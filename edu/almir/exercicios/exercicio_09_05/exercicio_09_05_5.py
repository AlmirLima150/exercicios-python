def valor_estoque(nome, quantidade, vl_unitario):
    valor_do_estoque = quantidade * vl_unitario
    return nome, valor_do_estoque

v1 = valor_estoque("shampoo", 4, 25)


print(f"O produto {v1[0]} custa {v1[1]}")

