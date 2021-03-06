
* <b>fact_lim</b>

For this problem, implement a function called ``fact_lim``. This function has the signature:
```
def fact_lim(n, lim)
```
where ``n`` is a positive integer >= 1 and ``lim`` is a positive integer >= 1. The function is responsible for calculating the summation of the factorials of all numbers starting from ``n`` and ending at ``n - lim`` from 1 to ``n``. For example:

```python
fact_lim(1, 1) -> 1 
fact_lim(2, 1) -> 2 + 1 = 3
fact_lim(2, 2) -> (2 * 1) + 1 = 3
fact_lim(3, 2) -> (3 * 2) + (2 * 1) + 1 = 9
fact_lim(5, 1) -> (5) + (4) + (3) + (2) + 1 = 15
fact_lim(5, 2) -> (5 * 4) + (4 * 3) + (3 * 2) + (2 * 1) + 1 = 41
fact_lim(5, 4) -> (5 * 4 * 3 * 2) + (4 * 3 * 2 * 1) + (3 * 2 * 1) + (2 * 1) + 1 = 153
```
