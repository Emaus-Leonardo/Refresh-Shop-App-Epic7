# Refresh Shop Automation

Este é um programa de automação escrito em Python com a biblioteca PyAutoGUI e a estrutura de interface gráfica KivyMD. O objetivo do programa é automatizar o processo de atualização de uma loja virtual em um jogo, comprando itens específicos quando disponíveis.

## Como funciona

O programa utiliza a biblioteca PyAutoGUI para simular interações de mouse e teclado, e a estrutura de interface gráfica KivyMD para criar uma interface simples para o usuário interagir com o programa.

### Funcionalidades principais:

1. **Atualização da loja**: O programa pode realizar um número específico de atualizações da loja.
2. **Compra de itens**: Quando determinados itens (BM e Mystic) estão disponíveis na loja, o programa os compra automaticamente.

## Requisitos

- Python 3.x
- PyAutoGUI
- KivyMD

## Configuração da Resolução

O programa está configurado para funcionar em telas com resolução de 1600 x 900 pixels. Se você estiver usando uma resolução diferente, pode ser necessário ajustar o código para garantir que as interações de mouse e o posicionamento de elementos da interface gráfica ocorram corretamente.

## Modificando para Outras Resoluções

Para modificar o programa para funcionar em resoluções maiores ou menores, você pode ajustar os valores de coordenadas usados para interações de mouse e o layout da interface gráfica. 

Por exemplo, se a resolução da sua tela for maior que 1600 x 900, você pode precisar aumentar os valores de deslocamento usados nas chamadas `pg.moveRel()` para garantir que o mouse clique nos elementos corretos na tela. Se a resolução for menor, você pode precisar diminuir esses valores.

Certifique-se de testar o programa em diferentes resoluções para garantir que ele funcione conforme o esperado.

### Exemplo de Ajuste para Outras Resoluções

```python
# Ajuste os valores de deslocamento para a sua resolução
pg.moveTo(mystic)
pg.moveRel(1000, 30)  # Ajuste o valor X
