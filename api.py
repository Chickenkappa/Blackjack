def get(a, b, c, s):
	if s > 21:
		return 'Вы проиграли'

	if s == 21:
		return 'Вы выиграли'

	elif s >= 17 and s < 21:

		if a == 9 and b == 9 and c >= 9:
			return 'Сплит (разделите ваши карты на 2 новые колоды)'

		elif (a == 11 or b == 11) and s == 18 and c >= 9:
			return 'Взять только 1 карту'

		elif (a == 11 or b == 11) and s == 17 and c == 7:
			return 'Взять только 1 карту'

		else:
			return 'Остановиесь'

	elif s >= 13 and s <= 16:

		if a == 8 and b == 8 and c == 9:
			return 'Сплит (разделите ваши карты на 2 новые колоды)'

		elif s == 16 and c >= 9:
			return 'Сдайтесь (вы получите полувину вашей ставки)'

		elif s == 15 and c == 10:
			return 'Сдайтесь (вы получите полувину вашей ставки)'

		elif c >= 2 and c <= 6:
			return 'Остановитесь'

		else:
			return 'Набрать карты до суммы номиналов 17 и остановитесь'
			
	elif s == 12:

		if c >= 4 and c <= 6:
			return 'Остановитесь'

		elif c == 2 or c == 3:
			return 'Возьмите одну карту и остановитесь'

		elif a == 6 and b == 6 and c <= 6 and c >=  4:
			return 'Сплит (разделите ваши карты на 2 новые колоды)'

		else:
			return 'Набрать карты до суммы номиналов 17'
			
	elif a == 3 and b == 3 and c <= 7 and c >=  5:
		return 'Сплит (разделите ваши карты на 2 новые колоды)'
		
	elif a == 2 and b == 2 and c <= 7 and c >=  5:
		return 'Сплит (разделите ваши карты на 2 новые колоды)'

	elif s <= 11:
		return 'Возьмите карту и попробуйте ещё раз'