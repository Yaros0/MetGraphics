import re

def is_valid(expr: str):
    """
    Проверяет выражение на допустимые буквенные комбинации.
    """


    # Допустимые буквенные комбинации
    allowed = {'sin', 'cos', 'tan', 'pi', 'e', 'abs', 'x'}

    # Находим все слова (последовательности букв)
    words = re.findall(r'[a-zA-Z]+', expr)

    # Проверяем каждое слово
    for word in words:
        if word not in allowed:
            return False

    return True

def simplify_expression(expr: str):

    def extract_coefficient(term: str) -> tuple:
        """Извлекает коэффициент из простого линейного терма"""
        term = term.strip()

        # Только простые формы: x, -x, 5x, 5*x, x*5
        patterns = [
            (r'^x$', 1),
            (r'^-x$', -1),
            (r'^(-?\d*\.?\d+)\*?x$', lambda m: float(m.group(1))),
            (r'^x\*(-?\d*\.?\d+)$', lambda m: float(m.group(1))),
        ]

        for pattern, result in patterns:
            match = re.match(pattern, term)
            if match:
                if callable(result):
                    return result(match), 'x'
                return result, 'x'

        # Константа
        try:
            return float(term), ''
        except:
            raise ValueError(f"Не могу разобрать терм: {term}")

    # Убираем пробелы
    expr = expr.replace(' ', '')

    # Разбиваем на термы
    terms = []
    current = ''
    i = 0
    while i < len(expr):
        if expr[i] in '+-' and i > 0 and expr[i - 1] not in '+-*':
            if current:
                terms.append(current)
            current = expr[i]
        else:
            current += expr[i]
        i += 1
    if current:
        terms.append(current)

    x_coef = 0
    const = 0

    for term in terms:
        try:
            # Пропускаем пустые термы
            if not term or term in '+-':
                continue

            coef, var = extract_coefficient(term)
            if var == 'x':
                x_coef += coef
            else:
                const += coef
        except:
            return expr

    # Формируем результат
    result_parts = []

    if x_coef != 0:
        if x_coef == 1:
            result_parts.append('x')
        elif x_coef == -1:
            result_parts.append('-x')
        else:
            coef_str = str(int(x_coef)) if x_coef.is_integer() else f"{x_coef:.10f}".rstrip('0').rstrip('.')
            result_parts.append(f"{coef_str}*x")

    if const != 0:
        const_str = str(int(const)) if const.is_integer() else f"{const:.10f}".rstrip('0').rstrip('.')
        if const > 0 and result_parts:
            result_parts.append(f"+{const_str}")
        elif const < 0:
            result_parts.append(const_str)
        elif const > 0 and not result_parts:
            result_parts.append(const_str)

    return ''.join(result_parts) if result_parts else '0'

print(simplify_expression('5x'))