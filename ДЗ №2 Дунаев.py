{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Для того чтобы оценка за данную работу пошла в зачёт нужно отправить ссылку на нее в гит или ноутбук до <b> 17.10.2021 17:00 </b>."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Задание 1.</b> Создайте массив, который состоит из целых чисел от -50 до 50 включительно. Затем удалите последние 25 элеметов массива. Затем разверните массив. Добавьте в конец массива 999. Создайте новый массив в который войдут все четные числа из ранее полученного массива и напечатайте его."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40, -42, -44, -46, -48, -50]\n"
     ]
    }
   ],
   "source": [
    "my_list = list(range(-50, 51))\n",
    "del my_list[76:101]\n",
    "my_list.reverse()\n",
    "my_list.append(999)\n",
    "new_list = []\n",
    "for i in my_list:\n",
    "    if i % 2 == 0:\n",
    "        new_list.append(i)\n",
    "print(new_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Задание 2.</b> Даны несколько массивов целых чисел (A, B, C, D). Напишите программный код, с помощью которого вы сможете определить длину самой длинной непрерывной последовательности равных значений для каждого из массивов."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# [1, 1, 1, 2, 3, 4, 5, 6, 3, 4, 1, 1, 1, 1] - самая длинная последовательность длины 4\n",
    "A = [1] * 20 + [1, 1, 3] * 30 + [1] * 21\n",
    "\n",
    "B = list(range(1, 9, 2)) * 3 + list(range(4, 1, 1)) * 2 + [3] * 3\n",
    "B.pop()\n",
    "B.reverse()\n",
    "B.pop()\n",
    "B.reverse()\n",
    "\n",
    "C = [b - 2 for b in B]\n",
    "C.reverse()\n",
    "C =  A + C\n",
    "\n",
    "D = [777] + [666] + [1,2,1,1] * 2 + [1,1,1,1,3]*3 + [1, 4] * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "2\n",
      "23\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def f(A):\n",
    "    maximum = 1\n",
    "    a = 1\n",
    "    for i in range(len(A) - 1):\n",
    "        if A[i + 1] == A[i]:\n",
    "            a += 1\n",
    "            if maximum < a:\n",
    "                maximum = a\n",
    "        else:\n",
    "            a = 1\n",
    "    return maximum\n",
    "print(f(A))\n",
    "print(f(B))\n",
    "print(f(C))\n",
    "print(f(D))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Задание 3.</b> Напишите функция, которая на вход принимает прямоугольную матрицу и возвращает транспонированную матрицу. Протестируйте функцию на матрицах A, B, C."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "A = [[1, 1], [1, 0]]\n",
    "B = [[2, 3, 4], [4, 5, 6], [7, -1, -2], [-4, -6, 99], [1, 0, 1]]\n",
    "C = [[1, 2, 3, 4, 5]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "object of type 'int' has no len()",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-27e801c7b02f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m         \u001b[0ma\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mAt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmatrixx\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmatrixx\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mB\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmatrixx\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mC\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-23-27e801c7b02f>\u001b[0m in \u001b[0;36mmatrixx\u001b[1;34m(A)\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mAt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0ma\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m             \u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: object of type 'int' has no len()"
     ]
    }
   ],
   "source": [
    "def matrixx(A):\n",
    "    At = []\n",
    "    a = []\n",
    "    for i in range(len(A[0])):\n",
    "        for j in range(len(A)):\n",
    "            a.append(A[j][i])\n",
    "        At.append(a)\n",
    "        a = []\n",
    "    return At\n",
    "print(matrixx(A))\n",
    "print(matrixx(B))\n",
    "print(matrixx(C))"
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
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
