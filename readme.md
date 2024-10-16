# Порівняння алгоритмів сортування: злиття, вставка і Timsort

## Мета
Це домашнє завдання полягало в порівнянні трьох алгоритмів сортування — злиття, вставки та Timsort — за часом виконання на різних наборах даних.

## Алгоритми:
- **Merge Sort (сортування злиттям)**: має складність O(n log n), ефективний для великих масивів.
- **Insertion Sort (сортування вставками)**: має складність O(n^2), неефективний на великих масивах, але добре працює на малих і майже впорядкованих масивах.
- **Timsort**: використовує поєднання сортування злиттям і вставками, що дозволяє досягти найкращої продуктивності для реальних даних.

## Емпіричні результати
Було проведено тестування на масивах різних розмірів (1000, 5000, 10000 елементів) і типів (випадкові, впорядковані, зворотно впорядковані).

Data Size: 1000

 - Data Type: **Random**
merge_sort: 0.002693 seconds.
insertion_sort: 0.020527 seconds.
tim_sort: 0.000109 seconds.
 - Data Type: **Sorted**
merge_sort: 0.001580 seconds.
insertion_sort: 0.000112 seconds.
tim_sort: 0.000011 seconds.
 - Data Type: **Reversed**
merge_sort: 0.001464 seconds.
insertion_sort: 0.045514 seconds.
tim_sort: 0.000012 seconds.

Data Size: 5000

 - Data Type: **Random**
merge_sort: 0.012186 seconds.
insertion_sort: 0.647099 seconds.
tim_sort: 0.000503 seconds.
 - Data Type: **Sorted**
merge_sort: 0.009034 seconds.
insertion_sort: 0.000543 seconds.
tim_sort: 0.000052 seconds.
 - Data Type: **Reversed**
merge_sort: 0.009038 seconds.
insertion_sort: 1.146114 seconds.
tim_sort: 0.000045 seconds.

Data Size: 10000

- Data Type: **Random**
merge_sort: 0.025749 seconds.
insertion_sort: 2.363906 seconds.
tim_sort: 0.001281 seconds.
- Data Type: **Sorted**
merge_sort: 0.019948 seconds.
insertion_sort: 0.001082 seconds.
tim_sort: 0.000161 seconds.
- Data Type: **Reversed**
merge_sort: 0.020067 seconds.
insertion_sort: 4.379344 seconds.
tim_sort: 0.000116 seconds.


За результатами тестування:
1. **Сортування злиттям** показало стабільну продуктивність на всіх типах масивів.
2. **Сортування вставками** працювало значно повільніше на великих масивах, особливо на випадкових і зворотно впорядкованих даних.
3. **Timsort** показав найкращу продуктивність, особливо на впорядкованих і майже впорядкованих масивах, що пояснюється його гібридною природою.

## Висновок
Timsort, будучи гібридним алгоритмом, поєднує переваги обох алгоритмів: сортування злиттям для великих даних і сортування вставками для невеликих і частково впорядкованих підмасивів. Саме тому Python використовує Timsort для вбудованих функцій сортування, що робить його найефективнішим для реальних сценаріїв.
