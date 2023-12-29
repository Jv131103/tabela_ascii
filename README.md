# tabela_ascii
Minha tabela ASCII em Python

# Tabela ASCII Generator

Este é um simples script em Python para gerar e exibir informações da tabela ASCII. A tabela inclui detalhes como o caractere, o valor decimal, a representação octal, hexadecimal e binária de cada código ASCII.

## ps: Este código é para fins de consulta, logo não retorna valores específicos.

## Uso

Você pode utilizar este script para gerar informações da tabela ASCII a partir de um intervalo de valores ou para obter informações sobre um caractere específico.

### Parâmetros
  . `numero_inicial`: Valor inicial da geração da tabela ASCII.
  . `numero_final`: Valor final da geração da tabela ASCII (opcional).
  . `intervalo`: Intervalo entre os valores (opcional).


# Exemplo de geração da tabela ASCII de 0 a 127 com intervalo padrão de 1
Ascii(0, 127)

# Exemplo de geração da tabela ASCII de 33 a 126 com intervalo de 5
Ascii(33, 126, 5)

# Exemplo para consulta de um único dado
Ascii(33) # retorna "!"

## Exemplo Concreto

### Importação do arquivo e execução na Shell do Python
```python
>>> from ASCII import Ascii # Também funciona: import ASCII
>>> Ascci(0, 190) #ou Ascii(0), "Ascii(0, 190, 2)"
```

### Execução do arquivo py
```terminal
python3 ASCII.py
```
ou
```terminal
python ASCII.py
```
ou
```terminal
py ASCII.py
```

## Contribuição
Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Configuração do Ambiente de Desenvolvimento
Para configurar seu ambiente de desenvolvimento, siga os passos abaixo:

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   ```

2. Navegue até o diretório do projeto:
  ```bash
   cd seurepositorio
  ```

### Como Contribuir
- Crie um fork deste repositório.
- Crie uma branch para a sua contribuição:
  ```bash
  git checkout -b sua-feature
  ```
- Faça suas alterações e commit:
  ```bash
  git commit -m "Adiciona nova funcionalidade"
  ```
- Push para o seu fork:
  ```bash
  git push origin sua-feature
  ```
- Abra um Pull Request para revisão.

  #### Diretrizes para Pull Requests
  Ao enviar um Pull Request, certifique-se de seguir estas diretrizes:

    . Descreva claramente a finalidade da sua contribuição.
    . Certifique-se de que seu código está em conformidade com as práticas de estilo do projeto.
    . Certifique-se de que os testes passam.
    . Se aplicável, atualize a documentação para refletir as alterações.

Lembre-se de que todas as contribuições estão sujeitas à aprovação antes de serem mescladas.

# Obrigado por contribuir!
  Lembre-se de substituir `seuusuario` e `seurepositorio` pelos seus dados específicos. Essas adições fornecem orientações para os contribuidores sobre como configurar o ambiente de desenvolvimento, executar testes e enviar Pull Requests formatados corretamente.
  
## Licença
Este projeto é licenciado sob a [Licença MIT](LICENSE.md) - veja o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.

