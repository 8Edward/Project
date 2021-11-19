{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# План занятия\n",
    "- циклы (while, for)\n",
    "- массивы (списки)\n",
    "- функции\n",
    "- реализация функции скалярного произведения\n",
    "- реализация метода обучения персептрона\n",
    "- тест на 5 минут"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "> 5\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "if a > 5:\n",
    "    print('> 5')\n",
    "else:\n",
    "    print('<= 5')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Циклы\n",
    "- while\n",
    "- for"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## While\n",
    "Вычисления нередко приходится повторять. Предназначенная для этого базовая конструкция Python имеет следующий формат:\n",
    "\n",
    "<code>while <логическое выражение>:\n",
    "    <оператор 1>\n",
    "    <оператор 2>\n",
    "    <оператор 3>\n",
    "        ...</code>\n",
    "        \n",
    "Оператор while имеет ту же форму, что и оператор if, но отличается назначением. Он работает следующим образом: если результат логического выражения False, то не делает ничего, если результат True - выполнить блок операторов ниже, а затем снова проверить выражение и выполнить ещё раз последовательность операторов, если выражение возвращает True, и продолжать до тех пор пока логическое выражение остаётся истинным. Логическое выражение - условие продолжения цикла."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i = 0\n",
      "i = 1\n",
      "i = 2\n",
      "i = 3\n",
      "i = 4\n",
      "i = 5\n"
     ]
    }
   ],
   "source": [
    "# пример\n",
    "i = 0 \n",
    "while i <= 5:\n",
    "    print('i =',i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Оператор while последовательности одинаковых операторов if: <br>\n",
    "<code>if <логическое выражение>:\n",
    "    <оператор 1>\n",
    "    <оператор 2>\n",
    "    <оператор 3>\n",
    "        ...</code> <br>\n",
    "<code>if <логическое выражение>:\n",
    "    <оператор 1>\n",
    "    <оператор 2>\n",
    "    <оператор 3>\n",
    "        ...</code> <br>\n",
    "<code>if <логическое выражение>:\n",
    "    <оператор 1>\n",
    "    <оператор 2>\n",
    "    <оператор 3>\n",
    "        ...</code><br>\n",
    "<code>if <логическое выражение>:\n",
    "    <оператор 1>\n",
    "    <оператор 2>\n",
    "    <оператор 3>\n",
    "        ...</code>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "i = 0 \n",
    "if i <= 5:\n",
    "    print('i =',i)\n",
    "    i = i + 1\n",
    "if i <= 5:\n",
    "    print('i =',i)\n",
    "    i = i + 1\n",
    "if i <= 5:\n",
    "    print('i =',i)\n",
    "    i = i + 1\n",
    "# if i <= 5:\n",
    "#     print('i =',i)\n",
    "#     i = i + 1\n",
    "# if i <= 5:\n",
    "#     print('i =',i)\n",
    "#     i = i + 1\n",
    "# if i <= 5:\n",
    "#     print('i =',i)\n",
    "#     i = i + 1\n",
    "# if i <= 5:\n",
    "#     print('i =',i)\n",
    "#     i = i + 1\n",
    "# if i <= 5:\n",
    "#     print('i =',i)\n",
    "#     i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Чтобы условие продолжения работы цикла стало в конечном счёте ложным (=False) и цикл завершился, в теле цикла должно изменяться значение одно или нескольких переменных."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    print(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 0\n",
    "j = 5\n",
    "while j > 0:\n",
    "    i = i + 1\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n",
      "Privet\n"
     ]
    }
   ],
   "source": [
    "# пример: вывести 10 раз Привет\n",
    "i = -5\n",
    "while i <= 4:\n",
    "    i = i + 1\n",
    "    print('Privet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример: вычисление степени числа\n",
    "n = 2 # число\n",
    "degree = 5 # степень\n",
    "i = 0\n",
    "p = 1\n",
    "while i < degree:\n",
    "    p = p * n\n",
    "    i = i+ 1\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 % 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# вывод на экран всех чётных чисел от 3 до 234 включительно\n",
    "i = 3\n",
    "while i <= 234:\n",
    "    if i % 2 == 0:\n",
    "        print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Сокращённая запись присвоения:\n",
    "<code>\n",
    "    i = i + 1\n",
    "</code>\n",
    "Можно записать\n",
    "<code>\n",
    "    i += 1\n",
    "</code>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 2\n",
    "i %= 10\n",
    "i"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Использую оператор while можно создавать практически любые циклы. Мы рассмотрим с вами альтернатиную конструкцию - оператор for, он добавит больше гибкости. Оператор for часто позволяет написать более компактный и читаемый код программы, чем при использовании оператора while."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## For"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Очень часто в программировании для решения задачи используют конструкцию цикл со счётчиком. \n",
    "<code>\n",
    "    <переменная> = <старт (начальное значение переменной)>\n",
    "    while <переменная> < <стоп>:\n",
    "        <блок операторов>\n",
    "        <переменная> += 1 # тоже самое, что и <переменная> = <переменная> + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Оператор for обеспечивает более компактный способ реализации цикла со счетчиком. В языке Python оператор for имеет несколько форматов. Пока рассмотрим следующий шаблон:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>for <переменная> in range(<старт>, <стоп>):\n",
    "    <блок операторов>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>Аргументы <старт> и <стоп> встроенной функции range() должны быть целыми числами. Когда оператор дан в этой форме Python многократно выполняет блок операторов с отступом. На первой итерации цикла <переменная> имеет значение <старт>, на второй <старт>  + 1 и так далее. На последний итерации цикла <переменная> имеет значение <стоп> - 1. Если говорить коротко, то оператор for многократно выполняет <блок операторов> с отступом, причём переменная меняется от <старт> до <стоп> - 1 включительно."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 0 # <переменная> = <старт> переменная - i, старт - 0\n",
    "while i < 5: # while <переменная> < <стоп> переменная - i, стоп - 5\n",
    "    # то есть пока i меньше пяти операторы с отступом следующие за while будут выполняться\n",
    "    print ('i =', i) # вывод на экран\n",
    "    i = i + 1 # увеличивает значение i на 1 на каждом шаге"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>for <переменная> in range(<старт>, <стоп>):\n",
    "    <блок операторов>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример: переписать данный цикл использую for\n",
    "for i in range(0, 5): #0, 1, 2, 3, 4\n",
    "    print ('i =', i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример: вычислить n!\n",
    "n = 7\n",
    "fact = 1\n",
    "for i in range(1, n + 1):\n",
    "    fact *= i # fact = fact * i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sum([1,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример: вычислить сумму от 1 до n\n",
    "n = 10\n",
    "summ = 1\n",
    "for i in range(1, n + 1):\n",
    "    sum += i # fact = fact * i\n",
    "print(summ)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Как обратиться к командной строке из ноутбука?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!ls -l -sh"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install sklearn"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Вложенный циклы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# пример\n",
    "for i in range(0, 3): # range(0, 3) = range(3) если в range передеать 1 параметр,\n",
    "                        # то начальное значение(старт) будет равно нулю\n",
    "    for j in range(0, 3):\n",
    "        print('i=',i,'j=',j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sys import stdout as std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "std.write('1')\n",
    "std.write('2')\n",
    "std.write('\\n')\n",
    "std.write('2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# пример\n",
    "for i in range(20):\n",
    "    for j in range(20):\n",
    "        if (i == 0) or (j == 4) or (i == 16) or (j == 19):\n",
    "            std.write('*')\n",
    "        else:\n",
    "            std.write(' ')\n",
    "    std.write('\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Наш следующий пример, демонстрирует ситуацию(обычную), когда компьютеры используются для моделирования того что могло бы произойти в реальном мире, чтобы принимать более обоснованные решения.\n",
    "\n",
    "Следующий пример относится к классу задач известных как задача о разорении игрока. Предположим, что игрок последовательно делает неограниченную серию ставок, начиная с некоторой заданной суммы. В конечно счёте игрок всегда проигрывает, но если установить некие пределы для игры, то возникают различные вопросы. Допустим, игрок решает уйти после получения определённого выигрыша. Какова вероятность того, что он выиграет? Сколько ставок может понадобиться чтобы выиграть или проиграть? Какова максимальная сумма, которую игрок будет иметь в течении игры."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "random.randrange(0, 3) # возвращает случайное целое число из диапазона range(0, 3)\n",
    "#  т. е. это может быть 0, 1, 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tqdm.auto import tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "win = 0\n",
    "N = 10000\n",
    "for i in tqdm(range(N)):\n",
    "    money = 500\n",
    "    goal = 530\n",
    "\n",
    "    while money < goal and money >0:\n",
    "        bet = random.randrange(0, 2) # 0 - red, 1 - black\n",
    "\n",
    "        result = random.randrange(0, 37)\n",
    "        if result == 0:\n",
    "            money -= 1\n",
    "        elif result % 2 == bet: # red\n",
    "            money += 1\n",
    "        else:\n",
    "            money -= 1\n",
    "    \n",
    "    if money == goal:\n",
    "        win += 1\n",
    "    #print(money)\n",
    "print(win/N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stake = 500 #начальная сумма\n",
    "goal = 1000 #цель\n",
    "\n",
    "bets = 0 #количество ставок\n",
    "\n",
    "while stake > 0 and stake < goal:\n",
    "    if random.randrange(2) == 1:\n",
    "        stake += 1\n",
    "    else:\n",
    "        stake -= 1\n",
    "    \n",
    "    bets += 1\n",
    "\n",
    "if (stake == goal):\n",
    "    print('win')\n",
    "else:\n",
    "    print('lose')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tqdm.auto import tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "stake = 500 #начальная сумма\n",
    "goal = 1000 #цель\n",
    "trial = 100000 #количество попыток\n",
    "\n",
    "bets = 0 #количество ставок\n",
    "wins = 0 #количесвто побед\n",
    "for i in tqdm(range(trial)):\n",
    "    cash = stake\n",
    "    while cash > 0 and cash < goal:\n",
    "        if random.randrange(2) == 1:\n",
    "            cash += 1\n",
    "        else:\n",
    "            cash -= 1\n",
    "\n",
    "        bets += 1\n",
    "\n",
    "    if (cash == goal):\n",
    "        wins += 1\n",
    "\n",
    "print(wins/trial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(bets/trial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stake * (goal-stake)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "# в чём состоит удоство задавать всё через переменные значения?\n",
    "stake = 500 #начальная сумма\n",
    "goal = 1000 #цель\n",
    "trial = 1000 #количество попыток\n",
    "\n",
    "bets = 0 #количество ставок\n",
    "wins = 0 #количесвто побед\n",
    "proba_arr = []\n",
    "bets_arr = []\n",
    "for i in tqdm(range(trial)):\n",
    "    cash = stake\n",
    "    bets = 0\n",
    "    while cash > 0 and cash < goal:\n",
    "        if random.randrange(2) == 1:\n",
    "            cash += 1\n",
    "        else:\n",
    "            cash -= 1\n",
    "\n",
    "        bets += 1\n",
    "\n",
    "    if (cash == goal):\n",
    "        wins += 1\n",
    "    proba_arr.append(wins/(i + 1))\n",
    "    bets_arr.append(bets)\n",
    "print(wins/trial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stake/goal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "plt.plot(proba_arr[:])\n",
    "plt.plot([1/2]*trial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "sum(bets_arr)/len(bets_arr) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stake * (goal - stake)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.plot(bets_arr)\n",
    "plt.plot([stake * (goal - stake)]*trial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.plot(np.log1p(bets_arr))\n",
    "plt.plot(np.log1p([stake * (goal - stake)]*trial))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Действительно ли модель точно отражает происходящее в жизни? \n",
    "- Сколько попыток нужно для получения точного ответа?\n",
    "- Каковы вычислительные пределы такой имитации?\n",
    "\n",
    "Моделирование широко используется в экономике, науке и технике, а вопросы такого рода очень важны для любой модели.\n",
    "\n",
    "В случае нашей задачи мы проверяли, что:\n",
    "- вероятность успеха - соотношение начальной суммы к цели\n",
    "- ожидаемое количество ставок - произведение начальной суммы и желаймой суммы выигрыша(выигрыш - желаемая сумма минус начальня)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Практическое значение моделирования в том, что оно может предложить ответы на вопросы, слишком трудные для аналитического решения."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>?</b> Сколько денег игрок может ожидать унести домой в случае, если он решает ограничить число ставок. (Допустим игрок максимум успеет поставить 500 ставок, начальная сумма 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Неполный цикл"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Иногда структура управления потоком for или while не очень точно соответствует необходимому циклу.\n",
    "- допустим вы хотите проверять условие не в начале цикла, а в середине т. е. сначала сделать некоторые операции, а затем проверить выполненение условий (необходимо, когда для проверки выполнения условий нужно сначала выполнить некоторые вычисления)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример: генерировать точки из квадрата 2 на 2 до тех пор пока они попадают в круг,\n",
    "# центр, которого в центре квадрата и радиус равен 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "random.random() #shift + tab чтобы посмотреть описание функции\n",
    "# shift + enter - чтобы выполнить код в ячейке и перейти к следующей\n",
    "# ctr + enter - чтобы выполнить код в ячейке и остаться"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "2 * random.random()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "while True: # это вечный цикл, мы не планируем останавливаться\n",
    "    # пусть квадрат - [0, 2] x [0, 2]\n",
    "    # тогда его центр (1, 1)\n",
    "    # генерируем два случайных числа от 0 до 2\n",
    "    x = 2 * random.random()\n",
    "    y = 2 * random.random()\n",
    "    if ((x - 1) ** 2 + (y - 1) ** 2) > 1:\n",
    "        break\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = []\n",
    "Y = []\n",
    "while True: # это вечный цикл, мы не планируем останавливаться\n",
    "    # пусть квадрат - [0, 2] x [0, 2]\n",
    "    # тогда его центр (1, 1)\n",
    "    # генерируем два случайных числа от 0 до 2\n",
    "    x = 2 * random.random()\n",
    "    y = 2 * random.random()\n",
    "    if ((x - 1) ** 2 + (y - 1) ** 2) >= 1:\n",
    "        break\n",
    "    X.append(x)\n",
    "    Y.append(y)\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "fig,ax = plt.subplots(1)\n",
    "plt.figure(figsize=(4,4), dpi = 200)\n",
    "circle = plt.Circle((1,1),1, fill = False)\n",
    "ax.add_patch(circle)\n",
    "ax.scatter(X, Y)\n",
    "ax.scatter([1], [1], color = 'red')\n",
    "ax.scatter([x], [y], color = 'g')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(10, 1, -2):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "! Когда реализуете цикл важно обдумать следующую ситуацию: что, если условие продолжения цикла будет всегда удовлетворяться?\n",
    "\n",
    "Ситуации две:\n",
    "- либо что-то бесконечно делается и мы это наблюдаем \n",
    "- либо кажется, что программа ничего не делает\n",
    "\n",
    "Можно попробовать проверить, что условие выхода всегда срабатывает, но это сделать бывает затруднительно. Один из способо поиска такой ошибки - трассировка ( на каждой операции цикла что-то выводить в лог или просто в окно вывода )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Один из фактов фундаметальной информатики состоит в том, что невозможно написать алгоритм, который будет всегда обнаруживать бесконечные циклы и сообщать нам. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Все программисты знают, что программы часто не работают сразу, как планировалось вначале, поэтому в программе придется разобраться и выяснить, что нужно делать. Сначала используйте явные трассировки для проверки своего понимания и ожиданий. По мере приобретения опыта в создании собственных циклов вы начнете думать в терминах того, что могла бы дать трассировка. Задайте себе следующие виды вопросов: каковы будут значения переменных после первой итерации цикла? После второй? Если ли у этой программы способ попасть в вечный цикл?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Что будет если пропустить двоеточие в операторах if, while, for?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# решение\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "У каждого оператора в блоке должен быть одинаковый отступ, если это не так то во время компиляции произойдет ошикба IndentationError. Обычно программисты Python используют четыре пробела.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример\n",
    "if 5 > 4:\n",
    "    print(1) # 4 пробела\n",
    "     print(2)# 5 пробелов"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример\n",
    "if 5 > 4:\n",
    "     print(1)# 5 пробелов\n",
    "     print(2)# 5 пробелов, теперь число пробелов одинаковое все работает"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Символы табуляции для пробелов использовать нельзя, во многих редакторах при нажатии <Tab> будут вставляться 4 пробела."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Чтобы написать разбить длинную строку кода на несколько нужно использова \\"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1 + 2 + 3 + 4 + # так получим ошибку\n",
    "1 + 2 + 3 + 4 +\n",
    "1 + 2 + 3 + 4 +\n",
    "1 + 2 + 3 + 4 +\n",
    "1 + 2 + 3 + 4 +\n",
    "1 + 2 + 3 + 4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1 + 2 + 3 + 4  + \\\n",
    "    1 + 2 + 3 + 4  + \\\n",
    "    1 + 2 + 3 + 4  + \\\n",
    "    1 + 2 + 3 + 4  + \\\n",
    "    1 + 2 + 3 + 4  + \\\n",
    "    1 + 2 + 3 + 4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# способ чтения аргументов из командой строки\n",
    "a = input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Если хотим преобразовать строку в целое чилсо использует оператор int('5'), если в действительное, то float('1.2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('5')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(int('5'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float('1.2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(float('1.2'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float('stroka')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Составьте программу, получающую в командной строке три целочисленных аргумента и выводящую слова 'equal', если все три равны и 'not equal' в противном случае"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b, c = int(input()), int(input()), int(input())\n",
    "if a == b == c:\n",
    "    print('equal')\n",
    "else:\n",
    "    print('not equal')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Составьте фрагмент кода, получающий два аргумента командной строки типа float и выводящий True, если они находятся в диапозоне от 0.0 до 1.0 иначе False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b = float(input()), float(input())\n",
    "print(0.0 <= a <= 1.0 and 0.0 <= b <= 1.0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Что выведет каждый из следующих фрагментов кода <br>\n",
    "a. <code> \n",
    "    j = 0\n",
    "    for i in range(j, 10):\n",
    "        j += 1 \n",
    "    print(j)\n",
    "</code> <br>\n",
    "_____________\n",
    "b. <code> \n",
    "    j = 0\n",
    "    for i in range(10):\n",
    "        j += j\n",
    "    print(j)\n",
    "</code>\n",
    "___________\n",
    "c. <code>\n",
    "    for j in range(10):\n",
    "        j += j\n",
    "    print(j)\n",
    "   </code>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "решение: запишите ответы для каждого фрагмента кода\n",
    "подсказка: можете запускить данный код с трассировкой для каждой итерации цикла, чтобы разобраться что происходит <br>\n",
    "a = <br>\n",
    "b = <br>\n",
    "c = <br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 10\n",
    "b = 0\n",
    "c = 18"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. В отличие от гармонического ряда, сумма последовательности\n",
    "$$ \\frac{1}{1^2} +\\frac{1}{2^2} + ... + \\frac{1}{n^2} $$\n",
    "сходится к константе при $n\\to \\infty$. Эта константа $\\frac{\\pi^2}{6}$ т. е.\n",
    "$$ \\frac{1}{1^2} +\\frac{1}{2^2} + ... + \\frac{1}{n^2} \\to \\frac{\\pi^2}{6}, \\text{ при } n \\to \\infty $$\n",
    "Напишите цикл, который вычисляет эту сумму при заданном $n$, число $n$ вводится. Сумма сохраняется в переменную total типа float, которая инициализируется 0.0.\n",
    "Насколько сумма при n = 1000 будет отличаться от $\\frac{\\pi^2}{6}$?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# чтобы получить число pi\n",
    "from numpy import pi# импортируем константу из библиотеки numpy\n",
    "n = int(input())\n",
    "total = 0.0\n",
    "for i in range(1, n + 1):\n",
    "    total += 1 / i ** 2\n",
    "print(total)\n",
    "print(pi ** 2 / 6 - total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pi # пи с некоторой точностью"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# решение\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Такси Рамануджана. С. Рамануджан - индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Г. Х. Харди навестил его однажды в больнице, он обмолвился, что номеров такси на котором он приехал, было 1729, такое скучное и заурядное число. На что Рамануджан ответил: \"Нет, нет! Это очень интересно число. Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами.\" Проверьте это заявление, создав программу, получающую $n$  в аргументе командной строки и выводящую все целые числа, меньше или равные  $n$, которые могут быть выражены как сумма двух кубов двумя разными способами. Другими словами, найдите различные положительные числа $a,b,c,d$, удовлетворяющие условию \n",
    "$$ a^3 + b^3 = c^3 + d^3 $$\n",
    "Используйте четыре вложенных цикла for."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7000\n",
      "1729\n",
      "4104\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "k = int(n ** (1 / 3))\n",
    "for a in range(1, k):\n",
    "    for c in range(1, a):\n",
    "        for d in range(1, c):\n",
    "            for b in range(1, d):\n",
    "                if a != c and a != d and b != c and b != d and a ** 3 + b ** 3 == c ** 3 + d ** 3 and a ** 3 + b ** 3 <= n:\n",
    "                    print(a ** 3 + b ** 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Мини тест"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Массивы (списки)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Функции"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Реализация функции скалярного произведения"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Реализация метода обучения персептрона"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Тест"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
