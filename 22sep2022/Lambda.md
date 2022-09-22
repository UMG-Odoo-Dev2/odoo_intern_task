# Lambda
> Anonymous Function

**Lambda Caculus**
  - Lambda caculus is a notation for describing mathematical functions and programs.

**Lambda Function in Python**
  - Lambda function is also known as nameless function.
  When other function need "del" keyword to define function, Lambda function can write just lambda.

**Syntax**
  - <span style="color:green">lambda args: expression</span>

  - Function နဲ့ သူ့ arguments ကို လက်သည်းကွင်းနဲ့လည်း ရေးနိုင်သည်.
    + eg
      
      * `(lambda args: expression)(value)`
  - You can add one or more arguments in lambda separating them with comma ,
    + eg

      * ```
        var = lambda arg1, arg2: expression
        var(value1, value2)
        ```

  - Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions.
    + eg.,

      * ```
        high_ord = lambda x, func : x + func(x)
        print(high_ord(2, lambda x: x * 3))
        ```
    + Output

      * ```
        8
        ```

