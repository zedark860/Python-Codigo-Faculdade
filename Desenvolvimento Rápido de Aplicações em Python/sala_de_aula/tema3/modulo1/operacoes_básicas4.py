arquivo_escrita = open('dados_write.txt', 'w')
arquivo_escrita.write("Conteúdo primeira linha")
arquivo_escrita.write("\nConteúdo segunda linha")
arquivo_escrita.close()


linhas = ["Conteúdo primeira linha", "\nConteúdo segunda linha"]

arquivo_escrita = open('dados_writelines.txt', 'w')
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()


arquivo_escrita = open('dados_write.txt', 'a')
arquivo_escrita.write("\nConteúdo terceira linha")
arquivo_escrita.close()
