todo:

- pegar as posicoes na tela pro python gui on-startup e usar @cachetools - https://pypi.org/project/cachetools/
assim o negocio fica funcional em qualquer computador e da pra mover as janelas tb pra n ficar chumbado


usar cachetools pra pegar a posicao cacheada das coisas q ele fica olhando, pra ajudar a diminuir processamento

https://pyautogui.readthedocs.io/en/latest/screenshot.html#:~:text=These%20%E2%80%9Clocate%E2%80%9D%20functions%20are%20fairly%20expensive%3B%20they%20can%20take%20a%20full%20second%20to%20run.%20The%20best%20way%20to%20speed%20them%20up%20is%20to%20pass%20a%20region%20argument%20(a%204%2Dinteger%20tuple%20of%20(left%2C%20top%2C%20width%2C%20height))%20to%20only%20search%20a%20smaller%20region%20of%20the%20screen%20instead%20of%20the%20full%20screen%3A

These “locate” functions are fairly expensive; they can take a full second to run.
The best way to speed them up is to pass a region argument (a 4-integer tuple of (left, top, width, height)) to only search a smaller region of the screen instead of the full screen: