// positives_negatives.cpp
// Отношение количества положительных к количеству отрицательных элементов.
// Пример: { 4, 1, 100, 0, 20, 0, -1, -2, 3, -6 } -> 5/3 = 1.6666667.
#include <cstddef>
#include <iostream>
using namespace std;


// П.1: обработка произвольного массива, переданного как адрес + размер,
// size_t -- стандартный тип (определён в Стандартной библиотеке C),
// предназначенный для хранения размеров массивов.
double pn_ratio(const double numbers[], size_t n)
{
  // Счётчики положительных и отрицательных чисел.
  size_t positives = 0, negatives = 0;
  for (size_t i = 0; i < n; ++i)
  {
    // Ключевое слово auto предписывает компилятору вывести тип переменной
    // автоматически по типу инициализирующего выражения.
    const auto x = numbers[i]; // следующий элемент последовательности
    if (x < 0.0)
      ++negatives;
    else if (x > 0.0)
      ++positives;
  }

  // Без приведения к double будет деление в целых числах.
  return double(positives) / negatives;
}

// П.2: тестирование функции из п.1 на заранее заданных массивах.
bool test_pn_ratio()
{
  const double test1[] = { 4, 1, 100, 0, 20, 0, -1, -2, 3, -6 };
  // sizeof возвращает размер статического массива в байтах
  // (!) при этом массив должен быть виден в данном контексте непосредственно,
  // (!) иначе программист рискует получить вместо размера массива размер указателя на него
  if (pn_ratio(test1, sizeof(test1) / sizeof(double)) != 5.0 / 3.0)
    return false;

  const double test2[] = { -40, -2, -111, 42, 0, 0, 2, -1000, -4 };
  if (pn_ratio(test2, sizeof(test2) / sizeof(double)) != 2.0 / 5.0)
    return false;

  // Все проверки прошли успешно.
  return true;
}

// П.3: считывание чисел с потока ввода.
double pn_ratio(istream &in)
{
  // Счётчики положительных и отрицательных чисел.
  size_t positives = 0, negatives = 0;
  for (double x; in >> x;)
  {
    if (x < 0.0)
      ++negatives;
    else if (x > 0.0)
      ++positives;
  }

  // Без приведения к double будет деление в целых числах.
  return double(positives) / negatives;
}

int main()
{
  // Тестирование варианта обработки данных для массива.
  cout << test_pn_ratio() << endl;

  // Вариант для обработки данных с потока ввода.
  const auto result = pn_ratio(cin);
  cout << "\nResult: " << result << endl;
  return EXIT_SUCCESS;
}
