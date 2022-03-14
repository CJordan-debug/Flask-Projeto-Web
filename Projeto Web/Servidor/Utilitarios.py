def validarDadosJogo(nome, categoria, idadeMin, foto, descricao):
    if len(nome) >= 5 and \
       len(categoria) > 0 and \
       isinstance(idadeMin, int) and \
       len(foto) > 0 and \
       len(descricao) > 0:
        return True
    else:
        return False