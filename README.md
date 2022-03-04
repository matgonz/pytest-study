### Repositório destinado a estudos da biblioteca Pytest com foco em Machine Learning


Instalando a biblioteca:
> pip install pytest

Exemplos de como executar um teste:
- pytest /diretorio_do_teste
- pytest /diretorio_do_teste/sub_diretorio/
- pytest /diretorio_do_teste/testes_v1.py
- pytest /diretorio_do_teste/testes_v1.py::teste_metodo_de_teste

Argumentos utilizados:
- -v = Exibe os métodos executados e o status final
- -m "marks" = Utilizado para informar qual mark (métodos ou classes anotadas) deve ser executado
- --pdb = Utilizado para depurar métodos quando não passam no teste